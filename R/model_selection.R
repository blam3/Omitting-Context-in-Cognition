compute_aic_proxy <- function(fit_obj) {
  -2 * fit_obj$loglik + 2 * fit_obj$df
}

compute_bic_proxy <- function(fit_obj, n_obs) {
  -2 * fit_obj$loglik + log(n_obs) * fit_obj$df
}

# Robust model-name extractor -------------------------------------------------
# Many internal helpers return wrapper lists that include model_name, but raw
# fitted objects (glm/lm/stanfit) do not. safe_model_name() tries sensible
# fallbacks so downstream selection labels are always readable.
safe_model_name <- function(fit_obj, fallback = NA_character_) {
  if (is.list(fit_obj) && !is.null(fit_obj$model_name)) return(as.character(fit_obj$model_name))
  if (is.list(fit_obj) && !is.null(fit_obj$fit) && is.list(fit_obj$fit) && !is.null(fit_obj$fit$model_name)) {
    return(as.character(fit_obj$fit$model_name))
  }
  mn_attr <- attr(fit_obj, "model_name")
  if (!is.null(mn_attr)) return(as.character(mn_attr))

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

  if (is.list(fit_obj) && !is.null(fit_obj$fit)) return(paste0("<", paste(class(fit_obj$fit), collapse = ","), ">"))
  if (!is.null(class(fit_obj))) return(paste0("<", paste(class(fit_obj), collapse = ","), ">"))
  fallback
}

compute_loglik_advantage <- function(candidate_fit, baseline_fit, n_obs) {
  data.frame(
    loglik_advantage = candidate_fit$loglik - baseline_fit$loglik,
    loglik_advantage_per_obs = (candidate_fit$loglik - baseline_fit$loglik) / n_obs,
    df_gap = candidate_fit$df - baseline_fit$df,
    aic_loglik_threshold = candidate_fit$df - baseline_fit$df,
    bic_loglik_threshold = 0.5 * log(n_obs) * (candidate_fit$df - baseline_fit$df)
  )
}

compare_pair_proxy <- function(baseline_fit, candidate_fit, n_obs, label) {
  baseline_bic <- compute_bic_proxy(baseline_fit, n_obs)
  candidate_bic <- compute_bic_proxy(candidate_fit, n_obs)
  baseline_aic <- compute_aic_proxy(baseline_fit)
  candidate_aic <- compute_aic_proxy(candidate_fit)
  adv <- compute_loglik_advantage(candidate_fit, baseline_fit, n_obs)

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
