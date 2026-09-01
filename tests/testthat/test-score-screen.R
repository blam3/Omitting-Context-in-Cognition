# Tests for the Proposition L3.4 score screen.

source(testthat::test_path("../../R/dgm.R"))
source(testthat::test_path("../../R/fit_models.R"))
source(testthat::test_path("../../R/score_screen.R"))

screen_test_data <- function(n = 25, trials = 20, context_effect = "moderate", seed = 42) {
  simulate_ambiguity_task(
    n = n,
    trials = trials,
    context_range = "unrestricted",
    context_effect = context_effect,
    seed = seed
  )
}

test_that("the simple-parameter block of the score vanishes at the simple fit", {
  # This is the first-order condition Proposition L3.4 relies on: the score of
  # the retained parameters is zero at the pseudo-true simple model, so a
  # nonzero total score must come from the extra block. If this ever fails, the
  # screen is not evaluating the score at the embedded simple fit.
  screen <- compute_score_screen(screen_test_data())

  expect_lt(max(abs(screen$simple_block_score_per_obs)), 1e-8)
})

test_that("the score statistic agrees with the likelihood-ratio statistic", {
  # The efficient score test and the likelihood-ratio test for the same nested
  # pair are asymptotically equivalent. Close agreement is strong evidence that
  # the screen is testing the intended hypothesis and that the extra design
  # block matches the complex model actually fitted.
  dat <- screen_test_data(n = 60, trials = 40, context_effect = "strong", seed = 7)

  screen <- compute_score_screen(dat)
  simple_fit <- fit_simple_omitted_context(dat)
  complex_fit <- fit_complex_omitted_context(dat)
  lr_stat <- 2 * (complex_fit$loglik - simple_fit$loglik)

  expect_equal(screen$df, complex_fit$df - simple_fit$df)
  expect_equal(screen$score_stat_naive, lr_stat, tolerance = 0.1)
})

test_that("the screen refuses to run on a non-nested pair", {
  # Proposition L3.4 has no content without the embedding, so a non-nested
  # complex class must raise rather than return an uninterpretable number.
  dat <- screen_test_data()

  expect_error(
    compute_score_screen(
      dat,
      simple_formula = choice ~ value + probability + ses,
      complex_formula = complex_omitted_context_formula()
    ),
    "nested"
  )
})

test_that("the screen localises which block of false complexity absorbs structure", {
  # A condition effect is injected into the DGM, which contains no true
  # source/condition mechanism otherwise. The condition block should carry the
  # signal far more strongly than the ambiguity blocks.
  dat <- screen_test_data(n = 50, trials = 40, context_effect = "none", seed = 5)
  dat$choice <- rbinom(
    nrow(dat),
    size = 1,
    prob = plogis(qlogis(dat$choice_prob) + 0.8 * (dat$condition == "source_a"))
  )

  screen <- compute_score_screen(dat)
  by_block <- screen$by_block
  condition_p <- by_block$p_value[by_block$block == "condition"]
  nonlinear_p <- by_block$p_value[by_block$block == "nonlinear_ambiguity"]

  expect_lt(condition_p, 0.001)
  expect_lt(condition_p, nonlinear_p)
})

test_that("the screen is calibrated when the simple model is correctly specified", {
  # Responses are regenerated from the simple model's own linear predictor, so
  # the population extra-block score is exactly zero and the naive statistic
  # should reject at roughly its nominal level.
  set.seed(2026)
  p_values <- vapply(seq_len(60), function(i) {
    dat <- prepare_proxy_features(
      simulate_ambiguity_task(
        n = 25, trials = 25,
        context_range = "unrestricted", context_effect = "none",
        seed = 1000 + i
      )
    )
    design <- model.matrix(simple_omitted_context_formula(), data = dat)
    beta <- c(-0.1, 0.6, 0.5, -0.3, 0.4, 0.1)[seq_len(ncol(design))]
    dat$choice <- rbinom(nrow(dat), size = 1, prob = plogis(as.numeric(design %*% beta)))
    compute_score_screen(dat)$p_value_naive
  }, numeric(1))

  # A loose bound: 60 replications cannot pin the rate precisely, but a broken
  # variance calculation would put this far outside the interval.
  expect_lt(mean(p_values < 0.05), 0.25)
})

test_that("score_screen_row returns one row with the expected columns", {
  row <- score_screen_row(compute_score_screen(screen_test_data()))

  expect_equal(nrow(row), 1)
  expect_true(all(c(
    "score_screen_df", "score_stat_naive", "score_p_naive",
    "score_stat_cluster", "score_p_cluster", "score_per_obs_l2",
    "score_p_block_condition", "score_p_block_color_cue"
  ) %in% names(row)))
  expect_gte(row$score_p_naive, 0)
  expect_lte(row$score_p_naive, 1)
})

test_that("summarise_score_screen reports rejection rates over replications", {
  rows <- do.call(rbind, lapply(c(11, 12, 13), function(s) {
    score_screen_row(compute_score_screen(screen_test_data(seed = s)))
  }))

  summary_row <- summarise_score_screen(rows)

  expect_equal(summary_row$n_runs, 3)
  expect_true("score_reject_rate_cluster" %in% names(summary_row))
  expect_true("score_reject_rate_block_condition" %in% names(summary_row))
})
