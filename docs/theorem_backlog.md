# OCECM theorem inventory

## Current primary scope — 2026-09-08

A-003 is approved as the primary route; T-003 is active but unproved beyond the explicitly qualified moment identities. Primary M4 is probability distortion; primary predictive target is trial-level LOO (A-012). The table below describes the preserved finite benchmark, not the new primary theorem.

| ID | Current role | Required next work |
|---|---|---|
| T-003 | Primary additive-context/moment route | Separate approved moments from additional residual/Gaussian conditions; derive observable implications. |
| T-004 | Existing benchmark KL result | Establish a distinct primary-model separation result; do not transfer the quadratic proof to distortion. |
| T-005 | Existing convergence/BIC result | Preserve participant sampling; trial holdout alone does not justify row-count BIC. |
| T-006 | Existing benchmark BF; primary extension open | Use selected proper priors and exact evidence; prove regularity and separation for the new model. |
| T-007 | Secondary benchmark LOPO | Retain its whole-participant scope. |
| T-009 | New primary trial-level LOO | Establish conditional deleted-trial score and convergence with within-person dependence. |
| T-008 | Existing simultaneous benchmark result | No simultaneous-primary claim before the new criteria are established. |

The old statement that A-003 was not adopted records the earlier route only. Work follows G1–G7 in the progress state; D1/D2 review evidence is retained for the benchmark.

## Historical finite-benchmark inventory


Updated 2026-09-05. Author proofs are distinct from independently reviewed or manuscript-accepted results. Authoritative source: `PROOF_PACKAGE.md`; daily workflow: `docs/proof_roadmap.md`.

| ID | Result / package units | Assumptions | Status | Next action |
|---|---|---|---|---|
| T-001 | Finite-response conditional mixture, L1 | Measurable conditional kernel, regular conditional law; A-001 interpretation | proof-draft, locally checked | Adversarial review of conditional statements |
| T-002 | Exogenous-design corollary | T-001 plus conditional independence; not primary A-006 | proof-draft, locally checked | Verify fixed-design wording |
| T-003 | Optional latent moment/Gaussian example | Explicit residual moment/distribution conditions in optional note | optional, outside main chain; A-003 not adopted | No work unless it helps a specific extension |
| T-004 | Strict participant KL separation, T1 | A-007, A-008 | complete local proof draft | Review O1–O3 |
| T-005 | Finite-state convergence and BIC, L2/C1 | A-007, A-008, A-010 | complete local proof draft | Review O4–O6 and finite-sample bound |
| T-006 | Proper-prior Bayes-factor corollary, C2 | A-007–A-010 | complete local proof draft | Review O7, prior constants and interior event |
| T-007 | Uniform deletion concentration and LOPO, L3/C3 | A-007–A-010 | complete local proof draft | Review O8–O9 |
| T-008 | Simultaneous selection, C4 | T-005–T-007 | complete local proof draft | Check union bound in integration review |

No main result is marked `accepted`. The manuscript supplement remains an acceptance-gated destination. `formal/OCECM/*.lean` contains historical metadata and placeholders, not proofs; its older T-003/T-005 descriptions do not define the current mathematical claims. Synchronize formal metadata after the mathematical review, rather than using a successful build as evidence for any theorem.

## Boundaries

- A correctly specified shared random-effect simple model can represent the true pair law and remove the gap.
- The construction does not claim that K beats the true contextual model in KL risk.
- Participant count grows with two trials fixed; no growing-trials or increasing-dimension result is supplied.
- BF uses proper specified priors; LOPO is exact deletion of whole participant pairs, not an automatic PSIS guarantee.
- Gaussian heterogeneity and final RAID model selection are not prerequisites for the constructive proof.

## Latest scoped review: 2026-09-06

D1 is complete: O1–O3 passed a separate LLM review pass after explicit corrections to the general participant-vector conditioning (A-011) and L1 exogeneity wording. The constructive T1 assumptions and conclusion are unchanged. See `docs/proof_reviews/review_01_KL.md`. T-001's vector extension uses A-011; the scalar tower identity does not. D2 (L2/C1 and O4–O6) is next. Independent external acceptance and the remaining criterion reviews are still pending.

## Latest scoped review: 2026-09-07

D2 is complete: L2/C1 and O4–O6 pass a separate LLM review with no main-proof or assumption changes. A sharper same-assumption bound is proved in `docs/proof_reviews/review_02_BIC.md` for consideration during D5 integration. Next is D3, the proper-prior Bayes-factor integral review. No result is promoted to final scientific acceptance.

## Status legend (retained from pre-2026-09-08 backlog)


- `backlog`: not yet stated in reviewable mathematical form.
- `statement-draft`: precise statement under construction.
- `proof-draft`: proof written but not accepted.
- `proof-critic-review`: proof awaiting adversarial review.
- `accepted`: proof accepted for manuscript or SI use.
- `decision-gated`: blocked on PI or theorem-review direction.

## Superseded planned route — pre-2026-09-08

This is the route that was current on `main` through 2026-09-06, retained for
auditability after the 2026-09-08 PI redirection. Its T-numbering is a
different scheme from the current inventory above: here T-004 through T-007
are the planned KL/LOOIC/BF/AIC-BIC bridge steps, whereas the inventory above
uses T-004 through T-008 for the finite-benchmark constructive package. Claim
references were renumbered to C-007 and C-008 per the 2026-09-08 claim-ID
renumbering recorded in `registries/claim_register.md`. Do not cite this table
as current scope.


| ID | Result | Claim | Assumptions | Status | Next proof action |
|---|---|---|---|---|---|
| T-001 | Omitted-context conditional mixture representation | C-002 | A-001, A-002, regular conditional distribution regularity stated in the draft | proof-critic-review | Proof Critic reviews Lemma 1.1 with `F_{Theta | X,Z}` as primary. |
| T-002 | Fixed or exogenous trial-design corollary | C-002 | Same as T-001 plus fixed-design or conditional-independence condition; A-006 remains rejected as a primary assumption | decision-gated | Keep as corollary only; do not promote to primary theorem statement without PI direction. |
| T-003 | Gaussian constructive heterogeneity result | C-007 | A-003 | decision-gated | Wait for PI/theorem review before treating A-003 as the primary formal theorem assumption. |
| T-004 | KL dominance bridge | C-008 | Model-class and pseudo-true-risk assumptions still to be drafted | backlog | Draft exact model classes, target law, and KL comparison criterion. |
| T-005 | LOO expected-predictive-score / LOOIC consequence | C-008 | T-004 plus a declared leave-out unit, population predictive target, and LOO regularity conditions | decision-gated | PI selects the primary leave-out unit; then draft a conditional result linking a positive predictive-score gap to lower LOOIC. |
| T-006 | Bayes-factor consequence under declared priors | C-008 | Proper prior families, prior scales, marginal-likelihood definition, and an explicit asymptotic regime | decision-gated | Do not infer this result from KL or LOOIC. Open a prior-and-estimator decision before writing the statement. |
| T-007 | AIC/BIC finite-sample threshold corollaries | C-008 | T-004 plus explicit sample-size and parameter-count conditions | backlog | Keep as secondary bridge corollaries; formalize conditional thresholds only. |

## Boundary conditions to preserve

Every theorem statement or proof draft must explicitly preserve these cases.
These are retained from the pre-2026-09-08 backlog and remain binding.


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

## Lean formalization backlog


The first Lean pass should remain selective and conservative.

| Lean file | Scope | Non-goal |
|---|---|---|
| `formal/OCECM/Basic.lean` | Shared labels, theorem-card status, and lightweight notation scaffolding. | No probability theory or theorem claims. |
| `formal/OCECM/MixtureLemma.lean` | Home for the future mixture statement using `F_{Theta | X,Z}` as primary. | No proof or axiom asserting Lemma 1.1. |
| `formal/OCECM/GaussianConstructive.lean` | Home for the Gaussian constructive statement after A-003 review. | No imported normal-distribution theory in this setup PR. |
| `formal/OCECM/AICBICThreshold.lean` | Home for secondary finite-sample AIC/BIC threshold statement shapes. | No universal model-selection theorem. |

## Procedure guardrails


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
