<!-- coherence-allow: F_Theta_given_Z, bare_delta_ell -->
# Approval Log

Decisions recorded here are binding on the theorem package, the simulation
design, and the manuscript. An agent may not reopen a recorded decision; it may
only request a new decision gate.

---

## 2026-09-09 / D-006 — Approve A-007, A-008, A-009 (the T-004 construction)

```text
Date: 2026-09-09
Requested by: autonomous research session (T-004 unblocking)
Decision needed: Whether the three modelling assumptions introduced by the
  rewritten T-004 statement may be treated as approved theorem assumptions.
Reason approval was required: docs/approval_policy.md gates new theorem
  assumptions. These three were recorded as decision_needed when T-004 was
  restated on 2026-09-08 and were the only remaining open gate in the package.
Options:
  (a) Approve all three.
  (b) Approve a subset.
  (c) Continue to defer.
User decision: (a) Approve A-007, A-008 and A-009.
Conditions or modifications:
  1. SCOPE. Like A-003 under D-001, these are assumptions of the CONSTRUCTIVE
     theorem, not of the package. They license T-003b, T-004 and the parts of
     T-005/T-007 that inherit from T-004. They do not license a general claim.
     In particular:
       - A-007 fixes a PROBIT kernel. The closed-form attenuation identity in
         Corollary T-003b is exact for probit and only approximate for logit.
         Any logit statement must be derived separately and labelled as an
         approximation; it may not be presented as a corollary of T-004.
       - A-008 fixes a finite, non-negative design with J >= 4 levels including
         a = 0. J >= 4 is what makes M_S over-determined and non-representability
         detectable; a = 0 and non-negativity are both used in Lemma T-004b.
         A design violating these does not falsify T-004, but T-004 says nothing
         about it.
       - A-009 fixes explicit parametric families for M_S and M_K. Results proved
         under A-009 transfer to other candidate models only by re-checking
         Lemma T-004a and the containment or score condition for those families.
  2. STATUS EFFECT. Clearing this gate advances the statements from
     `statement-draft` to `proof-draft`. It does NOT make them `accepted`.
     Proof-critic review (gate 3 of the four in loops/proof_loop.md) remains
     outstanding for every result, so nothing enters
     manuscript/supplement_proofs.tex yet.
  3. T-005 is deliberately NOT advanced. Its central result T-005b is a proof
     sketch: the leave-one-out expansion is quoted rather than derived. It stays
     at `statement-draft` until that is written out or replaced by an explicit
     citation.
  4. The manuscript must carry the A-007/A-008/A-009 conditions wherever T-004
     is stated, not only in a supplementary assumptions list. A reader who takes
     T-004 as a general result about omitted context has been misled.
Follow-up tasks:
  - registries/assumption_register.csv: A-007, A-008, A-009 -> approved.
  - docs/theorem_backlog.md: T-003, T-004, T-007 -> proof-draft.
  - Lean TheoremCard statuses resynced (enforced by scripts/check_coherence.py).
  - Next action for the package is proof-critic review, not manuscript writing.
```

---

## 2026-09-08 / D-001 — Approve A-003 as a primary theorem assumption

```text
Date: 2026-09-08
Requested by: autonomous research session (theorem-package unblocking)
Decision needed: Whether A-003 (Gaussian constructive case) may be treated as a
  primary assumption of the constructive theorem, rather than remaining
  decision_needed.
Reason approval was required: docs/approval_policy.md gates new theorem
  assumptions; A-003 has blocked T-003 and, transitively, T-004 and T-007.
Options:
  (a) Approve as a primary assumption of the constructive theorem only.
  (b) Approve as a general assumption of the whole theorem package.
  (c) Continue to defer.
User decision: (a) Approve.
Conditions or modifications:
  1. A-003 is approved as a CONSTRUCTIVE ILLUSTRATION assumption. It licenses
     T-003 and the constructive branch of T-004. It does NOT license any claim
     of generality: no statement may read "omitted context induces
     heteroskedasticity" without the Gaussian-linear qualifier.
  2. T-001 (the mixture representation) remains assumption-free with respect to
     A-003 and must not be restated in Gaussian terms.
  3. The manuscript must carry an explicit remark that the Gaussian-linear case
     is chosen for exact tractability, and that the qualitative mechanism
     (variance heterogeneity in the mixing law) is what generalises, not the
     closed form.
Follow-up tasks:
  - registries/assumption_register.csv: A-003 status planned -> approved,
    decision_status decision_needed -> approved.
  - docs/theorem_backlog.md: T-003 decision-gated -> statement-draft.
  - docs/theorems/T-003_gaussian_constructive.md created.
```

---

## 2026-09-08 / D-002 — Bind the LOO leave-out unit to the trial

```text
Date: 2026-09-08
Requested by: autonomous research session (T-005 unblocking)
Decision needed: Whether the prespecified leave-out unit G for the primary
  predictive comparison is a single TRIAL or a single PARTICIPANT.
Reason approval was required: docs/current_project_context.md records the LOO
  unit as an open PI decision gate; trial-level and participant-level leave-out
  answer different scientific questions for hierarchical cognitive models.
Options:
  (a) G = one trial (within-participant next-trial prediction).
  (b) G = one participant (generalisation to a new participant).
User decision: (a) G = one trial. Trial-level LOO is the PRIMARY predictive
  comparison.
Conditions or modifications:
  1. ESTIMAND RESTATEMENT. The primary predictive estimand is now
     within-participant, next-trial log predictive density, with that
     participant's remaining trials in the conditioning set. It is NOT
     generalisation to a new participant. Every occurrence of
     "generalisation to a new participant" as the primary target is superseded;
     docs/current_project_context.md is updated accordingly.
  2. CLAIM LIMIT. C-001 may not be supported by an appeal to new-participant
     generalisation on trial-level LOO evidence alone.
  3. MANDATORY SECONDARY ANALYSIS. Participant-level K-fold cross-validation is
     required as a secondary analysis in both simulation and empirical arms,
     reported alongside the primary result, whether or not it agrees.
  4. KNOWN DIRECTIONAL CONFOUND — MUST BE ADDRESSED IN THE MANUSCRIPT.
     For hierarchical models, trial-level leave-out leaves the participant's
     random effects informed by that participant's other trials. This is
     optimistic for models with more participant-level flexibility, i.e. it is
     biased TOWARD M_K, which is the direction of the paper's own claimed
     effect. The paper must therefore:
       (i) state this bias explicitly where the primary result is reported;
       (ii) show via condition 3 that the M_K advantage survives
            participant-level K-fold, or report plainly that it does not;
       (iii) treat a trial-level-only advantage as insufficient evidence for
            C-001.
     A reviewer will otherwise read the primary result as an artefact of the
     leave-out unit, and would be correct to do so.
  5. PSIS Pareto-k diagnostics are a validity check on the estimator, not a
     waivable assumption. k-hat >= 0.7 on any fold requires exact refit or
     K-fold for that fold.
Follow-up tasks:
  - registries/assumption_register.csv: add A-010 (approved).
  - docs/theorems/T-005_loo_predictive.md created with G bound to the trial.
  - docs/current_project_context.md: remove the "remains a PI decision gate"
    language and record the binding plus its consequences.
```

---

## 2026-09-08 / D-003 — Priors and marginal-likelihood estimator; demotion of T-006

```text
Date: 2026-09-08
Requested by: autonomous research session (T-006 unblocking)
Decision needed: (i) the prior families and scales and the marginal-likelihood
  estimator for the Bayes-factor arm; (ii) whether the Bayes-factor result
  remains a theorem target.
Reason approval was required: docs/theorem_backlog.md forbids stating a
  Bayes-factor theorem before the prior family, scale, and marginal-likelihood
  target have a recorded decision.
Options:
  (a) Declare priors/estimator and keep T-006 as a theorem target.
  (b) Declare priors/estimator and DEMOTE T-006 to a numerical prior-sensitivity
      study, not a theorem.
  (c) Drop the Bayes-factor arm entirely.
User decision: (b). The declared priors and estimator below now govern a
  numerical sensitivity study; T-006 is removed from the theorem route.
Conditions or modifications:
  1. DECLARED PRIORS (proper, predeclared, applied identically to the shared
     parameters of M_S and M_K):
       - standardised regression coefficients:      Normal(0, 1)
       - latent-parameter population means:         Normal(0, 1)
       - all standard deviations / scale parameters: half-Normal(0, 1)
       - correlation matrices:                       LKJ(2)
       - mixture / latent-class weights:             Dirichlet(1, ..., 1)
     All continuous predictors are standardised before fitting so these scales
     are interpretable and transferable between models.
  2. PRIOR-SCALE SENSITIVITY GRID: every scale parameter above is multiplied by
     s in {0.5, 1, 2} and the full comparison is rerun. Reporting a single
     prior scale is not permitted.
  3. MARGINAL-LIKELIHOOD ESTIMATOR: bridge sampling (Meng-Wong iterative
     scheme) applied to the full posterior draws, with the estimator's own
     relative-standard-error diagnostic reported. Naive harmonic-mean and
     posterior-mean estimators are prohibited.
  4. WBIC (Watanabe 2013), evaluated at inverse temperature 1/log n, is the
     required cross-check on any BIC-like quantity, because M_K is singular
     (see D-004). BIC itself may not be used as evidence for C-004.
  5. The Bayes-factor arm is reported as a ROBUSTNESS APPENDIX. It may not
     appear in the abstract, and it may not be cited in support of C-001.
Follow-up tasks:
  - docs/theorems/T-006_bayes_factor_deferred.md created with the full
    justification for demotion.
  - docs/theorem_backlog.md: T-006 moved out of the proof route into a
    "deferred / not a theorem target" section.
  - registries/claim_register.md: C-004 evidence sources updated to remove the
    Bayes-factor theorem.
```

---

## 2026-09-08 / D-004 — Singular-model policy for finite-sample selection criteria

```text
Date: 2026-09-08
Requested by: autonomous research session (T-007 correction)
Decision needed: How the theorem package should handle the fact that M_K is a
  singular statistical model, so that textbook AIC/BIC/Laplace asymptotics do
  not apply.
Reason approval was required: this changes which model-selection criteria the
  project may report as evidence, i.e. it changes an estimand.
Options:
  (a) Continue to state AIC/BIC threshold corollaries as previously drafted.
  (b) Split T-007 into an exact algebraic identity, a regular-case probabilistic
      bridge, and an explicit singular-case correction; demote AIC/BIC to legacy
      diagnostics.
User decision: (b).
Conditions or modifications:
  1. M_K (finite-mixture / latent-class / random-effects ambiguity models) is a
     SINGULAR model: at parameter values where a mixture component is empty or a
     variance is zero, the parameter is non-identifiable and the Fisher
     information degenerates. These points lie on the boundary of the parameter
     space and are exactly the points that matter under the project's own
     boundary conditions 1-3.
  2. Consequences that must be honoured throughout:
       - BIC's (k/2) log n penalty is invalid for M_K. The correct free-energy
         expansion is Watanabe's, with the real log canonical threshold lambda
         (lambda <= k/2) and multiplicity m. BIC therefore OVER-penalises M_K,
         so a BIC-based null result is not evidence against C-004.
       - AIC's 2k correction assumes correct specification. Under
         misspecification the correct correction is Takeuchi's
         tr(J^{-1} V); under singularity neither applies.
       - Boundary parameters also invalidate the chi-squared_{k_K - k_S} null
         reference for the likelihood-ratio statistic (Chernoff; Self & Liang).
         No significance reading of D_n is permitted.
  3. PRIMARY CRITERIA: PSIS-LOO / WAIC, which remain asymptotically valid for
     singular models. AIC and BIC are retained ONLY as legacy bridge diagnostics
     with an explicit caveat, and may not be cited in support of C-004.
  4. Nominal parameter counts k_S, k_K may not be reported as complexity.
     Report p_loo / p_waic instead.
Follow-up tasks:
  - docs/theorems/T-007_finite_sample_selection.md created, split into
    T-007a / T-007b / T-007c.
  - registries/assumption_register.csv: add A-011 (approved).
  - R/model_selection.R must label AIC/BIC output as legacy diagnostics.
```

---

## 2026-09-08 / D-005 — T-002 remains a corollary

```text
Date: 2026-09-08
Requested by: autonomous research session
Decision needed: Whether the F_{Theta|Z} display may be promoted to a primary
  theorem statement.
Reason approval was required: reversing the 2026-07-07 rejection of A-006 would
  change the primary theorem statement.
Options:
  (a) Keep F_{Theta|X,Z} primary; F_{Theta|Z} as Corollary 1.2 only.
  (b) Promote F_{Theta|Z} to primary under a fixed-design convention.
User decision: (a). Confirmed and now binding.
Conditions or modifications:
  1. A-006 remains rejected. This is not reopenable by an agent.
  2. F_{Theta|Z} may appear only inside T-002 / Corollary 1.2 and its
     discussion. scripts/check_coherence.py enforces this mechanically.
  3. Any downstream result that needs the simplified mixing law must declare
     T-002 in its depends_on block, which forces its exogeneity condition into
     that result's assumption set.
Follow-up tasks:
  - docs/notation_registry.md records the binding.
  - scripts/check_coherence.py enforces the restriction.
```

---

## Open gates

**None.** Every theorem assumption in
`registries/assumption_register.csv` is now `approved` or `approved_default`,
except A-006, which is rejected and not reopenable by an agent.

The package is no longer blocked on decisions. It is blocked on **review**:
proof-critic review is outstanding for T-001, T-003, T-004 and T-007, and T-005
additionally needs its T-005b expansion derived rather than quoted. See
`loops/proof_loop.md` for the four-part gate into the supplement.

## Entry template

```text
Date:
Requested by:
Decision needed:
Reason approval was required:
Options:
User decision:
Conditions or modifications:
Follow-up tasks:
```
