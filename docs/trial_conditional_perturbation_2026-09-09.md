# Trial-conditional KL under the same joint fits

Date: 2026-09-09. Status: author theorem and proof; separate review pending. Depends on `context_score_perturbation_2026-09-09.md`. This establishes a population conditional-risk expansion for the same finite exponential-family setting. It neither refits a conditional objective nor proves the nonlinear cognitive-model application. No additional empirical assumptions are adopted.

## Definitions and inherited hypotheses

Retain all hypotheses and notation of the context-perturbation lemma: finite W and participant response-vector support, strictly positive baseline p0, p_e=p0(1+e h), nested minimal exponential families, and the unique GLOBAL joint-optimal laws q_S,e* and q_K,e* for sufficiently small e. Let T>=2 be fixed. Expectations, inner products and conditional expectations below use H(w)p0(y|w), unless explicitly marked e.

For trial t define the orthogonal conditional-expectation operator

    E_-t g = E0[g(Y,W)|Y_-t,W], D_t=Id-E_-t,
    A=(1/T) sum_t D_t.

Each D_t is a self-adjoint orthogonal projection. Thus A is self-adjoint, positive semidefinite, and 0<=A<=Id. Define the residuals at the joint tangent projections

    r_M=h-P_M h, d=P_K h-P_S h=(B/J)V_perp,
    r_S=r_K+d.

In particular <r_K,d>=0 in the JOINT inner product. The averaged trial-conditional population risk of the JOINT fit is

    C_M(e)=(1/T) sum_t E_{e,W,Y_-t}
       KL(p_e(Y_t|Y_-t,W) || q_M,e*(Y_t|Y_-t,W)).

Let Delta_C(e)=C_S(e)-C_K(e), positive when K is better. These conditionals use each candidate's joint-fitted law; they are not separately optimized.

## Theorem TC: expansion and sign

Under the inherited hypotheses,

    C_M(e)=e² <r_M,A r_M>/2+o(e²),
    Delta_C(e)=e² L/2+o(e²),
    L=<d,A d>+2<r_K,A d>.

Therefore L>0 gives strict trial-conditional superiority for every sufficiently small nonzero e; L<0 gives strict preference for S in this population score. L=0 is inconclusive without higher-order analysis.

Equivalently, writing a=B/J,

    L=a² <V_perp,A V_perp>+2a <r_K,A V_perp>.

This is the extra sign condition beyond joint superiority. The joint gap is e² ||d||²/2+o(e²), which is positive whenever B!=0, regardless of L's sign.

## Proof of the conditional expansion

The preceding lemma gives q_M,e*/p0=1+e P_M h+O(e²), uniformly on the finite support, and normalization holds for each w. For any normalized smooth path q_e/p0=1+e g+e² j+o(e²), finite support permits termwise expansion; normalization gives E0[g|W]=E0[j|W]=0. Expanding log(p_e/q_e), multiplying by p_e and summing yields

    KL_H(p_e||q_e)=e² ||h-g||²/2+o(e²).

The terms of first order and the mean of j vanish by normalization; this explains why the second derivative of the fitted path does not appear in the leading risk.

Marginalizing over Y_t gives

    p_e,-t/p0,-t=1+e E_-t h,
    q_M,e*,-t/p0,-t=1+e E_-t(P_M h)+O(e²).

Apply the same expansion on the finite retained-response support to obtain marginal KL e² ||E_-t r_M||²/2+o(e²). The exact KL chain rule, with expectation under the ACTUAL perturbed retained-response law, gives

    E_{e,W,Y_-t} KL(p_e(Y_t|Y_-t,W)||q_M,e*(Y_t|Y_-t,W))
       = KL_H(p_e||q_M,e*)-KL_H(p_e,-t||q_M,e*,-t).

Subtract and use orthogonality of conditional expectation:

    ||r_M||²-||E_-t r_M||²=||D_t r_M||²=<r_M,D_t r_M>.

Averaging over the fixed finite number of trials proves the first formula. Substitute r_S=r_K+d, expand the quadratic form, and use self-adjointness of A to prove L. A nonzero leading coefficient determines the sign for sufficiently small nonzero e. No limit in participant sample size n is used here.

## Usable sufficient conditions

The exact leading-order criterion is L>0. Several stronger conditions are easier to check:

1. Favorable residual alignment: <r_K,A d>>=0 and <d,A d>>0 suffice.
2. Invariance: if A d belongs to the K tangent span, then <r_K,A d>=0, because r_K is orthogonal to that entire span. If additionally <d,A d>>0, the conditional gap is positive. The particularly simple case A d=lambda d with lambda>0 gives L=lambda ||d||².
3. A conservative quantitative bound: writing ||g||_A=sqrt(<g,A g>), Cauchy–Schwarz gives L>=||d||_A²-2||r_K||_A ||d||_A. Thus ||d||_A>2||r_K||_A is sufficient. It is not necessary.

These conditions concern how retained responses reveal the extra model direction and the remaining misspecification. Joint orthogonality <r_K,d>=0 does NOT generally imply <r_K,A d>=0.

On full Cartesian response support with p0 positive, a conditionally centered nonzero d has <d,A d>>0. Indeed zero energy implies d=E_-t d for every t, so d is unchanged when any one response coordinate changes. Connectivity of the Cartesian support then makes d constant within each w; conditional centering makes that constant zero. For response supports with structural zeros or deterministic constraints, retain the explicit positive-energy condition.

## Exact nested-family counterexample with global joint fits

Let W be constant, T=2, responses (x,y) in {-1,+1}², and p0=1/4. Let U=y, V=x+xy. Both are centered, <U,V>=0, I=1 and J=2, so the inherited minimality hypothesis holds. Define

    S: q_a(x,y) proportional to exp(a y),
    K: q_a,b(x,y) proportional to exp(a y+b(x+xy)),
    p_e(x,y)=[1+e(3x-xy)]/4, 0<|e|<1/4.

All true and candidate cells are positive. These are diagnostic observable laws, not the approved probability-distortion cognitive pair. This example uses the observable specialization p_e=p0(1+e h); it does not supply a cognitive additive-context witness.

Since E_e[y]=0, the simple global fit is q_S,e*=1/4. In K the conditional law of x given y=-1 is forced to be uniform, while the conditional law given y=+1 and the marginal law of y can be varied independently. Thus its global joint fit is exactly

    q_K,e*(x,+1)=(1+2e x)/4,
    q_K,e*(x,-1)=1/4.

For completeness b=(1/2)atanh(2e), a=-(1/2)log cosh(2b) realizes this law, with finite parameters. It matches the true y marginal and the true conditional on the adjustable stratum y=+1; the KL chain rule minimizes those independently. Both candidates are false for e!=0, because the true conditional on y=-1 has mean 4e.

Here P_S h=0, d=P_K h=x+xy, and r_K=2(x-xy). Under uniform independent binary responses, A x=x/2, A y=y/2, and A(xy)=xy. Direct inner products give

    ||d||²=2, ||r_K||²=8,
    <d,A d>=3/2, <r_K,A d>=-1,
    L=-1/2.

Consequently

    R_S-R_K=e²+o(e²)>0,
    R_K=4e²+o(e²)>0,
    Delta_C=-e²/4+o(e²)<0

for sufficiently small nonzero e. This reverses the conditional preference despite nesting and use of the exact GLOBAL joint-optimal fits. It is stronger than comparing two arbitrarily chosen candidate laws. Positivity of R_K also follows exactly from its forced uniform conditional in the y=-1 stratum.

## Positive control under the same fitted-likelihood procedure

With the same uniform baseline take U=x, V=y, and h=y+(xy)/2. Then q_S,e*=1/4 and q_K,e*=(1+e y)/4. Here d=y, r_K=xy/2 and A d=d/2, so

    R_S-R_K=e²/2+o(e²), R_K=e²/8+o(e²),
    Delta_C=e²/4+o(e²)>0.

Both models are false for e!=0 because p_e has a nonzero interaction. This diagnostic confirms the sign condition is achievable for nested observable exponential families without selecting a different fitting objective. As above, no claim of a realized cognitive context law is made.

## Consequences and remaining work

Combining the context-perturbation lemma with B!=0, ||r_K||>0 and L>0 gives, within its finite exponential-family scope, simultaneously positive joint and trial-conditional gaps and observable falsity for every sufficiently small fixed nonzero e. Separate BIC/BF/LOO transfer hypotheses remain necessary. In particular exact Bayesian trial-LOO asymptotics need concentration at these joint laws under response deletion and log-score control; this population theorem is not itself that convergence theorem.

Next bounded task: a separate adversarial review of the two perturbation lemmas and their positive/negative controls. Then formulate the observable regularity and global-localization requirements for extension beyond exponential families, identifying which can be proved for the approved cognitive hierarchy. Do not reopen the absorbed designs or claim that the observable diagnostic examples establish the cognitive mechanism.
