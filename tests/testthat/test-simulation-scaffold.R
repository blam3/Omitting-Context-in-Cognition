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

test_that("fixed-parameter control is representable by the shared model baseline", {
  source(testthat::test_path("../../R/dgm.R"))
  source(testthat::test_path("../../R/fit_models.R"))
  dat <- simulate_ambiguity_task(20, 60, context_effect = "none", seed = 902,
                                latent_heterogeneity = FALSE)
  expect_true(all(dat$theta == 0.75 & dat$tau == 4 & dat$theta_sd == 0))
  for (fit in list(fit_simple_omitted_context(dat),
                   fit_complex_omitted_context(dat),
                   fit_simple_contextual_true_family(dat))) {
    mm <- model.matrix(fit$fit)
    expect_equal(as.vector(qr.fitted(qr(mm), qlogis(dat$choice_prob))),
                 qlogis(dat$choice_prob), tolerance = 1e-10)
  }
})
