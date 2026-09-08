# OCECM Theorem Backlog

This backlog tracks proof work without upgrading any claim beyond its registry
status. It is an infrastructure artifact: adding an item here is not evidence
that a theorem has been proved or accepted for manuscript use.

## Status Legend

- `backlog`: not yet stated in reviewable mathematical form.
- `statement-draft`: precise statement under construction.
- `proof-draft`: proof written but not accepted.
- `proof-critic-review`: proof awaiting adversarial review.
- `accepted`: proof accepted for manuscript or SI use.
- `decision-gated`: blocked on PI or theorem-review direction.
- `corollary-only`: settled as a corollary; may not be promoted to a primary statement.
- `deferred`: removed from the theorem route by a recorded decision.

## Current Proof Route

| ID | Result | Claim | Assumptions | Status | Next proof action |
|---|---|---|---|---|---|
| T-001 | Omitted-context conditional mixture representation | C-002 | A-001, A-002, regular conditional distribution regularity stated in the draft | proof-critic-review | Proof Critic reviews Lemma 1.1 with `F_{Theta | X,Z}` as primary. |
| T-002 | Fixed or exogenous trial-design corollary | C-002 | Same as T-001 plus fixed-design or conditional-independence condition; A-006 remains rejected as a primary assumption | corollary-only (D-005) | Settled by D-005: stays a corollary. Not reopenable by an agent. |
| T-003 | Gaussian constructive heterogeneity result | C-003 | A-001, A-002, A-003 | statement-draft | A-003 approved by D-001. Proof critic reviews `docs/theorems/T-003_gaussian_constructive.md`, including the sharp iff in Corollary T-003a. |
| T-004 | KL dominance bridge | C-004 | A-001, A-002, A-003, A-007, A-008, A-009 | statement-draft | Statement rewritten to be non-circular (`docs/theorems/T-004_kl_dominance.md`). Blocked on PI approval of A-007, A-008, A-009. |
| T-005 | LOO expected-predictive-score / LOOIC consequence | C-004 | T-004 plus A-010, A-011 and regularity R1-R6 | statement-draft | Leave-out unit bound to the trial by D-002. Proof critic reviews the estimator/population bridge T-005b and the R5 degeneracy case. |
| T-006 | Bayes-factor consequence under declared priors | C-004 | A-011 | **deferred - not a theorem target** | Demoted by D-003 to a numerical prior-sensitivity study. See `docs/theorems/T-006_bayes_factor_deferred.md` for the justification and the reopening conditions. |
| T-007 | Finite-sample selection thresholds | C-004 | T-004 plus A-009, A-011 | statement-draft | Split by D-004 into T-007a (exact algebra), T-007b (regular bridge), T-007c (singular correction). Proof critic reviews the singular-case policy. |

## Boundary Conditions To Preserve

Every theorem statement or proof draft must explicitly preserve these cases:

1. `C` has no effect on `Theta`.
2. `C` is independent of relevant observed features and only adds correctly
   modeled iid noise.
3. The simple model already contains sufficient random-effect structure to
   represent the marginal law.
4. The complex model does not approximate the omitted-context mixture better
   than the simple model.
5. Model-selection penalties dominate the added fit in the finite sample.
6. The leave-out unit is mismatched to the intended predictive population or
   PSIS diagnostics fail.
7. A Bayes-factor result is driven by a prior or marginal-likelihood choice
   that has not been made explicit.

## Lean Formalization Backlog

The first Lean pass should remain selective and conservative.

| Lean file | Scope | Non-goal |
|---|---|---|
| `formal/OCECM/Basic.lean` | Shared labels, theorem-card status, and lightweight notation scaffolding. | No probability theory or theorem claims. |
| (dependency) | mathlib is now a pinned dependency (`v4.33.0`), and `lake build` runs in CI. | Lean formalisation is scoped to T-001, T-002, T-003 only. T-004 to T-007 stay LaTeX-only: mathlib has no M-estimation, cross-validation, or singular-learning theory, so those results are not formalisable today. |
| `formal/OCECM/MixtureLemma.lean` | Home for the future mixture statement using `F_{Theta | X,Z}` as primary. | No proof or axiom asserting Lemma 1.1. |
| `formal/OCECM/GaussianConstructive.lean` | Home for the Gaussian constructive statement after A-003 review. | No imported normal-distribution theory in this setup PR. |
| `formal/OCECM/AICBICThreshold.lean` | Home for secondary finite-sample AIC/BIC threshold statement shapes. | No universal model-selection theorem. |

## Procedure Guardrails

- Do not add new theorem assumptions without updating
  `registries/assumption_register.csv` or opening a PI decision gate.
- Do not promote claims in `registries/claim_register.md` from this backlog
  alone.
- Do not insert results into `manuscript/supplement_proofs.tex` until the proof
  loop accepts them.
- Keep each theorem PR bounded to one result or one formalization layer.
- Do not state a Bayes-factor theorem at all: T-006 is deferred by D-003.
- Do not cite AIC or BIC in support of C-004; D-004 restricts them to legacy
  bridge diagnostics because `M_K` is singular.
- Do not report `k_K - k_S` as the complexity of a comparison; report
  `p_loo` / `p_waic`.
- Every theorem document must carry a `theorem-meta` block and must pass
  `python3 scripts/check_coherence.py`.
- Do not state a LOOIC theorem before the leave-out unit and predictive target
  have a recorded decision.
