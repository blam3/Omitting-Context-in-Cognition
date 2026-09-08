# Current project context

Updated 2026-09-08 after explicit PI decisions. Authoritative decision record: [pi_decisions_2026-09-08.md](pi_decisions_2026-09-08.md).

## Scientific goal and current evidence

Test whether omitting context that changes latent cognitive parameters can make a false, more complex cognitive model outperform a simpler context-omitting model. This is not a claim that complexity always wins or beats the correctly specified contextual distribution.

The PI-approved primary route now uses A-003: theta=a0+a1 Z+gamma C+u with E[C|Z=z]=m(z) and Var(C|Z=z)=v(z). The primary false-complex model family is probability distortion. Primary predictive comparison is trial-level leave-out. The new combined theorem is not yet proved. Conditional moment identities do not alone imply Gaussianity, heteroskedasticity without residual conditions, or observable KL separation.

[PROOF_PACKAGE.md](../PROOF_PACKAGE.md) is a preserved finite two-context/two-trial linear-versus-quadratic benchmark with local KL/BIC/BF/LOPO derivations. Separate LLM reviews of O1–O6 are complete; BF/LOPO review and external acceptance remain pending. Its assumptions, prior and holdout unit remain unchanged. Do not present it as proof of the new Gaussian/distortion/trial-LOO route. Lean remains infrastructure only.

## Active workflow

Read the decision record, [comparison plan](bayesian_comparison_plan.md), assumption/claim registers, [roadmap](proof_roadmap.md), [progress state](../registries/proof_progress.json), latest update and working-tree changes. G1_primary_specification is next; G2–G7 cover primary separation, trial LOO, BF, review, computation and manuscript. Older D1–D10 items are benchmark work, not the primary completion inventory.

## Likelihood and prediction

Trial LOO removes one response and retains that person's other responses; predict using the deleted-data posterior over both participant effects and global parameters. Validate exact refits before relying on PSIS, inspect diagnostics, and account for participant clustering in comparison uncertainty. New-participant LOPO may be reported separately. Participant dependence still governs full likelihoods and BIC asymptotics; trial leave-out does not license treating every row as independently sampled.

BF remains a full-data evidence integral with proper priors. The LLM selected weakly informative defaults and bridge sampling under PI delegation, with exact integration/quadrature for tractable verification. See the comparison plan for parameter scales and sensitivity checks. No BF result has yet been established for the new primary models.

## RAID coding and model ladder

The PI confirmed: choice identifies the risky/ambiguous lottery (codes 1/2); probs is observed win probability; ambigs measures ambiguous information; vals is a monetary amount; refSide is risky-option side; condition is gain/loss domain. Follow-up confirms 1=risky, 2=ambiguous, probs/ambigs on 0–1, domain labels "gain"/"loss", colors coded 1/2 with unknown meaning, and vals for only one option. The PI says losses are not currently stored; whether this means absent loss trials or unsigned magnitudes remains unresolved. Side codes, option alignment, the other lottery definition, exclusions and the context merge remain open. [The coding memo](raid_variable_coding_memo.md) records those gaps. No final real-data fitting until they are resolved; no restricted-data access is inferred from the descriptions.

| Model | Role |
|---|---|
| M1 | Simple ambiguity, no context |
| M2 | Same mechanism with context-dependent latent mean |
| M3 | Context-dependent mean and dispersion |
| M4 | Probability distortion, no context (PI-selected family) |
| M5 | Probability distortion plus the matched context specification |
| M0/M6 | Descriptive checks / optional predictive benchmark |

Primary empirical contrast remains M2/M3 versus M4; a precise M2-versus-M3 primary designation and task-level equations remain to be fixed before comparison. A one-parameter weighting form is proposed in the comparison plan, not yet validated for RAID. Gain/loss domain terms must be shared fairly; condition is not an assumed cognitive source cue. Observational context effects remain noncausal by default.

## Implementation state and boundaries

GLM proxies share risky_value and ambiguous_value baseline terms; the contextual proxy adds SES and the complex proxy adds curvature/cue terms. They are not the selected probability-distortion models. The representable fixed-parameter null uses context_effect="none" and latent_heterogeneity=FALSE; default no-context-effect retains heterogeneity.

The existing single-level Stan skeleton needs equation review, a fitting wrapper, prior predictive checks and recovery. It does not yet implement a validated two-lottery gain/loss task, hierarchical suite, or primary trial-LOO comparison. Follow the revised Bayesian milestones. No publication-scale simulation or empirical result is established.

The finite benchmark gap is small and its three seeded computational checks favor the simple model; do not recast those checks as selection rates. A correctly specified shared-effect simple model can remove an approximation gap. Any increasing-trial claim requires its own asymptotic argument. Scientific acceptance and production compute/dissemination remain separate decisions; already settled PI choices need no repeat approval.

---

# Retained from the pre-2026-09-08 context document

The sections below were current on `main` through 2026-09-06 and are kept for
reference after the 2026-09-08 PI redirection. Where they conflict with the
sections above, the sections above govern. The formal Result statements are
the mathematical objects the proof loop works from and remain in force; the
route ordering around them is superseded.

## Project program

1. **Formal proof:** omitted context induces mixtures, heteroskedasticity, or nonlinear marginal response distributions.
2. **Simulation:** under realistic sample sizes and task designs, a false complex model can beat the context-omitting simple model.
3. **Empirical demonstration:** trial-level RAID decision-under-uncertainty data test whether context-aware simple models change conclusions relative to context-omitting complex models.

## Formal result statements

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

Let $M_S$ be the context-omitting simple model and $M_K$ be the context-omitting complex model. If

$$
\inf_{\psi \in M_K} \text{KL}(p_0 \mid\mid p_\psi) < \inf_{\eta \in M_S} \text{KL}(p_0 \mid\mid p_\eta),
$$

then the false complex model has higher asymptotic expected log likelihood than the context-omitting simple model.

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

This result must be kept distinct from the KL bridge. The theorem draft must
state the target population, whether $G$ is a participant or a trial, and the
regularity conditions connecting its population log predictive density to the
estimated LOOIC. PSIS Pareto-k diagnostics are an empirical validity check,
not an assumption that can be silently waived.

### Result 5: Bayes-factor consequence under declared priors

For proper, predeclared priors within each candidate model, define

$$
BF_{K,S} = p(y \mid M_K) / p(y \mid M_S).
$$

The Bayes-factor target is also conditional: a separate result can study when
the omitted-context mixture leads to $log BF_{K,S} > 0$. It cannot be inferred
from KL dominance or from a LOOIC advantage alone. The statement must specify
the prior families and scales, the marginal-likelihood estimator, and the
asymptotic regime. Bayes factors answer a model-evidence question under those
priors; they are not a predictive-score substitute.

### Result 6: secondary AIC/BIC finite-sample bridge

Let $Delta ell$ be expected per-observation log-score advantage of the complex model.

AIC-like selection favors the false complex model when

$$
2 n Delta ell > 2(k_K - k_S).
$$

BIC-like selection favors it when

$$
2 n Delta ell > (k_K - k_S) log n.
$$

Treat these as secondary threshold corollaries under stated assumptions, not
universal guarantees. They retain continuity with the fast GLM scaffold but
are not the primary Bayesian cognitive-modeling endpoint.

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
