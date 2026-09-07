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

## Current Proof Route

| ID | Result | Claim | Assumptions | Status | Next proof action |
|---|---|---|---|---|---|
| T-001 | Omitted-context conditional mixture representation | C-002 | A-001, A-002, regular conditional distribution regularity stated in the draft | proof-critic-review | Review received (`docs/proofs/reviews/L1_mixture_lemma_claude_review.md`, verdict REVISE). Apply edits E1-E8 after PI decisions on the A-001 sharpening and on serial choice-noise independence. |
| T-002 | Fixed or exogenous trial-design corollary | C-002 | Same as T-001 plus fixed-design or conditional-independence condition; A-006 remains rejected as a primary assumption | decision-gated | Keep as corollary only; do not promote to primary theorem statement without PI direction. |
| T-003 | Gaussian constructive heterogeneity result | C-003 | A-003 | decision-gated | Wait for PI/theorem review before treating A-003 as the primary formal theorem assumption. |
| T-004 | KL dominance bridge | C-004 | Lemma 1.1 at a declared unit; proposed A-009 for a common comparison unit and design distribution; proposed A-010 for kernel non-degeneracy | proof-draft | Review `docs/proofs/L3_kl_dominance.md`. Obtain the PI decision on whether `M_K` nests `M_S`, since under nesting the sign of the KL gap carries no OCECM content (Proposition L3.3). |
| T-005 | LOO expected-predictive-score / LOOIC consequence | C-004 | T-004 plus a declared leave-out unit, population predictive target, and LOO regularity conditions | decision-gated | PI selects the primary leave-out unit; then draft a conditional result linking a positive predictive-score gap to lower LOOIC. |
| T-006 | Bayes-factor consequence under declared priors | C-004 | Proper prior families, prior scales, marginal-likelihood definition, and an explicit asymptotic regime | decision-gated | Do not infer this result from KL or LOOIC. Open a prior-and-estimator decision before writing the statement. |
| T-007 | AIC/BIC finite-sample threshold corollaries | C-004 | T-004 plus explicit sample-size and parameter-count conditions | backlog | Keep as secondary bridge corollaries; formalize conditional thresholds only. Corollary L3.5 fixes `Delta ell` as `delta_S - delta_K` at the declared unit and requires `n` to count units of that declared type. |
| T-008 | Context-aware versus false-complex contrast | C-001, C-004 | To be drafted; presupposes T-004 | backlog | Proposed by the L3 draft (CE-2): the theorem route compares `M_S` with `M_K` only, while claim C-001 and the second contrast in `docs/bayesian_comparison_plan.md` require `M_{S+C}` versus `M_K`. Opening this item needs PI direction. |

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
- Do not state a Bayes-factor theorem before the prior family, scale, and
  marginal-likelihood target have a recorded decision.
- Do not state a LOOIC theorem before the leave-out unit and predictive target
  have a recorded decision.
