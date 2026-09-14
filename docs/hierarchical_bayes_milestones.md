# Hierarchical Bayesian Modeling Milestones

The current GLM models are smoke-test proxies. The final project needs hierarchical Bayesian structural models that estimate latent ambiguity parameters, participant-level context effects, and predictive criteria.

## Likelihood and holdout contract (PI revision 2026-09-08)

Primary trial-level LOO deletes one response and retains the participant's other trials. Integrate over the deletion posterior of participant effects and global parameters. Validate exact single-trial refits before PSIS; account for participant dependence when reporting uncertainty. LOPO is an optional new-person sensitivity, not the primary score. See [comparison plan](bayesian_comparison_plan.md).

The finite PROOF_PACKAGE.md remains a separate LOPO benchmark. Its theorem does not establish the revised primary result. BIC scaling remains a property of the likelihood and sampling regime; BF uses full-data evidence, proper weakly informative priors, and bridge sampling validated against tractable integrals. A-003 is primary, but additional residual/Gaussian conditions require explicit treatment.

## Goal

Move from fast GLM proxies to a staged Stan/brms model suite without losing alignment with the theorem and RAID empirical plan.

## Milestone 0: proxy scaffold integrity

**Purpose:** Keep CI fast and ensure the autonomous loop can detect broken simulation infrastructure.

**Models:**

- simple omitted-context GLM proxy;
- complex omitted-context GLM proxy;
- simple context-aware GLM proxy.

**Exit criteria:**

- `make smoke` passes;
- `make test` passes;
- proxy output includes false-complex selection rates and context-aware comparison rates;
- proxy claims remain marked `scaffold_only` in the claim register.

## Milestone 1: single-level structural ambiguity likelihood

The equation below is a historical scaffold. It must be checked against both lottery values and gain/loss coding before use; it is not the approved final RAID likelihood.

**Purpose:** Replace descriptive GLM terms with the ambiguity-value equation.

```math
SV_{it} = v_{it}(p_{it} - \beta A_{it}/2)
```

```math
Y_{it} \sim Bernoulli(logit^{-1}(\alpha + \tau SV_{it} + \delta_{side} refSide_{it}))
```

**Deliverables:**

- Stan model: `stan/simple_ambiguity_single_level.stan`;
- R fitting wrapper using `cmdstanr` or `rstan`;
- prior predictive simulation;
- recovery check on synthetic data.

**Exit criteria:**

- recovers known `beta` and `tau` in synthetic data;
- no divergent transitions in small test fits;
- posterior predictive checks recover broad choice rates by ambiguity and probability.

## Milestone 2: participant-level hierarchical ambiguity model

**Purpose:** Estimate participant-level latent ambiguity aversion and choice sensitivity.

```math
\beta_i \sim Normal(\mu_\beta, \sigma_\beta)
```

```math
\log \tau_i \sim Normal(\mu_\tau, \sigma_\tau)
```

**Deliverables:**

- Stan model: `stan/simple_ambiguity_hierarchical.stan`;
- non-centered parameterization;
- posterior predictive checks by participant and trial features;
- exact single-trial deletion/refit script; optional participant-holdout script.

**Exit criteria:**

- model recovery succeeds under idealized simulation;
- posterior intervals have reasonable calibration in small simulation grids;
- trial-level deletion log score is computed and validated without held-out-response leakage.

## Milestone 3: context-aware mean model

**Purpose:** Test whether observed context predicts latent ambiguity aversion without adding a new cognitive architecture.

```math
\beta_i \sim Normal(\mu_\beta + b_{inc} income_i + b_{edu} education_i, \sigma_\beta)
```

**Deliverables:**

- Stan model or generated quantities extension;
- income-only, education-only, and composite-SES variants;
- validated trial-level PSIS-LOO comparison with Milestone 2; optional separate LOPO sensitivity.

**Exit criteria:**

- context effects are recoverable in simulation;
- posterior predictive checks improve for context-stratified groups when true context effects exist;
- claim register updated only with evidence-supported statements.

## Milestone 4: context-aware mean-plus-variance model

**Purpose:** Implement the primary A-003 dispersion route subject to explicit residual conditions; approval of the additive equation alone is not a heteroskedasticity proof.

```math
\log \sigma_{\beta,i} = \omega_0 + \omega_{inc} income_i + \omega_{edu} education_i
```

**Deliverables:**

- heteroskedastic hierarchical model;
- simulation recovery of context-dependent dispersion;
- comparison to false-complex context-omitting models.

**Exit criteria:**

- recovers simulated context-dependent variance under nontrivial effect sizes;
- does not spuriously infer heteroskedasticity under null simulation;
- reports sensitivity to priors on variance effects.

## Milestone 5: primary false-complex model

**Purpose:** Fit the psychologically plausible complex model that omits context.

**PI decision 2026-09-08:** probability distortion is selected. The family-selection gate is closed. Specify its weighting function, option-value equation, domain handling and parameter hierarchy against the coding audit. The one-parameter form in `bayesian_comparison_plan.md` is a concrete proposal; other mechanisms are not co-primary by default.

**Exit criteria:**

- primary false-complex model is documented in the assumption and claim registries;
- model recovery distinguishes true context effects from true complexity under simulation;
- model comparison reports uncertainty and not only point estimates.

## Milestone 6: final empirical model suite

**Purpose:** Fit M1-M5 on cleaned RAID data after the variable-coding memo is complete.

**Primary comparison:** M2/M3 context-aware simplicity versus M4 context-omitting complexity.

**Primary metrics:**

- trial-level LOO ELPD with validated deletion predictions and participant-clustered uncertainty;
- exact held-out-trial log score checks;
- posterior predictive checks by SES/context group.

**Secondary metrics:**

- optional new-participant LOPO and WAIC sensitivities;
- AIC/BIC bridge for theorem/simulation continuity;
- Bayes factor or marginal likelihood only as prior-sensitive sensitivity.

## Immediate next implementation tasks

1. Audit the existing `stan/simple_ambiguity_single_level.stan` against the two-lottery gain/loss task and selected priors.
2. Add a synthetic-data model-recovery script.
3. Add posterior predictive check functions.
4. Add trial-level exact refit utilities; keep participant holdout as optional sensitivity.
5. Implement the selected probability-distortion model after task-equation and identifiability review; do not reopen its family-selection gate.
