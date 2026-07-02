# Data-generating mechanisms for the embedded cognition model-selection project.

simulate_context <- function(n, context_range = c("unrestricted", "range_restricted"), seed = NULL) {
  context_range <- match.arg(context_range)
  if (!is.null(seed)) set.seed(seed)
  if (context_range == "unrestricted") {
    ses <- rnorm(n, mean = 0, sd = 1)
  } else {
    ses <- pmin(pmax(rnorm(n, mean = 0, sd = 1), -0.5), 0.5)
  }
  ses
}

simulate_ambiguity_task <- function(
    n,
    trials,
    context_range = c("unrestricted", "range_restricted"),
    context_effect = c("weak", "strong"),
    seed = NULL
) {
  context_range <- match.arg(context_range)
  context_effect <- match.arg(context_effect)
  if (!is.null(seed)) set.seed(seed)

  ses <- simulate_context(n, context_range = context_range)
  beta_ses <- if (context_effect == "weak") 0.25 else 0.75

  # Placeholder true one-parameter contextual model.
  # Replace this with the actual ambiguity-attitude task and likelihood.
  theta_i <- 0.0 + beta_ses * ses + rnorm(n, 0, 0.25)

  trial_ambiguity <- runif(trials, min = 0, max = 1)
  trial_value <- runif(trials, min = -1, max = 1)

  dat <- expand.grid(id = seq_len(n), trial = seq_len(trials))
  dat$ses <- ses[dat$id]
  dat$theta <- theta_i[dat$id]
  dat$ambiguity <- trial_ambiguity[dat$trial]
  dat$value <- trial_value[dat$trial]

  # Placeholder binary choice process.
  linpred <- dat$theta * dat$value - 0.5 * dat$ambiguity
  dat$choice_prob <- plogis(linpred)
  dat$choice <- rbinom(nrow(dat), size = 1, prob = dat$choice_prob)

  dat
}
