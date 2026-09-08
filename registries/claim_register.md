# Claim Registry

This registry prevents the autonomous researcher from turning tentative ideas into manuscript claims without evidence tracking.

| Claim ID | Claim | Claim type | Evidence status | Evidence source | Allowed use | Decision status | Last updated |
|---|---|---|---|---|---|---|---|
| C-001 | Omitting contextual causes of latent decision parameters can make model comparison favor the wrong cognitive mechanism. | central thesis | planned | theorem + simulation + RAID demonstration | abstract/introduction only after theorem and simulation support | approved_default | 2026-07-04 |
| C-002 | Omitted context induces a marginal mixture over latent decision parameters. | theorem | in_progress | proof-review draft in `docs/omitted_context_mixture_lemma.md` | theorem section/SI after proof review | approved_default | 2026-07-08 |
| C-003 | In the Gaussian constructive case, omitted context can create context-dependent latent variance, and does so **if and only if** the context coefficient is non-zero and its conditional variance is non-constant. | theorem | in_progress | `docs/theorems/T-003_gaussian_constructive.md` (statement-draft; A-003 approved by D-001) | theorem section/SI after proof review | approved_default | 2026-09-08 |
| C-004 | Under explicit criterion-specific conditions, a false complex model can beat a context-omitting simple model in predictive score. The mechanism is **variance** heterogeneity in the omitted context; mean heterogeneity alone is absorbed by the simple random-effects model. | theorem/simulation bridge | in_progress | T-004 (KL dominance, `docs/theorems/T-004_kl_dominance.md`) + T-005 (trial-level LOO bridge) + T-007 (finite-sample thresholds, singular-case corrected). **Bayes factors removed** by D-003; **AIC/BIC not admissible as evidence** by D-004. | theorem section and simulation design after A-007/A-008/A-009 are approved and proof review completes | approved_default | 2026-09-08 |
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
