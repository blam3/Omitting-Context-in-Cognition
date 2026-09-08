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
