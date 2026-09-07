# Sweep the Proposition L3.4 score screen across context-effect strengths.
#
# The screen asks whether the false-complex class is even capable of strictly
# lower divergence than the context-omitting simple class, without fitting the
# complex model. Sweeping it over context-effect strength shows whether that
# capability tracks the omitted-context mechanism, which is the question the
# simulation track can answer cheaply before any Stan work begins.
#
# Read the caveats in the header of R/score_screen.R before interpreting the
# output. In particular a rejection is not evidence of omitted context, and a
# non-rejection is not evidence that Delta ell = 0.

source("R/run_replication.R")
source("R/score_screen.R")
source("R/metrics.R")

args <- commandArgs(trailingOnly = TRUE)

get_arg <- function(name, default = NULL) {
  key <- paste0("--", name)
  idx <- match(key, args)
  if (is.na(idx)) return(default)
  args[[idx + 1]]
}

n <- as.integer(get_arg("n", 40))
trials <- as.integer(get_arg("trials", 40))
context_range <- get_arg("context_range", "unrestricted")
replications <- as.integer(get_arg("replications", 20))
seed <- as.integer(get_arg("seed", 20260901))
effects <- strsplit(get_arg("context_effects", "none,weak,moderate,strong"), ",")[[1]]
out_dir <- get_arg("out_dir", "results")

dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

summaries <- lapply(effects, function(effect) {
  runs <- do.call(rbind, lapply(seq_len(replications), function(r) {
    run_replication(
      n = n,
      trials = trials,
      context_range = context_range,
      context_effect = effect,
      seed = seed + r
    )
  }))

  cbind(
    data.frame(
      context_effect = effect,
      n = n,
      trials = trials,
      stringsAsFactors = FALSE
    ),
    summarise_score_screen(runs),
    data.frame(
      mean_loglik_advantage_per_obs = mean(
        runs$loglik_advantage_per_obs_complex_minus_simple,
        na.rm = TRUE
      ),
      aic_proxy_complex_rate = mean(runs$selected_by_aic_proxy == "complex"),
      bic_proxy_complex_rate = mean(runs$selected_by_bic_proxy == "complex")
    )
  )
})

summary_table <- do.call(rbind, summaries)
out_path <- file.path(
  out_dir,
  sprintf("score_screen_%d_%d_%s_%d.csv", n, trials, context_range, seed)
)
write.csv(summary_table, out_path, row.names = FALSE)

print(summary_table)
cat("\nWrote:", out_path, "\n")
cat("Screen is a KL/log-score capability check only; it does not license a\n")
cat("LOOIC, Bayes-factor, or omitted-context conclusion.\n")
