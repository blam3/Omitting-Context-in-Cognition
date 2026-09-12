# Minimal ambiguity contract and direct separation proof

Date: 2026-09-12. Primary track under the user's explicit simplification request. Status: author proof and local checks; separate review pending. This supersedes the general/hierarchical route as the required main result, preserving it as an optional extension. Claim: a false two-parameter ambiguity model CAN outperform a one-parameter context-omitting model, not that complexity always wins.

## 1. Contract: exactly one versus two fitted parameters

Independent participants each complete two fixed gain-only trials. In both trials, option A pays 1 with nominal probability 1/2; option R pays 1/2 with certainty. Ambiguity widths are A_1=1/2 and A_2=1. Both reference amounts and probabilities are specified, and the widths give admissible symmetric probability intervals [1/4,3/4] and [0,1]. Y=1 means choose option A. Define x_t=2 A_t, so x=(1,2).

Use the previously specified kernel with shared sensitivity FIXED at tau=4, intercept and side effects FIXED at zero, and linear payoff utility. These are explicit restrictions of the theorem example, not empirical estimates or terms silently omitted from a fitted baseline. There is no fitted random-effect distribution. The parameters below are global parameters shared across participants, not one or two new parameters per participant.

    w(p;rho)=exp(-(-log p)^rho), w(1;rho)=1,
    logit Pr(Y_t=1)=4[w(1/2;rho)-1/2]-theta x_t.

S fits theta only and fixes rho=1. K fits theta and rho. Write delta=4[w(1/2;rho)-1/2]. Then the two candidate logits are simply

    S: -theta x_t,
    K: delta-theta x_t.

Delta is a one-to-one reparameterization of probability distortion, not a third parameter or a separately fitted intercept. Fix theta in [0,2] and delta in [-1/2,1/2]. Equivalently rho lies in [rho_L,rho_U], where

    rho_L=log(-log(3/8))/log(log 2),
    rho_U=log(-log(5/8))/log(log 2).

Both bounds are finite and positive, and rho=1 is interior. This follows from exp(-1)<3/8<1/2<5/8<1 and the strict increase of w(1/2;rho) in rho>0. The boxes ensure elementary existence and bounded likelihoods. The separation does not arise from artificially cutting off the simple optimum: the unrestricted simple optimum is inside (0,2), as proved below.

Each candidate asserts the participant likelihood q_M(y_1,y_2)=product_t Bern(y_t;p_M,t). This independence is part of the candidate misspecification, not an assumption about the marginal truth. Both use the same task information and omit context.

For BF and Bayesian trial LOO, use proper fixed Uniform[0,2] for theta; in K independently use Uniform[rho_L,rho_U]. A reparameterization to delta must carry its Jacobian. No evidence calculation can replace this with an unnormalized flat density in delta. Only positive prior mass near the optimum is needed below.

## 2. Explicit contextual truth and null

Let C_i be Bernoulli(1/2), shared across a participant's two trials. Set theta_i=C_i log 3, true rho=1, with the same fixed kernel constants. Given C_i, responses are independent and

    Pr(Y_it=1|C_i)=sigmoid(-C_i log 3 x_t).

This is an additive contextual DGP theta_i=0+(log 3) C_i+0 with no probability distortion. Its conditional ambiguity mechanism is simple. With C observed, the ONE-parameter model logit p=-a C x contains truth at a=log 3. The oracle supplies a contextual reference; no claim of causal identification in RAID follows.

For the context-null control set C identically zero. Then theta_i=0, the responses are independent fair choices, and S contains truth. The strict approximation advantage disappears: R_S=R_K=0. This does not imply equal finite-sample criteria or prove a particular model wins at zero asymptotic gap.

This example attributes improvement to compensating for a context-omitting homogeneous restriction. It does not establish superiority over every simple model with sufficiently flexible heterogeneity. Estimated sensitivity, extra intercepts and participant effects are separate extensions, not main-proof requirements.

## 3. Direct observable KL theorem

Let P denote the true marginal law. In cell order (00,10,01,11),

    P=(37,19,13,11)/80,
    p_1=3/8, p_2=3/10,
    Cov(Y_1,Y_2)=11/80-(3/8)(3/10)=1/40>0.

Proof of these cells: average the product law with success rates (1/2,1/2) and the product law with rates (1/4,1/10). This single averaging step is the entire mixture argument.

For any product candidate with rates (q_1,q_2), direct expansion of the logarithm gives

    KL(P || Bern(q_1) x Bern(q_2))
      = I_P(Y_1;Y_2)+kl(p_1||q_1)+kl(p_2||q_2),

where I_P=KL(P||P_1 x P_2)>0 because the covariance is nonzero. Every candidate is therefore observably false, including its optimum.

K matches both marginals exactly at

    theta_K=log(7/5), delta_K=log(21/25).

Indeed delta_K-theta_K=log(3/5)=logit(3/8) and delta_K-2 theta_K=log(3/7)=logit(3/10). The parameters are interior: 0<log(7/5)<2, and -1/2<log(21/25)<0 (use log(1+4/21)<4/21<1/2). Thus R_K=I_P>0 and the optimal observable law is unique. The corresponding rho_K is obtained from the displayed inverse map and differs from one, despite true rho=1.

S cannot match both rates: its logits require logit(p_2)=2 logit(p_1), whereas 3/7 != (3/5)^2. The continuous sum of the two nonnegative Bernoulli KL terms attains its minimum on [0,2]; a zero minimum would require both matches. Hence

    0<R_K<R_S, Delta=R_S-R_K>0.

This is the complete strict-separation argument: a four-cell mixture, a product-KL decomposition, and two unequal odds ratios. No smooth-family coverage theorem or latent inverse theorem is needed.

The expected S log likelihood has derivative sum_t x_t[sigmoid(-theta x_t)-p_t] and strictly negative second derivative -sum_t x_t² q_t(1-q_t). Its derivative is positive at theta=0 and negative at theta=2 (both predicted rates there are below their targets). Thus its unique optimum lies in (0,2) and is also the unrestricted real-line optimum. K's expected log likelihood is strictly concave in (delta,theta), because vectors (1,-1),(1,-2) span R² and both logistic variances are positive. Its exact matching solution is the unique global optimum on the rectangle. Reparameterization by rho preserves this optimizer.

## 4. One elementary convergence argument

Let n count participants, with T=2 fixed. Both parameter spaces are compact. All candidate logits lie in [-9/2,1/2], so success and failure probabilities are at least a=sigmoid(-9/2)>0; all participant cells are at least a². Set L=-log a.

Let hat P_n(y) be the four empirical participant-cell frequencies. Independence across participants gives Var(hat P_n(y))<=1/(4n), so a union bound and Chebyshev imply max_y|hat P_n(y)-P(y)| -> 0 in probability. For F_M=E_P log q_M and ell_M,n=sum_i log q_M(Y_i),

    sup_phi |ell_M,n(phi)/n-F_M(phi)|
      <= 2L sum_y |hat P_n(y)-P(y)| -> 0.

Taking suprema proves maximized log likelihood per participant tends to F_M*. Compactness, continuity and the unique optimum give a strictly positive population objective gap outside every neighborhood of that optimum.

For posterior concentration, choose such a gap g>0 and a smaller near-optimal neighborhood V with prior mass pi(V)>0 and F>=F*-g/4 on V. On a sufficiently accurate uniform-convergence event, the posterior mass outside the first neighborhood is at most pi(V)^(-1) exp(-n g/2). This follows by upper-bounding its likelihood and lower-bounding the evidence on V. The fixed uniform priors have positive mass on V because the optima are interior.

Deleting one response changes ell_M,n/n by at most L/n, uniformly over all 2n deletions and all parameters. The same good event and bounds therefore give concentration simultaneously for every response-deleted posterior. This deterministic bound avoids treating deletions as independent or using an invalid union bound over separate posterior events.

## 5. Three separate corollaries

All following convergence is in probability. These are author corollaries for this contract, not the empirical hierarchy.

**BIC.** Define BIC_M=-2 max ell_M,n+k_M log n, with k_S=1,k_K=2. The preceding uniform limit and the KL difference give

    (BIC_K-BIC_S)/n -> -2 Delta<0.

Thus K has lower BIC with probability tending to one. This proves preference of the stated criterion, without invoking BIC as a Bayes-factor approximation.

**Bayes factor.** Let m_M be the integrated likelihood under the stated normalized priors. Its upper bound is exp(max ell_M,n). For any eta>0, a positive-prior neighborhood where F>F*-eta gives a lower bound pi(V_eta) exp(n(F*-2eta)) with probability tending to one. Taking logarithms, dividing by n, and sending eta to zero yields

    log BF_KS/n -> F_K*-F_S*=Delta>0.

No Laplace approximation or sharper log-n penalty is required for this fixed positive gap.

**Exact trial LOO / LOOIC.** Delete only response y_it and form its exact posterior predictive probability using the retained data. Under these PRODUCT candidates, the conditional likelihood of y_it at fixed global parameters is just Bern(y_it;p_M,t); retaining the participant's other trial updates global parameters but there is no fitted participant effect to update. The uniform deletion concentration above and continuity imply every deleted predictive converges uniformly to Bern(y_it;p_M,t*). All probabilities exceed a, so logs are uniformly controlled. Applying the participant-cell LLN gives

    (ELPD_K-ELPD_S)/n -> sum_t E_P log[Ber(Y_t;p_K,t*)/Ber(Y_t;p_S,t*)]
                               =Delta>0,
    (LOOIC_K-LOOIC_S)/n -> -2 Delta<0.

Equivalently the per-trial ELPD advantage tends to Delta/2. The true conditional entropy cancels in the comparison. Therefore the population conditional KL advantage is EXACTLY Delta/2 for these product fits, despite dependence in the true data. No contradiction with the earlier general reversal example arises: this restricted candidate structure removes its additional conditional cross-term problem.

All three preference events hold simultaneously with probability tending to one by a union bound over their three failure probabilities. These are fixed-DGP, large-n conclusions, not guaranteed ordinary-sample-size wins. The exact construction has a small gap; unfavorable finite-sample evidence must be retained.

## 6. Scope and next action

Interpretation clarified in the September 12 review: because option A has the same nominal probability in both trials, rho is observationally equivalent to a free common utility offset delta on this design. The weighting equation provides a cognitive parameterization, but the example does not distinguish distortion from another mechanism producing that offset. The conclusion is that an extra fitted parameter can absorb omitted-context patterns, not identification of probability distortion. The ambiguity-adjusted utility coefficient is not constrained to be a literal probability; no clipping is performed.

This construction intentionally fixes shared nuisance constants and fits homogeneous global parameters. It is now authorized as the main theorem by the user's request for a genuine one-versus-two-parameter ambiguity comparison. It does not silently revise the earlier hierarchical model: that remains a separate empirical/general extension. Probability weighting is applied before the signed ambiguity cost, as in the approved kernel.

Next: adversarially review THIS short package and verify the ambiguity mapping, compact prior normalization, exact four-cell law and single-response deletion bound. Then run a small predeclared numerical validation and prepare a concise manuscript statement. Do not resume general chart coverage, Gaussian constructions, eight-trial latent identifiability or a full Lean probability library unless a specific defect in this minimal package requires it. Small Lean certificates are optional verification work, not prerequisites for the scientific argument.
