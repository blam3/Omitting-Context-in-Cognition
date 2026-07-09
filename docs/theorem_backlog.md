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
| T-001 | Omitted-context conditional mixture representation | C-002 | A-001, A-002, regular conditional distribution regularity stated in the draft | proof-critic-review | Proof Critic reviews Lemma 1.1 with `F_{Theta | X,Z}` as primary. |
| T-002 | Fixed or exogenous trial-design corollary | C-002 | Same as T-001 plus fixed-design or conditional-independence condition; A-006 remains rejected as a primary assumption | decision-gated | Keep as corollary only; do not promote to primary theorem statement without PI direction. |
| T-003 | Gaussian constructive heterogeneity result | C-003 | A-003 | decision-gated | Wait for PI/theorem review before treating A-003 as the primary formal theorem assumption. |
| T-004 | KL dominance bridge | C-004 | Model-class and pseudo-true-risk assumptions still to be drafted | backlog | Draft exact model classes, target law, and KL comparison criterion. |
| T-005 | LOO expected-predictive-score / LOOIC consequence | C-004 | T-004 plus a declared leave-out unit, population predictive target, and LOO regularity conditions | decision-gated | PI selects the primary leave-out unit; then draft a conditional result linking a positive predictive-score gap to lower LOOIC. |
| T-006 | Bayes-factor consequence under declared priors | C-004 | Proper prior families, prior scales, marginal-likelihood definition, and an explicit asymptotic regime | decision-gated | Do not infer this result from KL or LOOIC. Open a prior-and-estimator decision before writing the statement. |
| T-007 | AIC/BIC finite-sample threshold corollaries | C-004 | T-004 plus explicit sample-size and parameter-count conditions | backlog | Keep as secondary bridge corollaries; formalize conditional thresholds only. |

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
