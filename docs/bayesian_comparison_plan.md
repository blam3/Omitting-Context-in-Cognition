# Bayesian Comparison Plan

This plan restructures the theorem and simulation work around two primary but
noninterchangeable Bayesian comparison targets: LOOIC for predictive
performance and Bayes factors for marginal model evidence under declared
priors. It does not prove a new theorem or promote C-004 beyond `planned`.

## Comparison Questions

| Question | Contrast | Estimand | Selection direction |
|---|---|---|---|
| Can omitted context make false complexity predict better? | `M4` versus `M1`; then `M4` versus `M2/M3` | Expected leave-out log predictive density and LOOIC | Higher ELPD / lower LOOIC |
| Can omitted context make false complexity receive more Bayesian model evidence? | Same contrasts under the declared candidate models | `log BF_{K,S}` | Positive log Bayes factor |

`M1` is the simple context-omitting model, `M2/M3` are context-aware simple
models, and `M4` is the context-omitting false-complex candidate. The first
contrast demonstrates misselection pressure; the second tests whether the
context-aware explanation remains preferable once context is modeled.

## Theorem Route

1. Establish the omitted-context conditional mixture representation.
2. State the Gaussian constructive heterogeneity result after its existing
   decision gate.
3. State KL dominance for explicit model classes.
4. State a separate conditional LOO expected-predictive-score proposition.
   It must define the leave-out unit and regularity connecting that population
   target to LOOIC.
5. State a separate conditional Bayes-factor proposition. It must name proper
   priors, their scales, the marginal-likelihood target, and the asymptotic
   regime. KL or LOOIC dominance alone is insufficient.
6. Retain AIC/BIC thresholds as secondary finite-sample bridge corollaries.

## Simulation Contract

For each simulated data set, preserve the common DGM and candidate-model
definitions across all criteria. Fit only Bayesian models with proper priors.
Store posterior log likelihood at the unit needed for the declared LOO target
and record the marginal-likelihood method used for each Bayes factor.

Report:

- ELPD and LOOIC differences, selection rates, and type I/type II error;
- Pareto-k summaries, the number of unreliable units, and any refit or exact
  fallback;
- log Bayes factors, selection rates, and the full prior-scale sensitivity
  grid;
- held-out participant log score as a robustness check;
- AIC/BIC only as a labelled proxy bridge from the GLM scaffold.

The current GLM proxy simulation is not permitted to emit Bayes factors or
LOOIC. Its role is limited to DGM screening and AIC/BIC continuity until the
hierarchical Bayesian model path is implemented.

## Decision Gate

Before fitting the first Bayesian comparison cell, select one primary LOO
target. The recommended option is leave-one-participant-out because the
scientific question concerns generalization to new people rather than another
trial from an already-observed participant. Trial-level LOO may be reported
as a secondary conditional diagnostic.

The first Bayes-factor implementation must separately document its proper
prior families, prior-scale sensitivity grid, and marginal-likelihood
estimator. These are not assumed by this plan.
