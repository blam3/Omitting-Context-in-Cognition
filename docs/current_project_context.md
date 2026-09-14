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
