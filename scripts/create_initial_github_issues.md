# Initial GitHub Issues

Create these manually or through GitHub CLI.

## Issue 1: Formalize minimal theorem

Define the minimal DGM, candidate model classes, contextual variable, cognitive parameter, asymptotic regime, and model-selection criterion needed for the central theorem.

Acceptance criteria:

- Objects and notation defined.
- At least one theorem candidate written.
- Assumptions separated from claims.
- Proof Critic review completed.
- New assumptions routed through approval policy.

## Issue 2: Replace placeholder DGM with ambiguity-attitude model

Replace the placeholder binary-choice process with the actual ambiguity-attitude task likelihood.

Acceptance criteria:

- DGM matches the cognitive model.
- Contextual effect on cognitive parameter is explicit.
- Unit tests validate dimensions and parameter recovery in simple cases.
- Smoke simulation passes.

## Issue 3: Implement Bayesian model comparison

Implement Bayes factor and LOOIC comparison for the simple omitted-context and complex omitted-context models.

Acceptance criteria:

- Candidate models are explicitly documented.
- LOOIC calculation is reproducible.
- Bayes factor approximation or exact method is justified.
- Simulation output records selected model and uncertainty.
