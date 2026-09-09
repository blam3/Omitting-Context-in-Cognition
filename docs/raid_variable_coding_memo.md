# RAID variable coding memo

Updated 2026-09-08. Source: PI's project-conversation response. Status: partially resolved; no raw data inspected, no final empirical model fitted. The synthetic generator is a test fixture, not authority for real data coding.

| Field | Confirmed meaning | Still needed before transformation |
|---|---|---|
| choice | Chosen risky or ambiguous lottery, recorded as 1 or 2 | PI follow-up confirms 1=risky, 2=ambiguous; recode choice_ambiguous = as.integer(choice == 2). |
| probs | Observed probability of winning | Already 0–1 (PI-confirmed); which lottery it describes and the other lottery's probability information remain unresolved. |
| ambigs | Amount/percentage of ambiguous information on the trial | Already 0–1 (PI-confirmed); relationship to the occluded probability interval remains to be documented. |
| vals | Monetary amount | PI confirms one option's amount only and says losses are not currently stored. Which option, other payoff, unit, and whether loss trials are absent versus unsigned amounts remain unresolved. |
| refSide | Whether the risky option appeared left or right | Raw codes for left/right; it is risky-option side, not an assumed safe-reference side. |
| condition | Gain versus loss domain | PI confirms literal codes "gain" and "loss". Availability/encoding of loss observations remains unresolved. It is not a source cue. |
| colors | Raw codes 1 or 2 (PI-confirmed); meaning unknown | Code-to-color map and task meaning; possible relation to lottery identity. Do not use as a cognitive source dimension without documentation. |

## Data and quality-control requirements

Trial file, demographic file, protocol/stimulus lookup, participant merge keys, missingness, catch-field levels, primary exclusion threshold, and sensitivity rules remain to be documented. No data access or exclusion rule is inferred from semantic field descriptions. Secure data directories are empty in the inspected working tree.

## Readiness

- [x] Trial LOO and primary M4 probability-distortion family selected by PI.
- [x] Core semantic meanings supplied for six fields.
- [x] Binary choice transformation unambiguously defined: 1=risky, 2=ambiguous.
- [x] Probability and ambiguity scales confirmed as 0–1.
- [ ] Probability-to-option alignment verified.
- [ ] Both lottery payoff/probability definitions reconstructed, including losses.
- [ ] Side/domain raw codes and colors decoded.
- [ ] Catch-trial exclusions fixed before model comparison.
- [ ] Context merge and coding verified on authorized data.
- [ ] Structural likelihood validated on synthetic task-matched data.

Use `choice == 2` as ambiguous; do not divide probabilities or ambiguity by 100. Missing choices must remain missing, and unexpected codes should raise a validation error. Do not infer missing lottery payoffs from the existing one-value Stan skeleton. The remaining questions affect likelihood construction; they do not reopen already settled scientific choices.

## Confirmed recoding contract

```r
# Apply only after validating numeric input types; preserve missing values.
stopifnot(all(is.na(choice) | choice %in% c(1, 2)))
choice_ambiguous <- as.integer(choice == 2)
stopifnot(all(is.na(probs) | (probs >= 0 & probs <= 1)))
stopifnot(all(is.na(ambigs) | (ambigs >= 0 & ambigs <= 1)))
probability <- probs
ambiguity <- ambigs
stopifnot(all(is.na(condition) | condition %in% c("gain", "loss")))
```

These snippets specify transformations; they have not been run on RAID data. Do not synthesize missing loss-domain data, negate vals based solely on condition, or impute the unrecorded option's value. Obtain the task protocol or a stimulus lookup. Unknown color meaning need not block a model that does not use color, once the protocol confirms color is unnecessary for reconstructing lotteries.
