compute_aic_proxy <- function(fit_obj) {
  -2 * fit_obj$loglik + 2 * fit_obj$df
}

compute_bic_proxy <- function(fit_obj, n_obs) {
  -2 * fit_obj$loglik + log(n_obs) * fit_obj$df
}

compare_models_proxy <- function(simple_fit, complex_fit, n_obs) {
  # Placeholders:
  # - BIC difference can approximate log Bayes factor under regular conditions.
  # - AIC is used only as a placeholder for LOOIC until Bayesian model fitting is implemented.
  simple_bic <- compute_bic_proxy(simple_fit, n_obs)
  complex_bic <- compute_bic_proxy(complex_fit, n_obs)
  simple_aic <- compute_aic_proxy(simple_fit)
  complex_aic <- compute_aic_proxy(complex_fit)

  data.frame(
    selected_by_bic_proxy = ifelse(complex_bic < simple_bic, "complex", "simple"),
    selected_by_aic_proxy = ifelse(complex_aic < simple_aic, "complex", "simple"),
    bic_diff_complex_minus_simple = complex_bic - simple_bic,
    aic_diff_complex_minus_simple = complex_aic - simple_aic
  )
}
