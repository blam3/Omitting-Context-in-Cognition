compute_aic_proxy <- function(fit_obj) {
  -2 * fit_obj$loglik + 2 * fit_obj$df
}

compute_bic_proxy <- function(fit_obj, n_obs) {
  -2 * fit_obj$loglik + log(n_obs) * fit_obj$df
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

  out <- data.frame(
    selected_by_bic_proxy = ifelse(candidate_bic < baseline_bic, candidate_fit$model_name, baseline_fit$model_name),
    selected_by_aic_proxy = ifelse(candidate_aic < baseline_aic, candidate_fit$model_name, baseline_fit$model_name),
    bic_diff_candidate_minus_baseline = candidate_bic - baseline_bic,
    aic_diff_candidate_minus_baseline = candidate_aic - baseline_aic,
    comparison_label = label
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
      simple_complex$selected_by_bic_proxy == complex_fit$model_name,
      "complex", "simple"
    ),
    selected_by_aic_proxy = ifelse(
      simple_complex$selected_by_aic_proxy == complex_fit$model_name,
      "complex", "simple"
    ),
    bic_diff_complex_minus_simple = simple_complex$bic_diff_candidate_minus_baseline,
    aic_diff_complex_minus_simple = simple_complex$aic_diff_candidate_minus_baseline,
    loglik_advantage_complex_minus_simple = simple_complex$loglik_advantage,
    loglik_advantage_per_obs_complex_minus_simple = simple_complex$loglik_advantage_per_obs,
    df_gap_complex_minus_simple = simple_complex$df_gap,
    aic_threshold_loglik_complex_minus_simple = simple_complex$aic_loglik_threshold,
    bic_threshold_loglik_complex_minus_simple = simple_complex$bic_loglik_threshold
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
          complex_context$selected_by_bic_proxy == reference_fit$model_name,
          "context", "complex"
        ),
        selected_by_aic_proxy_context_vs_complex = ifelse(
          complex_context$selected_by_aic_proxy == reference_fit$model_name,
          "context", "complex"
        ),
        bic_diff_context_minus_complex = complex_context$bic_diff_candidate_minus_baseline,
        aic_diff_context_minus_complex = complex_context$aic_diff_candidate_minus_baseline,
        loglik_advantage_context_minus_complex = complex_context$loglik_advantage,
        loglik_advantage_per_obs_context_minus_complex = complex_context$loglik_advantage_per_obs
      )
    )
  }

  out
}
