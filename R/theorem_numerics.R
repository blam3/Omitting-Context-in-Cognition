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

# Design-averaged Bernoulli KL.
#
# Both arguments are guarded, and the 0 log 0 = 0 convention is applied
# explicitly. The earlier version clipped only the model probability `p`, so a
# target `p0` saturated at 0 or 1 produced 0 * log(0 / x) = 0 * -Inf = NaN --
# and because max(NaN, 0) is NaN in R, inf_kl() propagated it SILENTLY instead
# of erroring. That is reachable: Phi(x) == 1 in float64 for x >~ 8.3, which the
# heterogeneity scan of T-004 section 6 can hit. Found in proof-critic review
# (2026-09-09).
kl_design <- function(p0, p, q) {
  stopifnot(length(p0) == length(p), length(p0) == length(q))
  eps <- 1e-12
  p <- pmin(pmax(p, eps), 1 - eps)
  p0 <- pmin(pmax(p0, eps), 1 - eps)
  out <- sum(q * (p0 * log(p0 / p) + (1 - p0) * log((1 - p0) / (1 - p))))
  # Fail loudly rather than let a non-finite value drift through an optimiser.
  if (!is.finite(out)) {
    stop("kl_design produced a non-finite value; check p0 and p for saturation")
  }
  out
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
    if (!inherits(fit, "try-error") && is.finite(fit$value)) {
      best <- min(best, fit$value)
    }
  }
  if (!is.finite(best)) stop("inf_kl found no finite fit; check p0 for saturation")
  max(best, 0)
}

# --- Lemma T-004a / Corollary T-004c: membership criteria -------------------
#
# CAUTION. affine_residual() minimises over s^2, and that INFIMUM IS NOT ALWAYS
# ATTAINED. For a degenerate point of D with c_0 = 0 (see Lemma T-004b) the
# residual decays like s^{-2} to zero without ever reaching it, so the optimiser
# drives s -> Inf and returns a near-zero value for a law that is in the closure
# of M_S but NOT in M_S. This is the same non-closedness the lemma exists to
# handle, showing up in the test for it.
#
# Consequences for how these functions may be used:
#   * a STRICTLY POSITIVE affine residual certifies p not in M_S;
#   * a near-zero affine residual does NOT certify p in M_S -- it certifies at
#     most p in closure(M_S);
#   * T-004 condition (i) is p_0 not in closure(M_S), which is STRONGER than
#     not in M_S, so the affine residual alone never establishes it. Branch (b)
#     of Corollary T-004c must also be checked. Use closure_membership() rather
#     than affine_residual() when condition (i) is what is at stake.
#
# Lemma T-004a: p in M_S <=> exists s^2 >= 0 with
# a -> Phi^{-1}(p(a)) sqrt(1 + s^2 a^2) affine on the design support.
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
    if (!inherits(fit, "try-error") && is.finite(fit$value)) {
      best <- min(best, fit$value)
    }
  }
  if (!is.finite(best)) stop("inf_kl found no finite fit; check p0 for saturation")
  max(best, 0)
}

# Branch (b) of Corollary T-004c: is Phi^{-1}(p(a)) constant over a > 0?
# This is the branch affine_residual() cannot see, and it is exactly the
# degenerate family D of Lemma T-004b.
constant_index_spread <- function(p0, a) {
  g <- qnorm(p0[a > 0])
  if (length(g) < 2) return(0)
  max(g) - min(g)
}

# Corollary T-004c in full: p in closure(M_S) iff branch (a) OR branch (b).
# Returns both certificates and the verdict, so a caller can see which fired.
# `outside_closure = TRUE` is what T-004 condition (i) requires.
closure_membership <- function(p0, a, tol = 1e-9, restarts = 40, seed = 11) {
  branch_a <- affine_residual(p0, a, restarts = restarts, seed = seed)
  branch_b <- constant_index_spread(p0, a)
  in_closure <- (branch_a < tol) || (branch_b < tol)
  list(
    affine_residual = branch_a,          # branch (a); infimum may be unattained
    constant_index_spread = branch_b,    # branch (b)
    branch_a_holds = branch_a < tol,
    branch_b_holds = branch_b < tol,
    in_closure = in_closure,
    outside_closure = !in_closure        # T-004 condition (i)
  )
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

# --- Corollary T-003a: the support qualifier ------------------------------
#
# sigma^2(z) = sigma_u^2 + gamma^2 v(z), evaluated ONLY on the support of Z.
# A v that varies off the support contributes nothing, which is why T-003a
# must say "non-constant on supp(Z)" rather than "non-constant". Returns the
# induced variances and whether they are heteroskedastic where it matters.
induced_variance <- function(v_fun, supp, gamma, sigma_u2) {
  s2 <- sigma_u2 + gamma^2 * vapply(supp, v_fun, numeric(1))
  list(sigma2 = s2,
       heteroskedastic = diff(range(s2)) > 1e-12)
}

# --- T-003: the variance formula requires U independent of (Z, C) ----------
#
# With Cov(C, U | Z) != 0 the true conditional variance gains a cross term
# 2 * gamma * Cov(C, U | Z), which is first order, not a small correction.
theta_variance_true <- function(gamma, sigma_u2, v, rho) {
  gamma^2 * v + sigma_u2 + 2 * gamma * rho * sqrt(v * sigma_u2)
}
theta_variance_t003 <- function(gamma, sigma_u2, v) sigma_u2 + gamma^2 * v

# --- T-007b: the Vuong variance and the crossover --------------------------
#
# omega^2 = Var_{p0}( log p_K(Y|A) - log p_S(Y|A) ), computed exactly from the
# three probability vectors rather than simulated.
#
# CAUTION, from proof-critic review 2026-09-11: omega is NOT a free parameter in
# this project's regime. It is the sd of the POINTWISE log-likelihood difference
# between two models whose KL gap is ~1e-6, so the log densities differ by
# O(1e-3) pointwise and omega inherits that scale. An earlier draft of T-007b'
# used omega ~ 1 and quoted a crossover four orders of magnitude too large.
omega_sq <- function(p0, p_S, p_K, q) {
  eps <- 1e-12
  p_S <- pmin(pmax(p_S, eps), 1 - eps); p_K <- pmin(pmax(p_K, eps), 1 - eps)
  p0 <- pmin(pmax(p0, eps), 1 - eps)
  d1 <- log(p_K / p_S); d0 <- log((1 - p_K) / (1 - p_S))
  Ed <- sum(q * (p0 * d1 + (1 - p0) * d0))
  Ed2 <- sum(q * (p0 * d1^2 + (1 - p0) * d0^2))
  list(delta_ell_star = Ed, omega2 = Ed2 - Ed^2, omega = sqrt(max(Ed2 - Ed^2, 0)))
}

# Lemma T-007b-2: under containment (p0 in M_K) omega^2 -> 2*delta_ell_star, so
# Corollary T-007b-3 gives a crossover that is a FIXED multiple of the
# deterministic threshold 1/delta_ell_star, independent of the effect size.
aic_crossover_containment <- function(delta_ell_star, delta_k = 1, alpha = 0.05) {
  z <- qnorm(1 - alpha)
  u <- (z * sqrt(2) + sqrt(2 * z^2 + 4 * delta_k)) / 2
  list(multiplier = u^2, n_star = ceiling(u^2 / delta_ell_star))
}

# T-007b selection probability: P(AIC selects M_K) = Phi((n dl* - dk)/(sqrt(n) omega)).
aic_select_prob <- function(n, delta_ell_star, omega, delta_k = 1) {
  pnorm((n * delta_ell_star - delta_k) / (sqrt(n) * omega))
}
