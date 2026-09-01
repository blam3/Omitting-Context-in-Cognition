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

  dat <- na.omit(dat)
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

# Candidate-model formulas.
#
# The formulas are exposed as functions rather than written inline in each
# fitting wrapper so that the score screen in R/score_screen.R evaluates the
# same model classes the loop actually fits. Proposition L3.4 of
# docs/proofs/L3_kl_dominance.md is a statement about M_S embedded in M_K; if
# the screen and the fits could drift apart, the screened quantity would no
# longer be the score of the fitted complex model.

simple_omitted_context_formula <- function() {
  # `ambiguous_value` is part of M_S by PI decision on 2026-09-01. The DGM sets
  # sv_true = risky_value + theta * ambiguous_value, so the term is true rather
  # than false complexity; leaving it out of M_S made the complex-versus-simple
  # contrast conflate recovering a true main effect with false complexity. With
  # it retained here, M_K's extra block is exactly the condition, colour, and
  # nonlinear-ambiguity terms that A-004 designates as absorbers.
  choice ~ value + probability + ambiguity + risky_value + ambiguous_value +
    ref_side
}

complex_omitted_context_formula <- function() {
  choice ~ value + probability + ambiguity + risky_value + ambiguous_value +
    ambiguity_sq_value + condition + color_cue + ref_side
}

simple_contextual_formula <- function() {
  # Carries the same `ambiguous_value` main effect as M_S. The model ladder
  # defines M2 as M1 plus context terms, so omitting the main effect here while
  # M_S retains it would leave the context-aware reference strictly worse
  # specified than its own baseline and would make the context-versus-complex
  # comparison incoherent. It also restores the usual pairing of an interaction
  # with its main effect, since ses_ambiguous_value is ses * ambiguous_value.
  choice ~ value + probability + ambiguity + risky_value + ambiguous_value +
    ses + ses_ambiguous_value + ref_side
}

fit_simple_omitted_context <- function(dat) {
  dat <- prepare_proxy_features(dat)

  # One-parameter-style ambiguity-value proxy with no contextual predictors.
  fit_glm_binomial(
    simple_omitted_context_formula(),
    dat = dat,
    model_name = "simple_omitted_context"
  )
}

fit_complex_omitted_context <- function(dat) {
  dat <- prepare_proxy_features(dat)

  # Psychologically plausible but false complexity in the current DGM: condition,
  # color/source cues, and nonlinear ambiguity can absorb context-induced
  # residual structure even though no true source/color mechanism generated it.
  #
  # The L3.4 score screen found on 2026-09-01 that `ambiguous_value` is a true
  # term rather than an absorber, and the PI moved it into M_S the same day. The
  # extra block relative to M_S is now exactly the condition, colour, and
  # nonlinear-ambiguity terms A-004 covers, so a complex-versus-simple win here
  # no longer conflates true-term recovery with false complexity.
  fit_glm_binomial(
    complex_omitted_context_formula(),
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
    simple_contextual_formula(),
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
    breaks = unique(quantile(dat$ses, probs = c(0, 1/3, 2/3, 1), na.rm = TRUE)),
    include.lowest = TRUE,
    labels = c("low", "mid", "high")
  )

  fit_glm_binomial(
    choice ~ value + probability + ambiguity + risky_value + ses_bin * ambiguous_value + ref_side,
    dat = dat,
    model_name = "context_mean_variance_proxy"
  )
}
