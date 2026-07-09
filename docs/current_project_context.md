# Current Project Context for the Autonomous Researcher

_Last updated: 2026-07-09_

## Core thesis

The project is no longer only about biased parameter estimates. The central claim is now:

> Omitting contextual causes of latent decision parameters can make model comparison favor the wrong cognitive mechanism.

The target paper should combine three evidence streams:

1. **Formal proof:** omitted context induces mixtures, heteroskedasticity, or nonlinear marginal response laws.
2. **Simulation:** under realistic sample sizes and task designs, a false complex model can beat the context-omitting simple model.
3. **Empirical demonstration:** trial-level RAID decision-under-uncertainty data test whether context-aware simple models change conclusions relative to context-omitting complex models.

## Required governance files

Before making scientific changes, consult:

- `registries/assumption_register.csv` for assumptions and decision status;
- `registries/claim_register.md` for claim/evidence status;
- `docs/hierarchical_bayes_milestones.md` for the staged path from GLM proxies to Stan/brms models;
- `logs/research_updates/README.md` for required structured cycle reports.

Any new theorem assumption, causal claim, primary false-complex model choice, or estimand change must be recorded and decision-gated.

## Formal theorem package

The autonomous researcher should prioritize a publishable constructive theorem before attempting a fully general theorem.

### Result 1: omitted-context mixture representation

Let `Y_it` be choice, `X_it` trial features, `Z_i` observed participant covariates, `C_i` omitted context, and `theta_i` a latent decision parameter. If

```math
theta_i = h(Z_i, C_i, U_i)
```

and choices follow

```math
p(Y_it | X_it, theta_i; eta),
```

then the analyst who omits `C_i` observes

```math
p_0(y | x,z) = int p(y | x, theta; eta*) dF_{theta|Z}(theta | z).
```

This is the first theorem object the loop should try to formalize and check.

### Result 2: Gaussian constructive heterogeneity

Use the constructive case

```math
theta_i = alpha_0 + alpha_1 Z_i + gamma C_i + u_i,
```

with

```math
C_i | Z_i=z ~ N(m(z), v(z)).
```

Then

```math
theta_i | Z_i=z ~ N(alpha_0 + alpha_1 z + gamma m(z), sigma_u^2 + gamma^2 v(z)).
```

If `v(z)` is nonconstant, omission creates context-dependent latent variance. This is the clean bridge from omitted context to false complexity.

### Result 3: KL dominance

Let `M_S` be the context-omitting simple model and `M_K` be the context-omitting complex model. If

```math
inf_{psi in M_K} KL(p_0 || p_psi) < inf_{eta in M_S} KL(p_0 || p_eta),
```

then the false complex model has higher asymptotic expected log likelihood than the context-omitting simple model.

### Result 4: predictive-score consequence for LOOIC

Let `G` denote the prespecified unit left out for predictive evaluation, and
let `elpd_LOO(M)` be the expected log predictive density of model `M` for that
unit. For the context-omitting simple model `M_S` and the context-omitting
complex model `M_K`, define

```math
Delta_LOO = elpd_LOO(M_K) - elpd_LOO(M_S).
```

The target LOOIC consequence is conditional: if `Delta_LOO > 0`, the
leave-out unit is defined before fitting, and the LOO estimator is valid for
the fitted model class, then the complex model has lower LOOIC, because

```math
LOOIC(M) = -2 elpd_LOO(M).
```

This result must be kept distinct from the KL bridge. The theorem draft must
state the target population, whether `G` is a participant or a trial, and the
regularity conditions connecting its population log predictive density to the
estimated LOOIC. PSIS Pareto-k diagnostics are an empirical validity check,
not an assumption that can be silently waived.

### Result 5: Bayes-factor consequence under declared priors

For proper, predeclared priors within each candidate model, define

```math
BF_{K,S} = p(y | M_K) / p(y | M_S).
```

The Bayes-factor target is also conditional: a separate result can study when
the omitted-context mixture leads to `log BF_{K,S} > 0`. It cannot be inferred
from KL dominance or from a LOOIC advantage alone. The statement must specify
the prior families and scales, the marginal-likelihood estimator, and the
asymptotic regime. Bayes factors answer a model-evidence question under those
priors; they are not a predictive-score substitute.

### Result 6: secondary AIC/BIC finite-sample bridge

Let `Delta ell` be expected per-observation log-score advantage of the complex model.

AIC-like selection favors the false complex model when

```math
2 n Delta ell > 2(k_K - k_S).
```

BIC-like selection favors it when

```math
2 n Delta ell > (k_K - k_S) log n.
```

Treat these as secondary threshold corollaries under stated assumptions, not
universal guarantees. They retain continuity with the fast GLM scaffold but
are not the primary Bayesian cognitive-modeling endpoint.

## Boundary conditions the loop must preserve

Do **not** claim context omission always causes false-complex selection. Explicitly track these null or low-risk cases:

1. `C` has no effect on `theta`.
2. `C` is independent of relevant observed features and only adds correctly modeled iid noise.
3. The simple model already contains sufficient random-effect structure to represent the marginal law.
4. The complex model does not approximate the omitted-context mixture better than the simple model.
5. The LOO target is poorly aligned with the scientific generalization target,
   or PSIS diagnostics indicate unreliable importance sampling.
6. Bayes-factor conclusions change materially across defensible prior scales
   or marginal-likelihood estimators.
7. Model-selection penalties dominate the added fit in the finite sample.

## RAID empirical crosswalk

The current RAID variable map is:

| Theorem object | RAID counterpart |
|---|---|
| `Y_it` | `choice` |
| `X_it` | `probs`, `ambigs`, `vals`, `colors`, `refSide`, `condition` |
| `Z_i` | income, education, age, gender, race, ethnicity, other demographics |
| `C_i` | SES/resource context, proxied by income and education |
| `theta_i` | ambiguity aversion, risk sensitivity, choice stochasticity, source/condition sensitivity |
| `M_S` | one-parameter ambiguity model with no context predictors |
| `M_{S+C}` | same ambiguity model with SES/context predicting latent parameters |
| `M_K` | source/color/condition/nonlinear ambiguity model with no context predictors |

## Required RAID coding audit before empirical modeling

The loop must not fit final empirical models until a coding memo answers:

1. What does `choice` code: ambiguous/risky/reference, left/right, accept/reject, or something else?
2. Are `probs` and `ambigs` proportions, percentages, or task levels?
3. What does `vals` represent: gain magnitude, option value, reference value, or value difference?
4. How does `refSide` map to displayed options and `choice`?
5. What are `colors` and `condition`: cues, sources, arms, blocks, or processing labels?
6. Are catch-trial fields row-level, participant-level, or both?
7. What exclusion rule is primary, and which sensitivity rules are preregistered?

Use `docs/raid_variable_coding_memo_template.md` for the audit. Use `R/generate_synthetic_raid_data.R` and `make synthetic-raid` for public pipeline testing before restricted data are available.

## Current empirical model ladder

| Model | Context? | Complexity | Purpose |
|---|---:|---:|---|
| M0 descriptive logistic | optional | low | sanity check trial effects |
| M1 simple ambiguity | no | low | context-omitting baseline |
| M2 simple ambiguity + SES mean | yes | low | context shifts latent ambiguity aversion |
| M3 simple ambiguity + SES mean/variance | yes | moderate | theorem-predicted heteroskedasticity |
| M4 complex ambiguity | no | high | candidate false-complex model |
| M5 complex ambiguity + SES | yes | high | test whether complexity remains after context inclusion |
| M6 predictive benchmark | yes/no | flexible | guard against structural overinterpretation |

Primary empirical contrast: **M2/M3 vs. M4**.

## Bayesian comparison protocol

The simulation and final empirical analysis should report two primary but
noninterchangeable comparisons:

| Question | Primary quantity | Direction favoring `M_K` | Required safeguard |
|---|---|---|---|
| Does false complexity predict new data better after context is omitted? | `Delta elpd_LOO = elpd_LOO(M_K) - elpd_LOO(M_S)` and its LOOIC equivalent | Positive `Delta elpd_LOO` / lower LOOIC | Predeclare the leave-out unit and report Pareto-k diagnostics. |
| Does the declared Bayesian model assign greater marginal evidence to false complexity? | `log BF_{K,S}` | Positive `log BF_{K,S}` | Use proper priors, report prior-scale sensitivity, and identify the marginal-likelihood method. |

The preferred scientific target is generalization to a new participant. The
exact LOO unit remains a PI decision gate because trial-level and
participant-level leave-out answer different questions for hierarchical
cognitive models. Trial-level LOO can be a secondary within-participant
diagnostic; it must not be silently substituted for new-participant prediction.

AIC/BIC remain secondary bridge diagnostics. The current GLM scaffold must
label them as proxies and must not report fabricated Bayes factors or LOOIC
values. See `docs/bayesian_comparison_plan.md` for the implementation contract.

## Bayesian modeling path

The GLM scaffold is only for smoke tests. Follow `docs/hierarchical_bayes_milestones.md` to move toward:

1. single-level structural ambiguity likelihood;
2. participant-level hierarchical ambiguity model;
3. context-aware mean model;
4. context-aware mean-plus-variance model;
5. PI-selected primary false-complex model;
6. final M1-M5 empirical model suite.

The initial Stan skeleton is `stan/simple_ambiguity_single_level.stan`.

## Autonomous researcher priorities

1. Keep the theorem, simulation, and empirical analysis synchronized.
2. Prefer exact constructive results over vague general claims.
3. Convert every new assumption into an explicit assumption register entry.
4. Convert every model-selection claim into an explicit comparison criterion:
   KL, LOO expected log predictive density/LOOIC, Bayes factor under declared
   priors, held-out log score, or the secondary AIC/BIC bridge.
5. Ask the human PI before adding assumptions, changing estimands, choosing the primary false-complex model, or interpreting RAID results as causal.
6. Write a structured cycle report to `logs/research_updates/` for every autonomous researcher cycle.
