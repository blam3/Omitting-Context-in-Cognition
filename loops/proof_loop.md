# Proof Loop

## Purpose

Develop human-readable proofs with proof-critical review and optional selective formal verification.

## Steps

1. Mathematical Formalist drafts lemma/theorem/proof.
2. Proof Critic reviews each step.
3. Counterexample search attempts to falsify the statement.
4. The theorem is revised, downgraded, or rejected.
5. Accepted proof is written to supplement.
6. Proof status is recorded in the claim registry.

## Output files

- `docs/proof_review_log.md`
- `docs/claim_registry.md`
- `manuscript/supplement_proofs.tex`
- Optional `formal/lean/`
