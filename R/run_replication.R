source("R/dgm.R")
source("R/fit_models.R")
source("R/model_selection.R")
source("R/metrics.R")

run_replication <- function(n, trials, context_range, context_effect, seed) {
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

  comp <- compare_models_proxy(simple_fit, complex_fit, n_obs = nrow(dat))

  cbind(
    data.frame(
      n = n,
      trials = trials,
      context_range = context_range,
      context_effect = context_effect,
      seed = seed
    ),
    comp,
    data.frame(
      simple_value_coef = unname(simple_fit$estimate["value"]),
      complex_value_coef = unname(complex_fit$estimate["value"]),
      reference_value_coef = unname(reference_fit$estimate["value"])
    )
  )
}
