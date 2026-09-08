# Numerical harness for the OCECM theorem package.
#
# Every analytic claim in docs/theorems/ that can be evaluated numerically has a
# function here and an assertion in tests/testthat/test-theorem-numerics.R. The
# point is to make a wrong theorem statement fail CI rather than survive review.
#
# Notation follows docs/notation_registry.md.

# --- response laws ---------------------------------------------------------

# Omitted-context marginal response within one context cell (Corollary T-003b):
# P(Y = 1 | A = a, Z = z) = Phi((b0 + mu(z) a) / sqrt(1 + sigma^2(z) a^2)).
p_cell <- function(a, b0, mu, sigma2) {
  pnorm((b0 + mu * a) / sqrt(1 + sigma2 * a^2))
}

# Target of model comparison: mixture over a finite context support.
p0_mixture <- function(a, b0, mu, sigma2, pi) {
  stopifnot(length(mu) == length(sigma2), length(mu) == length(pi))
  rowSums(vapply(seq_along(pi), function(k) pi[k] * p_cell(a, b0, mu[k], sigma2[k]),
                 numeric(length(a))))
}

# Monte Carlo evaluation of the same object straight from the kernel, used to
# check the closed form rather than assume it.
p_cell_mc <- function(a, b0, mu, sigma2, draws = 2e5, seed = 1) {
  set.seed(seed)
  theta <- rnorm(draws, mu, sqrt(sigma2))
  vapply(a, function(ai) mean(pnorm(b0 + theta * ai)), numeric(1))
}

# --- divergence and model classes ------------------------------------------

kl_design <- function(p0, p, q) {
  p <- pmin(pmax(p, 1e-12), 1 - 1e-12)
  sum(q * (p0 * log(p0 / p) + (1 - p0) * log((1 - p0) / (1 - p))))
}

# M_S: three-parameter Gaussian random-ambiguity-sensitivity probit (A-009).
m_s_predict <- function(par, a) p_cell(a, par[1], par[2], par[3]^2)

# M_K^flex: nonlinear-ambiguity probit (A-009).
m_k_flex_predict <- function(par, a) {
  pnorm((par[1] + par[2] * a + par[3] * a^2) / sqrt(1 + par[4]^2 * a^2))
}

# M_K^mix: two-component latent-class mixture (A-009).
m_k_mix_predict <- function(par, a) {
  w <- plogis(par[7])
  w * p_cell(a, par[1], par[2], par[3]^2) +
    (1 - w) * p_cell(a, par[4], par[5], par[6]^2)
}

inf_kl <- function(p0, a, q, predict_fn, n_par, restarts = 40, seed = 7) {
  set.seed(seed)
  best <- Inf
  for (i in seq_len(restarts)) {
    start <- rnorm(n_par, 0, 1.5)
    fit <- try(optim(start, function(par) kl_design(p0, predict_fn(par, a), q),
                     method = "Nelder-Mead",
                     control = list(maxit = 20000, reltol = 1e-14)), silent = TRUE)
    if (!inherits(fit, "try-error")) best <- min(best, fit$value)
  }
  max(best, 0)
}

# --- Lemma T-004a: decidable membership criterion for M_S -------------------
#
# p in M_S  <=>  exists s^2 >= 0 such that a -> Phi^{-1}(p(a)) sqrt(1 + s^2 a^2)
# is affine on the design support. Returns the minimised affine residual: zero
# certifies membership, strictly positive certifies non-representability.
affine_residual <- function(p0, a, restarts = 40, seed = 11) {
  g <- qnorm(p0)
  X <- cbind(1, a)
  obj <- function(t) {
    h <- g * sqrt(1 + t[1]^2 * a^2)
    sum(residuals(lm.fit(X, h))^2)
  }
  set.seed(seed)
  best <- Inf
  for (i in seq_len(restarts)) {
    fit <- try(optim(rnorm(1, 0, 1.5), obj, method = "BFGS"), silent = TRUE)
    if (!inherits(fit, "try-error")) best <- min(best, fit$value)
  }
  max(best, 0)
}

# --- Proposition T-004d: Gaussian mean heterogeneity is absorbed ------------
#
# With sigma^2 constant and mu(Z) ~ N(mubar, omega2), the mixture collapses to a
# member of M_S with s^2 = sigma^2 + omega2. Computed by quadrature so the claim
# is checked, not assumed.
p0_gaussian_mean <- function(a, b0, mubar, omega2, sigma2) {
  vapply(a, function(ai) {
    integrate(function(m) dnorm(m, mubar, sqrt(omega2)) * p_cell(ai, b0, m, sigma2),
              lower = mubar - 12 * sqrt(omega2), upper = mubar + 12 * sqrt(omega2),
              rel.tol = 1e-12)$value
  }, numeric(1))
}

# --- T-007: finite-sample thresholds ---------------------------------------

# T-007a exact algebra, in terms of the REALISED log-likelihood difference D_n.
aic_favours_complex <- function(D_n, k_complex, k_simple) D_n > (k_complex - k_simple)
bic_favours_complex <- function(D_n, k_complex, k_simple, n) {
  D_n > 0.5 * (k_complex - k_simple) * log(n)
}

# T-007b' minimum sample size: solve n dl - z sqrt(n) omega - dk = 0 for sqrt(n).
aic_crossover_n <- function(delta_ell_star, omega, delta_k, alpha = 0.05) {
  stopifnot(delta_ell_star > 0)
  z <- qnorm(1 - alpha)
  disc <- z^2 * omega^2 + 4 * delta_ell_star * delta_k
  root <- (z * omega + sqrt(disc)) / (2 * delta_ell_star)
  ceiling(root^2)
}
