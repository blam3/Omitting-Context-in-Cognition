# Run from the repository root. No packages required.
source("R/dgm.R")
source("R/fit_models.R")
source("R/model_selection.R")

# The fixed-parameter DGM must lie exactly in each shared baseline's logit span.
# This checks a scientific invariant, not noisy coefficient recovery.
dat <- simulate_ambiguity_task(30, 60, context_effect = "none", seed = 902,
                              latent_heterogeneity = FALSE)
stopifnot(all(dat$theta == 0.75), all(dat$tau == 4), all(dat$theta_sd == 0))
fits <- list(fit_simple_omitted_context(dat), fit_complex_omitted_context(dat),
             fit_simple_contextual_true_family(dat))
truth_logit <- qlogis(dat$choice_prob)
for (fit in fits) {
  mm <- model.matrix(fit$fit)
  stopifnot(max(abs(qr.fitted(qr(mm), truth_logit) - truth_logit)) < 1e-10)
}
# Dropping the true interaction must fail this representation test.
old_mm <- model.matrix(~ value + probability + ambiguity + risky_value + ref_side, dat)
stopifnot(max(abs(qr.fitted(qr(old_mm), truth_logit) - truth_logit)) > 1e-3)
# Context mean-only control lies in the contextual proxy, while not in the simple one.
context_dat <- simulate_ambiguity_task(30, 60, context_effect = "moderate", seed = 903,
                                      latent_heterogeneity = FALSE)
context_fit <- fit_simple_contextual_true_family(context_dat)
mm <- model.matrix(context_fit$fit)
stopifnot(max(abs(qr.fitted(qr(mm), qlogis(context_dat$choice_prob)) -
                  qlogis(context_dat$choice_prob))) < 1e-10)
# Default heterogeneity remains on; no-context effect alone is not a fixed-effect null.
default_dat <- simulate_ambiguity_task(30, 60, context_effect = "none", seed = 902)
stopifnot(sd(default_dat$theta) > 0, sd(default_dat$tau) > 0)
# Realized likelihood thresholds, including the tie boundary.
base <- list(loglik = -100, df = 2)
threshold <- 0.5 * log(40)
tie <- list(loglik = -100 + threshold, df = 3)
win <- list(loglik = -100 + threshold + 0.1, df = 3)
stopifnot(abs(compute_bic_proxy(tie, 40)-compute_bic_proxy(base, 40)) < 1e-12)
stopifnot(compute_bic_proxy(win, 40) < compute_bic_proxy(base, 40))
cat("Shared-baseline representation, negative control, heterogeneity and threshold checks passed.\n")
