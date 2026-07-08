# Claim Registry

This registry prevents the autonomous researcher from turning tentative ideas into manuscript claims without evidence tracking.

| Claim ID | Claim | Claim type | Evidence status | Evidence source | Allowed use | Decision status | Last updated |
|---|---|---|---|---|---|---|---|
| C-001 | Omitting contextual causes of latent decision parameters can make model comparison favor the wrong cognitive mechanism. | central thesis | planned | theorem + simulation + RAID demonstration | abstract/introduction only after theorem and simulation support | approved_default | 2026-07-04 |
| C-002 | Omitted context induces a marginal mixture over latent decision parameters. | theorem | in_progress | proof-review draft in `docs/omitted_context_mixture_lemma.md` | theorem section/SI after proof review | approved_default | 2026-07-08 |
| C-003 | In the Gaussian constructive case, omitted context can create context-dependent latent variance. | theorem | planned | constructive proof | theorem section/SI after assumptions approved | decision_needed | 2026-07-04 |
| C-004 | A false complex model can beat a context-omitting simple model when its log-score advantage exceeds the model-selection penalty. | theorem/simulation bridge | planned | KL dominance + AIC/BIC threshold corollary | theorem section and simulation design | approved_default | 2026-07-04 |
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
