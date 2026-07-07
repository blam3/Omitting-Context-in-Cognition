args <- commandArgs(trailingOnly = TRUE)

get_arg <- function(name, default = NULL) {
  key <- paste0("--", name)
  idx <- match(key, args)
  if (is.na(idx)) return(default)
  args[[idx + 1]]
}

participants <- as.integer(get_arg("participants", 12))
trials <- as.integer(get_arg("trials", 20))
seed <- as.integer(get_arg("seed", 20260704))
out_dir <- get_arg("out_dir", "data_synthetic")

source("R/dgm.R")

set.seed(seed)
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

dat <- simulate_ambiguity_task(
  n = participants,
  trials = trials,
  context_range = "unrestricted",
  context_effect = "moderate",
  seed = seed
)

participant_ids <- sprintf("SYN%03d", seq_len(participants))
dat$participant <- participant_ids[dat$id]

participant_summary <- unique(dat[, c("id", "participant", "ses")])
participant_summary$income_usd_synthetic <- pmax(
  15000,
  round(55000 + 18000 * participant_summary$ses + rnorm(nrow(participant_summary), 0, 5000), -2)
)
education_levels <- c("high_school", "some_college", "college", "graduate")
participant_summary$education_synthetic <- sample(
  education_levels,
  size = nrow(participant_summary),
  replace = TRUE,
  prob = c(0.25, 0.30, 0.30, 0.15)
)
participant_summary$age_synthetic <- sample(18:70, nrow(participant_summary), replace = TRUE)
participant_summary$gender_synthetic <- sample(
  c("woman", "man", "nonbinary", "not_reported"),
  size = nrow(participant_summary),
  replace = TRUE,
  prob = c(0.47, 0.47, 0.03, 0.03)
)

catch_prop <- setNames(pmin(0.35, rbeta(participants, 1, 12)), participant_ids)
pass_fail <- ifelse(catch_prop <= 0.20, "pass", "fail")

is_catch <- dat$trial %% max(5, floor(trials / 4)) == 0
catch_status <- rep(NA_integer_, nrow(dat))
for (p in participant_ids) {
  idx <- which(dat$participant == p & is_catch)
  catch_status[idx] <- ifelse(runif(length(idx)) < catch_prop[[p]], 4L, 3L)
}

trial_out <- data.frame(
  `Unnamed: 0` = seq_len(nrow(dat)),
  Sheet = paste0("Sheet_", dat$participant),
  choice = dat$choice,
  colors = as.character(dat$color_cue),
  ambigs = round(dat$ambiguity, 3),
  probs = round(dat$probability, 3),
  vals = round(100 * dat$value, 2),
  refSide = ifelse(dat$ref_side > 0, "right", "left"),
  numTrials = trials,
  participant = dat$participant,
  condition = as.character(dat$condition),
  `Catch.trial.(3=pass,4=fail)` = catch_status,
  `Proportion.failed.catch.trials` = round(catch_prop[dat$participant], 3),
  `Pass/fail` = pass_fail[dat$participant],
  X10 = NA,
  `Proportion.of.catch.trials.failed` = round(catch_prop[dat$participant], 3),
  X12 = NA,
  check.names = FALSE
)

demo_out <- data.frame(
  participant = participant_summary$participant,
  income_usd_synthetic = as.integer(participant_summary$income_usd_synthetic),
  education_synthetic = participant_summary$education_synthetic,
  age_synthetic = participant_summary$age_synthetic,
  gender_synthetic = participant_summary$gender_synthetic,
  ses_z_synthetic = round(participant_summary$ses, 3)
)

trial_path <- file.path(out_dir, "raid_trial_synthetic.csv")
demo_path <- file.path(out_dir, "raid_demographics_synthetic.csv")

write.csv(trial_out, trial_path, row.names = FALSE, na = "")
write.csv(demo_out, demo_path, row.names = FALSE, na = "")

cat("Wrote synthetic trial data:", trial_path, "\n")
cat("Wrote synthetic demographics:", demo_path, "\n")
