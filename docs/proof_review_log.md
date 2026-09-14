# Proof Review Log

## 2026-07-08 omitted-context mixture lemma draft

Date: 2026-07-08
Branch/commit: codex/formalize-mixture-lemma, this PR branch
Agent: research_manager + mathematical_formalist draft
Theorem or lemma: Lemma 1.1, Omitted-Context Conditional Mixture
Claim registry ID: C-002
Assumptions used: A-001, A-002; proposed A-006 only for the simplified `F_{theta|Z}` display
Proof summary: The analyst's observed law follows by conditioning on `Theta` and integrating the choice kernel over the latent-parameter distribution. The registry-safe identity uses `F_{theta|X,Z}`. The issue's simplified `F_{theta|Z}` identity requires fixed trial design or conditional independence of `X` and `theta` given `Z`.
Unsupported steps: Measure-theoretic regularity conditions remain to be stated for a fully general SI version.
Counterexample search: Adaptive or stratified task assignment can make `F_{theta|X,Z}` differ from `F_{theta|Z}`.
Reviewer-2 critique: Pending.
Decision: revise with PI direction received on 2026-07-07; do not approve A-006, use `F_{theta|X,Z}` as primary, and mention `F_{theta|Z}` only as a corollary.
Next action: Proof critic should review Lemma 1.1 with `F_{theta|X,Z}` as the primary statement.

## Entry template

```text
Date:
Branch/commit:
Agent:
Theorem or lemma:
Claim registry ID:
Assumptions used:
Proof summary:
Unsupported steps:
Counterexample search:
Reviewer-2 critique:
Decision: accept | revise | downgrade to conjecture | reject
Next action:
```

## 2026-09-05 participant-level constructive package

Source: PROOF_PACKAGE.md, author working draft.
Scope: mixture, explicit strict joint KL separation, finite-state uniform convergence, BIC, proper-uniform-prior BF, uniform deletion concentration, exact LOPO and simultaneous selection.
Assumptions: A-007–A-010 for the constructive chain; Gaussian A-003 is optional and unused.
Author verification: O1–O10 closed by local derivations. Numerical four-cell/KL/criterion checks and shared-baseline representation checks pass. Structural proof lint is a completeness check, not proof certification.
Adversarial review: pending; next action D1_KL_review in registries/proof_progress.json.
Decision: retain as complete local draft; do not mark manuscript accepted or supported_final.
Limits: finite-sample numerical examples favor S; they do not contradict the positive asymptotic gap. Final hierarchical ambiguity extension is not claimed.

## 2026-09-06 D1: mixture and strict KL review

Review type: separate LLM review pass in the same task; not independent external verification.
Evidence: `docs/proof_reviews/review_01_KL.md` and exact-fraction/high-precision checks in `logs/theory_checks/2026-09-06_KL_review.json`.
Verdict: L1 scalar identity and T1 strict participant-level KL separation pass O1–O3 review. No change to the constructive DGM, model pair, priors, or prediction target.
Repairs: the general participant-vector corollary now explicitly conditions trial independence on both Theta and Z (new scoped A-011), because independence given Theta alone does not suffice. Replaced L1's “Only under” exogeneity wording with a sufficient-condition statement. Both repairs and counterexamples are documented in the review.
Limitations: the no-intercept one-slope comparator is essential to this particular contrast; a free-intercept-plus-slope model matches the two marginals as well as K. The positive gap survives removing the slope box, so it is not an artifact of bounding b below log(3).
Next: D2_BIC_review, O4–O6. No full-package or manuscript acceptance is implied.

## 2026-09-07 D2: BIC convergence and localization

Separate LLM review pass; not independent external acceptance. O4–O6 in L2/C1 pass without edits to the proof or assumptions. See `docs/proof_reviews/review_02_BIC.md`. The non-strict Chebyshev event, compact optimization, global curvature and interior-event geometry were checked explicitly.

A complete same-assumption refinement uses two sufficient statistics to give the exact objective error and a smaller probability-bound constant. It is preserved in the review for D5 rather than rewriting the valid main proof. Exact-fraction checks over 214 small-n multinomial count vectors passed; no new simulation or practical selection-rate claim.

State advances to D3_BF_review (O7). Full criterion-chain and external acceptance remain pending.
