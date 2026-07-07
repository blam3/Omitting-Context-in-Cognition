run_replication <- function(n, trials, context_range, context_effect, seed) {
  # Source helper functions when needed, using a relative path that works in both
  # package and script contexts
  helper_dir <- system.file("R", package = "OmittingContextInCognition")
  if (helper_dir == "") {
    # Fallback for development/script mode
    helper_dir <- dirname(rlang::caller_source())
  }
  
  source(file.path(helper_dir, "dgm.R"))
  source(file.path(helper_dir, "fit_models.R"))
  source(file.path(helper_dir, "model_selection.R"))
  source(file.path(helper_dir, "metrics.R"))
  
  dat <- simulate_ambiguity_task(
    n = n,
    trials = trials,
    context_range = context_range,
    context_effect = context_effect,
    seed = seed
  )

  simple_fit <- fit_simple_omitted_context(dat)
  complex_fit <- fit_complex_omitted_context(dat)
  reference_fit <- fit_simple_contextual_true_family(dat)

  comp <- compare_models_proxy(
    simple_fit = simple_fit,
    complex_fit = complex_fit,
    reference_fit = reference_fit,
    n_obs = nrow(dat)
  )

  truth <- attr(dat, "truth")

  cbind(
    data.frame(
      n = n,
      trials = trials,
      context_range = context_range,
      context_effect = context_effect,
      seed = seed,
      true_context_mean_effect = truth$context_mean_effect,
      true_context_log_sd_effect = truth$context_log_sd_effect
    ),
    comp,
    data.frame(
      simple_value_coef = coef_or_na(simple_fit, "value"),
      complex_value_coef = coef_or_na(complex_fit, "value"),
      reference_value_coef = coef_or_na(reference_fit, "value"),
      complex_nonlinear_ambiguity_coef = coef_or_na(complex_fit, "ambiguity_sq_value"),
      reference_ses_ambiguity_coef = coef_or_na(reference_fit, "ses_ambiguous_value")
    )
  )
}

coef_or_na <- function(fit_obj, term) {
  est <- fit_obj$estimate
  if (term %in% names(est)) return(unname(est[term]))
  NA_real_
}
