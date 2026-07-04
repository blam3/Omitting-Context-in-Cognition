# Candidate model wrappers.
#
# These are deliberately lightweight proxy models for smoke tests and fast
# screening. They are not substitutes for the final hierarchical Bayesian
# ambiguity models. Their role is to keep the autonomous researcher loop aligned
# with the current theory: compare context-omitting simplicity, context-omitting
# false complexity, and context-aware simplicity.

prepare_proxy_features <- function(dat) {
  required <- c("choice", "value", "probability", "ambiguity", "ses")
  missing <- setdiff(required, names(dat))
  if (length(missing) > 0) {
    stop("Missing required columns: ", paste(missing, collapse = ", "))
  }

  if (!"ref_side" %in% names(dat)) dat$ref_side <- 0
  if (!"condition" %in% names(dat)) dat$condition <- factor("baseline")
  if (!"color_cue" %in% names(dat)) dat$color_cue <- factor("unknown")

  dat$condition <- factor(dat$condition)
  dat$color_cue <- factor(dat$color_cue)

  dat$risky_value <- dat$value * dat$probability
  dat$ambiguous_value <- -0.5 * dat$value * dat$ambiguity
  dat$sv_base <- dat$risky_value + dat$ambiguous_value
  dat$ambiguity_sq_value <- -0.5 * dat$value * dat$ambiguity^2
  dat$ses_ambiguous_value <- dat$ses * dat$ambiguous_value

  dat
}

fit_glm_binomial <- function(formula, dat, model_name) {
  fit <- glm(formula, data = dat, family = binomial())
  ll <- logLik(fit)

  list(
    model_name = model_name,
    fit = fit,
    estimate = coef(fit),
    loglik = as.numeric(ll),
    df = attr(ll, "df")
  )
}

fit_simple_omitted_context <- function(dat) {
  dat <- prepare_proxy_features(dat)

  # One-parameter-style ambiguity-value proxy with no contextual predictors.
  fit_glm_binomial(
    choice ~ value + probability + ambiguity + sv_base + ref_side,
    dat = dat,
    model_name = "simple_omitted_context"
  )
}

fit_complex_omitted_context <- function(dat) {
  dat <- prepare_proxy_features(dat)

  # Psychologically plausible but false complexity in the current DGM: condition,
  # color/source cues, and nonlinear ambiguity can absorb context-induced
  # residual structure even though no true source/color mechanism generated it.
  fit_glm_binomial(
    choice ~ value + probability + ambiguity + sv_base + ambiguous_value +
      ambiguity_sq_value + condition + color_cue + ref_side,
    dat = dat,
    model_name = "complex_omitted_context"
  )
}

fit_simple_contextual_true_family <- function(dat) {
  dat <- prepare_proxy_features(dat)

  # Context-aware simple proxy. The key term is ses:ambiguous_value, which lets
  # SES shift the latent ambiguity-aversion contribution without adding a new
  # cognitive architecture.
  fit_glm_binomial(
    choice ~ value + probability + ambiguity + sv_base + ses +
      ses_ambiguous_value + ref_side,
    dat = dat,
    model_name = "simple_contextual_reference"
  )
}

fit_context_mean_variance_proxy <- function(dat) {
  dat <- prepare_proxy_features(dat)

  # Fast diagnostic proxy for the theorem's mean-plus-variance route. GLM cannot
  # estimate latent heteroskedasticity directly, so this uses coarse SES bins and
  # SES-by-ambiguity interactions as a screening model before Stan/brms work.
  dat$ses_bin <- cut(
    dat$ses,
    breaks = quantile(dat$ses, probs = c(0, 1/3, 2/3, 1), na.rm = TRUE),
    include.lowest = TRUE,
    labels = c("low", "mid", "high")
  )

  fit_glm_binomial(
    choice ~ value + probability + ambiguity + sv_base + ses_bin * ambiguous_value + ref_side,
    dat = dat,
    model_name = "context_mean_variance_proxy"
  )
}
