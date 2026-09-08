# Primary theorem specification — 2026-09-08

Status: G1 specification complete; positive primary separation and selection remain unproved. A subsequent author attempt records exact obstructions and conditional finite-design criterion limits in `primary_separation_attempt_2026-09-08.md`. Author derivations below have not received an independent review. Authority and scope: `pi_decisions_2026-09-08.md`. The earlier `PROOF_PACKAGE.md` remains a separate benchmark.

Approval update: the user approved sections 2–3 (P-G1) for synthetic theorem development on 2026-09-08. References below to that specification as proposed are historical; approval does not extend to P-G2a/b or P-G3. The general theorem remains the main deliverable, and this example supports its nonvacuity and boundary analysis.

## 1. Approved assumptions versus proposed specialization

The approved structural equation is Theta=a0+a1 Z+gamma C+u, with E[C|Z=z]=m(z) and Var(C|Z=z)=v(z). Under finite conditional second moments, define g(z)=E[u|z], s²(z)=Var(u|z), c(z)=Cov(C,u|z). Then

    E[Theta|z] = a0+a1 z+gamma m(z)+g(z),
    Var(Theta|z) = gamma² v(z)+s²(z)+2 gamma c(z).

Proof: conditional expectation is linear; expand the conditional variance of gamma C+u. No distributional conclusion follows. In particular u=-gamma(C-m(Z)) cancels contextual variance even when gamma is nonzero.

The observable law additionally needs a full joint law of (X,Z,C,u) and a response kernel. The short mixture statement is

    P(y|X,Z) = integral product_t f(y_t|theta,x_t,Z) dF(theta|X,Z),

provided trial responses are independent conditional on (Theta,X,Z). That independence is an explicit proposed model condition, not implied by the additive equation. Do not replace F(theta|X,Z) with F(theta|Z) without a separate design condition.

Proposed Gaussian subcase, not adopted: C|Z=z ~ Normal(m(z),v(z)); u|Z=z ~ Normal(0,sigma_u²); C and u conditionally independent given Z. This gives Theta|Z normal with the displayed mean (g=0) and variance gamma²v+sigma_u². It still does not determine Theta|X,Z. A fixed synthetic design can be specified for a restricted existence example; it cannot establish general design exogeneity.

### 1.1 What additional conditions buy (none follows from A-003)

All equalities are almost sure on the support of Z; a claim of varying variance means nonconstancy on sets of positive Z-probability. The coefficients are fixed population constants. Finite conditional second moments of C and u are the integrability conditions for the variance identities, not a Gaussian assumption.

| Additional condition | Exact consequence | What it does not give |
|---|---|---|
| E[u|Z]=0 | Removes g(z) from the mean only. | Zero covariance, constant residual variance, or normality. |
| Cov(C,u|Z)=0 | Removes 2 gamma c(z) from the variance only. | Independence or a constant s²(z). |
| Var(u|Z)=sigma_u² | Replaces s²(z) by a constant only. | Removal of the covariance term. |
| The preceding three conditions together (P-G2a) | Mean a0+a1 z+gamma m(z); variance gamma²v(z)+sigma_u². With gamma!=0 and nonconstant v, variance varies. | A normal law or observable separation. |
| E[u|C,Z]=0 | By iterated expectation, implies both g(z)=0 and c(z)=0. | Homoskedasticity or independence. It is stronger than the two needed moment restrictions. |
| C independent of u conditional on Z | Implies c(z)=0. | Centered u, constant s²(z), or Gaussian marginals. |
| Joint conditional Gaussianity of (C,u) | Theta|Z is normal with the general mean and variance, including c(z). | Independence unless the conditional covariance is zero; no simplified moments without their restrictions. |
| P-G2b: independent conditional Gaussian C and centered constant-variance Gaussian u | Gives the displayed simplified normal law. Its characteristic function is exp(it[a0+a1z+gamma m(z)] - t²[gamma²v(z)+sigma_u²]/2). | Any conclusion about Theta|X,Z without specifying the design joint law; any model preference. |

P-G2a is the minimal moment package proposed for the *shortened identities*, not a necessary condition for those identities to happen by cancellation. P-G2b is an optional stronger sufficient package for a normal-law construction; it is not needed for the primary mixture representation. Neither package is adopted here. Marginal conditional Gaussian laws without a joint-law condition do not suffice to make their sum Gaussian.

For actual choice conditioning write W=(X,Z), m_X(W)=E[C|W], g_X(W)=E[u|W], v_X(W)=Var(C|W), s_X²(W)=Var(u|W), c_X(W)=Cov(C,u|W). The same algebra gives

    E[Theta|W] = a0+a1 Z+gamma m_X(W)+g_X(W),
    Var(Theta|W) = gamma²v_X(W)+s_X²(W)+2 gamma c_X(W).

Restrictions given Z do not automatically hold given W. Keep the full F(Theta|W); A-006 remains rejected as a primary assumption. No causal identification claim follows from this conditional structural description.

## 2. Explicit candidate kernel for decision and analysis

Proposed synthetic gain-only task: each trial specifies both lotteries, with nonnegative scaled payoffs v_A,v_R, probabilities p_A,p_R in [0,1], ambiguity width A>=0, and recorded side s. Y=1 means ambiguous choice (RAID raw choice code 2). All these inputs must be known. This is not a validated loss-domain or real-RAID specification.

Define w(p;rho)=exp(-(-log p)^rho) for 0<p<1 and rho>0, with endpoints w(0;rho)=0,w(1;rho)=1. In particular w(p;1)=p. Define

    eta = alpha + beta_side s
          + tau [v_A {w(p_A;rho)-theta A/2} - v_R w(p_R;rho)],
    f(Y=1|theta,x) = sigmoid(eta), tau>0.

Weight raw probabilities before subtracting the signed ambiguity cost. The expression in braces is a utility coefficient, not a probability; do not clip it. Negative theta represents ambiguity seeking. Allowing rho>1 is part of this proposed specification.

The proposed true DGP uses this same kernel with rho=1, true shared constants alpha*, beta_side*, tau*>0, and Theta_i=a0+a1 Z_i+gamma C_i+u_i. Conditional on (Theta_i,X_i,Z_i), the T responses are independent Bernoulli draws from this kernel. Context has no additional direct response effect in this proposed DGP. Generate (X_i,Z_i,C_i,u_i) from a joint law H having the approved context moments and finite residual second moments, then generate the responses. Thus

    P_H(y_i|W_i) = integral product_t f(y_it|a0+a1 Z_i+gamma c+u,x_it;rho=1)
                           dH(c,u|W_i).

This defines the DGP class exactly, but not a separation witness: G2 must give explicit H, constants, design support and probabilities. Gaussian P-G2b is optional, not a hidden restriction on H. If context is recorded for a future context-aware reference fit, it enters that fit's conditioning explicitly; the S/K comparison below omits C from both training and prediction, while still integrating their working latent-effect distributions; neither candidate receives observed C.

For a tractable initial pair, both candidates retain Z and share the same working random-effect law G(theta|X,Z;psi)=Normal(mu0+mu1 Z,sigma_theta²), shared alpha, beta_side, and global tau. S fixes rho=1; K estimates one global log rho. Both omit C. The normal working law and its lack of further X dependence are candidate restrictions, not assertions about the true law. Here Z denotes retained covariates, not the omitted C. If Z itself denotes the context excluded by empirical M4, set mu1=0 in both candidates and restate the comparison; the retained-Z S/K pair is a restricted theoretical analogue, not automatically the full empirical M1/M4 suite. A richer shared baseline must be checked before interpreting separation as a cognitive-model result. Participant-varying tau or rho are later extensions requiring a new proof.

Use the matching proper priors and scales in `bayesian_comparison_plan.md` (including shared-parameter equality and the log-rho prior). Integrate latent participant effects. Do not count each latent draw as a new free BIC parameter. A compact theorem domain would be an explicit specialization with normalized truncated priors, not a silent replacement for the empirical priors.

No parameter values, design, or context law establishing separation for this pair have yet been proved. Unknown RAID payoff/probability and side mappings remain outside this synthetic specification.

## 3. Likelihood and primary prediction target

Proposed asymptotic regime: iid participants, fixed common finite T>=2, static trial design (or an explicitly specified random design law); n tends to infinity. More precisely, (W_i,Y_i) are iid participant clusters under H and the kernel, with a common law of W; likelihoods condition on all W and do not model their density. A deterministic common X is a restricted example within this regime, not approval of general A-006. All limits average over this participant population. Trial independence is conditional only. Variable T, longitudinal dependence, and increasing T need their own statements.

For candidate M, global parameter phi, and observed design, write

    q_M,i(y_i;phi) = integral product_t f_M(y_it|theta,x_it;phi) dG_M(theta|X_i,Z_i;phi),
    L_M(phi) = product_i q_M,i(y_i;phi).

Let q_M,i,-t be the marginal formed by integrating the product over t' != t against the SAME G_M. With D_-it deleting only response y_it,

    pi_M(phi|D_-it) proportional to pi_M(phi) q_M,i,-t(y_i,-t;phi)
                                          product_{k!=i} q_M,k(y_k;phi),
    p_M(y_it|D_-it) = integral [q_M,i(y_i;phi)/q_M,i,-t(y_i,-t;phi)]
                              pi_M(phi|D_-it) dphi.

This ratio learns the participant effect from their retained responses. Positivity is required. The equivalent evidence ratio is m_M(D)/m_M(D_-it), with identical design conditioning and priors. For an outcome-independent eligibility set I fixed before scoring, define the exact observed-data score

    ELPD_M^trial(D) = sum_{(i,t) in I} log p_M(y_it|D_-it, W_1:n),
    mean_ELPD_M^trial = ELPD_M^trial / |I|,
    LOOIC_M^trial = -2 ELPD_M^trial.

The theoretical result below uses every one of nT trials. For a different eligibility rule its target and limit must be restated. These sums are the LOO estimate of expected log predictive density, not an expectation over as-yet unseen responses. Delete the response only: retain all trial covariates including x_it, the same priors, and other participants. No preprocessing, fitted hyperparameter, or latent-effect estimate trained on the deleted response may be frozen into an exact refit. The full-posterior importance identity uses inverse conditional likelihood weights; PSIS is an approximation requiring diagnostics and exact-refit validation. Arbitrary trial deletion in a learning or adaptive-design model needs a fresh conditioning argument.

 Whole-person deletion has a different predictive target. Use participants as independent clusters for uncertainty. With unequal trial counts report trial-weighted primary results and equal-participant sensitivity.

## 4. Closed target distinction: joint KL is insufficient for trial LOO

For strictly positive laws P,Q on a finite T-trial response space, define R(Q)=KL(P||Q), R_-t(Q)=KL(P_-t||Q_-t), and the expected conditional risk

    C_t(Q)=E_{P_-t} KL(P(Y_t|Y_-t) || Q(Y_t|Y_-t)).

The chain rule gives C_t(Q)=R(Q)-R_-t(Q). Proof: substitute P(y)=P_-t(y_-t)P(y_t|y_-t) and the analogous factorization of Q into log(P/Q), and sum under P. Therefore, for two fixed candidate laws,

    Delta_cond = (1/T) sum_t [C_t(Q_S)-C_t(Q_K)]
               = Delta_joint - (1/T) sum_t [R_-t(Q_S)-R_-t(Q_K)].

For random W, all three risks mean their H_W averages, using P_H(.|W) and Q_M(.|W); the chain rule holds at each W and hence after averaging. Define joint pseudo-true parameters phi_M* in argmin_phi E_W KL(P_H(.|W)||q_M(.|W;phi)) and Q_M*=q_M(.|W;phi_M*). Delta_joint=R(Q_S*)-R(Q_K*) is measured per participant, and Delta_cond is measured per trial. These are the joint-likelihood fitted targets, not separately optimized conditional predictors. Nonunique parameter minimizers are harmless only if they yield the same relevant laws or if all posterior limits yield the same risks; otherwise a mixture-limit analysis is needed.

A positive joint gap alone has no implication for the sign of the conditional gap.

Exact counterexample, cells ordered (00,01,10,11):

    P=(2/5,1/10,1/10,2/5), Q_S=(7/10,1/10,1/10,1/10), Q_K=(1/4,1/4,1/4,1/4).

Each P marginal is (1/2,1/2), each S marginal (4/5,1/5), and each K marginal (1/2,1/2). Thus the marginal-risk difference is log(5/4), while

    Delta_joint = (1/5) log(3125/1568) > 0,
    Delta_cond  = (1/5) log(32/49) < 0.

Numerically these are 0.1379266723 and -0.0852168791 nats, respectively. This is a counterexample to a general implication, not an example from the selected cognitive pair or a refutation of its possible simultaneous superiority. Both Q laws are false. It blocks the shortcut from a BF/joint-KL theorem to a trial-LOO theorem.

## 5. Separate proof obligations and boundary controls

G2 must establish a fully specified P and the fitted joint-KL projections Q_S*,Q_K*: existence, identifiable observable laws (or handling nonunique minimizers), and strict 0<R_K<R_S. It must also establish Delta_cond>0 at those projections for the desired trial prediction conclusion. Optimizing conditional risk separately would describe different fitted models. Preserve both directions of the counterexample above as a regression check.

The approved moments alone cannot guarantee strict separation: even with gamma!=0, conditionally independent Gaussian context/residuals, affine m(z), constant v(z), and a fixed design can yield a normal Theta|Z exactly inside S's working law. With rho=1 and matching shared terms, R_S=0; K cannot strictly improve. This is an explicitly restricted counterexample, not an adoption of Gaussian assumptions for the primary theorem. Context-null and residual cancellation are additional negative controls.

BIC corollary (still open): using the integrated participant likelihood, prove n^-1(log Lhat_K-log Lhat_S) -> Delta_joint>0. Then BIC_K-BIC_S=-2n Delta_joint+o_p(n)+(k_K-k_S)log n -> -infinity for fixed dimensions. Establish the convergence hypotheses locally; ordinary regular BIC as a marginal-evidence approximation requires additional regularity and is not automatic for singular hierarchies.

BF corollary (still open): with the selected proper priors, prove n^-1 log BF_KS -> Delta_joint. Begin with prior mass near the KL optimum and likelihood bounds. A sharper dimension penalty is secondary and needs justified regularity; bridge-sampling agreement cannot prove it.

Trial-LOO corollary (still open): establish posterior predictive convergence uniformly across single-trial deletions, control logs, and apply a cluster law of large numbers. For fixed T, the intended result is (nT)^-1(ELPD_K-ELPD_S) -> Delta_cond>0, hence (nT)^-1(LOOIC_K-LOOIC_S) -> -2 Delta_cond. This requires the separate conditional gap and fitted joint projection assumptions. It is not inherited from the legacy LOPO corollary.

### 5.1 Lemma inventory and dependencies

The labels below are new specification obligations, not accepted theorems or replacements for legacy O1–O10.

| ID / target | Required statement and proof work | Dependencies / current gap |
|---|---|---|
| PG-L1: observable mixture | Normalize the conditional cluster law under H and the kernel; specify design conditioning and conditional independence. | A-003 + proposed response/design specification. Formula given; concrete H still missing. |
| PG-L2: moments | Derive general moments; prove each optional reduction and cancellation boundary. | A-003 and stated integrability; derivations above, author-only status. No selection consequence. |
| PG-L3: design and observable identifiability | Determine whether probability variation, ambiguity widths and payoff contrasts distinguish rho from mean ambiguity, dispersion, intercept and sensitivity after integration. Rule out identical observable laws, including zero ambiguity, degenerate payoffs or probability designs. Parameter identifiability is stronger than needed if laws are identifiable. | PG-L1; explicit design needed. A latent variance difference is insufficient. |
| PG-L4: joint projections and strict separation | Establish existence of KL minima and give a concrete H/design with 0<R_K<R_S, under matched baselines. Handle nonunique minimizers and boundary optima. Nesting S in K only gives R_K<=R_S; strictness and K being false each need proof. | PG-L3; entirely open for S/K. Context-null, representable Gaussian and residual-cancellation controls required. |
| PG-L5: integrated likelihood convergence | Prove a uniform cluster LLN or suitable local/global likelihood bounds, integrable log envelopes, and convergence of optimized log likelihoods. Use fixed-dimensional global parameters after random-effect integration. | PG-L1, PG-L4; compactness/positivity are possible routes, not approved facts. Supplies separate BIC criterion result, not automatically a Laplace approximation. |
| PG-L6: evidence rate (BF) | For each M prove n^-1 log m_M(D) -> sup_phi E log q_M(Y|W;phi); bound outside near-optimal sets and give positive fixed prior mass in KL neighborhoods. Retain all normalizers. Subtract limits to obtain log BF_KS/n -> Delta_joint. | PG-L4–5 plus A-014 proper priors. Noncompact normal-prior tails require control; a compact truncated-prior theorem would be a separately declared specialization. No need to assume regular Hessians for an exponential-rate result if direct bounds suffice. |
| PG-L7: deletion identity | Prove the q/q_-t posterior formula by integrating the participant effect and Bayes' rule, or equivalently by the evidence ratio with response-only deletion. | Positive normalized PG-L1 laws, identical priors/design. Algebra specified here; no asymptotic preference implied. |
| PG-L8: conditional gap | At the joint projections of PG-L4, prove Delta_cond>0 separately using conditional laws or the chain-rule subtraction. | PG-L4; open. Existing four-cell obstruction forbids inference from Delta_joint alone. |
| PG-L9: deleted posterior predictions | Prove concentration at relevant joint-optimal laws and average or uniform stability over nT response deletions; show predictive convergence to q_M/q_M,-t. Justify interchanging integration/limits and control logs by boundedness or uniform integrability. | PG-L4–5, PG-L7; fixed T alone does not prove deletion stability, especially with unbounded covariates/parameters or nonunique optima. |
| PG-L10: trial score limit | Combine PG-L9 with a cluster LLN for conditional log-score differences to obtain the displayed ELPD/LOOIC limits; distinguish this probability limit from a CLT or finite-sample uncertainty formula. | PG-L8–9. Trial contributions are dependent. Uncertainty needs a cluster argument including fitting effects; independence of individual trials cannot be asserted. |

Evidence/BF and trial-LOO branches are logically separate after joint projection and likelihood work. The work queue may sequence them, but PG-L6 does not depend on a positive conditional gap. A bridge-sampling estimate, numerical separation lead, or passing log validator establishes none of PG-L3–6 or PG-L8–10. The benchmark's quadratic comparator, binary context, uniform boxes and whole-participant deletion remain outside this inventory.

## 6. Next bounded task and backup routes

Next run: G2 first establish necessary design/identifiability conditions and test the proposed S/K pair for observable containment. Do not declare proposed Gaussian or kernel conditions approved. Seek an analytic finite-design construction; a numerical candidate is only a lead. If shared random effects absorb the context, record that obstruction and identify the exact restriction needed for a genuine gap, rather than dropping shared baseline terms. If the joint gap is positive but the conditional gap fails, record the narrower BF/BIC result and keep the requested simultaneous result open. If two attacks fail, write the failed equations and move to a finite-support context construction or a local perturbation calculation, with any scope change explicit.

Decision proposal: approve the synthetic gain-only kernel and the matched global-tau/global-rho candidate pair in section 2 for theorem development; P-G2a residual moment restrictions and P-G2b Gaussian joint-law conditions in section 1 remain separate, unapproved sufficient-condition proposals. Do not request reapproval of A-003, trial deletion, the probability-distortion family, or delegated priors/evidence computation. No extra moment or Gaussian package is required to finish G1; future adoption should name the exact subpackage needed by a concrete construction. Independent boundary and conditional-risk work can continue without that decision.

## 7. Subsequent G2 attempt — 2026-09-08

See [the proof and blockage record](primary_separation_attempt_2026-09-08.md). The affine-mean constant-variance Gaussian boundary is exactly represented in S. On a common two-trial design with opposite side codes, distortion offsets can be absorbed by the free intercept and side coefficient; S and K have identical observable families. A fully specified finite-support context with conditional variances 1 and 4 cannot overcome this obstruction. No design was retuned to produce a win.

PG-L7 now has an explicit local deletion derivation. Conditional on finite design support, strictly positive true cells and a unique optimal observable law (P-G3), the new artifact derives likelihood localization, uniform response-deletion posterior concentration and the participant-cluster trial-score limit. Separate evidence and BIC rate statements are derived there. These author results partially address PG-L5–PG-L10 but do not close strict PG-L4/PG-L8, general-design convergence, fitted-score uncertainty or independent review. Both normalized score and BF gaps are zero in the representable boundary. For the nonidentifiable two-trial design, a nominal BIC parameter-count penalty is not a regular evidence approximation.

Next: audit the full design support for nuisance absorption before any further separation construction. Keep all shared terms. P-G3 remains a conditional proposal, and no approval status or final claim changes follow from the derivations.

## 8. Full-support audit — 2026-09-08

[The design audit](design_absorption_audit_2026-09-08.md) stacks all four supported (W,t) rows of the existing primary design and proves distortion absorption for every rho>0 with one global parameter map. Shared sensitivity and dispersion remain in the model. The quotient criterion requires positive sensitivity scaling; rank equality alone does not suffice. No complete richer or RAID two-lottery support is currently specified. Its manifest must be reconstructed before a further actual-support audit and separation construction. P-G3 remains a conditional proposal, with no approval or final-claim change.
