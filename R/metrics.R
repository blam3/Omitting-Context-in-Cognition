compute_bias_metrics <- function(estimates, truth) {
  err <- estimates - truth
  data.frame(
    absolute_bias = mean(abs(err), na.rm = TRUE),
    relative_bias = mean(err / truth, na.rm = TRUE),
    rmse = sqrt(mean(err^2, na.rm = TRUE))
  )
}

summarise_model_selection <- function(results) {
  out <- data.frame(
    n_runs = nrow(results),
    bic_proxy_complex_rate = mean(results$selected_by_bic_proxy == "complex"),
    aic_proxy_complex_rate = mean(results$selected_by_aic_proxy == "complex")
  )

  if ("selected_by_bic_proxy_context_vs_complex" %in% names(results)) {
    out$bic_proxy_context_beats_complex_rate <- mean(
      results$selected_by_bic_proxy_context_vs_complex == "context"
    )
  }

  if ("selected_by_aic_proxy_context_vs_complex" %in% names(results)) {
    out$aic_proxy_context_beats_complex_rate <- mean(
      results$selected_by_aic_proxy_context_vs_complex == "context"
    )
  }

  # The score screen is reported next to the selection rates because it answers
  # the prior question: whether the complex class can attain strictly lower
  # divergence at all (Proposition L3.4), rather than whether it wins here.
  if ("score_p_cluster" %in% names(results)) {
    out$score_screen_reject_rate_cluster <- mean(results$score_p_cluster < 0.05, na.rm = TRUE)
  }

  if ("loglik_advantage_per_obs_complex_minus_simple" %in% names(results)) {
    out$mean_loglik_advantage_per_obs_complex_minus_simple <- mean(
      results$loglik_advantage_per_obs_complex_minus_simple,
      na.rm = TRUE
    )
  }

  out
}
