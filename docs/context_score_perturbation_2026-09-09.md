# Context perturbation after adjusting the shared baseline

Date: 2026-09-09. Status: author derivation, not independent review or final acceptance. This is a general sufficient-condition result for finite exponential-family candidates, not a completed theorem for the nonlinear probability-distortion pair. It advances the mechanism branch of general_theorem_architecture.md. No additional assumptions are adopted for the empirical model.

## Objects and explicit hypotheses

Let W have finite support with fixed positive weights H(w); Y is a finite participant response vector. All calculations condition on W, including the mixing law. Let a latent variable L=(C,u), Theta=a0+a1 Z+gamma C+u, and a fixed conditional response kernel f(y|L,w), which may be the product of conditionally independent trial kernels. Assume a baseline latent law F0(dL|w) induces a strictly positive observable law p0(y|w).

Consider the nested, normalized working families

    q_{a,b}(y|w)=p0(y|w) exp{a' U_w(y)+b V_w(y)-psi_w(a,b)},
    psi_w(a,b)=log sum_y p0(y|w) exp{a' U_w(y)+b V_w(y)}.

S fixes b=0; K allows b in R; a ranges over R^d in BOTH. Center U and V conditionally under p0; this changes no family. Assume the H-averaged covariance matrix of (U,V) is positive definite. This is observable minimality; a singular latent parameterization cannot simply inherit it. The exponential families here are a conditional mathematical specialization, not a replacement for approved P-G1.

Take a bounded latent perturbation k(L,w) with E0[k|W]=0 and define

    dF_epsilon=(1+epsilon k)dF0,  |epsilon| ||k||_infinity < 1.

The observable law is exactly p_epsilon=p0(1+epsilon h), where h(y,w)=E0[k|Y=y,W=w]. This follows by integrating f k and dividing by p0. Conditional centering of h follows by summing over Y. The response mechanism and additive equation remain unchanged; only the distribution of latent causes changes. The induced conditional context moments may change. If a construction requires prescribed m(z),v(z), it must additionally preserve the corresponding moment constraints; the tilt does not do that automatically.

Use inner product <g,h>=E0[g(Y,W)h(Y,W)]. Write

    I=E0[UU'], c=E0[UV], V_perp=V-c' I^{-1}U,
    J=E0[V_perp²]>0, B=E0[h V_perp]=E0[k V_perp(Y,W)].

Let P_S and P_K denote orthogonal projection onto the spans of U and (U,V), respectively. R_M(epsilon) is the global infimum of the participant conditional KL risk from p_epsilon to candidate M.

## Theorem: a positive joint gap with nuisance refitting

Under the preceding hypotheses,

    R_S(epsilon)-R_K(epsilon)=epsilon² B²/(2J)+o(epsilon²),
    R_K(epsilon)=epsilon² ||h-P_K h||²/2+o(epsilon²).

Consequently B!=0 implies strict joint superiority for all sufficiently small nonzero epsilon. If also ||h-P_K h||>0, then 0<R_K(epsilon)<R_S(epsilon): the better complex candidate is still observably false. Neither conclusion establishes trial-conditional superiority.

## Proof

Set t=(U,V), beta=(a,b), G=E0[tt'], and Psi(beta)=E_H psi_W(beta). Finite support makes Psi analytic. At zero its gradient is zero and Hessian is G. Under p_epsilon,

    E_epsilon[t]=epsilon E0[h t]=epsilon v.

The population negative log likelihood, up to a constant, is Psi(beta)-epsilon v'beta. Since G is invertible, the inverse function theorem gives a stationary solution beta_epsilon=epsilon G^{-1}v+O(epsilon²) near zero. This is the global optimum, not just a local fit: at every finite beta the Hessian of Psi is the averaged tilted covariance of t. A nonzero direction with zero such variance would be constant within every w-response support; positivity of p0 would then contradict positive definiteness of G. Hence Psi is strictly convex everywhere, and any stationary solution is its unique global minimizer. The same argument applies to S using I. This establishes attainment without restricting parameter boxes.

Taylor expansion gives

    KL_H(p_epsilon||p0)=epsilon² E0[h²]/2+O(epsilon³),
    Psi(beta_epsilon)-epsilon v'beta_epsilon
       =-epsilon² v'G^{-1}v/2+O(epsilon³).

The first expansion uses bounded h, positivity for small epsilon and E0 h=0. The second uses beta_epsilon=O(epsilon), so no unjustified expansion far from an optimum occurs. Since v'G^{-1}v=||P_K h||², this proves the K risk formula, and similarly the S formula. Orthogonal decomposition gives

    P_K h=P_S h+(B/J)V_perp,
    ||P_K h||²-||P_S h||²=B²/J.

Subtract the risk expansions. A positive leading coefficient dominates its o(epsilon²) remainder for sufficiently small nonzero epsilon, proving both strict conclusions. All risks concern the participant response vector; trials were never treated as independent observations.

## Producing alignment from a latent context distribution

The condition B!=0 can be generated at the latent level rather than simply assumed as the desired risk sign. Define

    g(L,w)=E0[V_perp(Y,W)|L,w].

Because E0[V_perp|W]=0, E0[g|W]=0. Finite response/design support makes g bounded. Choose k=g. Then

    B=E0[k g]=E0[g²].

Thus whenever g is not zero almost surely, this valid centered latent tilt produces a strictly positive joint gap after refitting ALL simple parameters. If only context C may be reweighted, replace g by g_C(C,w)=E0[V_perp(Y,W)|C,w] and use k=g_C; then B=E0[g_C²]. This preserves the baseline conditional law of u given (C,W), although its marginal distribution can change. No Gaussian distribution or design exogeneity is required.

This is a meaningful observable condition: after removing simple-model directions, responses must still carry context-dependent variation along the extra score. If g_C=0, every bounded context-only tilt has B=0 at first order; higher-order analysis might still yield a gap. A positive B does not ensure the residual ||h-P_K h|| is positive, so observable falsity remains a separate check.

If fixed context moments must be preserved, k must also be orthogonal to the relevant conditional moment functions. One cannot use k=g_C unless it satisfies these restrictions. Finding a bounded admissible tilt with nonzero alignment is then a separate constrained projection problem.

## Negative controls and limits

1. Full observable absorption: if V lies in the simple score span, J=0 and the theorem is inapplicable. Removing a nuisance term to make J positive changes the comparison. The saved two-trial and full-support distortion absorption proofs remain negative controls.
2. No latent-to-observable alignment: if g_C=0, every context-only tilt yields B=0. Nonzero gamma or heterogeneous latent variance alone does not change this fact.
3. Complex model captures the perturbation to first order: if h lies in the K score span, this result does not prove R_K>0. A higher-order residual could still make it false, but needs proof.
4. The theorem's fixed epsilon asymptotics are distinct from sample size n. BIC/BF transfer for each fixed nonzero epsilon does not imply uniform preference for epsilon_n tending to zero.
5. The result is not directly applicable to arbitrary smooth nonlinear mixtures or the approved distortion hierarchy. Extending it requires observable local coordinates plus control of global optimal laws; parameter Hessian inversion is unsafe when shared effects create nonidentifiability.
6. For trial LOO the conditional KL gap must still be established at these joint projections. The existing joint-minus-retained-marginal identity is the correct next calculation, not an automatic positive corollary.

## Implication and next bounded obligation

The proof isolates a mechanism condition stronger than latent heterogeneity and weaker than assuming the desired KL inequality: a context-induced response perturbation must have a nonzero component in an extra observable score direction after the shared simple fit adjusts. It also separates the remaining-falsity condition.

Next: derive the second-order trial-conditional KL difference for this same perturbation and the same JOINT projections, using conditional expectations over retained responses. Establish a usable sufficient sign condition or an exact counterexample. Keep this distinct from the later extension to nonlinear probability distortion. A separate adversarial review of this lemma should check global optimality, admissible tilts and the residual-risk claim before integration.
