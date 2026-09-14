# Richer synthetic support and observable nonabsorption

Date: 2026-09-11. Status: author construction under approved P-G1 for theorem development, not a RAID protocol, new model-family approval, or positive-selection witness. Uses the unchanged gain-only kernel and all shared baseline terms. General theorem remains primary.

## Complete design

Participants are iid with Z=-1 or +1, each with probability 1/2. Every participant receives the following same ordered eight trials. W=(X,Z) therefore has exactly two support points, each with probability 1/2. There is no extra trial randomization, missingness, or other permitted design combination. The ordering supplies a static response-vector likelihood, not a learning model. All values are dimensionless. Y=1 means choosing option A; s is the coded option-side contrast. The calibration rows have zero ambiguity; they are explicitly known-probability controls within the same kernel.

| t | v_A | v_R | p_A | p_R | ambiguity width | s |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 0 | 1/2 | 0 | -1 |
| 2 | 1 | 1 | 1/2 | 1/2 | 0 | -1 |
| 3 | 1 | 1 | 1 | 1/2 | 0 | -1 |
| 4 | 1 | 1 | 0 | 1/2 | 0 | +1 |
| 5 | 1 | 1 | 1/2 | 1/2 | 0 | +1 |
| 6 | 1 | 1 | 1 | 1/2 | 0 | +1 |
| 7 | 1 | 1 | 1/4 | 1/2 | 1/4 | -1 |
| 8 | 1 | 1 | 3/4 | 1/2 | 1/2 | +1 |

Both S and K retain alpha, beta_side, tau>0, mu0, mu1, sigma>0, and the same normal working participant effect. S fixes rho=1; K estimates rho>0. Endpoint weighting is w(0;rho)=0,w(1;rho)=1. The zero-width trials are allowed by the approved A>=0 specification; they are not a claim about actual RAID stimuli. The remaining context law H(C,u|W) and true parameter values are not chosen here, so this is a complete DESIGN manifest, not a complete separation DGP.

This construction replaces the absorbed support only for a new scoped attempt. The earlier counterexample and its negative-control status remain intact. Priors, response kernel, covariates and holdout unit are unchanged. Each participant likelihood contains the entire eight-response vector; trial LOO deletes one response and retains seven.

## Observable identity: distortion cannot be absorbed

Let ell_{p,s}=logit Pr_M(Y=1 on calibration row (p,s)|Z). Because b=v_A A/2=0 on calibration rows, integrating over the participant effect has no effect on these marginal probabilities. Exactly,

    ell_{p,s}=alpha+beta s+tau[w(p;rho)-w(1/2;rho)].

Define the observable contrast

    F_s=ell_{1/2,s}-(ell_{0,s}+ell_{1,s})/2
       =tau[w(1/2;rho)-1/2].

Every S law has F_s=0. For rho>0,

    w(1/2;rho)=1/2
    iff (log 2)^rho=log 2
    iff rho=1,

since log 2 is positive and not one. Thus every finite K parameter with rho!=1 has F_s!=0. No intercept, side effect, sensitivity rescaling or latent mean/variance adjustment can remove this observable contrast. Integration cannot create a hidden absorption map because the calibration responses do not involve the latent effect.

It follows that Q_S is a STRICT subset of Q_K on this support. More strongly, such a K law is outside the closure of Q_S: its calibration probabilities are interior, so logit and F_s are continuous in a neighborhood; every convergent S sequence with that interior limit would preserve F_s=0, a contradiction. Compactness and lower semicontinuity then give strictly positive KL distance from that fixed positive K law to Q_S.

This last separation is from a K-generated law, NOT from the intended rho=1 omitted-context DGP. It proves genuine observable expressiveness, not the requested false-complex superiority for the scientific truth.

## Global identification of the four calibration parameters

These calibration marginals recover alpha,beta,tau,rho uniquely for every finite candidate parameter. For either side,

    tau=ell_{1,s}-ell_{0,s}>0,
    m=(ell_{1/2,s}-ell_{0,s})/tau=w(1/2;rho),
    rho=log(-log m)/log(log 2),
    alpha=(ell_{1/2,+1}+ell_{1/2,-1})/2,
    beta=(ell_{1/2,+1}-ell_{1/2,-1})/2.

For model-generated interior parameters, m lies in (exp(-1),1), so this inverse is well-defined and rho>0. It is smooth near every such point. This verifies an identifiable calibration block in observable coordinates. It does not yet identify mu0,mu1,sigma from the two ambiguous trials, nor establish full-family chart coverage.

At rho=1,

    partial_rho F_s = -tau (log 2) log(log 2)/2 > 0.

All S-parameter derivatives of F_s vanish identically. Thus the extra observable derivative supplied by rho is outside the simple tangent span: applying the derivative of F_s annihilates that span but not the rho direction. This is an exact added-direction certificate, not a numerical rank check. Full derivative injectivity for the remaining latent parameters remains to establish.

## What this closes, and what remains

Closed locally at author level: complete richer support; failure of full observable absorption for every rho!=1; strict observable-family inclusion; unique smooth calibration-parameter recovery; an extra observable tangent direction at rho=1.

Open: a permitted omitted-context law producing a perturbation aligned with that extra direction AFTER the complete simple fit adjusts; positive complex residual risk; the separate conditional KL advantage; remaining latent-parameter rank and global coverage; Bayesian concentration and deletion transfer. The calibration controls are correctly specified by the rho=1 truth and may penalize distortion strongly. Their inclusion therefore does not guarantee favorable KL or LOO results.

Next bounded task: use the identified calibration block to isolate the ambiguous-trial latent inverse problem for (mu0,mu1,sigma), establish or delimit its rank and uniqueness, and only then construct context perturbations. Do not vary the number of calibration trials after observing criterion results to manufacture a win. Any later design change must be recorded with its mathematical reason before fitting.
