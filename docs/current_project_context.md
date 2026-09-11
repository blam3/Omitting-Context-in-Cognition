<!-- coherence-allow: bare_delta_ell -->
# Current Project Context for the Autonomous Researcher

_Last updated: 2026-09-08_

> **Binding decisions.** D-001 to D-005 in `docs/approval_log.md` are now in force.
> Symbols are bound by `docs/notation_registry.md`. Precise theorem statements
> live in `docs/theorems/`; the summaries below are orientation only and are
> superseded by those files wherever they differ.

## Core thesis

The project is no longer only about biased parameter estimates. The central claim is now:

> Omitting contextual causes of latent decision parameters can make model comparison favor the wrong cognitive mechanism.

The target paper should combine three evidence streams:

1. **Formal proof:** omitted context induces mixtures, heteroskedasticity, or nonlinear marginal response distributions.
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

### Result 1: Omitted-context mixture representation

Let $Y_{it}$ be choice, $X_{it}$ trial features, $Z_i$ observed participant covariates, $C_i$ omitted context, $theta_i$ a latent decision parameter, and $U_i$ represents unobserved individual-level random error/noise. If

$$
\theta_i = h(Z_i, C_i, U_i)
$$

and choices follow

$$
p(Y_{it} \mid X_{it}, \theta_i; \eta),
$$

then the analyst who omits $C_i$ observes

$$
p_0(y \mid x, z) = \int p(y \mid x, \theta; \eta*) dF_{\theta \mid X,Z}(\theta \mid x, z).
$$

where $p_0$ is the probability distribution under the omitted context.

This is the first theorem object the loop should try to formalize and check.

### Result 2: Gaussian constructive heterogeneity

Use the constructive case

$$
\theta_i = \alpha_0 + \alpha_1 Z_i + \gamma C_i + u_i,
$$

with

$$
C_i | Z_i=z ~ N(m(z), v(z)).
$$

Then

$$
\theta_i | Z_i=z ~ N(\alpha_0 + \alpha_1 z + \gamma m(z), \sigma_u^2 + \gamma^2 v(z)).
$$

If $v(z)$ is nonconstant, omission creates context-dependent latent variance. This is the clean bridge from omitted context to false complexity.

### Result 3: KL dominance

Let $M_S$ be the context-omitting simple model, indexed by $\beta_S$, and $M_K$
the context-omitting complex model, indexed by $\beta_K$. (The earlier draft used
$\eta$ and $\psi$ here, which clashed with $\eta$ as the choice-kernel parameter;
see `docs/notation_registry.md` §4.)

The previously stated form of this result — "if $\inf_{M_K}\mathrm{KL} <
\inf_{M_S}\mathrm{KL}$ then $M_K$ has higher asymptotic expected log-likelihood"
— is **circular**: the hypothesis and conclusion are the same proposition, since
$\mathrm{KL}(p_0\|p_\beta) = -\mathbb{E}[\log p_\beta] + \text{const}$.

The actual result, stated and proved in
`docs/theorems/T-004_kl_dominance.md`, gives conditions under which the
inequality holds:

$$\inf_{\beta_K} \mathrm{KL}_Q(p_0 \| p_{\beta_K}) = 0 < \inf_{\beta_S} \mathrm{KL}_Q(p_0 \| p_{\beta_S})$$

whenever (i) $p_0 \notin \bar{M}_S$ and (ii) $p_0 \in M_K$, with a decidable
criterion for (i) supplied by Lemma T-004a. The sharp finding is that the
mechanism is **variance** heterogeneity: if the omitted context shifts only the
mean of the latent parameter, and that induced mean is Gaussian, then
$p_0 \in M_S$ exactly and there is no gap at all (Proposition T-004d).

### Result 4: predictive-score consequence for LOOIC

Let $G$ denote the prespecified unit left out for predictive evaluation, and
let $elpd_{LOO(M)}$ be the expected log predictive density of model $M$ for that
unit. For the context-omitting simple model $M_S$ and the context-omitting
complex model $M_K$, define

$$
Delta_{LOO} = elpd_{LOO(M_K)} - elpd_{LOO(M_S)}.
$$

The target LOOIC consequence is conditional: if $Delta_LOO > 0$, the
leave-out unit is defined before fitting, and the LOO estimator is valid for
the fitted model class, then the complex model has lower LOOIC, because

$$
LOOIC(M) = -2 elpd_{LOO(M)}.
$$

**$G$ is bound to a single TRIAL by D-002 (2026-09-08).** The primary predictive
estimand is therefore within-participant next-trial prediction, *not*
generalisation to a new participant. Trial-level leave-out is optimistic for
models with more participant-level flexibility, i.e. biased toward $M_K$, which
is the direction of this paper's own claimed effect; participant-level K-fold is
a mandatory secondary analysis and the bias must be stated where the primary
result is reported. See `docs/theorems/T-005_loo_predictive.md`.

The content of the result is the **estimator-to-population bridge**, not the
identity $\mathrm{LOOIC} = -2\,\mathrm{elpd}$, which is arithmetic. PSIS
Pareto-$\hat k$ diagnostics are an empirical validity check, not an assumption
that can be silently waived.

### Result 5: Bayes factors — DEFERRED, not a theorem target

Demoted by D-003 (2026-09-08) to a numerical prior-sensitivity study reported as
a robustness appendix. It is not in the theorem route, may not appear in the
abstract, and may not be cited in support of C-001.

The reasons are recorded in full in
`docs/theorems/T-006_bayes_factor_deferred.md`: model evidence is a different
estimand from the predictive comparison the paper critiques; the sign of
$\log BF_{K,S}$ is manipulable through the prior scale on $M_K$'s extra
parameters; and the closed-form asymptotics a theorem would need are invalid
because $M_K$ is singular. Declared priors, scale grid, and the bridge-sampling
estimator are fixed by D-003.

### Result 6: finite-sample selection thresholds — CORRECTED

The previously stated thresholds ($2n\Delta\ell > 2(k_K-k_S)$ for AIC,
$2n\Delta\ell > (k_K-k_S)\log n$ for BIC) contained two errors and have been
split into three statements in
`docs/theorems/T-007_finite_sample_selection.md`:

1. **T-007a** the exact algebra, in terms of the *realised* log-likelihood
   difference $D_n$ — a rearrangement of definitions, not a result;
2. **T-007b** the probabilistic bridge $D_n/n \to_p \Delta\ell^{*}$ with a CLT,
   valid only under interior pseudo-true parameters and non-singular information,
   plus a minimum-sample-size corollary;
3. **T-007c** the singular-case correction.

The two errors were: conflating the population per-observation gap
$\Delta\ell^{*}$ with the realised $D_n$ (they differ by $O_p(\sqrt n)$, the same
order as the AIC penalty at moderate $n$); and using penalties whose derivations
require regularity that fails here.

**Singularity (D-004).** $M_K$ is a mixture / random-effects family and is a
singular statistical model: where a component is empty or a variance is zero the
parameter is not locally identifiable and the Fisher information degenerates —
and those are exactly the parameter values that boundary conditions 1-3 make
central. Therefore:

- BIC's $(k/2)\log n$ is invalid and **over-penalises** $M_K$ (the correct
  free-energy expansion uses the real log canonical threshold $\lambda \le k/2$),
  so a BIC null result is not evidence against C-004;
- AIC's $2k$ assumes correct specification; the misspecification-robust
  replacement $2\,\mathrm{tr}(J^{-1}V)$ does not exist when $J$ is singular;
- no $\chi^2_{\Delta k}$ significance reading of $D_n$ is permitted (boundary
  parameters give a chi-squared mixture);
- nominal counts $k_S, k_K$ may not be reported as complexity — report
  $p_\mathrm{loo}$ / $p_\mathrm{waic}$.

PSIS-LOO and WAIC are the primary criteria because they remain asymptotically
valid for singular models. AIC/BIC are legacy bridge diagnostics only.

## Boundary conditions the loop must preserve

Do **not** claim context omission always causes false-complex selection. Explicitly track these null or low-risk cases:

1. $C$ has no effect on $\theta$.
2. $C$ is independent of relevant observed features and only adds correctly modeled iid noise.
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
| _(deferred, D-003)_ Does the declared model assign greater marginal evidence to false complexity? | `log BF_{K,S}` — **robustness appendix only, not a theorem** | Positive `log BF_{K,S}` | Priors and estimator fixed by D-003; report the full prior-scale grid; not citable for C-001. |

**The LOO unit is settled: trial-level (D-002).** The primary estimand is
within-participant next-trial prediction. Generalisation to a new participant is
now the *secondary* analysis, via mandatory participant-level K-fold, and the
paper may not claim new-participant generalisation on trial-level evidence.

AIC/BIC are legacy diagnostics and are not admissible evidence for C-004
(D-004). The current GLM scaffold must
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
