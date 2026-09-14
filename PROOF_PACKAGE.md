# Observable false-complexity selection: a participant-level proof package

Date: 2026-09-05. Author: LLM working draft; independent adversarial review pending.
Scope: a constructive stochastic-choice example, not a theorem about every ambiguity model or the final RAID model pair. Supersedes the Gaussian-first route for this constructive track.

## Claim

There is a linear contextual utility mechanism and two context-omitting models, a one-parameter linear utility model $S$ and a two-parameter quadratic utility model $K$, such that **both fitted joint distributions are false**, but

$$0<R_K<R_S,\qquad \Delta=R_S-R_K>0.$$

For $n$ independent participants, each contributing the same two trials, BIC, the Bayes factor with the proper priors specified below, and exact leave-one-participant-out information criterion each select $K$ over $S$ with probability tending to one as $n\to\infty$. The conclusion concerns the context-omitting candidates. It does not say either beats the correct contextual distribution in population KL risk.

## Status

PROVABLE AS STATED for the explicit construction and priors below.
Verification: Verified by the local derivations below; author self-check only, not independent acceptance, formal verification, or general empirical validation.

## Assumptions

- **(A1 / A-007)** Participants are independent and identically distributed. Each receives two deterministic utility contrasts $x_1=1,x_2=2$. Context $C_i\sim\operatorname{Bernoulli}(1/2)$ is shared across the two trials. Conditional on $C_i$, responses are independent, with $P(Y_{it}=1\mid C_i)=\sigma(C_i\log(3)x_t)$, where $\sigma(u)=(1+e^{-u})^{-1}$. Thus the individual utility difference is linear in $x$; context changes its sensitivity. There is no quadratic cognitive mechanism.
- **(A2 / A-008)** The observed unit is the whole response vector $W_i=(Y_{i1},Y_{i2})\in\mathcal W=\{0,1\}^2$. Both candidates omit $C_i$ and assert the normalized participant likelihoods
  $$q_S(w;b)=\prod_{t=1}^2\sigma(bx_t)^{y_t}[1-\sigma(bx_t)]^{1-y_t},\quad b\in[-1,1],$$
  $$q_K(w;b,d)=\prod_{t=1}^2\sigma(bx_t+dx_t^2)^{y_t}[1-\sigma(bx_t+dx_t^2)]^{1-y_t},\quad(b,d)\in[-1,1]^2.$$
  All maxima are global over these compact boxes. The shared restriction of conditional independence in the candidates is part of their misspecification; it is not assumed true of the marginal data.
- **(A3 / A-009)** For BF and Bayesian LOO, use independent uniform priors on the respective boxes, with densities $2^{-k_j}$ and $k_S=1,k_K=2$. The priors are proper, fixed in $n$, and place positive mass around the interior population optima. No prior on model labels is required for the BF comparison itself.
- **(A4 / A-010)** The predictive target is the full response pair from a **new participant** under the same design and context population. LOO deletes both responses of participant $i$ before predicting their pair. The asymptotic sample size $n$ counts participants, with two trials fixed; it is not a growing-trials or growing-dimension result.

These constructive choices were selected under the user's 2026-09-05 instruction to select an explicit model pair, prove separation and write the criterion corollaries. They do not approve Gaussian assumptions or select a final RAID model.

## Notation

$P$ denotes the true marginal distribution on $\mathcal W$; $H(P)=-\sum_wP(w)\log P(w)$. Let

$$F_j(\theta)=\sum_wP(w)\log q_j(w;\theta),\quad
\theta_j^*=\arg\max_{\Theta_j}F_j(\theta),\quad
R_j=\operatorname{KL}(P\Vert q_j(\cdot;\theta_j^*)).$$

For observed data, $\ell_{j,n}(\theta)=\sum_{i=1}^n\log q_j(W_i;\theta)$, $\widehat\theta_{j,n}=\arg\max\ell_{j,n}$, and $D_n=\ell_{K,n}(\widehat\theta_{K,n})-\ell_{S,n}(\widehat\theta_{S,n})$. All logarithms are natural. All stochastic limits below are **in probability**.

## Verification Target and Bottleneck

- Verification target: compute a strict participant-level KL gap and show that normalized fitted likelihood, marginal likelihood and deleted-participant predictive score recover their respective population log scores.
- Bottleneck resolved here: a trial marginal identity alone does not establish joint KL separation or justify deletion-based Bayesian prediction. The four-state participant distribution makes both steps explicit.
- Resolution path: exact cell probabilities; a KL decomposition; a finite-state uniform convergence bound; deterministic curvature bounds; a uniform deletion posterior bound. No general misspecified Bernstein–von Mises or singular-learning theorem is invoked.

## Anchors and Borrowing

Relation to literature: **paper-self-contained**, using elementary finite probability and finite-dimensional analysis. The likelihood/KL connection and distinction between evidence and predictive criteria are established statistical ideas; no novelty claim is made for those tools.

Background only: [Vehtari, Gelman & Gabry, LOO and WAIC](https://arxiv.org/abs/1507.04544); [Chatterjee, Maitra & Bhattacharya, Bayes-factor convergence](https://arxiv.org/abs/1703.04956); [Vehtari, prediction-unit discussion](https://avehtari.github.io/modelselection/CV-FAQ.html). These sources are not load-bearing black-box steps.

Implicit Machinery Disclosure: core facts used are conditional expectation, $\log u\le u-1$, Markov/Chebyshev and the union bound, compactness/continuity, finite-dimensional Taylor's formula, eigenvalue bounds and Gaussian integration. All uniform convergence, estimator localization, likelihood integral orders and deletion stability are derived here. None of the proof assumes trial independence after marginalizing context.

## Proof Strategy

Compute the true pair law. Show that the quadratic model matches both marginal choice probabilities, while the linear model cannot, and that shared context leaves dependence neither candidate can represent. Then analyze the three criteria separately on participant likelihoods.

## Dependency Map

1. L1 mixture identity and A1 determine the four observable cells (O1).
2. T1 strict joint KL separation uses O1–O3.
3. L2 uniform objective convergence and interior localization use O4–O5.
4. C1 BIC uses T1 and L2 (O6).
5. C2 BF uses T1, L2 and quadratic integral bounds (O7).
6. L3 uniform deletion concentration and C3 LOO use O4, O5, O8–O9.
7. C4 simultaneous selection follows from C1–C3 by the union bound (O10).

## Obligation Ledger

- O1 participant marginalization — CLOSED-LOCAL.
  - Closed at: L1 and T1 Step 1, four-state probabilities and covariance.
- O2 optima, interiority and identifiability — CLOSED-LOCAL.
  - Closed at: T1 Step 2 and L2 Step 2, exact logits, root bracket and positive-definite Gram matrices.
- O3 strictly positive observable KL gap — CLOSED-LOCAL.
  - Closed at: T1 Steps 3–4, mutual-information decomposition and incompatible marginal logits.
- O4 finite-state uniform convergence — CLOSED-LOCAL.
  - Closed at: L2 Step 1, Chebyshev/union bound with explicit constants.
- O5 estimator localization — CLOSED-LOCAL.
  - Closed at: L2 Step 3, strong-concavity distance bound and interior margin.
- O6 BIC comparison — CLOSED-LOCAL.
  - Closed at: C1, exact algebra and normalized likelihood limit.
- O7 marginal-likelihood expansion under misspecification — CLOSED-LOCAL.
  - Closed at: C2, upper Gaussian integral and lower shrinking-ball integral on the localized event.
- O8 uniform concentration after deleting a participant — CLOSED-LOCAL.
  - Closed at: L3, empirical-frequency deletion bound and exponential posterior ratio.
- O9 logarithmic predictive-score convergence — CLOSED-LOCAL.
  - Closed at: C3, uniform continuity and positive probability floor, followed by empirical averaging.
- O10 joint probability of three selections — CLOSED-LOCAL.
  - Closed at: C4, finite union bound.

## Proof

### L1. Mixture identity (general finite-response statement)

Suppose the indicated regular conditional law exists and the measurable choice kernel satisfies $P(Y=y\mid X,Z,\Theta)=p(y\mid X,\Theta)$ almost surely. For each finite outcome $y$,

$$P(Y=y\mid X,Z)=E[E[1_{\{Y=y\}}\mid X,Z,\Theta]\mid X,Z]
=\int p(y\mid X,\theta)\,dF_{\Theta\mid X,Z}(\theta).$$

This is the tower property; bounded probabilities ensure integrability. A common null set works for all outcomes since there are finitely many. Under $\Theta\perp X\mid Z$, one may replace the mixing law by $F_{\Theta\mid Z}$; this is a sufficient condition, not a necessary condition for equality of a particular integrated response kernel. For a participant with responses conditionally independent given **both the shared latent parameter and retained covariates** (A-011), and fixed common design, marginalize the **product** of trial kernels over the shared parameter. Multiplying separately marginalized trial kernels is generally different. This proves L1.

### T1. Strict observable joint KL separation

**Step 1: the observed law.** In context zero both success probabilities are $1/2$; in context one they are $3/4$ and $9/10$. Marginalizing the product gives

| $w=(y_1,y_2)$ | $(0,0)$ | $(1,0)$ | $(0,1)$ | $(1,1)$ |
|---|---:|---:|---:|---:|
| $P(w)$ | $11/80$ | $13/80$ | $19/80$ | $37/80$ |

Hence $p_1=P(Y_1=1)=5/8$, $p_2=P(Y_2=1)=7/10$, and

$$\operatorname{Cov}(Y_1,Y_2)=37/80-(5/8)(7/10)=1/40>0.$$

All four cells have positive probability. Every candidate $q_j$ is a product distribution, so neither family contains $P$.

**Step 2: the population optima.** Set $a_1=\log(5/3)$ and $a_2=\log(7/3)$. The complex model matches both marginals at

$$b_K^*=2a_1-a_2/2,\qquad d_K^*=a_2/2-a_1.$$

These parameters lie strictly in $(-1,1)^2$. Indeed $d_K^*=-(1/2)\log(25/21)$ is negative with magnitude less than $2/21<1$, using $\log(1+u)<u$. Also $b_K^*=\log(25/(3\sqrt{21}))>0$ and $25/(3\sqrt{21})<25/12<5/2<e$, so $b_K^*<1$. The two-by-two predictor matrix with rows $(1,1)$ and $(2,4)$ is invertible.

For $S$, differentiation gives

$$F'_S(b)=p_1-\sigma(b)+2[p_2-\sigma(2b)],\quad
F''_S(b)=-\sigma'(b)-4\sigma'(2b)<0.$$

At $b=a_2/2$, the second bracket is zero and the first is positive; at $b=a_1$, the first bracket is zero and the second is negative. The strict signs follow from $2a_1>a_2$, equivalent to $25>21$. Thus the unique optimum $b_S^*$ lies in $(a_2/2,a_1)\subset(0,1)$.

**Step 3: risk decomposition.** Let $P_t$ be the Bernoulli marginal with success probability $p_t$, and let $r_t$ be any two candidate probabilities. Directly expanding the finite sum yields

$$\operatorname{KL}(P\Vert \operatorname{Bern}(r_1)\otimes\operatorname{Bern}(r_2))
=I_P(Y_1;Y_2)+\sum_{t=1}^2\operatorname{KL}(\operatorname{Bern}(p_t)\Vert\operatorname{Bern}(r_t)),$$

where $I_P(Y_1;Y_2)=\operatorname{KL}(P\Vert P_1\otimes P_2)$. For positive probability vectors, $\log u\le u-1$ proves KL nonnegativity, with equality only when the vectors coincide. Step 1 therefore gives $I_P(Y_1;Y_2)>0$.

**Step 4: strict separation.** The quadratic optimum matches both marginals, so $R_K=I_P(Y_1;Y_2)>0$. No slope $b$ can match both marginals in $S$: matching the first requires $b=a_1$, and the second requires $2b=a_2$, a contradiction. Its attained optimum consequently satisfies

$$\Delta=R_S-R_K=\sum_{t=1}^2\operatorname{KL}(\operatorname{Bern}(p_t)\Vert\operatorname{Bern}(\sigma(b_S^*x_t)))>0.$$

Attainment also follows from continuity on the compact box, so this is separation of the **infima**, not merely of selected parameter values. The cognitive curvature $d_K^*\ne0$ is absent from every individual contextual kernel. Both joint candidate distributions remain false. This proves T1.

### L2. Uniform convergence, curvature and localization

**Step 1: uniform convergence from four cell frequencies.** On either parameter box every trial linear predictor has magnitude at most $6$. Let $\delta=\sigma(-6)^2>0$ and $M=-\log\delta$. Then $q_j(w;\theta)\ge\delta$ and $|\log q_j(w;\theta)|\le M$ for all $j,w,\theta$. If $f_n(w)$ is the empirical frequency, then

$$U_n:=\max_j\sup_{\theta\in\Theta_j}|\ell_{j,n}(\theta)/n-F_j(\theta)|
\le M\sum_{w\in\mathcal W}|f_n(w)-P(w)|.$$

Independence of **participants** gives $\operatorname{Var}(f_n(w))\le1/(4n)$. Chebyshev and a union bound over the four cells imply, for every $u>0$,

$$P(U_n>u)\le\min\{1,16M^2/(nu^2)\}.$$

Thus $U_n\to_p0$. The elementary maximum inequality gives $|\max_\theta\ell_{j,n}(\theta)/n-\max_\theta F_j(\theta)|\le U_n$, so

$$D_n/n\to_p F_K(\theta_K^*)-F_S(\theta_S^*)=\Delta.$$

**Step 2: curvature bounds.** Write predictor vectors $v_{S,t}=x_t$ and $v_{K,t}=(x_t,x_t^2)^\mathsf T$. For either the empirical normalized log likelihood or $F_j$,

$$-\nabla^2F_j(\theta)=-\nabla^2[\ell_{j,n}(\theta)/n]
=\sum_{t=1}^2\sigma'(v_{j,t}^\mathsf T\theta)v_{j,t}v_{j,t}^\mathsf T.$$

The equality holds because this logistic Hessian is independent of responses. The Gram matrices are $G_S=(5)$ and $G_K=\begin{pmatrix}5&9\\9&17\end{pmatrix}$; the latter has determinant $4$ and positive trace. On the boxes, $\sigma'(u)\ge\sigma'(6)>0$ and $\sigma'(u)\le1/4$. Hence fixed constants

$$\lambda_j=\sigma'(6)\lambda_{\min}(G_j)>0,\qquad L_j=\tfrac14\lambda_{\max}(G_j)<\infty$$

bound the negative Hessian between $\lambda_j I$ and $L_j I$. Strict concavity ensures uniqueness of empirical and population optima. Compactness ensures existence.

**Step 3: localization before expansion.** T1 places each population optimum in the interior. By maximality of the empirical optimum and the definition of $U_n$,

$$F_j(\theta_j^*)-F_j(\widehat\theta_{j,n})\le2U_n.$$

Taylor's formula for the **population objective** along a segment in the convex box, with $\nabla F_j(\theta_j^*)=0$, bounds the left side below by $(\lambda_j/2)\|\widehat\theta_{j,n}-\theta_j^*\|^2$. Thus

$$\|\widehat\theta_{j,n}-\theta_j^*\|^2\le4U_n/\lambda_j.$$

Let $r_j>0$ be one quarter of the distance from $\theta_j^*$ to the box boundary, and define $E_n=\{U_n<\min_j\lambda_j r_j^2/4\}$. The bound in Step 1 gives $P(E_n^c)\to0$. On $E_n$, both empirical optima are interior and a ball of radius $r_j$ about each is inside its box. This proves L2, including the event accounting needed below.

### C1. BIC (and the exact finite-sample threshold)

Define $\operatorname{BIC}_j=-2\ell_{j,n}(\widehat\theta_{j,n})+k_j\log n$. Since $k_K-k_S=1$,

$$\operatorname{BIC}_K-\operatorname{BIC}_S=-2D_n+\log n.$$

Thus, exactly for any $n\ge1$, $K$ has smaller BIC iff $2D_n>\log n$; equality is a tie. L2 yields

$$\frac{\operatorname{BIC}_K-\operatorname{BIC}_S}{n}\to_p-2\Delta<0,$$

and therefore $P(\operatorname{BIC}_K<\operatorname{BIC}_S)\to1$. This follows directly from convergence in probability, taking a neighborhood of $-2\Delta$ wholly below zero. The corresponding AIC identity is $\operatorname{AIC}_K-\operatorname{AIC}_S=-2D_n+2$.

For a conservative finite-sample probability statement, $|D_n/n-\Delta|\le2U_n$. If $\Delta>\log(n)/(2n)$, then

$$P(\operatorname{BIC}_K\ge\operatorname{BIC}_S)
\le\min\left\{1,\frac{64M^2}{n[\Delta-\log(n)/(2n)]^2}\right\}.$$

This is a valid but usually very loose bound, not a practical sample-size recommendation. It explicitly retains sampling variation. This proves C1.

### C2. Bayes factor with proper uniform priors

Let $m_{j,n}=\int_{\Theta_j}\exp\{\ell_{j,n}(\theta)\}\,2^{-k_j}d\theta$ and $\operatorname{BF}_{K,S}=m_{K,n}/m_{S,n}$. These are evidences for the same observed response pairs; latent contexts have not been supplied to one candidate but withheld from the other.

On $E_n$ from L2, the empirical optimum is interior, so its gradient is zero. The global curvature bounds and Taylor's formula along the segment from the optimum give

$$-\frac{nL_j}{2}\|h\|^2\le\ell_{j,n}(\widehat\theta_{j,n}+h)-\ell_{j,n}(\widehat\theta_{j,n})
\le-\frac{n\lambda_j}{2}\|h\|^2$$

whenever both endpoints are in the box. Integrating the upper bound over all of $\mathbb R^{k_j}$ yields

$$m_{j,n}\le e^{\ell_{j,n}(\widehat\theta_{j,n})}\,2^{-k_j}\left(\frac{2\pi}{n\lambda_j}\right)^{k_j/2}.$$

For $n^{-1/2}<r_j$, integrate the lower bound over $\|h\|\le n^{-1/2}$, a ball contained in the box on $E_n$:

$$m_{j,n}\ge e^{\ell_{j,n}(\widehat\theta_{j,n})}\,2^{-k_j}e^{-L_j/2}V_{k_j}n^{-k_j/2},$$

where $V_k$ is the positive volume of the unit Euclidean ball in dimension $k$. These fixed positive upper and lower constants imply, since $P(E_n^c)\to0$,

$$\log m_{j,n}=\ell_{j,n}(\widehat\theta_{j,n})-\frac{k_j}{2}\log n+O_p(1).$$

Subtracting gives

$$\log\operatorname{BF}_{K,S}=D_n-\tfrac12\log n+O_p(1),\qquad
\frac1n\log\operatorname{BF}_{K,S}\to_p\Delta>0.$$

Hence $P(\operatorname{BF}_{K,S}>1)\to1$. This proves C2 without a correctly specified likelihood assumption or an imported Laplace theorem. The $O_p(1)$ term includes prior/curvature constants; this is not exact finite-sample equivalence to BIC and does not license replacing $D_n$ by $n\Delta$ with an $O_p(1)$ error.

### L3. Posterior concentration uniformly over participant deletions

For $n\ge2$, let $\Pi_{j,-i}$ be the posterior based on the $n-1$ entire participant pairs other than $i$. Deleting one observation changes empirical frequencies by at most $2/(n-1)$ in $\ell_1$, so the normalized deleted objective $F_{j,-i}^{\rm emp}$ satisfies

$$\max_{j,i}\sup_\theta|F_{j,-i}^{\rm emp}(\theta)-F_j(\theta)|
\le U_n+2M/(n-1)=:V_n\to_p0.$$

Fix a model and a sufficiently small $\epsilon>0$ so its $\epsilon$-ball about $\theta_j^*$ is inside the box. Set $g=\lambda_j\epsilon^2/2>0$. Population curvature implies $F_j(\theta)\le F_j(\theta_j^*)-g$ outside that ball. Continuity gives a smaller fixed ball $B_\rho$ with $\rho<\epsilon$ on which $F_j(\theta)\ge F_j(\theta_j^*)-g/4$. Its uniform-prior mass $a_j>0$.

On $\{V_n<g/8\}$, the deleted empirical objective is at most $F_j(\theta_j^*)-7g/8$ outside the $\epsilon$-ball and at least $F_j(\theta_j^*)-3g/8$ on $B_\rho$. Bounding numerator and denominator of the posterior separately gives, simultaneously for every deletion,

$$\max_i\Pi_{j,-i}(\|\theta-\theta_j^*\|\ge\epsilon)
\le a_j^{-1}\exp\{-(n-1)g/2\}.$$

The complement of the event tends to zero by the explicit bound for $U_n$; for large $n$, $2M/(n-1)<g/16$, so its probability is at most $P(U_n\ge g/16)$, tending to zero. The same conclusion holds for both models by a finite union bound. This proves L3; no unjustified pointwise-to-uniform upgrade over deletions is used.

### C3. Exact leave-one-participant-out information criterion

The joint predictive probability for the omitted pair is

$$\widetilde q_{j,-i}(w)=\int q_j(w;\theta)\,d\Pi_{j,-i}(\theta),\qquad
\operatorname{ELPD}_{j,\rm LOPO}=\sum_{i=1}^n\log\widetilde q_{j,-i}(W_i),\quad
\operatorname{LOPOIC}_j=-2\operatorname{ELPD}_{j,\rm LOPO}.$$

This is LOOIC with the held-out unit explicitly a participant. The parameter integral encloses the product of both trial probabilities.

On the compact boxes, the finitely many functions $q_j(w;\theta)$ are uniformly continuous. For a modulus $\omega_j(\epsilon)\to0$, splitting the posterior inside and outside the $\epsilon$-ball gives

$$\max_{i,w}|\widetilde q_{j,-i}(w)-q_j(w;\theta_j^*)|
\le\omega_j(\epsilon)+\max_i\Pi_{j,-i}(\|\theta-\theta_j^*\|\ge\epsilon).$$

Both probabilities inside the absolute difference are at least $\delta$, so the mean value theorem for $\log$ bounds the corresponding logarithmic difference by the right side divided by $\delta$. For any desired tolerance, first choose a fixed small $\epsilon$ making $\omega_j(\epsilon)/\delta$ small, then use L3 to make the posterior term small in probability. It follows that the maximum logarithmic difference tends to zero in probability.

Consequently,

$$\left|\frac{\operatorname{ELPD}_{j,\rm LOPO}}n-\frac1n\sum_i\log q_j(W_i;\theta_j^*)\right|\to_p0.$$

The last empirical average converges to $F_j(\theta_j^*)$ by L2's frequency bound. Therefore

$$\frac{\operatorname{LOPOIC}_K-\operatorname{LOPOIC}_S}{n}\to_p-2\Delta<0,$$

and $P(\operatorname{LOPOIC}_K<\operatorname{LOPOIC}_S)\to1$. This proves C3. It proves exact Bayesian deletion, not the numerical accuracy of PSIS. There is no BIC-style parameter-count penalty in the definition of LOPOIC.

### C4. All three criteria select the false complex model

For each criterion the probability of failing to select $K$ tends to zero by C1, C2 and C3. The probability that any fails is at most the sum of these three probabilities, which tends to zero. Thus the probability that all three select $K$ tends to one. No independence among the criteria is assumed. This proves C4.

## Corrections or Missing Assumptions

This is an explicit existence theorem with two trials and fixed-dimensional, compact candidate families. The compactness and proper uniform priors are declared proof choices, not consequences of the earlier mixture lemma. The old Gaussian assumption A-003 is not used. A-006 is still rejected as a general primary assumption; the deterministic design here is specific to A1.

A more general theorem for the final hierarchical ambiguity model is **not claimed here**. A simple model allowed the correct shared two-point random-effect distribution would represent $P$ exactly and remove this example's advantage. Setting the contextual sensitivity to the same value for every participant removes the gap when that common slope lies in the simple candidate’s parameter box (for example, $b=1/2$). Constancy outside the box alone is not sufficient. These boundaries are features of the scientific claim, not exceptions to hide.

## Verification Checks

- Localization before expansion: L2 proves the empirical interior event before C2 expands around the empirical maximizer. The earlier population expansion uses a known interior population optimum.
- Wrong norm/mode: probability-vector $\ell_1$ controls objective suprema; parameter distance is Euclidean; every statistical limit is in probability.
- Good-event bookkeeping: L2 supplies a Chebyshev bound; C2 carries $P(E_n^c)\to0$; L3 bounds the deletion-event complement.
- Rate leakage: only $D_n/n\to_p\Delta$ is needed; $D_n-n\Delta$ is never declared bounded. BF's $O_p(1)$ is relative to the fitted likelihood.
- Quantifier inflation: L3's deletion bound is simultaneous over all participants. The construction is an existence example, not universal dominance over models or designs.
- Citation identity: background citations only; no unverified theorem number closes an obligation.
- Imported-result applicability: elementary inequalities and finite-dimensional calculus are applied with finite variance, compact boxes, positive probabilities and full-rank design checked locally.
- Negligibility closure: $\log n/n\to0$, bounded likelihood-integral constants divided by $n$ vanish, and L3's exponential bound vanishes for fixed $\epsilon$.
- Boundary/singularity: both population optima are interior and both Gram matrices positive definite. Shared latent context is integrated in the true law; no mixture-parameter singularity is concealed in a candidate's parameter count.
- Acceptance limit: closed local proof obligations do not replace an independent adversarial review. Numerical tests verify selected calculations, not the theorems.
