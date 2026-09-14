# General theorem architecture: separation before selection

Status: author theorem architecture and local sufficient-condition derivation, 2026-09-08. General theorem is primary; approved P-G1 is a supporting construction. No positive gap for that cognitive pair is claimed. This document distinguishes sufficient mathematical hypotheses from assumptions established for the research DGP.

## 1. Common observable object

Let W=(X,Z) and Y=(Y_1,...,Y_T) be a participant's observed design and response vector. Fix the target design law H. Under conditional trial independence given (Theta,W), the omitted-context law is

    p_w(y) = integral product_t f_0(y_t|theta,x_t,z) dF(theta|W=w).

Theta=a0+a1 Z+gamma C+u determines this mixing law only after a joint law of (X,Z,C,u) is specified. Conditional means and variances alone do not determine p. Retain conditioning on X. Shared random effects, intercepts, side terms and sensitivity belong in both candidates.

For candidate observable families Q_S and Q_K define

    R_M = inf_{q in Q_M} E_H KL(p_W || q_W),
    Delta_J = R_S-R_K.

The scientific target includes R_K>0: the complex model is still observably false. Mechanistic falsity alone is a distinct, weaker assertion and does not establish positive observable KL risk. Nesting S in K yields only Delta_J>=0.

## 2. Mechanism layer: when context creates an advantage

Three distinct requirements must be established from the response kernel, context law and design:

1. Context changes the observable law in a way the shared simple baseline cannot represent or approximate arbitrarily well. Nonzero gamma or changing latent variance does not suffice.
2. An observable direction available to K improves approximation at the best S fit. Additional parameters, noncontainment, or an unabsorbed logit direction alone do not prove improvement for this particular p.
3. The improved candidate remains separated from truth if the claim is 0<R_K<R_S. Showing every individual parameter is false does not rule out an infimum of zero at a parameter limit.

A useful general sufficient condition proves requirement 2 without assuming the KL gap itself.

### Proposition M: observable score alignment

Assume q_S* attains the simple population optimum with finite risk. Suppose K contains a one-sided differentiable path q_epsilon through q_0=q_S*, for 0<=epsilon<epsilon_0. On the relevant observable support define

    s_w(y) = d/d epsilon log q_epsilon,w(y) at epsilon=0+.

Assume differentiation can pass through expectation under P and through normalization of q_epsilon. A finite design/response support with strictly positive q_0 and differentiable cell probabilities is one sufficient specialization. For general support, specify integrable derivative bounds instead. If

    A = E_H sum_y [p_w(y)-q_S*,w(y)] s_w(y) > 0,

then R_K<R_S. For non-discrete responses replace sums with integrals against a common dominating measure.

Proof. Differentiating normalization gives sum_y q_S*,w(y)s_w(y)=0. Hence A=E_P s_W(Y). Differentiating risk gives

    d/d epsilon R(q_epsilon) at 0+ = -E_P s_W(Y) = -A < 0.

By the definition of a right derivative, some sufficiently small epsilon>0 satisfies R(q_epsilon)<R(q_0)=R_S. Since q_epsilon belongs to K, R_K<=R(q_epsilon)<R_S. This proves strictness, not merely nesting. A two-sided path with a nonzero derivative allows selection of its decreasing orientation. If the derivative is zero this test is inconclusive; it does not prove equality.

For an interior, differentiable simple optimum, all simple nuisance scores have expectation zero under P. Therefore any added score in their linear span has A=0. This explains why matched nuisance terms must be kept and why the existing distortion-absorption examples fail. A direction outside that span still needs A!=0: novelty is not alignment.

To connect this proposition to omitted context, substitute the actual mixture into A:

    A = E_H integral [sum_y f_0(y|theta,W) s_W(y)] dF(theta|W),
    f_0(y|theta,W)=product_t f_0(y_t|theta,x_t,z).

This formula identifies the outstanding mechanism proof: derive an allowable F from the additive equation and a design for which the observable score aligns with the context-induced residual at the best shared baseline. It must also establish that baseline optimum and the candidate path. An assumption merely saying A>0 is a sufficient-condition theorem, not a completed demonstration that omitted context produces it. Continuous-design and nonattained-optimum cases need extensions; do not pretend this attained-optimum proposition covers them.

To prove R_K>0 on a finite response/design space with positive true cells, it suffices to show p is outside the closure of K's observable-law image. Proof: that closure is compact; KL is lower semicontinuous, attains its minimum, and is zero only at p. This is a closure separation obligation, stronger than parameter nonrepresentation. In general spaces an appropriate positive-distance or compactness argument must replace it.

## 3. Transfer layer: what each criterion additionally requires

All likelihoods below integrate each participant's latent effects before multiplying across participants. Let n be the number of independent participants and T fixed. The following are separate sufficient transfer conditions, not consequences of the additive context equation.

| Criterion | Population sign needed | Additional transfer obligations | Result when obligations hold |
|---|---|---|---|
| BIC | Delta_J>0 | Fitted integrated log likelihood per participant converges to each population optimum; numerical optimization error is o_p(n); difference in penalties is o(n) | (BIC_K-BIC_S)/n -> -2 Delta_J |
| Bayes factor | Delta_J>0 | Fixed proper normalized priors, positive prior mass near population optima, likelihood/evidence upper bound and prior-neighborhood lower bound yielding log m_M/n -> ell_M* | log BF_KS/n -> Delta_J |
| Exact trial LOO | Delta_C>0, defined below at joint-fitted limiting laws | Observable posterior-predictive concentration under response deletion, control of log predictions, and a participant-cluster law of large numbers | (ELPD_K-ELPD_S)/(nT) -> Delta_C; LOOIC difference/(nT) -> -2 Delta_C |

Here all arrows denote convergence in probability. A positive limiting advantage gives preference with probability tending to one; it is not an ordinary-sample-size guarantee. With Delta=0, these first-order statements do not determine preference.

BIC: for fixed global parameter counts k_M, the penalty is k_M log n. The displayed result follows by subtracting the two likelihood limits and using log n/n -> 0. It describes the computed criterion. Interpreting ordinary BIC as an evidence approximation additionally requires appropriate identifiable regular local geometry; latent hierarchies may violate it. Integrating participant effects does not automatically establish that geometry.

BF: the sufficient bounds are m_M<=exp(n sup ell_n) and, for every delta>0, m_M>=Pi(V_delta) exp(n(ell_M*-delta+o_p(1))), where Pi(V_delta)>0 is fixed and V_delta is a suitable near-optimal neighborhood. Divide logs by n and then send delta to zero. This avoids a needless Laplace expansion for a fixed positive gap. A sharper log-n penalty is an extra theorem, not needed for exponential preference. Improper or shrinking/exponentially unfavorable priors cannot silently inherit this proof.

LOO: the scored target is one missing response of an already observed participant, retaining their other responses. At a joint-fitted limiting law q_M*, the prediction is q_M*(y|w)/q_M*,-t(y_-t|w), not an unconditional response marginal. Define

    C_M = (1/T) sum_t E_{W,Y_-t} KL(p(Y_t|Y_-t,W) || q_M*(Y_t|Y_-t,W)),
    Delta_C = C_S-C_K.

The chain rule gives exactly

    Delta_C = Delta_J - (1/T) sum_t [KL_H(p_-t||q_S*,-t)-KL_H(p_-t||q_K*,-t)].

Thus Delta_C>0 is equivalent to the joint advantage exceeding the average advantage on retained-response marginals. This is an additional population condition, not merely a technical convergence assumption. The counterexample in primary_theorem_specification.md section 4 proves Delta_J>0 can coexist with Delta_C<0. Do not optimize C_M separately and then describe it as the limit of joint-likelihood Bayesian fits.

Uniqueness of the joint-optimal observable law is sufficient for a single LOO limit, not always necessary. If multiple optima induce the same relevant conditionals, a weaker theorem may suffice; otherwise characterize posterior weights or withhold the single-limit result. BF and BIC optimal-value limits do not inherently require uniqueness.

## 4. Existing evidence and remaining general work

- Mixture and conditional moments: local identities; they establish the observable object, not strictness.
- Existing primary_separation_attempt_2026-09-08.md L1 and L2, and design_absorption_audit_2026-09-08.md: exact negative controls. Shared effects can represent the truth, and the audited support absorbs distortion. Those designs cannot supply the desired gap.
- The same attempt's L4–L8: author finite-support transfer proofs under conditional proposal P-G3, including positivity and unique observable optimum for LOO. They are not reviewed general continuous-design theorems, and supply no positive sign.
- Proposition M here: a general local route to strict joint superiority. Its alignment and remaining-falsity premises have not been verified for the approved cognitive pair.
- Conditional risk identity: separates the extra population requirement for trial prediction. It is not supplied by Proposition M.
- Legacy PROOF_PACKAGE.md: separate finite linear/quadratic benchmark, with different prediction target; not evidence that probability distortion wins trial LOO.

## 5. Dependency order and bounded next task

General mechanism: additive DGP + observable kernel + design -> best shared baseline and genuinely available observable direction -> score alignment -> strict joint gap; separately prove positive residual complex risk. Then assess the conditional-risk advantage. BIC and BF can proceed from the joint branch while the conditional branch remains open. Criterion transfer proofs do not close the mechanism branch.

Next bounded task: formulate and prove a context-perturbation sufficient condition that evaluates Proposition M's alignment after allowing the simple nuisance fit to adjust. State smoothness and observable identifiability requirements explicitly, distinguish first-order absorption from higher-order effects, and use the existing absorbed designs as negative controls. Prefer an observable finite-dimensional lemma before imposing Gaussian structure. If two attacks yield no usable sign condition, record the exact obstruction and switch to a finite-mixture reweighting argument; do not rerun the absorbed design or manufacture a gap by dropping shared terms. The synthetic example is used only when it demonstrates nonvacuity or resolves a named general obligation.
