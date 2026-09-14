# Claim Registry

This registry prevents the autonomous researcher from turning tentative ideas into manuscript claims without evidence tracking.

| Claim ID | Claim | Claim type | Evidence status | Evidence source | Allowed use | Decision status | Last updated |
|---|---|---|---|---|---|---|---|
| C-001 | Omitting contextual causes of latent decision parameters can make model comparison favor the wrong cognitive mechanism. | central thesis | planned | theorem + simulation + RAID demonstration | abstract/introduction only after theorem and simulation support | approved_default | 2026-07-04 |
| C-002 | Omitted context induces a marginal mixture over latent decision parameters. | theorem | in_progress | proof-review draft in `docs/omitted_context_mixture_lemma.md` | theorem section/SI after proof review | approved_default | 2026-07-08 |
| C-003 | Under explicit residual conditions, the approved additive context model can create context-dependent latent variance; Gaussian distributional conclusions need additional conditions. | theorem | in_progress | docs/optional_gaussian_heterogeneity.md; docs/pi_decisions_2026-09-08.md | internal development; manuscript after proof review | primary_route_PI_approved_not_proved | 2026-09-08 |
| C-004 | In the specified two-trial utility construction, both joint candidate laws are false, K has strictly smaller KL risk, and BIC/BF/exact participant LOO favor K with probability tending to one. | constructive theorem | in_progress | PROOF_PACKAGE.md T1, L2, C1–C4; local proof complete, adversarial review pending | internal proof review; manuscript after acceptance | authorized_scope | 2026-09-05 |
| C-005 | The current GLM simulation scaffold can reveal failure modes worth testing in hierarchical Bayesian models. | infrastructure | scaffold_only | R proxy DGM and model suite | internal reports only | approved_default | 2026-07-04 |
| C-006 | RAID empirical results should be interpreted as context-aware model-sensitivity evidence, not causal SES evidence, unless additional design information supports causality. | empirical interpretation | planned | RAID analysis plan | methods/discussion limitation | approved_default | 2026-07-04 |

## Evidence status rules

- `scaffold_only`: supported only by infrastructure or toy proxy code.
- `planned`: conceptually endorsed but not yet tested/proved.
- `in_progress`: proof, simulation, or empirical analysis is underway.
- `supported_preliminary`: supported by reviewable but not final artifacts.
- `supported_final`: supported by finalized proof/results.
- `unsupported`: current evidence does not support the claim.
- `rejected`: claim should not be used.

## Promotion checklist

Before promoting a claim to `supported_preliminary` or `supported_final`, record:

1. the theorem, script, model fit, or source that supports it;
2. whether boundary cases are stated;
3. whether the claim is causal, predictive, descriptive, or mechanistic;
4. whether PI approval is required.

## 2026-09-05 scope note

The user authorized selecting the constructive model pair, correcting the shared simulation baseline, and developing separate BIC/BF/LOPO corollaries. A-007–A-010 record the resulting explicit choices. This does not adopt A-003, reinstate A-006 as a primary general assumption, select the final empirical model, or promote any claim to final support. The numerical KL gap is positive but small; the three seeded finite-sample verification datasets favor S, and must not be presented as false-complex selection-rate evidence.

## 2026-09-08 PI decisions

C-004 retains its finite benchmark scope and previous review status; it is not a trial-LOO, Gaussian or probability-distortion theorem. C-003 is now primary-route work, not final support. M4 probability distortion is selected, but no empirical evidence exists for its superiority or falsity in RAID. See `docs/pi_decisions_2026-09-08.md` and `docs/bayesian_comparison_plan.md`.

## 2026-09-08 primary separation attempt (author work; no promotion)

`docs/primary_separation_attempt_2026-09-08.md` records exact Gaussian representability and two-trial nuisance-absorption counterexamples for the primary candidate pair. Strict primary separation remains unestablished, including for a finite-support context with varying variance. Conditional finite-design deletion/score and separate evidence/BIC rate derivations have author-only status. They are not C-004 extensions, evidence that M4 wins, or final support for C-001. Existing claim statuses are unchanged; review and PI acceptance remain required.
