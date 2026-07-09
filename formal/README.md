# OCECM Lean Formalization Scaffold

This directory is a minimal Lean 4 project for theorem-proof infrastructure.
It does not prove a new theorem and does not add scientific assumptions.

## Current Scope

- Provide stable file locations for the OCECM proof route.
- Keep theorem status aligned with `docs/theorem_backlog.md`,
  `registries/assumption_register.csv`, and `registries/claim_register.md`.
- Compile without external dependencies or mathlib.

## Files

- `lakefile.lean`: Lean package definition.
- `lean-toolchain`: Toolchain pin used for local validation.
- `OCECM/Basic.lean`: Shared status and notation scaffolding.
- `OCECM/MixtureLemma.lean`: Future home for the omitted-context mixture lemma.
- `OCECM/GaussianConstructive.lean`: Future home for the Gaussian constructive
  heterogeneity result.
- `OCECM/AICBICThreshold.lean`: Future home for the secondary AIC/BIC
  threshold corollaries.
- Future LOOIC and Bayes-factor statement files must wait for the decision
  gates in `docs/theorem_backlog.md`.

## Validation

From this directory:

```bash
lake build
```

The first substantive theorem-formalization PR should decide whether to add
mathlib or another probability library. That dependency decision should be a
separate, reviewable change because it affects CI, build time, and notation.

## Governance

Lean statements must not outrun the project registries. In particular:

- C-002 remains `in_progress` until proof review accepts the mixture lemma.
- C-003 remains `planned` and A-003 remains `decision_needed`.
- A-006 remains rejected as a primary assumption; any `F_{Theta | Z}` statement
  belongs only in a corollary under fixed-design or exogeneity conditions.
