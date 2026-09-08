# OCECM Lean Formalization

Lean 4 project for the OCECM theorem package. Toolchain and mathlib version are
pinned; `lake-manifest.json` pins the exact mathlib revision.

## Scope, and why it is narrow

Lean formalisation here is a **verification gate**, not a goal in itself. It is
scoped to what mathlib can actually support today:

| Result | Formalised? | Reason |
|---|---|---|
| Lemma T-004a (algebraic core) | **yes** — `OCECM/AttenuationAlgebra.lean` | pure real algebra; no measure theory needed |
| T-001 mixture representation | not yet | needs a disintegration / `Kernel` API pass; tractable, deferred to its own PR |
| T-002, T-003 | not yet | T-003 needs Gaussian affine-combination lemmas; thin in mathlib |
| T-004 (full), T-005, T-007 | **no, and not planned** | mathlib has no M-estimation, cross-validation, or singular-learning theory. These stay LaTeX-only. |

Claiming otherwise would mean committing Lean that cannot be checked, which is
the failure mode this gate exists to prevent.

## Dependency

mathlib is now a real dependency (pinned to `v4.33.0`, matching
`lean-toolchain`). That decision is deliberate and reviewable: it is what makes
`lake build` capable of rejecting a wrong statement. It costs CI time, which the
path filter in `.github/workflows/formal-lean.yml` limits to changes under
`formal/`.

## Files

- `lakefile.lean` — package definition and the mathlib requirement.
- `lean-toolchain` — pinned toolchain (`leanprover/lean4:v4.33.0`).
- `lake-manifest.json` — pinned dependency revisions; commit changes to it.
- `OCECM/Basic.lean` — status metadata and notation scaffolding, no claims.
- `OCECM/AttenuationAlgebra.lean` — Lemma T-004a's algebraic core. The only file
  with mathematical content.
- `OCECM/MixtureLemma.lean`, `GaussianConstructive.lean`, `AICBICThreshold.lean`
  — statement-shape placeholders. They assert nothing.

## Validation

```bash
cd formal
lake exe cache get     # mathlib oleans; without this a source build takes hours
lake build
```

`make lean` from the repository root does both. CI runs the same via
`leanprover/lean-action`.

## Governance

Lean statements must not outrun the registries. `scripts/check_coherence.py`
enforces mechanically that each `TheoremCard` status here matches
`docs/theorem_backlog.md`; a divergence fails CI.

- C-002 remains `in_progress` until proof review accepts the mixture lemma.
- A-006 remains rejected; any `F_{Theta | Z}` statement belongs only in the
  T-002 corollary.
- A-007, A-008 and A-009 were approved by D-006 (2026-09-09), so
  `AttenuationAlgebra.lean` may assume them. It is nevertheless stated without
  them: its content is real algebra on the index scale, and it holds for any
  `s^2 >= 0` and any real design point, so it is strictly more general than the
  A-007/A-008 setting T-004 uses it in.
