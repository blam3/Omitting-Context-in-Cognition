# Candidate model wrappers.
# These are placeholders. Replace with brms/rstan/cmdstanr/custom likelihoods as the project matures.

fit_simple_omitted_context <- function(dat) {
  # Omitted-context one-parameter model.
  fit <- glm(choice ~ value + ambiguity, data = dat, family = binomial())
  list(
    model_name = "simple_omitted_context",
    fit = fit,
    estimate = coef(fit),
    loglik = as.numeric(logLik(fit)),
    df = attr(logLik(fit), "df")
  )
}

fit_complex_omitted_context <- function(dat) {
  # Omitted-context two-parameter proxy model.
  # Here the interaction is a placeholder for a more flexible ambiguity model.
  fit <- glm(choice ~ value * ambiguity, data = dat, family = binomial())
  list(
    model_name = "complex_omitted_context",
    fit = fit,
    estimate = coef(fit),
    loglik = as.numeric(logLik(fit)),
    df = attr(logLik(fit), "df")
  )
}

fit_simple_contextual_true_family <- function(dat) {
  # Contextual model included as an oracle/reference model, not necessarily part of the omitted-context contest.
  fit <- glm(choice ~ value + ambiguity + ses:value, data = dat, family = binomial())
  list(
    model_name = "simple_contextual_reference",
    fit = fit,
    estimate = coef(fit),
    loglik = as.numeric(logLik(fit)),
    df = attr(logLik(fit), "df")
  )
}
