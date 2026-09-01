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

## 2026-09-01 omitted-context mixture lemma proof-critic review received

Date: 2026-09-01
Branch/commit: review authored 2026-07-12 on `agent/gaussian-constructive-heterogeneity-v2`; copied to this branch so it is not held in an unmerged draft PR
Agent: proof_critic
Theorem or lemma: Lemma 1.1, Omitted-Context Conditional Mixture
Claim registry ID: C-002
Assumptions used: A-001, A-002, Assumption 4 regularity
Proof summary: The tower-property and disintegration argument is correct; the a.e. qualifier, the demotion of the `F_{theta|Z}` display to a corollary, and the boundary-case treatment are sound.
Unsupported steps: F1, Step 3 does not follow from A-001 as registered; it needs the exclusion restriction `Y independent of (Z,C,U) given (X,Theta)`. F2, the lemma is a per-trial identity and the multi-trial deployment in sections 1 and 6 overreaches; the within-participant joint law does not factor into products of trial-level marginals, so participant-level predictive targets need the joint mixture derived first. N1, joint measurability of the kernel is missing from Assumption 4. N2-N6 are exposition and register-hygiene items.
Counterexample search: CE-1 succeeds against Step 3 (latent heterogeneity leaking into the choice shock), establishing that the exclusion restriction is substantive rather than notational. CE-2 to CE-5 fail against the lemma.
Reviewer-2 critique: Not yet run.
Decision: revise
Next action: PI decisions on sharpening A-001 to A-001' and on a serial choice-noise independence assumption; then apply edits E1-E8 and re-review. Do not promote C-002 before those decisions.

## 2026-09-01 KL dominance bridge proof draft

Date: 2026-09-01
Branch/commit: claude/project-status-next-steps-y57zxy
Agent: mathematical_formalist draft
Theorem or lemma: Proposition L3.1, Theorem L3.2, Propositions L3.3 and L3.4, Corollary L3.5 in `docs/proofs/L3_kl_dominance.md`
Claim registry ID: C-004 (status unchanged, `planned`)
Assumptions used: Lemma 1.1 at a declared comparison unit; proposed A-009; proposed A-010
Proof summary: The expected conditional divergence decomposes as risk minus a model-free entropy term, so the KL gap between the two context-omitting classes equals the population log-score gap exactly. Under nesting the gap is non-negative for every target law. A nonzero extra-parameter score at the embedded pseudo-true simple model is sufficient for strict dominance and is estimable without fitting the complex model.
Unsupported steps: None inside the stated conditional algebra. A-009 and A-010 are proposed and decision-gated. The participant-level target law is taken as supplied rather than derived, pending the F2 derivation.
Counterexample search: CE-1 shows dominance can occur with no omitted context at all, so the KL gap is not diagnostic of context omission. CE-2 shows the theorem route lacks the context-aware versus false-complex contrast that claim C-001 requires. CE-3 limits Proposition L3.4 to the attained case. CE-4 and CE-5 motivate A-010 and A-009 respectively.
Reviewer-2 critique: Not yet run.
Decision: draft submitted for proof-critic review
Next action: PI decision on whether `M_K` nests `M_S`; under nesting the sign of the KL gap carries no OCECM content and the theorem package's weight must move to T-005, T-006, and T-007.

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
