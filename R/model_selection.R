compute_aic_proxy <- function(fit_obj) {
  -2 * fit_obj$loglik + 2 * fit_obj$df
}

compute_bic_proxy <- function(fit_obj, n_obs) {
  -2 * fit_obj$loglik + log(n_obs) * fit_obj$df
}

# Compute simple log-likelihood and per-observation advantage diagnostics.
compute_loglik_advantage <- function(candidate_fit, baseline_fit, n_obs) {
  data.frame(
    loglik_advantage = candidate_fit$loglik - baseline_fit$loglik,
    loglik_advantage_per_obs = (candidate_fit$loglik - baseline_fit$loglik) / n_obs,
    df_gap = candidate_fit$df - baseline_fit$df,
    aic_loglik_threshold = candidate_fit$df - baseline_fit$df,
    bic_loglik_threshold = 0.5 * log(n_obs) * (candidate_fit$df - baseline_fit$df)
  )
}

# Robust model-name extractor -------------------------------------------------
# Many internal helper functions in this package return a wrapper list that
# includes a `model_name` element (e.g., list(model_name = "foo", fit = ..., ...)).
# However, callers might pass raw modeling objects (glm/lm/stanfit) that do not
# carry a `$model_name` field. To avoid NULL dereference and confusing empty
# labels in downstream comparisons, `safe_model_name()` attempts several fallbacks
# in order:
#  1) fit_obj$model_name (wrapper lists produced by our fit_* helpers)
#  2) fit_obj$fit$model_name (nested wrappers)
#  3) attr(fit_obj, "model_name") (explicit attribute)
#  4) a compact class/formula-based label for common model objects (glm/lm)
#  5) a class-based fallback like "<glm>" or "<stanfit>"
#  6) the user-specified `fallback` string (default NA_character_)
# This ensures `compare_pair_proxy()` and related utilities can produce useful
# human-readable labels even when the input is a bare fitted model object.
safe_model_name <- function(fit_obj, fallback = NA_character_) {
  # 1) direct wrapper list
  if (is.list(fit_obj) && !is.null(fit_obj$model_name)) return(as.character(fit_obj$model_name))

  # 2) nested wrapper (e.g., list(fit = <glm>, model_name = ...))
  if (is.list(fit_obj) && !is.null(fit_obj$fit) && is.list(fit_obj$fit) && !is.null(fit_obj$fit$model_name)) {
    return(as.character(fit_obj$fit$model_name))
  }

  # 3) attribute
  mn_attr <- attr(fit_obj, "model_name")
  if (!is.null(mn_attr)) return(as.character(mn_attr))

  # 4) try to build a compact label from the formula for common fitted objects
  try_formula_label <- tryCatch({
    if (inherits(fit_obj, "glm") || inherits(fit_obj, "lm")) {
      paste0(class(fit_obj)[1], ":", paste(deparse(formula(fit_obj)), collapse = ""))
    } else if (is.list(fit_obj) && !is.null(fit_obj$fit) && (inherits(fit_obj$fit, "glm") || inherits(fit_obj$fit, "lm"))) {
      paste0(class(fit_obj$fit)[1], ":", paste(deparse(formula(fit_obj$fit)), collapse = ""))
    } else {
      NULL
    }
  }, error = function(e) NULL)
  if (!is.null(try_formula_label)) return(try_formula_label)

  # 5) class-based fallback
  if (is.list(fit_obj) && !is.null(fit_obj$fit)) return(paste0("<", paste(class(fit_obj$fit), collapse = ","), ">" ) )
  if (!is.null(class(fit_obj))) return(paste0("<", paste(class(fit_obj), collapse = ","), ">"))

  # 6) final fallback
  fallback
}

# Compare two fitted objects and return AIC/BIC-based selection labels.
compare_pair_proxy <- function(baseline_fit, candidate_fit, n_obs, label) {
  baseline_bic <- compute_bic_proxy(baseline_fit, n_obs)
  candidate_bic <- compute_bic_proxy(candidate_fit, n_obs)
  baseline_aic <- compute_aic_proxy(baseline_fit)
  candidate_aic <- compute_aic_proxy(candidate_fit)
  adv <- compute_loglik_advantage(candidate_fit, baseline_fit, n_obs)

  # Use safe_model_name() to avoid assuming a $model_name field exists on the
  # provided objects. If we used candidate_fit$model_name directly, callers that
  # passed a plain glm/lm/stanfit would get NULL and the resulting labels would
  # be empty or cause errors. This function therefore builds readable labels and
  # still works with both our wrapper lists (which include model_name) and
  # bare fitted-model objects.
  cand_name <- safe_model_name(candidate_fit, fallback = "candidate")
  base_name <- safe_model_name(baseline_fit, fallback = "baseline")

  out <- data.frame(
    selected_by_bic_proxy = ifelse(candidate_bic < baseline_bic, cand_name, base_name),
    selected_by_aic_proxy = ifelse(candidate_aic < baseline_aic, cand_name, base_name),
    bic_diff_candidate_minus_baseline = candidate_bic - baseline_bic,
    aic_diff_candidate_minus_baseline = candidate_aic - baseline_aic,
    comparison_label = label,
    stringsAsFactors = FALSE
  )

  cbind(out, adv)
}

compare_models_proxy <- function(simple_fit, complex_fit, n_obs, reference_fit = NULL) {
  # AIC/BIC are only fast proxies for the current scaffold. Final analyses should
  # use PSIS-LOO, held-out participant log score, and simulation-calibrated
  # thresholds. These proxy columns operationalize the theorem's finite-sample
  # condition: the false-complex model wins only when its log-likelihood gain
  # exceeds the relevant penalty for added flexibility.
  simple_complex <- compare_pair_proxy(
    baseline_fit = simple_fit,
    candidate_fit = complex_fit,
    n_obs = n_obs,
    label = "complex_vs_simple"
  )

  out <- data.frame(
    selected_by_bic_proxy = ifelse(
      simple_complex$selected_by_bic_proxy == safe_model_name(complex_fit, "complex"),
      "complex", "simple"
    ),
    selected_by_aic_proxy = ifelse(
      simple_complex$selected_by_aic_proxy == safe_model_name(complex_fit, "complex"),
      "complex", "simple"
    ),
    bic_diff_complex_minus_simple = simple_complex$bic_diff_candidate_minus_baseline,
    aic_diff_complex_minus_simple = simple_complex$aic_diff_candidate_minus_baseline,
    loglik_advantage_complex_minus_simple = simple_complex$loglik_advantage,
    loglik_advantage_per_obs_complex_minus_simple = simple_complex$loglik_advantage_per_obs,
    df_gap_complex_minus_simple = simple_complex$df_gap,
    aic_threshold_loglik_complex_minus_simple = simple_complex$aic_loglik_threshold,
    bic_threshold_loglik_complex_minus_simple = simple_complex$bic_loglik_threshold,
    stringsAsFactors = FALSE
  )

  if (!is.null(reference_fit)) {
    complex_context <- compare_pair_proxy(
      baseline_fit = complex_fit,
      candidate_fit = reference_fit,
      n_obs = n_obs,
      label = "context_vs_complex"
    )

    out <- cbind(
      out,
      data.frame(
        selected_by_bic_proxy_context_vs_complex = ifelse(
          complex_context$selected_by_bic_proxy == safe_model_name(reference_fit, "context"),
          "context", "complex"
        ),
        selected_by_aic_proxy_context_vs_complex = ifelse(
          complex_context$selected_by_aic_proxy == safe_model_name(reference_fit, "context"),
          "context", "complex"
        ),
        bic_diff_context_minus_complex = complex_context$bic_diff_candidate_minus_baseline,
        aic_diff_context_minus_complex = complex_context$aic_diff_candidate_minus_baseline,
        loglik_advantage_context_minus_complex = complex_context$loglik_advantage,
        loglik_advantage_per_obs_context_minus_complex = complex_context$loglik_advantage_per_obs,
        stringsAsFactors = FALSE
      )
    )
  }

  out
}
