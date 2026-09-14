# Proposed Assumptions

Agents may append proposed assumptions here. They must not move them into `assumption_registry.md` without human approval.

## A-006 Trial-design exogeneity for simplified mixture

Status: rejected by PI direction on 2026-07-07. Do not approve A-006 for the
primary theorem statement. Use `F_{theta|X,Z}` as primary and mention
`F_{theta|Z}` only as a corollary under additional fixed-design or exogeneity
conditions.

For the omitted-context mixture lemma to use
`dF_{theta|Z}(theta|z)` rather than `dF_{theta|X,Z}(theta|x,z)`,
trial features `X_it` are fixed by design or assigned independently of
`theta_i` conditional on `Z_i`.

Rationale: Issue #4 proposes the simplified `theta | Z` mixture display, but
the direct conditional law of total probability gives a mixture over
`theta | X,Z`. The simplified display is appropriate only under a fixed-design
convention or conditional trial-design exogeneity.

## P-G1 Synthetic probability-distortion specification

Status: approved by the user on 2026-09-08 for restricted theorem development; the general theorem remains primary. See primary_theorem_specification.md sections 2–3 for the complete gain-only kernel, matched normal working random effects, shared global sensitivity, one global distortion parameter, and iid-participant fixed-T regime. Approval authorizes this restricted theorem example, not establish a RAID measurement model or general exogeneity.

## P-G2a Residual moment specialization

Status: proposed, not approved; needed only if the shortened moment formulas are used. Require E[u|Z]=0, Var(u|Z)=sigma_u²<infinity constant, and Cov(C,u|Z)=0. Then the approved equation implies mean a0+a1 Z+gamma m(Z) and variance gamma²v(Z)+sigma_u². For a varying-variance claim additionally require gamma!=0 and v nonconstant on the support of Z. No independence or Gaussianity is imposed. This does not simplify conditioning on X or imply observable separation.

## P-G2b Gaussian sufficient specialization (refines prior P-G2)

Status: proposed, not approved; optional stronger construction, not required for G1 or the mixture identity. Conditional on Z=z require C~Normal(m(z),v(z)), u~Normal(0,sigma_u²), and conditional independence. This includes P-G2a and implies the corresponding normal Theta|Z law. It says nothing further about Theta|X,Z without a joint design law. Separate normal marginals without independence or joint Gaussianity are insufficient. See primary_theorem_specification.md section 1.1 for the condition-by-condition consequences.

P-G1 remains the restricted synthetic gain-only kernel, no direct C response effect beyond Theta, matched candidate working normal effects, global tau/rho, and iid-participant fixed-T specification in sections 2–3. It supplies a DGP class, not an explicit separation witness. P-G1 is now approved in the live assumption register; P-G2a/b remain unapproved. No decision is requested again on the already approved additive equation, primary trial LOO, probability-distortion family, or delegated priors/estimator. Numerical design values and any extra compactness/tail conditions belong to a future explicit construction; they are currently proof gaps, not newly adopted assumptions.

## P-G3 Finite-design score-convergence specialization

Status: conditional theorem proposal, not adopted as a general primary assumption. For iid participants and fixed T, require W=(X,Z) to have finite support with positive probability at every support point, every true response-vector cell to have positive conditional probability, and each candidate's observable-law closure to have a unique joint population log-likelihood maximizing law. This requires uniqueness of the observable law only; parameter identifiability is not assumed. Retain the selected fixed proper priors with positive mass on interior parameter neighborhoods.

Under these precise conditions, `primary_separation_attempt_2026-09-08.md` L4–L6 derives uniform single-trial deletion concentration and the normalized conditional-score limit without compact parameter truncation. L7 and L8 give separate evidence and BIC rate limits; their optimal-value argument does not need uniqueness. The Gaussian representable finite-design boundary satisfies the uniqueness condition because the true law belongs to both candidates. The misspecified two-trial example has no uniqueness assertion. This proposal buys convergence, not a positive gap; it does not cover continuous Z, general random-design support, or standard errors for fitted LOO scores. No change to approved A-003 or rejected primary A-006 is implied.
