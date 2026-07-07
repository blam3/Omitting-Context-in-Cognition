source(testthat::test_path("../../R/dgm.R"))

testthat::test_that("simulate_context returns requested length", {
  ses <- simulate_context(100, context_range = "unrestricted", seed = 1)
  testthat::expect_equal(length(ses), 100)
})

testthat::test_that("range restriction works", {
  ses <- simulate_context(1000, context_range = "range_restricted", seed = 1)
  testthat::expect_true(all(ses <= 0.5))
  testthat::expect_true(all(ses >= -0.5))
})

testthat::test_that("simulate_ambiguity_task has expected rows", {
  dat <- simulate_ambiguity_task(
    n = 10,
    trials = 20,
    context_range = "unrestricted",
    context_effect = "weak",
    seed = 1
  )
  testthat::expect_equal(nrow(dat), 200)
  testthat::expect_true(all(c("id", "trial", "ses", "theta", "choice") %in% names(dat)))
})
