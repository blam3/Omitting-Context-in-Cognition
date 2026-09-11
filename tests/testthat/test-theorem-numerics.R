# Numerical verification of the OCECM theorem package.
#
# Each block corresponds to a claim in docs/theorems/. A failure here means a
# stated theorem is wrong, not that a tolerance needs loosening.

source(testthat::test_path("../../R/theorem_numerics.R"))

A_DESIGN <- c(0, 0.25, 0.5, 0.75, 1)   # A-008: J = 5 >= 4 levels, includes a = 0
Q_DESIGN <- rep(1 / 5, 5)
B0 <- 0.30

test_that("T-003b: the closed-form attenuated response matches Monte Carlo", {
  analytic <- p_cell(A_DESIGN, B0, mu = 1.2, sigma2 = 0.8)
  mc <- p_cell_mc(A_DESIGN, B0, mu = 1.2, sigma2 = 0.8, draws = 4e5, seed = 42)
  # Monte Carlo error at 4e5 draws is ~8e-4; the closed form must sit inside it.
  expect_lt(max(abs(analytic - mc)), 3e-3)
})

test_that("T-003a: heteroskedasticity holds iff gamma != 0 and v(z) is non-constant", {
  sigma_u2 <- 0.5
  v <- c(0.2, 2.5)
  # gamma != 0 and v non-constant -> non-constant induced variance
  expect_gt(diff(range(sigma_u2 + 1.1^2 * v)), 0)
  # gamma == 0 -> constant
  expect_equal(diff(range(sigma_u2 + 0^2 * v)), 0)
  # v constant -> constant
  expect_equal(diff(range(sigma_u2 + 1.1^2 * c(0.7, 0.7))), 0)
})

test_that("T-004d: Gaussian mean heterogeneity is absorbed exactly by M_S", {
  mubar <- 1.2; omega2 <- 0.9; sigma2 <- 0.8
  quad <- p0_gaussian_mean(A_DESIGN, B0, mubar, omega2, sigma2)
  closed <- p_cell(A_DESIGN, B0, mubar, sigma2 + omega2)   # member of M_S
  expect_lt(max(abs(quad - closed)), 1e-10)
  # and therefore the KL gap vanishes
  expect_lt(inf_kl(quad, A_DESIGN, Q_DESIGN, m_s_predict, 3), 1e-10)
  expect_lt(affine_residual(quad, A_DESIGN), 1e-10)
})

test_that("T-004 boundary condition: homogeneous context leaves no KL gap", {
  p0 <- p0_mixture(A_DESIGN, B0, mu = c(1.2, 1.2), sigma2 = c(0.8, 0.8), pi = c(0.5, 0.5))
  expect_lt(inf_kl(p0, A_DESIGN, Q_DESIGN, m_s_predict, 3), 1e-10)
  expect_lt(affine_residual(p0, A_DESIGN), 1e-10)
})

test_that("T-004: variance heterogeneity yields a strict KL gap that M_K closes", {
  p0 <- p0_mixture(A_DESIGN, B0, mu = c(1.2, 1.2), sigma2 = c(0.2, 2.5), pi = c(0.5, 0.5))

  kl_s <- inf_kl(p0, A_DESIGN, Q_DESIGN, m_s_predict, 3, restarts = 60)
  kl_mix <- inf_kl(p0, A_DESIGN, Q_DESIGN, m_k_mix_predict, 7, restarts = 120)
  kl_flex <- inf_kl(p0, A_DESIGN, Q_DESIGN, m_k_flex_predict, 4, restarts = 60)

  # (i) non-representability: p0 is outside M_S
  expect_gt(kl_s, 1e-8)
  expect_gt(affine_residual(p0, A_DESIGN), 1e-8)
  # (ii) containment: M_K^mix reaches p0 exactly
  expect_lt(kl_mix, 1e-10)
  # Theorem T-004: strict dominance
  expect_lt(kl_mix, kl_s)
  # Theorem T-004': strict improvement without containment
  expect_lt(kl_flex, kl_s)
})

test_that("T-004: mean heterogeneity alone gives a far smaller gap than variance", {
  common <- list(a = A_DESIGN, b0 = B0, pi = c(0.5, 0.5))
  p_mean <- p0_mixture(common$a, common$b0, mu = c(0.6, 1.8), sigma2 = c(0.8, 0.8), pi = common$pi)
  p_var <- p0_mixture(common$a, common$b0, mu = c(1.2, 1.2), sigma2 = c(0.2, 2.5), pi = common$pi)
  expect_lt(inf_kl(p_mean, A_DESIGN, Q_DESIGN, m_s_predict, 3, restarts = 60),
            inf_kl(p_var, A_DESIGN, Q_DESIGN, m_s_predict, 3, restarts = 60))
})

test_that("T-007a: the AIC/BIC threshold identities are exact rearrangements", {
  set.seed(9)
  for (i in 1:200) {
    D_n <- rnorm(1, 0, 5); k_s <- 3; k_k <- sample(4:9, 1); n <- sample(50:5000, 1)
    aic_s <- -2 * 0 + 2 * k_s; aic_k <- -2 * D_n + 2 * k_k
    bic_s <- -2 * 0 + k_s * log(n); bic_k <- -2 * D_n + k_k * log(n)
    expect_equal(aic_favours_complex(D_n, k_k, k_s), aic_k < aic_s)
    expect_equal(bic_favours_complex(D_n, k_k, k_s, n), bic_k < bic_s)
  }
})

test_that("T-007b': the crossover formula solves its defining quadratic", {
  n_star <- aic_crossover_n(delta_ell_star = 7e-6, omega = 1, delta_k = 1, alpha = 0.05)
  z <- qnorm(0.95)
  # at n_star the objective is non-negative; just below it, negative
  expect_gte(n_star * 7e-6 - z * sqrt(n_star) * 1 - 1, -1e-6)
  lower <- floor(n_star * 0.9)
  expect_lt(lower * 7e-6 - z * sqrt(lower) * 1 - 1, 0)
  # The probabilistic crossover is ~5.5e10, five orders of magnitude above the
  # deterministic threshold 1/delta_ell_star = 1.4e5. Guarding the magnitude
  # keeps the docs honest: quoting the deterministic value as if it were the
  # detectability threshold overstates power by ~4e5.
  expect_gt(n_star, 1e10)
  expect_lt(n_star, 1e11)
  expect_gt(n_star, 100 / 7e-6)
})

test_that("T-004b: D overlaps M_S exactly on the diagonal rho == c0", {
  # Counterexample found in proof-critic review (2026-09-09). The lemma
  # originally asserted closure(M_S) \ M_S == D. It is false: when rho == c0
  # the degenerate law is the constant response Phi(c0), which is in M_S at
  # (beta_0, beta_1, s^2) = (c0, 0, 0). The lemma now states a union.
  # Tolerance is 1e-9, matching closure_membership()'s default: the exact
  # residual is 0 at s^2 = 0, but the optimiser lands near rather than on it
  # (observed 1e-14 to 3e-12). Off-diagonal points sit at 6.6e-3 and above, so
  # the two families are separated by six orders of magnitude regardless.
  for (c0 in c(0.5, -1.2, 0.0, 2.0)) {
    p_diag <- pnorm(rep(c0, length(A_DESIGN)))            # rho == c0
    expect_lt(affine_residual(p_diag, A_DESIGN), 1e-9)    # i.e. IN M_S
  }
  # Off the diagonal with c0 != 0 the degenerate law is genuinely outside M_S.
  for (pair in list(c(0.5, 1.3), c(-1.2, 0.4), c(2.0, -0.7))) {
    g <- ifelse(A_DESIGN > 0, pair[2], pair[1])
    expect_gt(affine_residual(pnorm(g), A_DESIGN), 1e-3)
  }
})

test_that("T-004a: the affine-residual infimum is not always attained", {
  # Same review finding. For a degenerate point with c0 = 0 the residual decays
  # like s^-2 to zero without reaching it, so a near-zero affine residual does
  # NOT certify membership in M_S. Guarding the decay keeps the docs honest.
  g <- ifelse(A_DESIGN > 0, 1.0, 0.0)                     # c0 = 0, rho = 1
  X <- cbind(1, A_DESIGN)
  resid_at <- function(s) {
    h <- g * sqrt(1 + s^2 * A_DESIGN^2)
    sum(residuals(lm.fit(X, h))^2)
  }
  r <- vapply(10^(2:5), resid_at, numeric(1))
  expect_true(all(diff(r) < 0))                           # strictly decreasing
  expect_lt(r[length(r)], 1e-9)                           # decays to zero
  expect_true(all(r > 0))                                 # never attains zero
  expect_lt(abs(log10(r[1] / r[2]) - 2), 0.2)             # s^-2 rate
})

test_that("T-004c: closure_membership checks both branches", {
  # branch (b) is the one affine_residual() cannot see
  g <- ifelse(A_DESIGN > 0, 1.0, 0.0)
  r <- closure_membership(pnorm(g), A_DESIGN)
  expect_true(r$branch_b_holds)
  expect_true(r$in_closure)
  expect_false(r$outside_closure)
})

test_that("T-004 condition (i) holds for the table cases via BOTH branches", {
  # The review confirmed the table's conclusions survive, but the certificate
  # backing them was incomplete: branch (b) was never checked. It is now.
  cases <- list(
    list(mu = c(0.6, 1.8), s2 = c(0.2, 2.5)),   # A mean + variance
    list(mu = c(1.2, 1.2), s2 = c(0.2, 2.5))    # B variance only
  )
  for (cs in cases) {
    p0 <- p0_mixture(A_DESIGN, B0, cs$mu, cs$s2, c(0.5, 0.5))
    r <- closure_membership(p0, A_DESIGN, restarts = 60)
    expect_false(r$branch_a_holds)                        # not affine-representable
    expect_false(r$branch_b_holds)                        # index not constant on a>0
    expect_true(r$outside_closure)                        # T-004 condition (i)
    expect_gt(r$constant_index_spread, 0.3)
  }
  # Boundary case D must fail condition (i): p0 IS in M_S, so it is in closure.
  p_bd <- p0_mixture(A_DESIGN, B0, c(1.2, 1.2), c(0.8, 0.8), c(0.5, 0.5))
  expect_true(closure_membership(p_bd, A_DESIGN)$in_closure)
})

test_that("kl_design guards a saturated p0 with the 0 log 0 = 0 convention", {
  # Proof-critic review 2026-09-09. The earlier version clipped only the model
  # probability, so a p0 saturated at 0 or 1 gave 0 * log(0/x) = NaN -- and
  # max(NaN, 0) is NaN in R, so inf_kl propagated it SILENTLY. Phi(x) == 1 in
  # float64 for x >~ 8.3, which the T-004 section 6 heterogeneity scan can hit.
  q <- rep(0.2, 5); p <- rep(0.5, 5)
  expect_true(is.finite(kl_design(c(1, .9, .8, .7, .6), p, q)))
  expect_true(is.finite(kl_design(c(0, .1, .2, .3, .4), p, q)))
  # symmetric saturation gives the same divergence against a flat model
  expect_equal(kl_design(c(1, .9, .8, .7, .6), p, q),
               kl_design(c(0, .1, .2, .3, .4), p, q), tolerance = 1e-12)
  # a genuinely broken input must fail loudly, not drift through an optimiser
  expect_error(kl_design(c(NA, .9, .8, .7, .6), p, q))
  expect_error(kl_design(c(.5, .5), p, q))          # length mismatch
})

test_that("T-004: condition (i) is necessary -- KL to M_S vanishes without it", {
  # p0 in closure(M_S) \ M_S (rho != c0): the divergence decays like s^-2 to
  # zero, so inf KL over M_S is 0 and T-004's conclusion c > 0 fails. This is
  # what makes condition (i) load-bearing rather than decorative.
  c0 <- 0.5; rho <- 1.3
  p0 <- pnorm(ifelse(A_DESIGN > 0, rho, c0))
  kls <- vapply(10^(1:5), function(s) {
    # m_s_predict squares its third argument, so pass s (variance s^2) to
    # match the sequence beta^(n) = (c0, rho*s, s^2) of Lemma T-004b.
    kl_design(p0, m_s_predict(c(c0, rho * s, s), A_DESIGN), Q_DESIGN)
  }, numeric(1))
  expect_true(all(diff(kls) < 0))                   # strictly decreasing
  expect_lt(kls[length(kls)], 1e-10)                # -> 0
  expect_true(all(kls > 0))                         # never attained
  expect_lt(abs(log10(kls[2] / kls[3]) - 2), 0.3)   # s^-2 rate
  # and p0 is genuinely in the closure, via branch (b)
  expect_true(closure_membership(p0, A_DESIGN)$in_closure)
})

test_that("T-004': the M_S minimiser is interior and unique for the table cases", {
  # T-004' and T-007b (P1) assume this; it does NOT follow from condition (i)
  # (see the preceding test, where no minimiser exists in M_S at all). Guarding
  # it keeps the empirical claim in T-004 section 3 honest.
  fit_S <- function(p0, restarts = 40, seed = 5) {
    set.seed(seed)
    best <- list(value = Inf, par = NULL)
    for (i in seq_len(restarts)) {
      f <- try(optim(rnorm(3, 0, 2.5),
                     function(par) kl_design(p0, m_s_predict(par, A_DESIGN), Q_DESIGN),
                     method = "Nelder-Mead",
                     control = list(maxit = 20000, reltol = 1e-14)), silent = TRUE)
      if (!inherits(f, "try-error") && is.finite(f$value) && f$value < best$value) best <- f
    }
    best
  }
  # boundary case D must recover the generating parameters exactly
  p_bd <- p0_mixture(A_DESIGN, B0, c(1.2, 1.2), c(0.8, 0.8), c(0.5, 0.5))
  fd <- fit_S(p_bd)
  expect_equal(fd$par[1], B0, tolerance = 1e-3)
  expect_equal(fd$par[2], 1.2, tolerance = 1e-3)
  expect_equal(fd$par[3]^2, 0.8, tolerance = 1e-3)
  # and the heterogeneous cases have a finite, interior s^2 (not drifting to Inf)
  for (cs in list(list(mu = c(0.6, 1.8), s2 = c(0.2, 2.5)),
                  list(mu = c(1.2, 1.2), s2 = c(0.2, 2.5)))) {
    f <- fit_S(p0_mixture(A_DESIGN, B0, cs$mu, cs$s2, c(0.5, 0.5)))
    expect_lt(f$par[3]^2, 1e3)
    expect_gt(f$par[3]^2, 1e-3)
  }
})

test_that("T-004: the KL gap collapses as p0 approaches the boundary", {
  # Mathematically p0 is always in (0,1)^J so the premise never fails, but the
  # gap shrinks toward zero near the boundary: condition (i) can hold while c is
  # numerically indistinguishable from 0. This compounds the section 6 caveat.
  gaps <- vapply(c(0.3, 3.0, 6.0), function(b0) {
    p0 <- p0_mixture(A_DESIGN, b0, c(0.6, 1.8), c(0.2, 2.5), c(0.5, 0.5))
    inf_kl(p0, A_DESIGN, Q_DESIGN, m_s_predict, 3, restarts = 60)
  }, numeric(1))
  expect_true(all(diff(gaps) < 0))                  # monotone collapse
  expect_gt(gaps[1] / gaps[length(gaps)], 1e3)      # by orders of magnitude
})

test_that("T-003a: the criterion needs the support qualifier to be true", {
  # Proof-critic review 2026-09-09. v(z) = (z-1)^2 with gamma = 1 satisfies the
  # UNQUALIFIED antecedent (gamma != 0, v non-constant on R) in both rows below.
  # Only the support placement decides whether there is any heteroskedasticity,
  # which is why T-003a must say "non-constant on supp(Z)".
  v_fun <- function(z) (z - 1)^2
  gamma <- 1.0; sigma_u2 <- 0.5

  # v non-constant on R but CONSTANT on supp(Z) -> no heteroskedasticity
  off <- induced_variance(v_fun, c(0, 2), gamma, sigma_u2)
  expect_equal(off$sigma2, c(1.5, 1.5))
  expect_false(off$heteroskedastic)

  # v non-constant ON supp(Z) -> heteroskedasticity
  on <- induced_variance(v_fun, c(0, 3), gamma, sigma_u2)
  expect_equal(on$sigma2, c(1.5, 4.5))
  expect_true(on$heteroskedastic)

  # and the KL consequence follows: no gap in the first case, a gap in the second
  p_off <- p0_mixture(A_DESIGN, B0, c(0, 0), off$sigma2, c(0.5, 0.5))
  p_on  <- p0_mixture(A_DESIGN, B0, c(0, 0), on$sigma2,  c(0.5, 0.5))
  expect_lt(affine_residual(p_off, A_DESIGN), 1e-9)   # in M_S
  expect_gt(affine_residual(p_on, A_DESIGN), 1e-8)    # outside M_S
  expect_true(closure_membership(p_off, A_DESIGN)$in_closure)
  expect_true(closure_membership(p_on, A_DESIGN)$outside_closure)
})

test_that("T-003: independence of U and C is load-bearing, not a technicality", {
  # The cross term is 2 * gamma * Cov(C, U | Z) -- first order. Correlating them
  # breaks the variance formula by tens of percent, so the assumption cannot be
  # quietly relaxed.
  gamma <- 1.0; sigma_u2 <- 0.5; v <- 2.0
  expect_equal(theta_variance_true(gamma, sigma_u2, v, 0),
               theta_variance_t003(gamma, sigma_u2, v))
  errs <- vapply(c(0.3, 0.6, 0.9), function(rho) {
    abs(theta_variance_true(gamma, sigma_u2, v, rho) -
        theta_variance_t003(gamma, sigma_u2, v)) / theta_variance_t003(gamma, sigma_u2, v)
  }, numeric(1))
  expect_true(all(diff(errs) > 0))                    # monotone in rho
  expect_gt(errs[length(errs)], 0.5)                  # >50% error at rho = 0.9
})
