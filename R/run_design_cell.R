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
context_effect <- get_arg("context_effect", "weak")
replications <- as.integer(get_arg("replications", 10))
seed <- as.integer(get_arg("seed", 20260630))

source(file.path(dirname(rlang::caller_source()), "run_replication.R"))

dir.create("results", showWarnings = FALSE)
dir.create("simulations", showWarnings = FALSE)

results <- do.call(
  rbind,
  lapply(seq_len(replications), function(r) {
    run_replication(
      n = n,
      trials = trials,
      context_range = context_range,
      context_effect = context_effect,
      seed = seed + r
    )
  })
)

run_id <- paste(n, trials, context_range, context_effect, replications, seed, sep = "_")
out_path <- file.path("results", paste0("sim_", run_id, ".csv"))
write.csv(results, out_path, row.names = FALSE)

registry_path <- "simulations/run_registry.csv"
entry <- data.frame(
  run_id = run_id,
  n = n,
  trials = trials,
  context_range = context_range,
  context_effect = context_effect,
  replications = replications,
  seed = seed,
  status = "complete",
  output_path = out_path,
  timestamp = as.character(Sys.time())
)

if (!file.exists(registry_path)) {
  write.csv(entry, registry_path, row.names = FALSE)
} else {
  old <- read.csv(registry_path)
  write.csv(rbind(old, entry), registry_path, row.names = FALSE)
}

print(out_path)
