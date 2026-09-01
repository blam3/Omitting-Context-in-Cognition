# Score screen for the false-complex model class.
#
# This implements the screen described in Proposition L3.4 and Remark 4.5 of
# docs/proofs/L3_kl_dominance.md.
#
# Background. Let M_S be the context-omitting simple class and M_K the
# context-omitting complex class, with M_S nested in M_K through the embedding
# that sets M_K's extra coefficients to zero. Write eta_dagger for the
# pseudo-true simple parameter, i.e. the minimiser of the expected divergence
# from the omitted-context marginal law. Proposition L3.4 states that if the
# population score of the extra parameters is nonzero at the embedded
# pseudo-true simple model,
#
#   s_dagger = E_{p_0}[ d/d psi_extra log q_psi ] evaluated at (eta_dagger, 0),
#
# then the complex class attains strictly lower divergence, so Delta ell > 0.
#
# Why this is worth computing. The condition is checkable WITHOUT ever fitting
# the complex model. For a binomial GLM the score is X^T (y - mu), so at the
# embedded simple fit the extra-parameter block is just the extra design matrix
# weighted by the simple model's residuals. This makes the screen roughly the
# cost of one simple fit rather than a full complex fit, and it reports which
# blocks of false complexity carry the dominance rather than only whether some
# complex model wins.
#
# What the screen does NOT establish.
#
#   1. s_dagger != 0 is sufficient but not necessary for strict dominance.
#      A screen that fails to reject is not evidence that Delta ell = 0.
#   2. Delta ell > 0 does not imply lower LOOIC or a positive log Bayes factor
#      (Corollary L3.5). The screen speaks only to the KL/log-score bridge.
#   3. A nonzero score is not evidence of omitted context. Counter-example CE-1
#      of the L3 draft shows plain trial-level misspecification produces the
#      same signal with nothing omitted at all.
#   4. Proposition L3.4 requires nesting. verify_nesting() enforces it and
#      errors rather than returning a number that would have no interpretation.
#
# Everything here is a GLM proxy, consistent with A-004 and with the
# scaffold_only status of C-005. It is a screening device for choosing which
# false-complex parameterisations are worth carrying into the hierarchical
# Bayesian model suite, not a Bayesian criterion.

#' Verify that the simple design is nested in the complex design
#'
#' Proposition L3.4 applies only when M_S is embedded in M_K. This checks the
#' embedding at the level of realised design-matrix columns, which is the form
#' the nesting takes for these GLM proxies.
#'
#' @param x_simple Simple-model design matrix.
#' @param x_complex Complex-model design matrix.
#'
#' @return Invisibly, the names of the extra columns.
verify_nesting <- function(x_simple, x_complex) {
  simple_terms <- colnames(x_simple)
  complex_terms <- colnames(x_complex)

  missing_terms <- setdiff(simple_terms, complex_terms)
  if (length(missing_terms) > 0) {
    stop(
      "Score screen requires the simple model to be nested in the complex model. ",
      "Columns present in the simple design but absent from the complex design: ",
      paste(missing_terms, collapse = ", "),
      ". Proposition L3.4 does not apply to non-nested classes; a separate ",
      "sufficient condition for strict KL dominance would be required.",
      call. = FALSE
    )
  }

  extra_terms <- setdiff(complex_terms, simple_terms)
  if (length(extra_terms) == 0) {
    stop(
      "Score screen requires at least one extra parameter in the complex model, ",
      "but the two designs span the same columns.",
      call. = FALSE
    )
  }

  invisible(extra_terms)
}

# Assign each extra column to an interpretable block of false complexity. The
# block breakdown is the screening payoff: it says which kind of extra
# machinery absorbs the omitted-context residual structure.
classify_extra_terms <- function(extra_terms) {
  block <- rep("other", length(extra_terms))
  block[grepl("^ambiguity_sq_value", extra_terms)] <- "nonlinear_ambiguity"
  block[grepl("^ambiguous_value", extra_terms)] <- "linear_ambiguity"
  block[grepl("^condition", extra_terms)] <- "condition"
  block[grepl("^color_cue", extra_terms)] <- "color_cue"
  stats::setNames(block, extra_terms)
}

# Drop extra columns that are constant or collinear with the retained set. A
# rank-deficient extra block makes the score covariance singular, and silently
# inverting it would fabricate precision.
drop_degenerate_columns <- function(x_extra, x_simple) {
  keep <- rep(TRUE, ncol(x_extra))
  names(keep) <- colnames(x_extra)

  for (j in seq_len(ncol(x_extra))) {
    if (stats::sd(x_extra[, j]) == 0) keep[j] <- FALSE
  }

  if (any(keep)) {
    combined <- cbind(x_simple, x_extra[, keep, drop = FALSE])
    qr_combined <- qr(combined)
    if (qr_combined$rank < ncol(combined)) {
      kept_names <- colnames(combined)[qr_combined$pivot[seq_len(qr_combined$rank)]]
      aliased <- setdiff(colnames(x_extra)[keep], kept_names)
      keep[aliased] <- FALSE
    }
  }

  keep
}

# Solve a symmetric positive-definite system, returning NULL rather than
# erroring when the matrix is numerically singular.
safe_quadratic_form <- function(u, v) {
  solved <- tryCatch(solve(v, u), error = function(e) NULL)
  if (is.null(solved)) return(NULL)
  as.numeric(crossprod(u, solved))
}

#' Compute the L3.4 score screen
#'
#' Fits only the simple model, then evaluates the complex model's
#' extra-parameter score at the embedded simple fit.
#'
#' @param dat Trial-level data frame from simulate_ambiguity_task().
#' @param cluster Name of the column identifying the clustering unit for the
#'   robust variance, or NULL for no clustered statistic.
#' @param simple_formula,complex_formula Model formulas; defaults come from
#'   R/fit_models.R so the screen tracks the fitted classes.
#'
#' @return A list with the per-observation score estimate, naive and clustered
#'   score-test statistics, and a per-block breakdown.
compute_score_screen <- function(
    dat,
    cluster = "id",
    simple_formula = simple_omitted_context_formula(),
    complex_formula = complex_omitted_context_formula()
) {
  prepared <- prepare_proxy_features(dat)

  # A single model frame for both designs guarantees the two matrices describe
  # the same rows, so the residuals of one align with the design of the other.
  all_vars <- unique(c(all.vars(simple_formula), all.vars(complex_formula)))
  if (!is.null(cluster)) all_vars <- unique(c(all_vars, cluster))
  model_data <- prepared[stats::complete.cases(prepared[, all_vars, drop = FALSE]), , drop = FALSE]

  x_simple <- stats::model.matrix(simple_formula, data = model_data)
  x_complex <- stats::model.matrix(complex_formula, data = model_data)
  extra_terms <- verify_nesting(x_simple, x_complex)

  y <- model_data[[all.vars(simple_formula)[1]]]

  simple_fit <- stats::glm.fit(
    x = x_simple,
    y = y,
    family = stats::binomial()
  )
  mu <- simple_fit$fitted.values
  residual <- y - mu
  weights_w <- mu * (1 - mu)

  x_extra <- x_complex[, extra_terms, drop = FALSE]
  keep <- drop_degenerate_columns(x_extra, x_simple)
  dropped_terms <- names(keep)[!keep]
  x_extra <- x_extra[, keep, drop = FALSE]
  extra_terms <- colnames(x_extra)

  if (ncol(x_extra) == 0) {
    stop(
      "No usable extra columns remain after removing constant or aliased terms.",
      call. = FALSE
    )
  }

  # Efficient score of the extra block at the embedded simple fit.
  u_total <- as.numeric(crossprod(x_extra, residual))
  names(u_total) <- extra_terms
  n_obs <- nrow(x_extra)

  # Residualise the extra design against the simple design in the GLM metric.
  # x_extra_resid carries the part of the extra columns the simple model cannot
  # already represent; the first-order condition of the simple fit means
  # crossprod(x_extra_resid, residual) equals u_total exactly.
  a_matrix <- crossprod(x_simple, x_simple * weights_w)
  b_matrix <- crossprod(x_simple, x_extra * weights_w)
  projection <- tryCatch(solve(a_matrix, b_matrix), error = function(e) NULL)
  if (is.null(projection)) {
    stop("Simple-model information matrix is singular; cannot residualise.", call. = FALSE)
  }
  x_extra_resid <- x_extra - x_simple %*% projection

  v_naive <- crossprod(x_extra_resid, x_extra_resid * weights_w)
  lm_naive <- safe_quadratic_form(u_total, v_naive)

  # Clustered score covariance. Trials share a participant's latent parameters,
  # so the independent-observation variance is anticonservative. A-009 makes the
  # comparison unit an explicit commitment; this reports the statistic at the
  # participant unit as well as the trial unit.
  lm_cluster <- NULL
  n_clusters <- NA_integer_
  if (!is.null(cluster) && cluster %in% names(model_data)) {
    cluster_id <- model_data[[cluster]]
    n_clusters <- length(unique(cluster_id))
    contributions <- rowsum(x_extra_resid * residual, group = cluster_id, reorder = FALSE)
    v_cluster <- crossprod(contributions)
    if (n_clusters > ncol(x_extra)) {
      lm_cluster <- safe_quadratic_form(u_total, v_cluster)
    }
  }

  blocks <- classify_extra_terms(extra_terms)
  block_rows <- lapply(unique(blocks), function(bl) {
    idx <- which(blocks == bl)
    u_bl <- u_total[idx]
    v_bl <- v_naive[idx, idx, drop = FALSE]
    stat_bl <- safe_quadratic_form(u_bl, v_bl)
    data.frame(
      block = bl,
      n_terms = length(idx),
      score_per_obs_l2 = sqrt(sum((u_bl / n_obs)^2)),
      score_stat = if (is.null(stat_bl)) NA_real_ else stat_bl,
      p_value = if (is.null(stat_bl)) NA_real_ else stats::pchisq(stat_bl, df = length(idx), lower.tail = FALSE),
      stringsAsFactors = FALSE
    )
  })

  list(
    score_per_obs = u_total / n_obs,
    simple_block_score_per_obs = as.numeric(crossprod(x_simple, residual)) / n_obs,
    extra_terms = extra_terms,
    dropped_terms = dropped_terms,
    n_obs = n_obs,
    n_clusters = n_clusters,
    df = ncol(x_extra),
    score_stat_naive = if (is.null(lm_naive)) NA_real_ else lm_naive,
    p_value_naive = if (is.null(lm_naive)) NA_real_ else stats::pchisq(lm_naive, df = ncol(x_extra), lower.tail = FALSE),
    score_stat_cluster = if (is.null(lm_cluster)) NA_real_ else lm_cluster,
    p_value_cluster = if (is.null(lm_cluster)) NA_real_ else stats::pchisq(lm_cluster, df = ncol(x_extra), lower.tail = FALSE),
    by_block = do.call(rbind, block_rows)
  )
}

#' Flatten a score screen into one row of simulation output
#'
#' @param screen Result of compute_score_screen().
#'
#' @return A one-row data frame suitable for cbind into a replication record.
score_screen_row <- function(screen) {
  out <- data.frame(
    score_screen_df = screen$df,
    score_screen_n_obs = screen$n_obs,
    score_screen_n_clusters = screen$n_clusters,
    score_stat_naive = screen$score_stat_naive,
    score_p_naive = screen$p_value_naive,
    score_stat_cluster = screen$score_stat_cluster,
    score_p_cluster = screen$p_value_cluster,
    score_per_obs_l2 = sqrt(sum(screen$score_per_obs^2)),
    stringsAsFactors = FALSE
  )

  for (i in seq_len(nrow(screen$by_block))) {
    bl <- screen$by_block$block[i]
    out[[paste0("score_p_block_", bl)]] <- screen$by_block$p_value[i]
    out[[paste0("score_per_obs_l2_block_", bl)]] <- screen$by_block$score_per_obs_l2[i]
  }

  out
}

#' Summarise score screens across replications
#'
#' @param results Data frame of replication rows carrying score-screen columns.
#' @param alpha Nominal level for the rejection-rate summaries.
summarise_score_screen <- function(results, alpha = 0.05) {
  out <- data.frame(n_runs = nrow(results))

  if ("score_p_naive" %in% names(results)) {
    out$score_reject_rate_naive <- mean(results$score_p_naive < alpha, na.rm = TRUE)
  }
  if ("score_p_cluster" %in% names(results)) {
    out$score_reject_rate_cluster <- mean(results$score_p_cluster < alpha, na.rm = TRUE)
  }
  if ("score_per_obs_l2" %in% names(results)) {
    out$mean_score_per_obs_l2 <- mean(results$score_per_obs_l2, na.rm = TRUE)
  }

  block_cols <- grep("^score_p_block_", names(results), value = TRUE)
  for (col in block_cols) {
    out[[sub("^score_p_block_", "score_reject_rate_block_", col)]] <-
      mean(results[[col]] < alpha, na.rm = TRUE)
  }

  out
}
