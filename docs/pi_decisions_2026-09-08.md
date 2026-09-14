# PI decisions and revised scientific contract

Date: 2026-09-08. Authority: the PI's explicit responses in the project conversation. These decisions supersede conflicting September 5 defaults. They authorize direction and implementation choices, not acceptance of unproved scientific claims.

## Decisions recorded

| Topic | Decision | Consequence |
|---|---|---|
| Primary LOO unit | Trial-level leave-out | Predict one response of an observed participant using their other responses. Whole-participant LOPO is a secondary, distinct target. |
| A-003 | Adopt theta = a0 + a1 Z + gamma C + u, with conditional context mean m(z) and variance v(z), as the primary formal route | T-003 becomes active; the finite binary-context proof remains a benchmark, not the newly requested theorem. |
| Primary M4 | Probability distortion | The model-family selection gate is closed. The weighting equation and its use in the gain/loss task still need explicit specification and validation. |
| BF priors | LLM authorized to choose diffuse or weakly informative proper families and reasonable scales | Adopt the defaults in bayesian_comparison_plan.md; prior predictive validation precedes final fitting. |
| Marginal likelihood | LLM authorized to choose estimator | Bridge sampling for fitted structural models; exact integrals for theory and deterministic quadrature for low-dimensional validation. |
| RAID fields | PI supplied semantic meanings | Coding memo partially resolved; code-to-option mappings, units and several task details still need confirmation. |

## Trial-level prediction contract

Let D denote all responses and D_{-(it)} omit only y_it, retaining participant i's other trials. Under a conditionally independent trial model, the primary score uses

    p(y_it | D_{-(it)}, X, Z, M)
      = integral p(y_it | theta_i, eta, x_it, M)
                 p(theta_i, eta | D_{-(it)}, X, Z, M) dtheta_i deta.

Sum its logarithm over eligible trials for ELPD; LOOIC is -2 times that sum. Participant effects may be learned from the other trials, but the held-out response cannot train its own exact-refit posterior. PSIS uses full-posterior draws with leave-one-out correction, not uncorrected in-sample scores. Validate against exact single-trial refits and report diagnostics. Learning/time-dependent models require a separate conditioning audit; arbitrary deletion is not automatically a forecast.

Report the trial-weighted primary total and per-trial mean. Summarize paired score differences by participant and account for within-person dependence when quantifying uncertainty; do not treat all trial contributions as independent. If trial counts differ, report equal-participant weighting as sensitivity. Holdout unit does not change the independent sampling unit into trials: BIC scaling and asymptotic proofs require their own sampling regimes.

This interpretation follows the distinction between conditional-observation and new-group targets in the [loo cross-validation FAQ](https://mc-stan.org/loo/articles/online-only/faq.html). It does not assert that trial-level LOO is universally preferable. A scientific implication to test is that other responses can already reveal a person's latent parameters, potentially reducing the incremental predictive value of context.

## A-003: what is approved and what remains to establish

Approved: the additive equation and the stated first two conditional moments of C. Write g(z)=E[u|z], s²(z)=Var(u|z), and c(z)=Cov(C,u|z). With finite conditional second moments,

    E[theta|z] = a0 + a1 z + gamma m(z) + g(z)
    Var(theta|z) = gamma² v(z) + s²(z) + 2 gamma c(z).

These identities do not require Gaussianity. The shorter variance gamma² v(z)+sigma_u² requires additional residual conditions; a normal conditional law requires distributional conditions as well. For example, conditionally independent Gaussian C and u with centered, constant-variance u would suffice, but those extra conditions are a proposal, not a consequence of the PI's wording. The residual choice u=-gamma(C-m(z)) cancels the contextual variance and shows why the distinction matters.

The next theorem task must separate approved hypotheses, sufficient-condition proposals, and conclusions. It must also connect latent heterogeneity to observable choice laws and a specified probability-distortion comparator. Moment heterogeneity alone does not prove a strict KL gap, a trial-LOO preference, or a BF preference. Keep the full F(theta|X,Z) mixture law primary; A-006 has not been approved by this decision.

## What existing results retain their status

PROOF_PACKAGE.md remains an unchanged finite two-trial, linear-versus-quadratic, proper-uniform-prior benchmark. Its KL/BIC review history remains usable for that benchmark only. Its LOPO theorem is not a trial-level theorem; its quadratic comparator is not probability distortion. New Gaussian/distortion/LOO statements need their own proof and review. The theorem identifiers now distinguish T-007 (legacy LOPO) and T-009 (new trial-LOO target); T-005 currently denotes convergence/BIC, even though older planning material used it differently.

No final RAID model has been fitted and no final claim is promoted by this decision record.

## 2026-09-08 P-G1 approval and general-theorem priority

The user explicitly approved the synthetic gain-only distortion model and matched baseline in primary_theorem_specification.md sections 2–3 for theorem development. P-G1 is approved for that restricted construction. The general theorem remains the priority; the example is a supporting route when useful, not the definition of project completion. This does not approve P-G2a/b or P-G3, establish a strict gap, validate the RAID model, or accept a proof.

Develop general sufficient conditions connecting omitted-context observable laws to strict joint and trial-conditional KL advantages, with separate BIC, BF and LOO implications. A theorem that merely assumes the desired positive gaps is a useful transfer result but does not by itself establish the research mechanism. Use the synthetic pair to demonstrate nonvacuity and expose necessary conditions. Preserve the proved absorption boundaries and do not retry absorbed designs.
