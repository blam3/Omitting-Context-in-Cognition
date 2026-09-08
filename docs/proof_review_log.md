<!-- coherence-allow: F_Theta_given_Z -->
# Proof Review Log

## 2026-09-09 proof-critic: counterexample search against Theorem T-004 proper

Date: 2026-09-09
Branch/commit: claude/llm-formal-proofs-strategy-q4r0aj
Agent: proof-critic pass (counterexample search), at PI request
Theorem or lemma: Theorem T-004 (compactness / lower-semicontinuity argument),
  Theorem T-004' (score-condition variant)
Claim registry ID: C-004
Assumptions used: A-001, A-002, A-003, A-007, A-008, A-009

RESULT: NO COUNTEREXAMPLE TO THEOREM T-004. Every step was checked and holds:
  c < infinity via beta_S = (0,0,0); no coordinate of the limit at 0 or 1 (else
  q_j * d diverges, contradicting a bounded minimising sequence); continuity on
  (0,1)^J; the limit lies in closure(M_S) as T-004b defines it; and KL = 0 iff
  equality at every design point, which needs q_j > 0 for all j, supplied by
  A-008.

Probe A - condition (i) is NECESSARY, not decorative. For p_0 in
  closure(M_S)\M_S the divergence decays like s^-2 to zero
  (6.18e-4, 1.74e-5, 1.90e-7, 1.91e-9, 1.91e-11 for (c0,rho)=(0.5,1.3)), so the
  infimum is 0 and the conclusion c > 0 fails outright. Reproduced independently
  in R and Python to identical values. This vindicates the proof's decision to
  work in closure(M_S) rather than assume a minimiser exists in M_S.

Probe B/C - interiority and uniqueness hold for the studied family but are NOT
  implied. The M_S minimiser is interior and unique for all four cases of T-004
  section 5 (s^2 in [0.97, 1.21], parameter spread below 1e-6 over 60 restarts);
  case D recovers the generating parameters exactly. A 58-configuration scan
  found no case with s^2 > 1e3 (largest 578.6). BUT condition (i) does NOT
  logically imply interiority: T-004's proof places the minimiser only in
  closure(M_S) = M_S union D, and Probe A exhibits a p_0 whose minimiser sits in
  D, i.e. at s = infinity, where no pseudo-true parameter exists in the
  parameter space at all. So T-004' interiority/uniqueness and T-007b (P1) are
  INDEPENDENT assumptions, empirically satisfied here but not derivable from
  T-004's hypotheses. This resolves the T-004'/T-007c tension flagged in the
  previous pass: the documents are consistent, but only because the assumption
  is separate, and neither said so.

Probe D - the premise never fails, but the content degrades. p_0 is a convex
  combination of Phi values so p_0 in (0,1)^J always holds. The gap however
  collapses toward the boundary (6.9e-6, 4.1e-8, 3.6e-12, 4.2e-17 as b_0 rises),
  so condition (i) can hold while c is numerically indistinguishable from zero.
  Compounds the effect-size caveat of T-004 section 6.

Probe E - the two hypotheses are asymmetric. Condition (ii) is attainment (KL
  exactly 0 at an interior parameter point, w = 1/2); condition (i) concerns an
  infimum that may lie in the closure. Section 3 read as though they were the
  same kind of object.

NEW HARNESS DEFECT (found while running Probe D, in code CI was passing).
  kl_design() clipped the model probability p but not the target p0, so a
  saturated p0 gave 0 * log(0/x) = 0 * -Inf = NaN. Because max(NaN, 0) is NaN in
  R, inf_kl() propagated it SILENTLY rather than erroring. Reachable: Phi(x) == 1
  in float64 for x >~ 8.3, which the heterogeneity scan of section 6 can hit.

Repairs applied (commit 2876a28):
  1. T-004 section 3: remarks recording that (i) is necessary (with the decay
     table) and that (i) and (ii) are asymmetric.
  2. T-004' and T-007b section 2: interiority/uniqueness stated as independent
     assumptions, with the failure mode named and the two documents
     cross-referenced; T-007 section 4 gains the corresponding boundary row.
  3. kl_design() guards both arguments with the 0 log 0 = 0 convention, checks
     lengths, and stops on a non-finite result; inf_kl() ignores non-finite fits
     and errors if none is finite.
  4. Four regression tests: the p0 saturation guard, the necessity of condition
     (i) including its s^-2 rate, interiority/uniqueness on the table cases with
     exact parameter recovery for case D, and the boundary gap collapse.

Note on the repair itself: the first draft of the necessity test passed sqrt(s)
  where m_s_predict expects the pre-squared scale, so the sequence had variance s
  against slope rho*s and the KL rose instead of decaying. The test caught it;
  after the fix R reproduces the Python figures exactly.

Unsupported steps: unchanged. T-003, T-007 and T-001 have not had a critic pass.
  T-007b's proof remains a citation to White and Vuong, both still unverified in
  docs/citation_claim_map.csv.

Reviewer-2 critique: Pending.
Decision: revise (applied). T-004 remains proof-draft, not accepted.
Next action: proof-critic pass on T-003, then T-007, then T-001.

## 2026-09-09 proof-critic: counterexample search against Lemma T-004b

Date: 2026-09-09
Branch/commit: claude/llm-formal-proofs-strategy-q4r0aj
Agent: proof-critic pass (counterexample search), at PI request
Theorem or lemma: Lemma T-004b (closure characterisation), Lemma T-004a
Claim registry ID: C-004
Assumptions used: A-007, A-008, A-009 (approved D-006)

Counterexample search: three probes against T-004b's closure characterisation.
  Probe 1 (subset direction): 2100 divergent sequences across growth rates
    s^0.25 to s^2. All limits constant on a > 0. No counterexample.
  Probe 2 (superset direction): 500 (c_0, rho) pairs against the lemma's own
    construction at n = 1e8; max deviation 3.7e-7. No counterexample.
  Probe 3 (disjointness): COUNTEREXAMPLE FOUND.

FINDING 1 - T-004b's set-difference equality was false on the diagonal.
  The lemma asserted closure(M_S) \ M_S = D. Taking rho = c_0 makes
  Phi^-1(p(a)) = c_0 for every a including a = 0, so p is the constant response
  Phi(c_0), which is in M_S at (beta_0, beta_1, s^2) = (c_0, 0, 0). A set
  difference cannot contain elements of the set subtracted. Affine residuals for
  (c_0, rho) in {(0.5,0.5), (-1.2,-1.2), (0,0), (2,2)} are machine zero.
  The overlap is exactly the diagonal: with J >= 4 there are >= 3 distinct
  positive design points, enough to determine the quadratic in
  (c_0 + beta_1 a)^2 = rho^2 (1 + s^2 a^2), forcing rho = c_0.
  Severity: cosmetic. Theorem T-004 uses closure(M_S) only as a set and
  Corollary T-004c is an inclusive disjunction, so nothing downstream breaks.
  REPAIR: the lemma now states the union closure(M_S) = M_S union D, with the
  overlap recorded as a remark.

FINDING 2 - the numerical certificate did not implement Lemma T-004a.
  affine_residual() minimises over s^2 and that infimum is not always attained.
  For a degenerate point with c_0 = 0 the residual decays like s^-2 to zero
  without reaching it (2.21e-4, 2.21e-6, 2.21e-8, 2.21e-10 at s = 1e2..1e5), so
  the optimiser returns near-zero for a law outside M_S. The value is also
  optimiser-dependent: 2e-12 under a deep search, 2e-5 under the harness
  defaults. Branch (b) of Corollary T-004c was never implemented at all.
  Severity: real, and in code CI was passing. T-004 condition (i) is
  p_0 not in closure(M_S), which is stronger than not in M_S, so a positive
  affine residual alone never established it.
  REPAIR: added constant_index_spread() (branch b) and closure_membership()
  (both branches with verdict); documented the unattained infimum in the
  function header and in T-004 section 5; four regression tests added.

Do the published results survive? YES. Branch (b) was checked directly on all
  four table cases: spreads of Phi^-1(p_0) on a > 0 are 0.393, 0.466, 0.436 and
  0.532, nowhere near constant, so condition (i) genuinely holds wherever a
  strict gap is claimed. No number in T-004 section 5 changes.

Unsupported steps: unchanged. Proof-critic review of Theorem T-004 itself,
  T-003, T-007 and T-001 remains outstanding; this pass covered Lemma T-004b
  only. T-004' still assumes uniqueness and interiority of beta_S-circ without
  establishing them, and that assumption sits in tension with T-007c's
  observation that the pseudo-true parameter is on the boundary under boundary
  conditions 1-3; the two documents should be reconciled explicitly.

Reviewer-2 critique: Pending.
Decision: revise (applied). T-004 remains proof-draft, not accepted.
Next action: proof-critic pass on Theorem T-004 proper (the compactness and
  lower-semicontinuity argument), then T-004' interiority versus T-007c.

## 2026-09-09 A-007/A-008/A-009 approved; statuses advanced

Date: 2026-09-09
Branch/commit: claude/llm-formal-proofs-strategy-q4r0aj
Agent: autonomous research session (governance update, not a proof pass)
Theorem or lemma: T-003, T-004, T-007 (status), T-005 (deliberately unchanged)
Claim registry ID: C-003, C-004
Assumptions used: A-007, A-008, A-009 approved by D-006

Proof summary: No mathematics changed in this entry. The PI approved the three
  assumptions introduced by the 2026-09-08 T-004 rewrite, which was the last
  open decision gate in the package. T-003, T-004 and T-007 advance from
  `statement-draft` to `proof-draft`.

Deliberately NOT advanced: T-005. Its central result T-005b quotes the
  leave-one-out expansion rather than deriving it, so it is a sketch and stays
  at `statement-draft`. Advancing it alongside the others would have
  misrepresented what has actually been proved.

Unsupported steps (unchanged from 2026-09-08, and now the only blockers):
  - proof-critic review is outstanding for T-001, T-003, T-004 and T-007;
  - T-005b needs its expansion derived or explicitly cited;
  - the RLCTs for M_S and M_K remain unknown, which is why T-006 stays deferred
    and T-007c remains a policy rather than a theorem.

Counterexample search: not repeated; the 2026-09-08 numerical checks stand and
  continue to pass in CI.

Scope recorded with the approval (D-006 condition 1): A-007 makes the
  attenuation identity exact only for probit; A-008's J >= 4, a = 0 and
  non-negativity are each load-bearing in Lemma T-004b; A-009 fixes the model
  families, so transfer to other candidate models requires re-checking Lemma
  T-004a and the containment or score condition.

Reviewer-2 critique: Pending.
Decision: revise. Nothing is accepted; the package is now blocked on review
  rather than on decisions.
Next action: proof-critic pass on T-004, starting with Lemma T-004b, which is
  the load-bearing step and the one a naive argument gets wrong.

## 2026-09-08 theorem-package restatement (T-003 to T-007)

Date: 2026-09-08
Branch/commit: claude/llm-formal-proofs-strategy-q4r0aj
Agent: autonomous research session (statement rewrite; not a proof-critic pass)
Theorem or lemma: T-003, T-004, T-005, T-006 (deferred), T-007
Claim registry ID: C-003, C-004
Assumptions used: A-001, A-002, A-003 (approved D-001), A-007/A-008/A-009
  (NEW, `decision_needed`), A-010 (approved D-002), A-011 (approved D-004)

Proof summary:
  Three of the four remaining route statements were not theorems and have been
  rewritten rather than proved.
  - T-004 was circular: `KL(p_0||p) = -E[log p] + const`, so its hypothesis and
    conclusion were the same proposition. It is replaced by an explicit
    construction with a decidable non-representability criterion
    (Lemma T-004a), a closure argument (Lemma T-004b) and a strict-dominance
    theorem under containment, plus a score-condition variant T-004' for
    complex classes that do not contain the target.
  - T-005 was a definition (`LOOIC = -2 elpd`). It is replaced by the
    estimator-to-population bridge T-005b, whose implicit penalty is `p_loo`,
    not `k`, with regularity conditions R1-R6 stated explicitly.
  - T-007 conflated the population per-observation gap with the realised
    log-likelihood difference, and used penalties whose derivations fail for
    singular models. It is split into T-007a (exact algebra), T-007b (regular
    probabilistic bridge plus a minimum-sample-size corollary) and T-007c (the
    singular-case correction).
  - T-006 is deferred, not proved. Justification in
    `docs/theorems/T-006_bayes_factor_deferred.md`.

New substantive finding:
  The mechanism is VARIANCE heterogeneity, not mean shift. Proposition T-004d
  shows that if the omitted context shifts only the latent mean and that induced
  mean is Gaussian, then `p_0` lies in `M_S` exactly and the KL gap is zero.
  This makes registered boundary conditions 1-3 exact rather than rhetorical and
  narrows C-004 to a more defensible claim.

Unsupported steps:
  - A-007, A-008, A-009 are proposed, not approved. T-004 cannot be accepted
    into `manuscript/supplement_proofs.tex` until they are.
  - T-005b is stated with a proof sketch, not a full proof; the leave-one-out
    expansion is quoted rather than derived.
  - The real log canonical thresholds for `M_S` and `M_K` are unknown, which is
    why T-006 is deferred and why T-007c is a policy rather than a theorem.
  - T-001 remains at proof-critic-review; nothing here upgrades it.

Counterexample search:
  Four registered boundary cases were checked numerically in two independent
  implementations (R and Python), which agree to reported precision:
  homogeneous context gives an exactly zero gap; Gaussian mean heterogeneity
  with `gamma = 0` gives an exactly zero gap (machine precision against the
  closed form); discrete mean-only heterogeneity gives a negligible `1e-8` gap;
  variance heterogeneity gives a strict `1.07e-6` gap that the mixture model
  closes exactly.

Numerical harness caught a drafting error:
  The first draft of T-007b' quoted the AIC crossover as `n ~ 1e5-1e6`. That is
  the DETERMINISTIC threshold `1/Delta-ell-star = 1.4e5`. The probabilistic
  crossover at 95% is `5.5e10` - the same expected-versus-realised conflation
  the rewrite exists to fix. Both documents were corrected and the test now
  guards the magnitude.

Reviewer-2 critique: Pending.
Decision: revise. These are statement drafts. None is accepted.
Next action:
  1. PI decision on A-007, A-008, A-009.
  2. Proof critic reviews T-003 (Corollary T-003a's iff), T-004 (Lemma T-004b's
     closure argument is the load-bearing step), and T-005 R5 degeneracy.
  3. Full proof of the T-005b expansion, or an explicit citation in its place.

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
