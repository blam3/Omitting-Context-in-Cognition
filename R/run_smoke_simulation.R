source("R/run_replication.R")

res <- run_replication(
  n = 40,
  trials = 40,
  context_range = "unrestricted",
  context_effect = "weak",
  seed = 20260630
)

stopifnot(nrow(res) == 1)
stopifnot(all(c("selected_by_bic_proxy", "selected_by_aic_proxy") %in% names(res)))
print(res)
cat("Smoke simulation completed.\n")
