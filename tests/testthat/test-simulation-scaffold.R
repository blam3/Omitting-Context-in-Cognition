test_that("simulation DGM returns aligned trial-level columns", {
  source(testthat::test_path("../../R/dgm.R"))

  dat <- simulate_ambiguity_task(
    n = 5,
    trials = 8,
    context_range = "unrestricted",
    context_effect = "moderate",
    seed = 123
  )

  expect_equal(nrow(dat), 5 * 8)
  expect_true(all(c(
    "choice", "probability", "ambiguity", "value", "ref_side",
    "condition", "color_cue", "theta", "theta_sd", "tau"
  ) %in% names(dat)))
  expect_true(all(dat$probability >= 0 & dat$probability <= 1))
  expect_true(all(dat$ambiguity >= 0 & dat$ambiguity <= 1))
  expect_true(all(dat$choice %in% c(0, 1)))
  expect_equal(length(dat$condition), nrow(dat))
  expect_equal(length(dat$color_cue), nrow(dat))
})

test_that("one replication returns model-selection diagnostics", {
  source(testthat::test_path("../../R/run_replication.R"))

  res <- run_replication(
    n = 8,
    trials = 8,
    context_range = "unrestricted",
    context_effect = "weak",
    seed = 456
  )

  expect_equal(nrow(res), 1)
  expect_true(all(c(
    "selected_by_bic_proxy",
    "selected_by_aic_proxy",
    "loglik_advantage_complex_minus_simple",
    "reference_ses_ambiguity_coef"
  ) %in% names(res)))
})
