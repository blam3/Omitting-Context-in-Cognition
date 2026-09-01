find_repo_root <- function(start = getwd()) {
  path <- normalizePath(start, mustWork = TRUE)
  repeat {
    if (file.exists(file.path(path, "DESCRIPTION"))) return(path)
    parent <- dirname(path)
    if (parent == path) {
      stop("Could not locate repository root (no DESCRIPTION file found).")
    }
    path <- parent
  }
}

run_replication <- function(n, trials, context_range, context_effect, seed) {
  # Source helper functions when needed, using a relative path that works in both
  # package and script contexts
  helper_dir <- system.file("R", package = "OmittingContextInCognition")
  if (helper_dir == "") {
    # Fallback for development/script mode: the working directory varies
    # between callers (repo root for Rscript, tests/testthat for
    # testthat::test_dir()), so locate the repo root by walking up from cwd.
    helper_dir <- file.path(find_repo_root(), "R")
  }

  source(file.path(helper_dir, "dgm.R"))
  source(file.path(helper_dir, "fit_models.R"))
  source(file.path(helper_dir, "model_selection.R"))
  source(file.path(helper_dir, "metrics.R"))
  source(file.path(helper_dir, "score_screen.R"))
  
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

  # Theorem-aligned screen from Proposition L3.4 of the L3 KL dominance draft.
  # It runs alongside the AIC/BIC proxies but answers a different question: the
  # AIC/BIC columns say which model this sample selects, while the score screen
  # says whether the complex class is even capable of strictly lower divergence.
  # A screen failure is not evidence of no dominance, and a screen rejection is
  # not evidence of omitted context; see the header of R/score_screen.R.
  screen_row <- tryCatch(
    score_screen_row(compute_score_screen(dat, cluster = "id")),
    error = function(e) {
      warning("Score screen failed: ", conditionMessage(e), call. = FALSE)
      data.frame(score_screen_error = conditionMessage(e), stringsAsFactors = FALSE)
    }
  )

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
    ),
    screen_row
  )
}

coef_or_na <- function(fit_obj, term) {
  est <- fit_obj$estimate
  if (term %in% names(est)) return(unname(est[term]))
  NA_real_
}
