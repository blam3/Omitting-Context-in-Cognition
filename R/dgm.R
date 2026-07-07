# Data-generating mechanisms for the omitted-context cognitive-model project.
#
# The simulation is intentionally lightweight so smoke tests can run without
# Stan/brms. It now mirrors the current project thesis more closely than the
# original placeholder: context shifts both the mean and dispersion of a latent
# ambiguity-aversion parameter, and the analyst can then compare a simple
# context-omitting model, a complex context-omitting model, and a simple
# context-aware reference model.

#' Simulate Context
#'
#' @param n Number of context values to simulate
#' @param context_range Either "unrestricted" or "range_restricted"
#' @param seed Random seed for reproducibility
#'
#' @export
simulate_context <- function(
    n,
    context_range = c("unrestricted", "range_restricted"),
    seed = NULL
) {
  context_range <- match.arg(context_range)
  if (!is.null(seed)) set.seed(seed)

  if (context_range == "unrestricted") {
    ses <- rnorm(n, mean = 0, sd = 1)
  } else {
    ses <- pmin(pmax(rnorm(n, mean = 0, sd = 1), -0.5), 0.5)
  }

  ses
}

context_effect_parameters <- function(context_effect = c("none", "weak", "moderate", "strong")) {
  context_effect <- match.arg(context_effect)

  switch(
    context_effect,
    none = list(mean = 0.00, log_sd = 0.00),
    weak = list(mean = -0.25, log_sd = 0.15),
    moderate = list(mean = -0.50, log_sd = 0.30),
    strong = list(mean = -0.80, log_sd = 0.50)
  )
}

simulate_trial_design <- function(trials, seed = NULL) {
  if (!is.null(seed)) set.seed(seed)

  data.frame(
    trial = seq_len(trials),
    probability = runif(trials, min = 0.20, max = 0.80),
    ambiguity = runif(trials, min = 0.00, max = 0.80),
    value = runif(trials, min = 0.25, max = 1.00),
    ref_side = sample(c(-0.5, 0.5), size = trials, replace = TRUE),
    condition = factor(sample(c("baseline", "source_a", "source_b"), size = trials, replace = TRUE)),
    color_cue = factor(sample(c("blue", "red", "yellow"), size = trials, replace = TRUE))
  )
}

#' Simulate Ambiguity Task
#'
#' @param n Number of participants
#' @param trials Number of trials per participant
#' @param context_range Either "unrestricted" or "range_restricted"
#' @param context_effect Strength of context effect
#' @param seed Random seed
#' @param design Study design of the decision-making task
#'
#' @export
simulate_ambiguity_task <- function(
    n,
    trials,
    context_range = c("unrestricted", "range_restricted"),
    context_effect = c("none", "weak", "moderate", "strong"),
    seed = NULL,
    design = NULL
) {
  context_range <- match.arg(context_range)
  context_effect <- match.arg(context_effect)
  if (!is.null(seed)) set.seed(seed)

  ses <- simulate_context(n, context_range = context_range)
  effect <- context_effect_parameters(context_effect)

  # Latent ambiguity aversion. Negative SES effects mean lower-SES participants
  # are, on average, more ambiguity averse when SES is coded high = advantaged.
  # The log-SD term makes low-SES participants more heterogeneous, matching the
  # current theorem route in which omission induces apparent mixture or
  # heteroskedastic structure.
  theta_sd_i <- exp(log(0.25) + effect$log_sd * (-ses))
  theta_i <- 0.75 + effect$mean * ses + rnorm(n, mean = 0, sd = theta_sd_i)

  # Choice sensitivity is individual-varying but not the target construct here.
  tau_i <- exp(log(4.0) + rnorm(n, mean = 0, sd = 0.15))

  if (is.null(design)) {
    design <- simulate_trial_design(trials)
  } else {
    stopifnot(all(c("probability", "ambiguity", "value") %in% names(design)))
    if (!"trial" %in% names(design)) design$trial <- seq_len(nrow(design))
    if (!"ref_side" %in% names(design)) design$ref_side <- 0
    if (!"condition" %in% names(design)) design$condition <- factor("baseline")
    if (!"color_cue" %in% names(design)) design$color_cue <- factor("unknown")
    trials <- nrow(design)
  }

  dat <- expand.grid(id = seq_len(n), trial = seq_len(trials))
  match_idx <- match(dat$trial, design$trial)

  dat$probability <- design$probability[match_idx]
  dat$ses <- ses[dat$id]
  dat$theta <- theta_i[dat$id]
  dat$theta_sd <- theta_sd_i[dat$id]
  dat$tau <- tau_i[dat$id]
  dat$ambiguity <- design$ambiguity[match_idx]
  dat$value <- design$value[match_idx]
  dat$ref_side <- design$ref_side[match_idx]
  dat$condition <- factor(design$condition[match_idx])
  dat$color_cue <- factor(design$color_cue[match_idx])

  # Standard ambiguity-value form: SV = v * (p - beta_i * A / 2).
  dat$risky_value <- dat$value * dat$probability
  dat$ambiguous_value <- -0.5 * dat$value * dat$ambiguity
  dat$sv_true <- dat$value * (dat$probability - dat$theta * dat$ambiguity / 2)

  # No true source/color cognitive parameter is included. Apparent source/color
  # effects in complex omitted-context models are therefore false-complexity
  # absorbers in this DGM.
  linpred <- -0.10 + dat$tau * dat$sv_true + 0.10 * dat$ref_side
  dat$choice_prob <- plogis(linpred)
  dat$choice <- rbinom(nrow(dat), size = 1, prob = dat$choice_prob)

  attr(dat, "truth") <- list(
    dgm = "simple_contextual_ambiguity",
    context_effect = context_effect,
    context_mean_effect = effect$mean,
    context_log_sd_effect = effect$log_sd,
    false_complex_terms = c("condition", "color_cue", "nonlinear_ambiguity")
  )

  dat
}
