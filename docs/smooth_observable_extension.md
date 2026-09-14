# Smooth observable families: global KL projections and conditional risk

Date: 2026-09-10. Status: author theorem and proof; separate review pending. Extends the reviewed finite exponential-family perturbation results. The local completeness condition below is a substantive hypothesis to verify for any cognitive application, not an approved or established property of the probability-distortion hierarchy.

## Objects and hypotheses

W has a finite support with fixed positive weights H(w). Each participant response vector Y has finite support; T is fixed. Let p0(y|w)>0 on that support and let p_e=p0(1+e h), with E0[h|W]=0. The function h is bounded automatically on the finite support, and e is sufficiently small that p_e>0. Inner products use H p0. A bounded latent tilt from the previous lemma is one way to generate this path while retaining conditioning on W=(X,Z).

For M=S,K let Q_M be a family of conditional probability vectors and C_M its closure in the finite product of probability simplexes. Assume Q_S subset Q_K and p0 belongs to both. Define global risk R_M(e)=inf_{q in Q_M} KL_H(p_e||q). The closure is used for the existence proof, not to discard parameter-limit competitors.

For each M assume:

(H1) A C3 map q_M:B_r(0) subset R^{d_M}->Q_M, with q_M(0)=p0 and strictly positive cells. Its derivative at zero is injective. The chart can be made locally one-to-one by shrinking r (choose an invertible derivative minor and use the inverse function theorem).

(H2) Local completeness of the observable chart: there is an ambient open neighborhood O_M of p0 such that every q in C_M intersect O_M is represented in this chart, and there is a continuous inverse coordinate map kappa_M on C_M intersect O_M with kappa_M(p0)=0 and q_M(kappa_M(q))=q. After shrinking the chart and neighborhood if necessary, q_M and kappa_M are mutual inverses on this portion of the family.

(H2) rules out additional branches or parameter-limit laws approaching p0 outside the regular chart. It permits arbitrarily many global parameter values representing the same observable law: the chart is for laws, not for the original latent parameterization. No global compact parameter box, global parameter identifiability or global convexity is assumed. Conversely a nonsingular Hessian at one original parameter does not prove (H2).

Set s_M=partial_theta log q_M(theta)|0, G_M=E0[s_M s_M'], and V_M=span of its component scores. G_M is positive definite by injectivity and p0>0. Differentiating normalization gives E0[s_M|W]=0. Assume V_S subset V_K explicitly; this follows for compatible smooth embedded nested charts, but stating it avoids relying on an unproved parameter embedding. Let P_M be the orthogonal tangent projection and define

    g_M=P_M h, r_M=h-g_M, d=g_K-g_S,
    A=(1/T) sum_t (Id-E0[ . |Y_-t,W]).

Use a different symbol C_M^trial(e) for trial-conditional risk below; C_M without superscript denotes the observable-law closure only.

## Theorem SO

Under these hypotheses, for all sufficiently small |e| the infimum defining R_M(e) is attained at a unique observable law q_M,e* in the stated chart. Its coordinates and density ratio satisfy

    theta_M(e)=e G_M^{-1} E0[h s_M]+O(e²),
    q_M,e*/p0=1+e P_M h+O(e²).

The remainders are uniform over the finite observable support. Consequently,

    R_M(e)=e² ||r_M||²/2+o(e²),
    R_S(e)-R_K(e)=e² ||d||²/2+o(e²),
    C_M^trial(e)=e² <r_M,A r_M>/2+o(e²),
    Delta_C(e)=e² {<d,A d>+2<r_K,A d>}/2+o(e²).

All fitted laws here are GLOBAL JOINT KL projections. C_M^trial uses the actual p_e distribution of retained responses and q_M,e*'s conditional probabilities; it is not minimized separately.

Thus ||d||>0, ||r_K||>0 and L=<d,A d>+2<r_K,A d>>0 imply simultaneously 0<R_K<R_S and Delta_C>0 for all sufficiently small nonzero e. If L<0 the conditional preference reverses despite the positive joint gap. Zero coefficients require higher-order work.

## Proof 1: global minimizers must approach p0

For fixed small e, KL_H(p_e||q) is lower semicontinuous on compact C_M, with value infinity if a positive true cell receives zero probability. Since p0 is available and has finite risk, a minimizer q_e exists in C_M and has positive cells. Moreover

    0<=KL_H(p_e||q_e)<=KL_H(p_e||p0)=O(e²).

Every sequence e_j->0 of such minimizers has a convergent subsequence in C_M. Joint lower semicontinuity of finite KL and p_ej->p0 imply KL_H(p0||q_limit)=0. Positivity of H and Gibbs' inequality give q_limit=p0. Therefore ALL minimizers approach p0: otherwise a sequence staying outside a fixed neighborhood would have a subsequential limit different from p0, contradicting the preceding argument.

This step localizes observable laws, not parameters. It handles remote or boundary parameter sequences without assuming they are irrelevant.

By (H2), all these minimizers eventually belong to the chart, with coordinates kappa_M(q_e)->0. Since the chart maps into Q_M rather than just its closure, the closure minimum is attained in the original family for small e. This is the exact point at which local completeness turns law localization into regular coordinate localization.

## Proof 2: the localized global minimizer is the unique smooth branch

Let F_M(theta,e)=KL_H(p_e||q_M(theta)). Positivity and C3 regularity make this C3 near (0,0). Differentiating normalized q gives

    gradient_theta F_M(0,0)=0,
    Hessian_theta F_M(0,0)=G_M,
    partial_e gradient_theta F_M(0,0)=-E0[h s_M].

For the Hessian identity, differentiate sum_y q_M(y|w)=1 twice: E0[partial² log q_M|0+s_M s_M']=0. The expected negative log-density Hessian is therefore G_M; global exponential-family structure is unnecessary.

The inverse/implicit function theorem gives a unique local stationary branch theta_M(e), with derivative at zero G_M^{-1}E0[h s_M] and a bounded second derivative near zero. Continuity of the Hessian and G_M>0 give a convex coordinate ball and a neighborhood of e=0 on which that Hessian is uniformly positive definite. Thus F_M is strictly convex on THAT ball, though it need not be globally convex.

Proof 1 puts every global minimizer inside a smaller interior ball for small e. Each is stationary and hence equals the implicit branch. This proves uniqueness of the global observable law and the coordinate expansion. Global uniqueness was not inferred from local convexity alone.

Differentiating q_M/p0 at zero gives the score vector, so substitution yields 1+e s_M'G_M^{-1}E0[h s_M]+O(e²). This coefficient equals P_M h by the normal equations for finite-dimensional orthogonal projection.

## Proof 3: risks at the global joint fits

For any normalized C2 path q_e/p0=1+e g+e² j+o(e²), expanding log(p_e/q_e) and using conditional normalization yields

    KL_H(p_e||q_e)=e² ||h-g||²/2+o(e²).

The mean of the second-order density coefficient j is zero within each w. With g=P_M h this proves the individual risk formula. Nested tangent projections imply r_S=r_K+d and <r_K,d>=0, giving the joint difference formula.

Marginalizing a first-order density perturbation over trial t replaces its coefficient by E0[ . |Y_-t,W]. Apply the finite KL expansion separately to the joint laws and their retained-response marginals. The exact KL chain identity then yields

    C_M^trial(e)=e² average_t [||r_M||²-||E0[r_M|Y_-t,W]||²]/2+o(e²).

Orthogonality of conditional expectation gives the A quadratic form. Substitute r_S=r_K+d and use self-adjointness to obtain L. No second-order curvature term survives in these leading risk coefficients; curvature matters in the remainder and in proving the fitted branch is globally relevant.

Strictness follows by dividing by e² and taking e->0. This is a local DGP-perturbation limit; it is not a uniform-in-n model-selection theorem for shrinking e_n.

## Why local regularity alone fails: exact competing-branch example

Take one W, three response cells, p0=(1,1,1)/3, u=(1,-1,0), v=(1,1,-2), and

    Q={p0(1+a u): |a|<1/4} union {p0(1+b v): |b|<1/4}.

Each parameter branch is smooth and positive; a disconnected open parameter domain can parameterize this family smoothly. The chart a->p0(1+a u) has an injective derivative and positive information at zero. But it does not cover all observable laws near p0: the second branch crosses it there.

Let p_e=p0(1+e v), 0<|e|<1/4. On the first branch the unique optimum is a=0: its a-dependent expected log likelihood is (1+e)log(1-a²)/3, maximized at zero. Since <u,v>=0 and ||v||²=2, its local residual calculation gives risk e²+o(e²). Over the FULL Q, however, p_e itself lies on the second branch, so the global risk is exactly zero. Hypothesis (H2) fails for the chosen chart; all smoothness and information checks on that branch miss the failure.

This is why replacing global localization with multi-start numerical fitting or a Hessian test cannot close the theorem. The example is an observable diagnostic, not a cognitive construction.

## Sufficient route for verifying (H2), and cognitive checklist

If the full observable-law closure is a C3 embedded submanifold without boundary in a neighborhood of p0, that neighborhood lies inside the actual family, and its dimension matches the chart, then the required local chart and inverse supply (H1)–(H2). This is a sufficient geometric condition to establish, not a conclusion from parameter smoothness. Boundaries, crossings, singularities and extra limiting branches require separate treatment, potentially tangent cones or unions of tangent spaces.

For the approved cognitive hierarchy, the next obligations are:

1. Work with the integrated participant law. Prove C3 differentiation under the latent integral on a neighborhood, using an explicit integrable envelope; merely smooth conditional logits do not suffice.
2. Identify observable redundancies in shared sensitivity, latent mean/variance, intercept and side terms. Construct charts after accounting for redundancies, or prove why a regular chart is unavailable. Do not discard shared nuisance terms to force injectivity.
3. Prove local completeness for the full family AND its closure, including parameter sequences escaping to infinity or approaching zero variance. A successful numerical Jacobian rank check addresses neither closure nor competing branches.
4. Construct a permitted context perturbation h, then prove ||d||>0, ||r_K||>0 and the separate conditional sign. No such certificate for the approved pair is claimed here.

The general theorem now covers regular smooth observable families with verified local completeness. It does not cover every cognitive mixture. Bayesian posterior/deletion convergence, proper-prior support and finite-sample scoring remain separate downstream obligations.
