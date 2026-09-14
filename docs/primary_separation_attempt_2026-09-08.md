# Primary separation attempt: exact obstructions and trial-deletion limits

## Claim

Attempt the G1 simple $S$ versus probability-distortion $K$ comparison under the additive no-distortion DGP, seeking $0<R_K<R_S$ and a positive trial-conditional gap at the joint KL projections. Preserve the correctly specified shared-effect boundary. The original existence target is retained; no new winning design is substituted after a failed attempt.

## Status

NOT CURRENTLY JUSTIFIED for the strict-separation and positive-selection target.
Verification: Gap found. Author derivations only; no independent review or PI acceptance.

Two exact obstructions are proved below. The correctly specified boundary has $R_S=R_K=0$. A two-trial design with a free intercept and opposite side codes has identical observable candidate families, for every context distribution in the DGP class. Thus strict separation is impossible in that design, not merely numerically elusive. These results refute a universal guarantee, not existence on every richer design.

A separate, fully stated finite-design theorem below proves exact trial-deletion score convergence under a unique observable joint optimum. It applies to the correctly specified boundary and gives zero limiting score difference there. It does not assert a positive gap for the unconstructed main example. Its additional finite-support/uniqueness conditions are labeled P-G3, not adopted as general primary assumptions.

## Assumptions

- (A1) Use precisely the G1 kernel, shared free real-valued $\alpha,\beta,\mu_0,\mu_1$, $\tau>0$, $\sigma>0$, and normal working latent law. $S$ fixes $\rho=1$ and $K$ permits every $\rho>0$. No compact parameter boxes are introduced. All covariates are retained in $W=(X,Z)$; $C$ is omitted from both candidates.
- (A2) Participants are iid; $T$ is fixed; responses are independent only conditional on their shared latent effect and observed design. All probabilities are obtained by integrating the entire response vector against the same effect.
- (A3) The boundary and second attack below are explicitly declared DGP instances of A-003, not assumptions about RAID or general design exogeneity. No loss-domain extension is made.
- (A4) For evidence and posterior statements, use the proper fixed priors of the Bayesian plan with positive density on every finite interior parameter neighborhood. Shared priors are unchanged; priors need not be invariant under the reparameterization below.
- (A5 / P-G3, conditional theorem only) $W$ has a finite support $\mathcal W$, each support probability $h_w>0$, and every true response-vector probability $p_w(y)>0$. The closure of each candidate's observable-law image has a unique maximizer of the population log likelihood. If uniqueness fails, the single-limit theorem is not asserted. This condition concerns laws, not latent-parameter identifiability. A4 implies prior mass near that optimum as proved below.

The user authorized this attempt on the exact proposed laws, boundary cases and failure records. These conditional analyses do not enter P-G1/P-G2/P-G3 as approved assumptions in the live register.

## Notation

Set $b_t=v_{A,t}A_t/2$ and $d_t(r)=v_{A,t}w(p_{A,t};r)-v_{R,t}w(p_{R,t};r)$. With $E\sim N(0,1)$ the candidate logit is

$$\eta_t(r,E)=\alpha+\beta s_t+\tau d_t(r)-\tau b_t(\mu_0+\mu_1Z+\sigma E).$$

$q_M(y\mid W;\phi)$ is the integrated participant-vector law; $q_{M,-t}$ its response-only marginal. $R_M$ is the infimum of $E_W\operatorname{KL}(p_W\Vert q_M)$ over its original parameter space; using an infimum avoids claiming a finite optimizer where none is established. In the finite-design theorem $q_M^*$ is the unique optimal law in the closure, which need not have a finite parameter representative. Write $\ell_M^*=E\log q_M^*(Y\mid W)$.

## Verification Target and Bottleneck

- Verification target: a concrete $H$, design and joint fitted laws with $0<R_K<R_S$; separately, $\Delta_{\rm cond}>0$ at those laws.
- Bottleneck: the first Gaussian route is contained in $S$; the finite-support two-trial route has $\mathcal Q_S=\mathcal Q_K$. No optimizer can create a gap between identical families.
- Resolution path: record these failures, preserve all nuisance terms, and require a design-identifiability analysis before a further existence construction. Finite-support score convergence can be derived independently without claiming a positive sign.

## Anchors and Borrowing

Paper-self-contained. No quadratic/LOPO benchmark lemma or external posterior-concentration theorem is invoked.

Implicit machinery disclosure: elementary Gaussian convolution, dominated convergence for bounded Bernoulli integrands, compactness in a finite-dimensional probability simplex, the inequality $\log x\leq x-1$, Bayes' rule, and Chebyshev's inequality. The only sampling limit used is proved via finite cell counts. We derive posterior concentration, uniform response-deletion stability and the score limit locally. No Laplace approximation, Bernstein–von Mises result, nonparametric mixture-identifiability theorem or empirical-process theorem is implicit.

## Proof Strategy

First compare the latent distributions in the representable boundary. Then compare logits pointwise in the shared normal draw to test exact observable containment before optimization. For score convergence, work in the finite-dimensional space of observable laws, suppress near-zero cells by their likelihood cost, and use the resulting compact positive-cell set to prove concentration. Control all single-trial deletions by first removing the participant for an intermediate posterior calculation, then restoring exactly their retained responses. The scored holdout remains one response throughout.

## Dependency Map

1. L1 (representability) closes O1; L2 (design absorption) closes O2 and blocks the attempted strict gap O9.
2. L3 (exact deletion) closes O3 without requiring separation.
3. L4 (finite-law likelihood bounds) closes O4; L5 (posterior and deletion stability) closes O5 using L3–L4.
4. L6 (trial score convergence) closes O6 from L5 and a participant-cell LLN.
5. L7 (BF rate) and L8 (BIC criterion) close O7 and O8 independently of O6's conditional gap.
6. No positive-selection conclusion is derived because O9 is blocked.

## Obligation Ledger

- O1 Gaussian shared-effect boundary — CLOSED-LOCAL. Closed at: L1, equality of mixing laws and KL nonnegativity.
- O2 Distortion absorption on the attempted design — CLOSED-LOCAL. Closed at: L2, explicit parameter map and reverse nesting.
- O3 Exact response deletion — CLOSED-LOCAL. Closed at: L3, joint deletion posterior integration and evidence ratio.
- O4 Finite-law likelihood localization and prior support — CLOSED-LOCAL. Closed at: L4, small-cell exclusion, compact uniform bound and neighborhood lower bound.
- O5 Uniform deletion posterior concentration — CLOSED-LOCAL. Closed at: L5, uniform cluster-removal bound and retained-response tilt.
- O6 Cluster trial-score limit — CLOSED-LOCAL. Closed at: L6, uniform log-prediction convergence and cell-count variance bound.
- O7 Separate evidence rate — CLOSED-LOCAL. Closed at: L7, upper/lower evidence sandwich.
- O8 Separate BIC criterion statement — CLOSED-LOCAL. Closed at: L8, likelihood supremum identity and normalized criterion limit.
- O9 Strict joint and trial-conditional separation — BLOCKED.
  - statement: Supply a concrete G1 DGP/design with $0<R_K<R_S$ and $\Delta_{\rm cond}>0$ at the joint projections.
  - bridge attempted: First use omitted Gaussian context with affine mean and constant variance; then use a finite-support context with varying conditional variance and the two-trial side-balanced design below.
  - failure reason: L1 gives exact representation in S for the first route. L2 gives identical S/K observable families for the second route, irrespective of the non-Gaussian context or variance variation.
  - alternative considered: A local distortion perturbation on the same two-trial design has a score in the nuisance span and cannot open a gap. A richer design is not selected here after failure; its observable rank and noncontainment must be checked before another construction. Dropping the intercept, side term or shared effects would change the specified comparison and is not used.
  - isolated as: Conjecture C1, existence of a richer-design witness for the original exact families; not a universal statement.

## Proof

### L1. Correctly specified shared-effect boundary

Let $Z$ take $-1,1$ with equal probability, use a common deterministic finite trial design, and draw independently across participants

$$C\mid Z=z\sim N(1+z/2,1),\qquad u\mid Z=z\sim N(0,1/4),\qquad C\perp u\mid Z.$$

Set $a_0=0$, $a_1=1/4$, $\gamma=1$, and use the true kernel with $(\alpha^*,\beta^*,\tau^*,\rho^*)=(0,0,1,1)$. Gaussian convolution, or multiplication of characteristic functions, gives

$$\Theta\mid X,Z=z\sim N(1+3z/4,5/4).$$

This equality conditions on the full $X,Z$; the reduction here follows from this explicitly common design and is not general A-006. In $S$ choose $(\mu_0,\mu_1,\sigma)=(1,3/4,\sqrt{5}/2)$ and match the true kernel constants. The integrands and measures in the participant-vector law agree, so $q_S=p$ in every response cell. Taking $\rho=1$ in $K$ gives $q_K=p$.

For positive probability vectors, $-\log x\geq 1-x$ implies $\operatorname{KL}(p\Vert q)\geq\sum_y(p_y-q_y)=0$, with equality only for $p=q$. Consequently $R_S=R_K=0$, and their optimal observable laws and all trial conditionals coincide. Context has nonzero structural coefficient and nonzero variance; its omission has been absorbed by correctly specified shared effects. This boundary does not establish harmlessness for every context law.

### L2. Exact design absorption and the failed finite-support attack

A sufficient pointwise absorption condition on the entire design support is that, for each fixed $r>0$, constants $c>0,h_0,h_s,h_b,h_z$ exist with

$$d_t(r)=c\,d_t(1)+h_0+h_s s_t+h_b b_t+h_z b_t Z.$$

They must work simultaneously for every participant design and retained $Z$, not separately for each participant. Given a $K$ parameter, define an $S$ parameter by

$$\tau_S=c\tau_K,\quad \alpha_S=\alpha_K+\tau_K h_0,\quad \beta_S=\beta_K+\tau_K h_s,$$
$$\mu_{0S}=(\mu_{0K}-h_b)/c,\quad \mu_{1S}=(\mu_{1K}-h_z)/c,\quad \sigma_S=\sigma_K/c.$$

Substitution into the displayed logit cancels $c$ in the random-effect term and yields $\eta_{S,t}(E)=\eta_{K,t}(E)$ for every $E,t,W$. All transformed parameters remain in their stipulated full supports. Integrating products of Bernoulli factors preserves equality. Conversely every $S$ law is a $K$ law at $r=1$. Thus the absorption condition for every $r$ implies equality of the observable families. Arbitrary compact boxes need not preserve the transformation; no such boxes are used.

For a concrete attempt, set $T=2$ and use this common gain-only design:

| Trial | $v_A$ | $v_R$ | $p_A$ | $p_R$ | $A$ | $s$ |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1/4 | 1/2 | 1/4 | -1 |
| 2 | 1 | 1 | 3/4 | 1/2 | 1/2 | +1 |

Let $\delta_t(r)=d_t(r)-d_t(1)$. For every $r$, take $c=1$, $h_b=h_z=0$,

$$h_0=(\delta_1+\delta_2)/2,\qquad h_s=(\delta_2-\delta_1)/2.$$

The absorption condition holds identically. This is not a numerical rank guess: $(1,1)$ and $(-1,1)$ span all two-trial offset vectors. All the probabilities are interior, ambiguity widths are positive, and nuisance terms remain matched.

To test a route beyond L1 without selecting parameters to favor $K$, let $Z=\pm1$ equiprobably, let $u=0$, $a_0=a_1=0$, $\gamma=1$, and draw $C=\pm1$ equiprobably when $Z=-1$ and $C=\pm2$ equiprobably when $Z=1$. Use $(\alpha^*,\beta^*,\tau^*,\rho^*)=(0,0,1,1)$. This completely specifies $H$ and the DGP: $m(z)=0$, $v(-1)=1$, $v(1)=4$, and $\Theta=C$. It satisfies the residual moment package with $\sigma_u^2=0$ and exhibits latent variance heterogeneity. Nevertheless $\mathcal Q_S=\mathcal Q_K$, hence their KL infima are equal for this DGP and indeed any DGP on this design. No claim that both are false is needed or made; finite trial laws might admit an unexpected representation.

The derivative route also fails: $\partial_r d(r)$ has only two coordinates and lies in the same intercept/side span. The extra distortion direction gives no new observable tangent direction. The experiment ends at this obstruction; no repeated fitting, design tuning or nuisance-term removal is performed.

### L3. Exact single-trial deletion under the original hierarchical law

For fixed $\phi$ and participant $i$, the posterior effect law after retaining their other responses is

$$dG_{i,-t}(\theta\mid\phi)=\frac{\prod_{s\ne t}f_M(y_{is}\mid\theta,x_{is};\phi)\,dG_M(\theta\mid W_i;\phi)}{q_{M,-t}(y_{i,-t}\mid W_i;\phi)}.$$

The denominator is the integral of the numerator and is positive. Its predictive integral is exactly $q_M(y_i\mid W_i;\phi)/q_{M,-t}(y_{i,-t}\mid W_i;\phi)$. Global parameters have the response-deleted posterior

$$\Pi_{-it}(d\phi)=\frac{q_{M,-t}(y_{i,-t}\mid W_i;\phi)\prod_{k\ne i}q_M(y_k\mid W_k;\phi)\Pi(d\phi)}{m_M(D_{-it}\mid W_{1:n})}.$$

Tonelli applies to the nonnegative, bounded likelihood factors and the proper priors. Integrating first over the effect and then global parameters gives

$$p_M(y_{it}\mid D_{-it},W_{1:n})=\int\frac{q_M(y_i\mid W_i;\phi)}{q_{M,-t}(y_{i,-t}\mid W_i;\phi)}\Pi_{-it}(d\phi)=\frac{m_M(D\mid W_{1:n})}{m_M(D_{-it}\mid W_{1:n})}.$$

The effect is learned from $y_{i,-t}$; it is not drawn afresh without that information or frozen at its full-data estimate. All covariates and priors are identical in the numerator and denominator. Summing the logs gives G1's exact trial ELPD. The identity is valid for finite $n$ even in the failed separation example and does not imply predictive preference.

### L4. Finite-design likelihood bounds without compact parameter boxes

Assume A5 for this lemma and the following lemmas. Index the $J=|\mathcal W|2^T$ cells by $(w,y)$. Let $r_{wy}=h_wp_w(y)>0$, $\widehat r_{wy}=n^{-1}\sum_i1\{(W_i,Y_i)=(w,y)\}$, and $r_{\min}=\min r_{wy}$. For any $a>0$, independence of participants and the variance bound for indicators give

$$P\{\max_{wy}|\widehat r_{wy}-r_{wy}|>a\}\leq J/(4na^2).$$

For a candidate law vector $q=(q_w(y))$ define $\ell(q)=\sum r_{wy}\log q_w(y)$ and $\ell_n(q)=\sum\widehat r_{wy}\log q_w(y)$. Let $\mathcal A$ be its image and $\overline{\mathcal A}$ its closure in the product of probability simplexes. Every finite candidate parameter gives strictly positive cells. Fix one such $q_0$. The population objective is upper semicontinuous on this compact closure, with value $-\infty$ if any cell is zero; hence a maximum exists and every maximizer has positive cells. This can also be seen from the following explicit bound.

If some $q_w(y)<\epsilon$, then, on the event $\widehat r_{wy}\geq r_{\min}/2$ for all cells,

$$\ell_n(q)\leq (r_{\min}/2)\log\epsilon,$$

because all other logarithms are nonpositive. Choose $\epsilon>0$ small enough that this bound is less than $\ell(q_0)-2$, and that an optimum's cells exceed $2\epsilon$. Such a choice is possible since $\ell(q_0)$ is finite and the optimum is positive. This excludes all small-cell laws from empirical near-maximizers with probability tending to one. On the remaining compact set $B_\epsilon=\{q:q_w(y)\geq\epsilon\}$,

$$\sup_{B_\epsilon}|\ell_n(q)-\ell(q)|\leq J|\log\epsilon|\max_{wy}|\widehat r_{wy}-r_{wy}|\ \longrightarrow_p 0.$$

These two bounds prove $\sup_{\mathcal A}\ell_n\to_p\ell^*$. For a unique optimum $q^*$, compactness of $\overline{\mathcal A}\cap B_\epsilon$ and continuity give a strict population gap outside every fixed sup-norm neighborhood of $q^*$. The small-cell bound supplies a gap on its complement. Thus for every neighborhood $U$ there is a $g>0$ such that, on events with probability tending to one,

$$\sup_{q\notin U}\ell_n(q)\leq\ell^*-g.$$

For a small enough neighborhood $V$ of $q^*$, positive-cell continuity gives $\inf_{q\in V}\ell_n(q)\geq\ell^*-g/4$ on those events. The prior mass $\Pi(V)>0$: a positive optimum in the closure is approximated by some finite interior parameter law in $V$; continuity of the normal-integrated kernel follows by bounded dominated convergence using its standard-normal representation; an open parameter neighborhood maps into $V$ and has positive prior mass by A4. This argument also handles optima attainable only as parameter limits. No parameter uniqueness or prior tail truncation is needed.

### L5. Posterior and uniform response-deletion stability

Integrating the L4 bounds shows

$$\Pi(q\notin U\mid D)\leq\Pi(V)^{-1}\exp(-3ng/4)$$

on events with probability tending to one. To control every trial deletion, form the intermediate posterior $\Pi_{-i}$ using the $n-1$ complete participants other than $i$. Its empirical cell proportions differ from full proportions by at most $1/(n-1)$ in every cell, uniformly over $i$. Therefore all L4 bounds hold simultaneously for these $n$ intermediate posteriors, with reduced positive gap and $n-1$ replacing $n$. No union bound over $n$ independent bad events is asserted: a single full-sample frequency event controls all deletions. It follows that

$$\max_i\Pi_{-i}(q\notin U)\longrightarrow_p0.$$

Restore participant $i$'s retained responses. The response-deleted posterior is exactly the tilt of $\Pi_{-i}$ by $q_{-t}(y_{i,-t}\mid W_i)$, which is at most one. Let $a_* =\min_{w,y}q_w^*(y)>0$. On a sufficiently small neighborhood $V_0$ of $q^*$, every joint cell is at least $a_*/2$, so every required marginal is at least $a_*/2$. The normalizing constant of the tilt is at least $(a_*/2)\Pi_{-i}(V_0)$. Hence

$$\Pi_{-it}(U^c)\leq\frac{\Pi_{-i}(U^c)}{(a_*/2)\Pi_{-i}(V_0)}.$$

Both concentration statements hold uniformly in $i,t$, proving uniform response-deleted posterior concentration. The prediction functional $q_w(y)/q_{w,-t}(y_{-t})$ lies in $[0,1]$ and is continuous in a neighborhood of $q^*$, with denominator bounded away from zero there. Splitting its posterior integral between that neighborhood and its complement proves

$$\max_{i,t}\left|p_M(y_{it}\mid D_{-it},W_{1:n})-\frac{q_M^*(y_i\mid W_i)}{q_{M,-t}^*(y_{i,-t}\mid W_i)}\right|\longrightarrow_p0.$$

The finitely many limiting conditional probabilities are at least $a_*$ because their numerator is at least $a_*$ and denominator at most one. Thus, with probability tending to one, all predictions are at least $a_*/2$. On this event $\log$ is Lipschitz with constant $2/a_*$. This proves uniform convergence of the corresponding log predictions; an unbounded full parameter space causes no omitted log-integrability step here.

### L6. Trial-score convergence with participant dependence

For each candidate let

$$H_M(w,y)=\frac1T\sum_{t=1}^T\log\frac{q_M^*(y\mid w)}{q_{M,-t}^*(y_{-t}\mid w)}.$$

It is a bounded function on the finite participant-cell space. L5 bounds the discrepancy between $\mathrm{ELPD}_M/(nT)$ and $n^{-1}\sum_iH_M(W_i,Y_i)$ by a random quantity tending to zero in probability. Moreover the latter average equals $\sum\widehat r_{wy}H_M(w,y)$; the L4 cell-count bound proves convergence to $E H_M(W,Y)$, without treating trials as independent. Consequently

$$\frac{\mathrm{ELPD}_K-\mathrm{ELPD}_S}{nT}\longrightarrow_p\Delta_{\rm cond},\qquad
\frac{\mathrm{LOOIC}_K-\mathrm{LOOIC}_S}{nT}\longrightarrow_p-2\Delta_{\rm cond},$$

where

$$\Delta_{\rm cond}=\frac1T\sum_t E\log\frac{q_K^*(Y\mid W)/q_{K,-t}^*(Y_{-t}\mid W)}{q_S^*(Y\mid W)/q_{S,-t}^*(Y_{-t}\mid W)}.$$

The true conditional log density cancels, giving the conditional KL-risk difference in G1. Its chain-rule relation to joint and marginal KL follows by writing each joint density as conditional times marginal and summing under $p$. No sign follows from this identity. If $\Delta_{\rm cond}>0$ is separately proved, convergence implies probability tending to one of a positive ELPD difference. Without that strict inequality it does not.

In L1 both unique optimal observable laws equal $p$, so A5's uniqueness is verified, $\Delta_{\rm cond}=0$, and the normalized trial-score difference tends to zero under the stated priors. This is a genuine boundary score limit, not a statement that finite-sample scores are equal. For L2, equal families alone need not imply a unique misspecified optimum; if uniqueness holds the limits coincide, and if not the above single-limit theorem is withheld.

For the fixed limiting participant score $H_K-H_S$, its average has variance $\operatorname{Var}(H_K-H_S)/n$; that variance includes all within-person cross-trial covariances. The actual fitted LOO contributions also share training data. We prove no CLT or standard-error consistency for them: a fitting-effect expansion or separately justified cluster resampling argument is still required. Thus a naive independent-trial standard error is unsupported.

### L7. Separate BF rate

L4 gives $m_M(D)\leq\exp(n\sup_q\ell_n(q))$. For every $\delta>0$ choose a fixed positive-prior neighborhood $V_\delta$ of $q_M^*$ on which $\ell(q)>\ell_M^*-\delta$ and all cells are bounded away from zero. Uniform convergence there yields

$$m_M(D)\geq\Pi(V_\delta)\exp\{n(\ell_M^*-2\delta)\}$$

on events with probability tending to one. Taking logs, dividing by $n$, and then making $\delta$ arbitrarily small proves

$$n^{-1}\log m_M(D)\longrightarrow_p\ell_M^*,\qquad n^{-1}\log\mathrm{BF}_{KS}\longrightarrow_p\ell_K^*-\ell_S^*=\Delta_{\rm joint}.$$

This is a direct evidence-integral argument with normalized proper priors. It does not use L6 or its conditional gap. In L1 the BF rate is zero; in L2 equality of families also gives zero rate (the likelihood/evidence argument does not need uniqueness if its optimum set is used). A zero exponential rate leaves polynomial, bounded, or other subexponential preferences undetermined. The parameter map in L2 need not preserve the induced prior on observable laws, so family equality does not imply $\mathrm{BF}=1$. No numerical bridge estimator or ordinary BIC approximation is invoked.

### L8. Separate BIC criterion

Define the supremum-based criterion $\mathrm{BIC}_M=-2\sup_\phi\log L_M(\phi)+k_M\log n$ for fixed declared counts of global parameters. If a maximum is attained, this is the usual fitted-likelihood expression. L4 alone gives

$$n^{-1}(\mathrm{BIC}_K-\mathrm{BIC}_S)\longrightarrow_p-2\Delta_{\rm joint}.$$

In L2 the likelihood suprema are exactly equal for every dataset by the pointwise family transformation. Using nominal counts $k_K-k_S=1$ therefore gives $\mathrm{BIC}_K-\mathrm{BIC}_S=\log n$. This is algebra for a nominal criterion, not a valid regular evidence approximation: $\rho$ is not identifiable on this design. With equal observable dimension the same fitted-law criterion would tie. In L1 without the L2 design obstruction, a zero normalized difference does not settle the lower-order comparison. Nothing here supplies an unproved Hessian, effective dimension or Laplace penalty.

## Corrections or Missing Assumptions

The new conditional score theorem P-G3 restricts design/covariates to finite support and requires a unique observable optimum. It does not require compact parameter boxes, Gaussian truth, or a positive gap. These are conditional mathematical results for review; they are not a silent revision of A-003 or A-006. L1 explicitly satisfies P-G3; the misspecified L2 example has no uniqueness claim. The strict main target would additionally require observable noncontainment, positive KL risks and a separately positive conditional gap. Nonconstant latent variance is insufficient.

## Verification Checks

- Localization before expansion: no Taylor expansion; the likelihood proof excludes small cells before its uniform log bound.
- Norm/mode: sup-norm law and prediction convergence in probability; no almost-sure, CLT or rate strengthening.
- Good events: Chebyshev controls one finite-cell frequency event; uniform deletion uses deterministic $1/(n-1)$ perturbations on that event.
- Rate leakage: only normalized limits claimed; no $O_p(1)$ or logarithmic evidence remainder.
- Quantifiers: family equality is restricted to a design satisfying L2 for all $r$; the positive-gap existence problem remains open elsewhere.
- Citation identity and applicability: no source-specific result imported; graduate-core tools and their conditions disclosed locally.
- Negligibility closure: uniform log-prediction discrepancy bounds the normalized ELPD discrepancy directly.
- Boundary/singularity: full parameter supports preserved; variance-zero DGP in the second attack is permitted by its moments; fitted variances stay positive. Nonidentifiable distortion invalidates regular-BIC interpretation.
- Numerical checks are diagnostics of the algebra, not certificates of a positive gap or proof acceptance.

## Blockage Record

O9 remains blocked. The first bridge failed because the simple model contains the Gaussian context mixture. The second failed for every context law on its design because distortion is absorbed by the shared intercept and side term. A local perturbation on the same design has the same obstruction. No sample size, optimizer, prior scale, context rescaling or Monte Carlo repetition can turn those population family equalities into strict KL separation.

The next dependency is a structural design audit on the full support: determine whether $d(r)$ can be absorbed by $d(1),1,s,b,bZ$ with a positive scaling of sensitivity. Failure of this sufficient absorption test is necessary to escape this particular obstruction, but is not sufficient for observable mixture separation or identifiability. A new concrete design/context proposal must retain the G1 nuisance terms, establish projection behavior and both KL gaps, and receive review before any positive result is promoted. General random-design/continuous-Z score limits and fitted-score uncertainty remain outside P-G3. The original existence target is not disproved by these counterexamples, and neither benchmark results nor conditional lemmas close O9.
