# M1: review of the minimal ambiguity proof

Date: 2026-09-12. Scope: `docs/minimal_ambiguity_proof.md`, sections 1–6. Reviewer: same LLM in a separate adversarial pass; not independent external or Lean verification. Verdict: PASS mathematically for the explicit fixed-constant, homogeneous global-parameter contract. One scientific interpretation clarification added to section 6. No equation, model parameter, prior or holdout target changed.

## Checks and reconstructed reasoning

1. Task mapping: multiplying v_A[w(1/2;rho)-theta A/2]-v_R w(1;rho) by tau=4, with v_A=1 and v_R=1/2, yields delta-theta(2A). Thus the declared widths give x=1,2 exactly. Only theta is fitted in S; theta and rho are fitted in K. Shared constants are fixed, not omitted fitted parameters. Adjusted utility coefficients need not be probabilities.
2. Prior and parameter support: w(1/2;rho) increases from exp(-1) to 1 as rho increases from zero to infinity. The specified interval maps bijectively onto delta in [-1/2,1/2]. Both optima and rho=1 lie inside the relevant supports. Densities are 1/2 for theta in S and 1/[2(rho_U-rho_L)] in K. With m=1/2+delta/4, the induced K density in (theta,delta) is

       1/[2(rho_U-rho_L)] times 1/[4 m log(m) log(log 2)].

   It is positive, finite and integrates to one by change of variables. Uniform rho is not uniform delta. Numerical evidence must preserve this distinction.
3. True cells: direct averaging of fair independent choices and success rates (1/4,1/10) gives (37,19,13,11)/80 in the declared order. Marginals are (3/8,3/10), covariance 1/40. These exact rational calculations pass the existing verifier.
4. KL separation: adding and subtracting log(P_1 P_2) gives the product-KL decomposition. Nonzero covariance proves positive mutual information. K's matching parameters are exact and interior. S's incompatible odds condition rules out zero marginal discrepancy; compactness makes its positive minimum rigorous. Thus the claim concerns infima, not selected fits.
5. Globality: S is strictly concave with score changing sign before the parameter limits; its optimizer is not forced by truncation. K is strictly concave in the equivalent rectangular (delta,theta) coordinates, with two linearly independent design rows. Concavity need not hold in rho, but global uniqueness is preserved by the bijection. No local optimizer is substituted for a global one.
6. Uniform likelihood convergence: all binary outcome factors exceed a=sigmoid(-9/2), so all log-pair likelihoods are bounded in magnitude by 2L. The four participant frequency errors control the objective uniformly. Participant independence is sufficient; marginal trial independence is neither assumed nor used.
7. Posterior concentration constants: outside U let F<=F*-g, and in V let F>=F*-g/4. On the event sup|ell/n-F|<=g/8, the likelihood separation is at least g/2. Integrating upper/lower bounds gives pi(V)^(-1) exp(-ng/2). For all single-response deletions, the uniform objective error is at most the full-data error plus L/n. Requiring that total error to be <=g/8 yields the same bound simultaneously. No union over independently generated deletion events is required.
8. BIC: the fixed one-parameter penalty difference is log n; normalized likelihood difference tends to Delta. This proves the stated BIC criterion preference, not an unproved evidence approximation.
9. BF: normalized proper prior mass is at most one for the upper bound and positive on every small optimum neighborhood for the lower bound. Divide the likelihood-integral sandwich by n and let the neighborhood error tend to zero. No log-n expansion is needed.
10. Exact trial LOO: the candidate ratio q(y_1,y_2)/q(y_-t) is exactly its t-th Bernoulli factor, even though true P is dependent. Uniform posterior concentration plus uniform continuity gives predictive convergence; the floor a makes taking logs safe. The participant LLN yields ELPD difference/n -> Delta and LOOIC difference/n -> -2 Delta. Per-trial conditional KL advantage is Delta/2. The retained response still affects global-parameter inference at finite n.
11. Controls: the context-aware model contains truth at a=log 3; the C=0 null is in both families. Zero normalized gaps do not settle finite-sample preference. Simultaneous positive-gap preference follows by a union bound over the three criterion failures.

## Interpretation clarification

With a single nominal probability, distortion is equivalent on this design to a common utility offset. This does not invalidate the one-versus-two-parameter comparison or the specified weighting model, but it limits mechanistic interpretation. Section 6 now explicitly says the example cannot distinguish distortion from other offset-producing mechanisms. Do not reword this result as evidence that people use probability distortion.

The fixed nuisance constants and homogeneous global fits are substantive restrictions authorized by the minimal contract. A model with a fitted common intercept would change the simple family. Per-participant fitting, flexible random effects, or a calibrated empirical model would also be different comparisons. No universal superiority statement follows.

## Verification, provenance and next step

Executed the existing minimal verifier: exact cells/covariance, weighting map, marginal matching, numerical optimal risk and direct conditional-risk identity passed. No simulations, posterior quadrature, Lean proof or external review performed in this pass. Source and review hashes are recorded in `logs/theory_checks/2026-09-12_minimal_review.json`.

M1 closes at separate-same-LLM-review level. Next M2: implement deterministic quadrature under the stated uniform-rho priors, validate exact response deletion on a tiny fixed dataset, and predeclare a small simulation pilot before looking at preference rates. Report numerical error and every outcome; the small gap is not a license to choose favorable seeds.
