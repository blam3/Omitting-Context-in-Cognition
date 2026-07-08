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
