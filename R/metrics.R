compute_bias_metrics <- function(estimates, truth) {
  err <- estimates - truth
  data.frame(
    absolute_bias = mean(abs(err), na.rm = TRUE),
    relative_bias = mean(err / truth, na.rm = TRUE),
    rmse = sqrt(mean(err^2, na.rm = TRUE))
  )
}

summarise_model_selection <- function(results) {
  data.frame(
    n_runs = nrow(results),
    bic_proxy_complex_rate = mean(results$selected_by_bic_proxy == "complex"),
    aic_proxy_complex_rate = mean(results$selected_by_aic_proxy == "complex")
  )
}
