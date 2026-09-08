# Project status: Omitting Contextual Factors in Cognitive Models

Updated September 8, 2026 after PI decisions. Based on the local working tree and recorded checks; no new model fitting or proof acceptance is implied.

## Current position

**The major design choices are now recorded, but the newly selected primary theorem and model suite still need to be developed and validated.** The existing complete local proof draft concerns a different finite linear-versus-quadratic benchmark. Its KL/BIC reviews remain useful evidence for that example; they do not establish the revised additive-context, probability-distortion, trial-LOO result.

The central goal remains to show when omitted context can make a false complex cognitive model outperform a simple context-omitting candidate, and demonstrate the implications through simulations and RAID data.

## PI decisions now settled

| Decision | Selected direction | Remaining work |
|---|---|---|
| Primary LOO | Trial-level leave-out | Derive and validate prediction conditional on the person's remaining trials; preserve clustering in uncertainty. |
| A-003 | Additive contextual equation with conditional context mean/variance may be primary | Explicit residual/Gaussian conditions; observable separation and criterion proofs. Approval is not proof. |
| M4 | Probability distortion | Exact weighting and gain/loss lottery equation, identifiability and recovery. |
| Priors | LLM delegated proper diffuse/weakly informative choices and scales | Weakly informative defaults selected; validate on documented scales using prior predictive checks. |
| Evidence estimator | LLM delegated choice | Bridge sampling selected for computation; exact evidence integrals for proofs and quadrature for tractable validation. |
| RAID fields | Six semantic meanings supplied | Choice mapping, 0–1 scales and domain labels confirmed; side/color meaning, both lottery definitions and quality-control rules remain. |

See the [decision record](docs/pi_decisions_2026-09-08.md), [Bayesian comparison plan](docs/bayesian_comparison_plan.md), and [coding memo](docs/raid_variable_coding_memo.md). Do not ask the PI to choose these model families or holdout units again.

## Evidence by project goal

| Goal | Current evidence | Gap |
|---|---|---|
| Formal explanation | [Finite benchmark](PROOF_PACKAGE.md) has local KL/BIC/BF/LOPO derivations; O1–O6 passed separate LLM reviews. | New primary route unproved; benchmark BF/LOPO and external reviews still pending. |
| Simulation demonstration | GLM scaffold and shared-baseline fixes; historical smoke/numerical checks. | GLM curvature/cue model is not probability distortion. No production selection-rate study; run registry has only a header. |
| Structural cognitive models | Single-level Stan skeleton. | Validated two-lottery gain/loss equation, fitting wrapper, priors/recovery, hierarchy, M4 and trial-LOO implementation. |
| RAID analysis | Partially completed coding memo based on PI responses. | Secure directories inspected locally are empty; data/protocol access, exact coding, exclusions and context merge remain needed. |
| Paper and reproducibility | Manuscript/SI skeletons, registries and verification scripts. | Reviewed primary theory, simulation/empirical evidence, figures/tables and PI acceptance. Lean remains infrastructure. |

The benchmark gap is about 0.000699 nats per participant. Its three seeded finite-sample checks favor the simple model and are not selection-rate estimates. The September 5 log reports smoke and package-free checks passed but the full testthat suite was not run. September 7 records passing BIC checks. This decision update does not claim new runtime verification of scientific code or remote CI.

## Concrete next steps for the PI

1. **Resolve remaining coding details.** Choice mapping (1=risky, 2=ambiguous), 0–1 scales, and "gain"/"loss" labels are now settled. Resolve which option probs/vals describe, the other lottery's payoff/probability, side codes, and whether loss data are absent or stored as unsigned magnitudes. Colors are 1/2, but their meaning is unknown. Supply protocol/codebook and authorize local data access when ready. Semantics alone cannot determine the likelihood.
2. **Review the next primary theorem specification.** A-003 is approved. Decide only on any additional residual/distribution conditions actually needed after the LLM presents an exact proposal. Conditional moments alone do not imply normality or a strict observable KL gap.
3. **Review task-specific M4 implementation and context specification.** Probability distortion is settled. Confirm the concrete weighting/task equation, primary M2 versus M3 designation, context coding, and predeclared exclusions after the design audit. Avoid outcome-driven selection.
4. **Review recovery/pilot evidence and approve production resources.** Require all cells, failures, prior sensitivities, and Monte Carlo uncertainty. Existing expensive-job thresholds remain in [approval policy](docs/approval_policy.md); no production launch is authorized by choosing priors or LOO.
5. **Arrange independent scientific review and accept the final package.** Separate local author derivations, LLM review, external review, and PI acceptance. Venue and dissemination remain later decisions.

## Bounded LLM prompts for the revised route

### 1. Specify the primary theorem without importing old conclusions

```text
Read docs/pi_decisions_2026-09-08.md, docs/bayesian_comparison_plan.md, the live
assumption/claim registers and registries/proof_progress.json. Complete
G1_primary_specification in docs/primary_theorem_specification.md: define the
approved A-003 equation, conditioning, sampling regime, choice DGP and candidate
probability-distortion comparison. Separate approved moment assumptions from any
extra residual/Gaussian hypotheses. Give the general mean/variance identities
and show what each proposed extra condition buys. Define the exact trial-deletion
score. Inventory the lemmas needed for observable separation, BF and trial LOO;
do not transfer the benchmark's quadratic/LOPO result. Provide a precise proposal
only for genuinely new assumptions. Update state and a validated research log;
completion is a reviewable specification and explicit gaps, not theorem acceptance.
```

### 2. Establish separation, then trial-level prediction

```text
After the primary specification is resolved, attempt strict observable separation
for its exact simple and probability-distortion laws. Check a correctly specified
shared-effect simple model as a boundary case. If separation fails, record the
counterexample and implication rather than tuning the example for a win. Once
separation is established, derive exact single-trial deletion under the same
sampling regime: retain other trials of that participant, integrate over the
deleted-data posterior, and handle within-person dependence. Establish the needed
score convergence instead of invoking the old LOPO proof. Keep BF and BIC arguments
separate. Record proofs, targeted checks, failures and next dependencies; no final
claim promotion without review and PI acceptance.
```

### 3. Finish the coding memo and task-level model specification

```text
Read docs/raid_variable_coding_memo.md and the PI's latest answers. Preserve the
confirmed meanings; never infer choice-code order, percent scaling, loss signs
or color semantics. Reconstruct both lottery values and their probabilities from
the protocol. Specify a probability-distortion M4 with matched baseline terms,
a no-distortion restriction and explicit gain/loss handling. Inspect whether the
proposed weighting form can be identified by this task. Document unresolved inputs
and complete synthetic-only work while waiting. Do not fit final empirical models
or infer restricted-data permission from field descriptions.
```

### 4. Implement and validate the smallest structural pilot

```text
Inspect the existing Stan skeleton and approved task equation. Add a fitting
wrapper, prior predictive checks and a seeded recovery pilot using the selected
proper weakly informative scales in docs/bayesian_comparison_plan.md. Verify
parameter scales before fitting. Include correct-specification, no-context with
heterogeneity, fixed-parameter null and true-distortion controls. Validate exact
trial-level refits before PSIS; report diagnostics and participant-clustered score
uncertainty. Validate bridge sampling against quadrature in tractable cases,
including normalization constants and Jacobians. Report all failures and sensitivity
runs. Respect the local compute cap and obtain a concrete budget decision before
production work. Do not claim that a working GLM scaffold validates M4.
```

### 5. Reconcile evidence and draft the paper

```text
Read current decisions, reviewed proof artifacts and actual simulation/RAID reports.
Build a claim-to-evidence table. Distinguish the old finite quadratic benchmark
from the primary additive-context/probability-distortion result. State trial-level
LOO's conditional prediction target, finite-sample limits and noncausal RAID scope.
Draft only supported material into manuscript/SI; mark absent results explicitly.
Verify references, compile if possible, and prepare independent-review and PI
acceptance checklists. No publication or claim promotion follows automatically
from an assumption approval or a successful numerical run.
```

**G1 complete for specification review only:** see [primary specification](docs/primary_theorem_specification.md), including explicit proposal packages and PG-L1–PG-L10 proof gaps. No primary theorem has been accepted.

**Next executable task:** G2_observable_separation in the [revised progress state](registries/proof_progress.json). Historical D1/D2 review evidence is retained under the finite benchmark; the old BF review is no longer the sole primary next step.


## Latest primary attempt — September 8, 2026

[The G2 proof and failure record](docs/primary_separation_attempt_2026-09-08.md) gives two exact obstructions: a correctly specified Gaussian shared-effect boundary and a two-trial design where intercept/side terms absorb all distortion. The attempted finite-support varying-variance context does not create separation. No example was tuned to win. A conditional finite-design trial-deletion score theorem and separate BF/BIC rate statements are now author drafts; positive primary gaps and independent review remain open. Next G2 work is a full-support design-absorption audit, preserving the matched nuisance terms.


The [full-support design audit](docs/design_absorption_audit_2026-09-08.md) now confirms all-rho absorption across both Z levels and both trials. The current support cannot yield strict S/K separation. A complete richer or RAID support is still missing; its probability/payoff/side mappings must be specified before another support audit. No P-G3 or final-claim approval status changed.
