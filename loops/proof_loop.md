# Proof Loop

## Purpose

Develop human-readable proofs with proof-critical review, mechanical coherence
checking, numerical falsification, and selective formal verification.

## Before drafting: is the statement well posed?

Three of the four results in the original proof route were not theorems. Two
were circular or definitional and one conflated a population quantity with a
realised one. An LLM asked to prove an ill-posed statement will silently repair
it into a nearby provable-but-vacuous claim and write a fluent proof of that.
So the first pass is adversarial reading of the *statement*, not the proof:

1. Substitute the definitions. If the hypothesis becomes the conclusion, the
   statement is circular (this is what happened to T-004).
2. Ask what would have to be *measured* to check it. If nothing, it is a
   definition, not a result (this is what happened to T-005).
3. Separate population from realised quantities, and per-observation from
   total. If one symbol is doing both jobs, split it (this is what happened to
   T-007).
4. Check that every regularity condition the proof will need is stated. Name
   the model class explicitly; "a flexible model" is not a model class.
5. Check the assumption set against `registries/assumption_register.csv`. An
   unregistered assumption opens a decision gate; it does not get used.

## Steps

1. Mathematical Formalist drafts the statement, with a `theorem-meta` block
   declaring `id`, `claim`, `status`, `assumptions`, and `depends_on`.
2. `make check-coherence` — mechanical: notation drift, assumption leaks across
   `depends_on`, dependency cycles, registry disagreement, Lean/doc divergence.
3. Numerical falsification: add the claim to `R/theorem_numerics.R` and
   `tests/testthat/test-theorem-numerics.R`, **including every registered
   boundary case**, and run `make theorem-numerics`. A claim that cannot be
   evaluated numerically must say why in its document.
4. Proof Critic reviews each step, in a separate pass from the drafting.
5. Counterexample search attempts to falsify the statement against the boundary
   conditions in `docs/theorem_backlog.md`.
6. Optional Lean formalisation where mathlib supports it (`make lean`).
7. The theorem is revised, downgraded, or rejected. Record in
   `docs/proof_review_log.md`.
8. Accepted proof is written to the supplement — only if every gate below is
   clear.
9. Proof status is recorded in `registries/claim_register.md`.

## Gate for entering `manuscript/supplement_proofs.tex`

All four must hold:

1. status in `docs/theorem_backlog.md` is `accepted`;
2. every assumption used is `approved` in the assumption register — no
   `decision_needed` gates anywhere in the transitive `depends_on` closure;
3. a proof-critic entry exists in `docs/proof_review_log.md`;
4. `make verify` passes.

`scripts/check_coherence.py` enforces (1) and (2) mechanically: a theorem marked
`accepted` while resting on an open gate fails CI.

## Output files

- `docs/theorems/` — precise statements, one file per result
- `docs/proof_review_log.md`
- `registries/claim_register.md`, `registries/assumption_register.csv`
- `docs/approval_log.md` — for any new decision gate
- `manuscript/supplement_proofs.tex` — accepted results only
- `formal/OCECM/` — where mathlib supports it
