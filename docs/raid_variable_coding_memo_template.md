# RAID Variable Coding Memo Template

Complete this memo before fitting final empirical structural models.

## Data sources

- Trial-level file:
- Demographic/context file:
- Task protocol or stimulus lookup:
- Date audited:
- Auditor:

## Executive answer

Can `choice` be converted into a binary indicator of choosing the ambiguous/risky option?

- [ ] Yes
- [ ] No
- [ ] Not yet; requires task documentation

If yes, define the transformation here:

```r
# choice_ambiguous <- ...
```

## Variable audit table

| Raw variable | Clean name | Unique values / range | Scale | Missingness | Interpretation | Action |
|---|---|---:|---|---:|---|---|
| `choice` | `choice` |  |  |  |  |  |
| `colors` | `color_cue` |  |  |  |  |  |
| `ambigs` | `ambiguity` |  |  |  |  |  |
| `probs` | `probability` |  |  |  |  |  |
| `vals` | `value` |  |  |  |  |  |
| `refSide` | `reference_side` |  |  |  |  |  |
| `numTrials` | `n_trials_design` |  |  |  |  |  |
| `participant` | `participant_id` |  |  |  |  |  |
| `condition` | `condition` |  |  |  |  |  |
| `Catch.trial.(3=pass,4=fail)` | `catch_trial_status` |  |  |  |  |  |
| `Proportion.failed.catch.trials` | `prop_failed_catch_trials` |  |  |  |  |  |
| `Pass/fail` | `pass_fail` |  |  |  |  |  |
| `Proportion.of.catch.trials.failed` | `prop_catch_failed_alt` |  |  |  |  |  |

## Required coding decisions

### `choice`

- Does it code left/right, accept/reject, ambiguous/reference, risky/safe, or something else?
- Which value means the participant chose the ambiguity/risky option?
- Does the answer depend on `refSide`?

Decision:

### `probs`

- Proportion scale `0-1`, percent scale `0-100`, or task level?
- Does it apply to the risky option, ambiguous option, or reference option?

Decision:

### `ambigs`

- Proportion scale `0-1`, percent scale `0-100`, or task level?
- Does higher mean more ambiguity?

Decision:

### `vals`

- Gain magnitude, option value, reference value, or value difference?
- Is it always positive, or can it encode losses/differences?

Decision:

### `refSide`

- Which side does it identify?
- How is it used to reconstruct the chosen option?

Decision:

### `colors` and `condition`

- Are these stimulus cues, ambiguity sources, experimental arms, blocks, or processing artifacts?
- Which, if any, should be considered candidate false-complex cognitive dimensions?

Decision:

## Quality-control rule

Primary catch-trial exclusion rule:

Sensitivity rules:

1.
2.
3.

## Merge with demographics/context

- Participant ID key in trial file:
- Participant ID key in demographic file:
- Merge success rate:
- SES/context variables available:
- Income coding:
- Education coding:
- SES composite construction, if any:

## Modeling readiness checklist

- [ ] `choice_ambiguous` or equivalent is defined.
- [ ] `probability` is scaled to `0-1`.
- [ ] `ambiguity` is scaled to `0-1`.
- [ ] `value` has a documented interpretation.
- [ ] `reference_side` is centered or encoded as a side-bias covariate.
- [ ] `condition` and `color_cue` are decoded.
- [ ] Participant-level catch-trial exclusions are fixed before model comparison.
- [ ] Demographic/context merge is verified.
- [ ] No confidential raw data are committed.

## Open PI questions

1.
2.
3.
