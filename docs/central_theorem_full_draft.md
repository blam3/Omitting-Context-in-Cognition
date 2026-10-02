# Central theorem, end to end: from omitted context to systematic false-complex selection

Date: 2026-10-02. **Status: one-shot exploratory author draft.** Written at the PI's request to display the complete logical chain and what a full proof requires. Not reviewed. It does not replace [`minimal_ambiguity_proof.md`](minimal_ambiguity_proof.md) as the authoritative primary proof and changes no assumption, claim, or roadmap status. Every hypothesis below is a labeled condition of a stated result, not an adopted project assumption. New identities, expansions and numbers are checked by [`scripts/verify_central_theorem_draft.py`](../scripts/verify_central_theorem_draft.py) (output: [`logs/theory_checks/2026-10-02_central_theorem_draft.json`](../logs/theory_checks/2026-10-02_central_theorem_draft.json)); those checks are diagnostics, not proofs.

## 0. Overview

### 0.1 The argument in one paragraph

When a contextual variable $C$ shifts a latent cognitive parameter $\Theta$ but is omitted, each participant responds from a person-specific $\Theta$ the model cannot see, so the observed response law is a **mixture** over $\Theta$ (Lemma 1.1). Mixing changes the response distribution in two precise ways: it makes a person's responses **positively dependent** (Proposition 1.3), and it **attenuates** each trial's choice probability toward $1/2$ by an amount proportional to that trial's squared sensitivity to $\Theta$. That attenuation bends the marginal choice function into a shape the simple kernel cannot produce (Theorem 1.4, Corollary 1.5). A simple model fitted to such data therefore leaves systematic marginal residuals. Suppose a more complex model's extra parameter (for example probability distortion) has a logit signature that correlates with those residuals *after the simple model's own parameters are refit*. Then the complex model is strictly closer to the truth in Kullback–Leibler (KL) divergence, although still false (Theorem 2.4). The size of that advantage can be read off the simple model's fit as half the squared score-test drift over the extra parameter's partial information (Proposition 2.5). In the small-heterogeneity limit it is a weighted partial covariance between the attenuation pattern and the extra parameter's design signature (Theorem 2.6, Corollary 2.7). BIC and Bayes factors estimate the joint KL gap; exact trial-level LOO estimates a trial-conditional KL gap. Each therefore selects the false complex model with probability tending to one (Part III). Meanwhile the context-aware simple model is exactly correct and wins whenever context is measured (Proposition 1.6). Part IV identifies which links can break.

### 0.2 Logical flow

```text
Omitted context C            Theta = a0 + a1 Z + gamma C + U   (A-003)
  |  Lemma 1.1: mixture over F(theta | w); the integral encloses the product over trials
  v
Observed response law p(y | w)
  |-- Prop 1.3 (exact):  within-person dependence  => every homogeneous model is false
  |-- Thm 1.4 (2nd order): p = p0 (1 + eps^2 h + O(eps^3)),  h = h_A (attenuation) + h_D (dependence)
  |-- Prop 1.6:  context-aware simple model has zero risk; omission costs I(Y;C|W)
  v
Population separation (KL projections)
  |-- Thm 2.4:  extra-score drift Lambda != 0      =>  0 < R_K < R_S        (Delta_J > 0)
  |-- Prop 2.5: Delta_J >= Lambda^2/(2 Bbar),   Delta_J ~ Lambda^2/(2 I_rho|S)
  |-- Thm 2.6 / Cor 2.7:  Lambda ~ eps^2 <a, M_S e>_Omega   (why the drift is nonzero)
  |-- Lemma 2.3 / Thm 2.6: Delta_C = Delta_J / T (homogeneous) or Delta_C ~ eps^4 L / 2 (general)
  v
Criteria (n participants -> infinity, T fixed)
  |-- Thm 3.3  BIC:       (BIC_K - BIC_S)/n        -> -2 Delta_J
  |-- Thm 3.4  BF:        (1/n) log BF_KS          ->    Delta_J
  |-- Thm 3.7  trial LOO: (LOOIC_K - LOOIC_S)/(nT) -> -2 Delta_C
  v
Cor 3.8: P(BIC, BF and trial LOO all select the false complex model) -> 1;
         the test of "no distortion" rejects w.p. -> 1; the distortion estimate converges to rho_K* != 1.
Part IV: the links that can fail (representable, absorbed, hierarchical absorption, parity, reversal).
```

### 0.3 What is reused and what is new

| Element | Role here | Source |
|---|---|---|
| Mixture lemma; A-003 moment identities | Restated | [`omitted_context_mixture_lemma.md`](omitted_context_mixture_lemma.md); [`primary_theorem_specification.md`](primary_theorem_specification.md) §1 |
| Dependence signature implies every homogeneous model is false | New statement (elementary) | Prop. 1.3 |
| Second-order heterogeneity expansion; attenuation/dependence split | New for this project; classical idea of neglected heterogeneity | Thm. 1.4, Cor. 1.5 |
| Extra-score drift criterion and gap bounds | New; drift form of Proposition M in [`general_theorem_architecture.md`](general_theorem_architecture.md) | Thm. 2.4, Prop. 2.5 |
| Local projection theorem | Adapted from [`smooth_observable_extension.md`](smooth_observable_extension.md) to an $\varepsilon^2$ perturbation | Thm. 2.6 |
| Weighted-least-squares criterion; $\Delta_C=\Delta_J/T$ for homogeneous candidates | New | Lemma 2.3, Cor. 2.7 |
| BIC/BF/trial-LOO transfer | Restated from [`primary_separation_attempt_2026-09-08.md`](primary_separation_attempt_2026-09-08.md) L3–L8, plus explicit exponential bounds | Part III |
| Hierarchical absorption ($\varepsilon^6$/$\varepsilon^8$) and parity obstruction | New | Props. 4.3–4.4 |
| Ambiguity witness | Restated with new diagnostics | Part V; [`minimal_ambiguity_proof.md`](minimal_ambiguity_proof.md) |

## 1. Setting and the central theorem

### 1.1 Data-generating process

- **(D1) Sampling.** Participants $i=1,\dots,n$ are iid. Each has a retained design/covariate cell $W_i=(X_i,Z_i)$ in a finite set $\mathcal W$ with $H(w)=P(W=w)>0$, and $T\ge2$ binary responses $Y_i\in\{0,1\}^T$, with $T$ fixed. Asymptotics are $n\to\infty$.
- **(D2) Latent equation (A-003).** $\Theta=a_0+a_1Z+\gamma C+U$. Write $\bar\theta(w)=E[\Theta\mid W=w]$.
- **(D3) Simple cognitive kernel; context acts only through $\Theta$.** Given $(\Theta,W,C)$ the $T$ responses are independent, with
  $$P(Y_t=1\mid\Theta=\theta,W=w,C)=\pi_t(\theta,w)=\sigma(\eta_t(\theta,w)),\qquad \eta_t(\theta,w)=\kappa_t(w)-\beta_t(w)\,\theta .$$
  For the PI's gain-only kernel at $\rho=1$: $\kappa_t=\alpha+\beta_{\rm side}s_t+\tau(v_{A,t}p_{A,t}-v_{R,t}p_{R,t})$ and $\beta_t=\tau v_{A,t}A_t/2\ge0$, which is zero on calibration rows.
- **(D4) Nondegeneracy (used only where stated).** For some $w$, $\Theta\mid W=w$ is nondegenerate and at least two trials have $\beta_t(w)\ne0$ of the same sign.

### 1.2 Candidate models

Both candidates omit $C$; each is a family $\mathcal Q_M$ of participant laws $q(\cdot\mid w)$ on $\{0,1\}^T$.

- **Homogeneous (product) candidates:** $q_M(y\mid w;\phi)=\prod_t\mathrm{Bern}\big(y_t;\sigma(\eta^M_t(w;\phi))\big)$, global parameters only. This is the minimal ambiguity contract. Per-participant fixed-effect fits are outside this fixed-dimensional framework.
- **Hierarchical candidates:** $q_M(y\mid w;\phi)=\int\prod_t\mathrm{Bern}\big(y_t;\sigma(\eta^M_t(\vartheta,w;\phi))\big)\,G_M(d\vartheta\mid w;\phi)$, with a working random-effect law $G_M$. This is the PI's G1 pair.
- **Nesting.** $K$ adds one parameter $\rho$ with $K|_{\rho=1}=S$, for example Prelec weighting $w(p;\rho)=\exp(-(-\ln p)^\rho)$. Parameter counts $k_S<k_K$ are fixed. The **extra logit signature** at the simple fit is $e_t(w)=\partial_\rho\eta^K_t(w;\phi,\rho)\vert_{\rho=1}$. For Prelec weighting, $\partial_\rho w(p;1)=p\ln p\,\ln(-\ln p)$ (zero at $p\in\{0,1\}$), so
  $$e_t=\tau\big[v_{A,t}\,\partial_\rho w(p_{A,t};1)-v_{R,t}\,\partial_\rho w(p_{R,t};1)\big].$$
- **Contextual reference $S^C$:** $S$ with $C$ in the latent equation. It contains the truth when $U\equiv0$, or when $U$'s law lies in $S^C$'s working family.

### 1.3 Population targets

$$\mathrm{KL}_H(p\Vert q)=\sum_wH(w)\,\mathrm{KL}\big(p(\cdot\mid w)\Vert q(\cdot\mid w)\big),\qquad R_M=\inf_{q\in\mathcal Q_M}\mathrm{KL}_H(p\Vert q),\qquad \Delta_J=R_S-R_K .$$

$R_M$ and $\Delta_J$ are per participant. For the joint projections $q_M^\star$ (attained; unique where stated) define the per-trial conditional risk and gap

$$C_M=\frac1T\sum_{t=1}^TE_{W,Y_{-t}}\,\mathrm{KL}\big(p(Y_t\mid Y_{-t},W)\,\Vert\,q_M^\star(Y_t\mid Y_{-t},W)\big),\qquad\Delta_C=C_S-C_K .$$

The conditionals are those of the **joint** fits; nothing is re-optimized for the conditional target.

### 1.4 Criteria

Likelihoods are participant likelihoods, and $n$ counts participants. Write $\ell_{M,n}(\phi)=\sum_i\log q_M(Y_i\mid W_i;\phi)$.

- **BIC:** $\mathrm{BIC}_M=-2\sup_\phi\ell_{M,n}(\phi)+k_M\log n$.
- **Bayes factor:** $m_M=\int e^{\ell_{M,n}}\,d\Pi_M$ with fixed proper priors, and $\mathrm{BF}_{KS}=m_K/m_S$.
- **Exact trial LOO:** $\mathrm{ELPD}_M=\sum_{i,t}\log p_M(y_{it}\mid D_{-it})$ and $\mathrm{LOOIC}_M=-2\,\mathrm{ELPD}_M$, where $D_{-it}$ deletes only response $y_{it}$.

"$K$ selected" means $\mathrm{BIC}_K<\mathrm{BIC}_S$, $\mathrm{BF}_{KS}>1$, and $\mathrm{LOOIC}_K<\mathrm{LOOIC}_S$, respectively.

### 1.5 The central theorem

Transfer conditions (as P-G3 in the repository):

- **(T1)** Finite support (D1) and $p(y\mid w)>0$ for every cell; automatic under D3.
- **(T2)** Fixed proper priors give positive mass to every law-space neighbourhood of each optimal law.
- **(T3)** (Trial LOO only.) Each closure $\overline{\mathcal Q}_M$ has a unique KL-optimal law. For full-rank affine-logit homogeneous families this is automatic, by strict convexity.

> **Theorem 0 (systematic false-complex selection).** Assume D1–D3, T1–T2, and the mechanism conditions
>
> **(M1)** $\Delta_J>0$, **(M2)** $R_K>0$, **(M3)** $\Delta_C>0$.
>
> Then, as $n\to\infty$ with $T$ fixed:
>
> 1. $(\mathrm{BIC}_K-\mathrm{BIC}_S)/n\to_p-2\Delta_J$;
> 2. $n^{-1}\log\mathrm{BF}_{KS}\to_p\Delta_J$;
> 3. under T3, $(\mathrm{LOOIC}_K-\mathrm{LOOIC}_S)/(nT)\to_p-2\Delta_C$;
> 4. under T3, $P(\text{BIC, BF and trial LOO all select }K)\to1$;
> 5. the likelihood-ratio statistic for $\rho=1$ diverges. When $\rho$ is a continuous function of the law near $q_K^\star$ and T3 holds, $\hat\rho\to_p\rho_K^\star\ne1$;
> 6. a correctly specified context-aware simple model $S^C$ has zero risk. When $C$ has finite support and is observed, BIC and BF prefer $S^C$ to $K$ with probability tending to one; trial LOO does too under the condition of Cor. 3.9.
>
> (M1)–(M3) hold in each of the following situations:
>
> - **(a) Homogeneous candidates (exact).** D4 holds and the extra-score drift $\Lambda\ne0$ (Thm. 2.4). Then $R_K\ge\sum_wH(w)I_w>0$ and $\Delta_C=\Delta_J/T$; and, if $K$'s logits are affine in its parameters, $\Delta_J\ge\Lambda^2/(2\bar B)$ (Prop. 2.5).
> - **(b) Small heterogeneity (any regular candidates).** The hypotheses of Thm. 2.6 hold with $d\ne0$, $r_K\ne0$ and $L>0$. Then (M1)–(M3) hold for all sufficiently small $\varepsilon\ne0$.
> - **(c) Explicit ambiguity witness (Thm. 5.1).** $\Delta_J=6.985\times10^{-4}$ nats per participant, $\Delta_C=\Delta_J/2$, $\rho_K^\star=0.663$.

How to read (M1)–(M3):

- (M1) is the false-complex advantage.
- (M2) says the selected complex model is still wrong. It is not needed for conclusions 1–5; it is the scientific content.
- (M3) is needed separately because trial LOO scores a different target than BIC and BF (Lemma 2.2).

None of the three is automatic: Part IV shows how each can fail.

*Proof of Theorem 0.*

- Conclusions 1–3: Theorems 3.3, 3.4 and 3.7.
- Conclusions 4 and 5: Corollary 3.8.
- Conclusion 6: Proposition 1.6 and Corollary 3.9.
- Case (a): Theorem 2.4, Proposition 1.3, Lemma 2.3 and Proposition 2.5.
- Case (b): Theorem 2.6.
- Case (c): Theorem 5.1. $\square$

---

## Part I. What omitting context does to the response distribution

**Lemma 1.1 (omitted-context mixture).** Under D3, for every $w$ and $y$,
$$p(y\mid w)=\int\prod_{t=1}^T\pi_t(\theta,w)^{y_t}\{1-\pi_t(\theta,w)\}^{1-y_t}\,F(d\theta\mid w),$$
where $F(\cdot\mid w)$ is the law of $\Theta$ given $W=w$ (not given $Z$ alone). The same formula holds with $F(\cdot\mid w,c)$ for $p(y\mid w,c)$.

*Proof.* Apply the tower property to $1\{Y=y\}$, conditioning on $(W,\Theta)$. Conditional independence factorizes the inner probability, and by D3, $C$ enters only through $\Theta$. $\square$

The integral encloses the product over trials; multiplying separately marginalized trial probabilities gives a different and wrong law. *Role:* this is the only place omission enters. Everything downstream is a property of this mixture.

**Lemma 1.2 (what A-003 contributes).** Assume finite conditional second moments. Let $m_X,v_X$ be the conditional mean and variance of $C$ given $W$; let $g_X,s_X^2$ be those of $U$; and let $c_X=\mathrm{Cov}(C,U\mid W)$. Then
$$\bar\theta(W)=a_0+a_1Z+\gamma m_X(W)+g_X(W),\qquad\mathrm{Var}(\Theta\mid W)=\gamma^2v_X(W)+s_X^2(W)+2\gamma c_X(W).$$
*Proof:* linearity of conditional expectation, and expanding the conditional variance of $\gamma C+U$ ([specification §1](primary_theorem_specification.md)). The residual choice $U=-\gamma(C-m_X(W))$ cancels all contextual variance. Moments alone determine neither the shape of $F(\cdot\mid w)$ nor any selection result. $\square$

**Proposition 1.3 (omission creates within-person dependence; every homogeneous model is false).** Fix $w$ with $\Theta\mid W=w$ nondegenerate, and let $\pi_t(\cdot,w)$ and $\pi_u(\cdot,w)$ be strictly monotone in the same direction. Then $\mathrm{Cov}(Y_t,Y_u\mid W=w)>0$. Consequently, under D4:

- $p(\cdot\mid w)$ is not a product law;
- its multi-information $I_w=\mathrm{KL}\big(p(\cdot\mid w)\Vert\otimes_tp_t(\cdot\mid w)\big)$ is positive;
- every homogeneous candidate, with any number of parameters, satisfies $R_M\ge\sum_wH(w)I_w>0$.

*Proof.* Conditional independence gives $E[Y_tY_u\mid w]=E[\pi_t(\Theta)\pi_u(\Theta)\mid w]$. Take an independent copy $\Theta'$; then
$$\mathrm{Cov}(Y_t,Y_u\mid w)=\tfrac12E\big[(\pi_t(\Theta)-\pi_t(\Theta'))(\pi_u(\Theta)-\pi_u(\Theta'))\big].$$
Same-direction strict monotonicity makes the integrand nonnegative, and positive on $\{\Theta\ne\Theta'\}$, which has positive probability by nondegeneracy. A nonzero covariance rules out a product law, so $I_w>0$ by Gibbs' inequality. For a product $q$, Lemma 2.3 gives $\mathrm{KL}(p_w\Vert q)=I_w+\sum_t\mathrm{KL}(p_{w,t}\Vert q_t)\ge I_w$. Limits of product laws are product laws, so the bound also holds for the infimum. $\square$

For the PI's kernel, $\partial\eta_t/\partial\theta=-\tau v_{A,t}A_t/2<0$ on every ambiguous row. All ambiguous trials are therefore positively dependent, while calibration rows ($A_t=0$) are unaffected by $\Theta$. *Role:* for homogeneous candidates (M2) is automatic. Extra cognitive complexity cannot represent what omission does to the joint law.

**Theorem 1.4 (second-order heterogeneity expansion).** Assume D3 and write $\Theta\mid W=w$ as $\bar\theta(w)+\varepsilon V_w$, with
$$E V_w=0,\qquad\mathrm{Var}\,V_w=v(w),\qquad E\lvert V_w\rvert^3\le m_3<\infty .$$
Here $\varepsilon\ge0$ is a bookkeeping scale, and $\varepsilon^2v(w)=\mathrm{Var}(\Theta\mid W=w)$ is the Lemma 1.2 variance. Let $\pi^0_t(w)=\pi_t(\bar\theta(w),w)$, $\sigma'_t(w)=\pi^0_t(1-\pi^0_t)$ and $p_0(y\mid w)=\prod_t\mathrm{Bern}(y_t;\pi^0_t(w))$. Then, uniformly over the finite support,
$$p_\varepsilon(y\mid w)=p_0(y\mid w)\{1+\varepsilon^2h(y,w)+R_\varepsilon(y,w)\},\qquad\lvert R_\varepsilon\rvert\le C\varepsilon^3,$$
with
$$h=\tfrac12v(w)\Big[\big(\textstyle\sum_t\ell'_t\big)^2+\sum_t\ell''_t\Big]=h_A+h_D,$$
$$h_A(y,w)=\tfrac12v(w)\sum_t\beta_t^2(1-2\pi^0_t)(y_t-\pi^0_t)\quad\text{(attenuation)},$$
$$h_D(y,w)=v(w)\sum_{t<u}\beta_t\beta_u(y_t-\pi^0_t)(y_u-\pi^0_u)\quad\text{(dependence)}.$$
Here $\ell'_t,\ell''_t$ are the $\theta$-derivatives of $\log\mathrm{Bern}(y_t;\pi_t(\theta,w))$ at $\bar\theta(w)$. Under $p_0$, $E[h_A\mid w]=E[h_D\mid w]=E[h_Ah_D\mid w]=0$. If $V_w$ is symmetric with $EV_w^4<\infty$, then $\lvert R_\varepsilon\rvert\le C\varepsilon^4$.

*Proof.*
1. Fix $(y,w)$ and let $g(\theta)=\prod_t\mathrm{Bern}(y_t;\pi_t(\theta,w))>0$. For the logistic kernel, each derivative of $g$ up to order three is a polynomial in the $\pi_t$ and $\beta_t$, hence bounded on $\mathbb R$ by some $G_3$.
2. Taylor's theorem with Lagrange remainder gives $g(\bar\theta+\varepsilon V)=g+\varepsilon Vg'+\tfrac12\varepsilon^2V^2g''+R$ with $\lvert R\rvert\le(G_3/6)\varepsilon^3\lvert V\rvert^3$.
3. Take expectations. $EV=0$ removes the first-order term and $EV^2=v(w)$ leaves $\tfrac12\varepsilon^2v\,g''$. Divide by $g(\bar\theta)$, which is bounded below on the finite support.
4. Use $g''/g=(\log g)''+((\log g)')^2=\sum_t\ell''_t+(\sum_t\ell'_t)^2$. For the logistic kernel, $\ell'_t=-\beta_t(y_t-\pi^0_t)$ and $\ell''_t=-\beta_t^2\sigma'_t$.
5. Expand the square and use the binary identity $(y-\pi)^2-\pi(1-\pi)=(1-2\pi)(y-\pi)$ for $y\in\{0,1\}$. This gives $h_A+h_D$.
6. Under $p_0$ the coordinates are independent with centered $y_t-\pi^0_t$. Each term of $h_A$ is a centered function of one coordinate; each term of $h_D$ is a product of two distinct centered coordinates; and $E[(y_s-\pi_s)(y_t-\pi_t)(y_u-\pi_u)]=0$ for $t\ne u$. This gives the three zero moments.
7. For symmetric $V$ the cubic term vanishes in expectation and a fourth-order bound applies. $\square$

*Role:* identifies, to leading order, the direction in which omission moves the response law. This is the classical neglected-heterogeneity (information-matrix) direction (Cox, 1983; Chesher, 1984). Script check E1 confirms the closed form against exact mixtures, with observed remainder orders $0.96\to0.99$ (skewed $V$, order 1) and $2.000$ (symmetric $V$, order 2).

**Corollary 1.5 (what the two pieces do).** To order $\varepsilon^2$:

- **(a) Attenuation.** Let $a_t(w)=\tfrac12v(w)\beta_t(w)^2\{1-2\pi^0_t(w)\}$. Then
  $$\mathrm{logit}\,P(Y_t=1\mid w)=\eta_t(\bar\theta(w),w)+\varepsilon^2a_t(w)+O(\varepsilon^3).$$
  Each marginal moves toward $1/2$, by an amount proportional to $\beta_t^2$. The marginal psychometric function is therefore not of the kernel's form: it bends, more on trials more sensitive to $\Theta$.
- **(b) Dependence.** $\mathrm{Cov}(Y_t,Y_u\mid w)=\varepsilon^2v(w)\beta_t\beta_u\sigma'_t\sigma'_u+O(\varepsilon^3)$.

*Proof.* (a) $E_\varepsilon[Y_t-\pi^0_t\mid w]=\varepsilon^2E_0[h\,(y_t-\pi^0_t)]+O(\varepsilon^3)=\varepsilon^2a_t\sigma'_t+O(\varepsilon^3)$. Then use $\mathrm{logit}(\pi+\delta)=\mathrm{logit}\,\pi+\delta/\sigma'+O(\delta^2)$.

(b) The expected product $E_\varepsilon[(Y_t-\pi^0_t)(Y_u-\pi^0_u)]$ equals $\varepsilon^2E_0[h_D(y_t-\pi^0_t)(y_u-\pi^0_u)]+O(\varepsilon^3)=\varepsilon^2v\beta_t\beta_u\sigma'_t\sigma'_u+O(\varepsilon^3)$. The product of the mean shifts is $O(\varepsilon^4)$. $\square$

In the witness of Part V the exact shifts are $+0.038$ logits at $x=1$ and $+0.251$ at $x=2$. That is the bend the simple ambiguity model cannot reproduce and the distortion parameter partly can.

**Proposition 1.6 (what omission costs; the context-aware model).** For any context-omitting law $q(\cdot\mid w)$,
$$E_{W,C}\,\mathrm{KL}\big(p(\cdot\mid W,C)\Vert q(\cdot\mid W)\big)=\mathrm{KL}_H(p\Vert q)+I(Y;C\mid W).$$
A correctly specified $S^C$ therefore has zero risk for the context-conditional target. Every context-omitting model, however complex, has risk at least $I(Y;C\mid W)$, which is positive iff the law of $Y$ given $(W,C)$ varies with $C$.

*Proof.* Write $\log\frac{p(y\mid w,c)}{q(y\mid w)}=\log\frac{p(y\mid w,c)}{p(y\mid w)}+\log\frac{p(y\mid w)}{q(y\mid w)}$ and average. $\square$

In the witness, $I(Y;C\mid W)=0.1293$ nats while $\Delta_J=0.0007$. The complex model recovers about $0.5\%$ of the information lost by omitting context; $S^C$ recovers all of it. *Role:* conclusion 6 of Theorem 0. Complexity is not a substitute for context.

**Remark 1.7 (what exactly is "omitted").** The mechanism is unmodelled heterogeneity of $\Theta$ given the retained cell $W$. Omitted context contributes $\gamma^2v_X(w)$ (plus covariance terms) to it. If $U\not\equiv0$ is also unmodelled, the same mathematics applies with the total conditional variance; the context-aware comparator is then correct only if it also models $U$. Including context removes the context share of the heterogeneity, not necessarily all of it.

---

## Part II. From the response law to population separation

**Lemma 2.1 (existence, nesting, falsity).** Under T1:

- $R_M$ is finite and attained on $\overline{\mathcal Q}_M$, and every optimal law has positive cells;
- $\mathcal Q_S\subseteq\mathcal Q_K$ implies $\Delta_J\ge0$;
- $R_M>0$ iff $p\notin\overline{\mathcal Q}_M$.

*Proof.* Use compactness of the finite product of simplices, lower semicontinuity of KL (value $+\infty$ when a positive true cell receives mass 0), and Gibbs' inequality. $\square$

Nesting gives only $\ge$; strictness is the content of (M1).

**Lemma 2.2 (joint versus trial-conditional risk).** For positive laws,
$$E_{Y_{-t}}\,\mathrm{KL}\big(p(Y_t\mid Y_{-t})\Vert q(Y_t\mid Y_{-t})\big)=\mathrm{KL}(p\Vert q)-\mathrm{KL}(p_{-t}\Vert q_{-t}),$$
so
$$\Delta_C=\Delta_J-\frac1T\sum_t\big[\mathrm{KL}_H(p_{-t}\Vert q^\star_{S,-t})-\mathrm{KL}_H(p_{-t}\Vert q^\star_{K,-t})\big].$$
(M1) does not imply (M3). There is an exact nested-family counterexample with global joint fits giving $\Delta_J=\varepsilon^2+o(\varepsilon^2)$ and $\Delta_C=-\varepsilon^2/4+o(\varepsilon^2)$ ([`trial_conditional_perturbation_2026-09-09.md`](trial_conditional_perturbation_2026-09-09.md)). $\square$

**Lemma 2.3 (homogeneous candidates: product reduction).** If $q=\otimes_tq_t$, then
$$\mathrm{KL}(p\Vert q)=I(p)+\sum_t\mathrm{KL}(p_t\Vert q_t),\qquad E_{Y_{-t}}\,\mathrm{KL}\big(p(Y_t\mid Y_{-t})\Vert q_t\big)=I(Y_t;Y_{-t})+\mathrm{KL}(p_t\Vert q_t).$$
Hence, for homogeneous $S$ and $K$:

- the joint projections minimize only the weighted marginal sum;
- $\Delta_J=\sum_wH(w)\sum_t\big[\mathrm{KL}(\bar p_{wt}\Vert\pi^{S\star}_{wt})-\mathrm{KL}(\bar p_{wt}\Vert\pi^{K\star}_{wt})\big]$;
- $\Delta_C=\Delta_J/T$ **exactly**.

*Proof.* Write $\log(p/q)=\log(p/\prod_tp_t)+\sum_t\log(p_t/q_t)$. For the conditional, write $\log\frac{p(y_t\mid y_{-t})}{q_t(y_t)}=\log\frac{p(y_t\mid y_{-t})}{p_t(y_t)}+\log\frac{p_t(y_t)}{q_t(y_t)}$. The dependence terms do not involve $q$ and cancel in $S$–$K$ differences. Averaging the conditional identity over $t$ gives $C_S-C_K=\Delta_J/T$. $\square$

*Role:* for homogeneous candidates (M3) follows from (M1). The joint-versus-conditional problem arises only with participant effects. Script check L1 confirms $\Delta_C=\Delta_J/T$ to $10^{-12}$ in every row.

**Theorem 2.4 (extra-score drift implies a strict false-complex advantage).** Let $q_S^\star=q_S(\phi_S^\star)$ be the simple projection (attained, with positive cells). Suppose $K$ contains the path $\rho\mapsto q_K(\phi_S^\star,\rho)$ through $q_S^\star$ at $\rho=1$, differentiable on a two-sided neighbourhood (or one-sided in the direction of $\mathrm{sign}\,\Lambda$). Define the **extra-score drift**
$$\Lambda=E_P\big[\partial_\rho\log q_K(Y\mid W;\phi_S^\star,\rho)\vert_{\rho=1}\big].$$

- **(a)** If $\Lambda\ne0$ then $R_K<R_S$; that is, (M1) holds.
- **(b)** For homogeneous candidates,
  $$\Lambda=\sum_wH(w)\sum_te_t(w)\,\big(\bar p_{wt}-\pi^{S\star}_{wt}\big):$$
  the design-weighted covariance between the extra logit signature and the simple model's marginal residuals. Under D4, (M2) holds with $R_K\ge\sum_wH(w)I_w$, and (M3) holds with $\Delta_C=\Delta_J/T$.

*Proof.* (a) Finite support permits differentiation:
$$\partial_\rho\,\mathrm{KL}_H\big(p\Vert q_K(\phi_S^\star,\rho)\big)\big\vert_{\rho=1}=-E_P[\partial_\rho\log q_K]=-\Lambda .$$
A small move of $\rho$ away from 1 in the direction of $\mathrm{sign}\,\Lambda$ gives a law in $\mathcal Q_K$ with risk strictly below $R_S$.

(b) For product laws $\partial_\rho\log q_K=\sum_te_t(y_t-\pi_t)$, whose $P$-mean is the displayed $\Lambda$. The rest is Proposition 1.3 and Lemma 2.3. $\square$

*Remarks.*
1. $\Lambda$ is the population mean of the Rao score statistic for the restriction $\rho=1$. False-complex selection occurs exactly when omitted context gives that score test a nonzero drift.
2. $\mathrm{sign}\,\Lambda$ predicts the direction of the spurious effect. In the witness $\Lambda<0$ and $\rho_K^\star=0.663<1$: inverse-S weighting.
3. For hierarchical candidates (a) still applies, but (M2) and (M3) need separate arguments (Lemma 2.1, Theorem 2.6).

**Proposition 2.5 (the gap from the drift).** Take homogeneous candidates whose logits are affine in $(\phi,\tilde\rho)$ for some coordinate $\tilde\rho$ of the extra parameter; in the witness, $\tilde\rho=\delta=4[w(1/2;\rho)-1/2]$. Write $e$ for the $\tilde\rho$ signature and $\Lambda$ for the drift in that coordinate. Let:

- $\mathbf G$ be the logistic information at the $S$ projection, $\mathbf G_{ab}=\sum_wH(w)\sum_t\sigma'(\eta^{S\star}_{wt})\,\partial_a\eta_{wt}\,\partial_b\eta_{wt}$;
- $\mathcal I_{\rho\mid S}=\mathbf G_{ee}-\mathbf G_{eS}\mathbf G_{SS}^{-1}\mathbf G_{Se}$ be the partial information of the extra parameter;
- $c=e-\mathbf J_S\mathbf G_{SS}^{-1}\mathbf G_{Se}$ be the efficient direction in logit space, where $\mathbf J_S$ is $S$'s logit Jacobian stacked over $(w,t)$, and $\bar B=\tfrac14\sum_wH(w)\sum_tc_{wt}^2$.

If the step $s=\Lambda/\bar B$ along the efficient path stays in $K$'s parameter domain, then
$$\Delta_J\ \ge\ \frac{\Lambda^2}{2\bar B},$$
and in the regime of Theorem 2.6, $\Delta_J=\dfrac{\Lambda^2}{2\mathcal I_{\rho\mid S}}\{1+o(1)\}$.

*Proof.*
1. Let $f(s)=\mathrm{KL}_H\big(p\Vert q_K(\phi_S^\star-s\mathbf G_{SS}^{-1}\mathbf G_{Se},\,\tilde\rho_0+s)\big)$.
2. Because the $S$ projection is interior, $E_P[\partial_\phi\log q_S(\phi_S^\star)]=0$, so $f'(0)=-\Lambda$.
3. Along an affine-logit path the second derivative of $-\log\mathrm{Bern}(y;\sigma(\eta))$ in $\eta$ is $\sigma'(\eta)$ whatever $y$ is. So $f''(s)=\sum_wH\sum_t\sigma'(\eta_{wt}(s))c_{wt}^2\le\bar B$.
4. Hence $f(s)\le R_S-\Lambda s+\tfrac12\bar Bs^2$, and minimizing at $s=\Lambda/\bar B$ gives the bound.
5. For the asymptotic statement, use Theorem 2.6 with one extra parameter: $d=\big(\langle r_S,s_e\rangle/\lVert\mathbf M_Ss_e\rVert^2\big)\mathbf M_Ss_e$, $\Lambda=\varepsilon^2\langle r_S,s_e\rangle+O(\varepsilon^3)$ and $\lVert\mathbf M_Ss_e\rVert^2=\mathcal I_{\rho\mid S}+O(\varepsilon^2)$. $\square$

Numerically (checks I1/L1), $\Delta_J\big/\{\Lambda^2/(2\mathcal I_{\rho\mid S})\}$ lies in $[0.9999,1.0003]$ across all local rows and is $1.003$ in the witness, far outside the small-$\varepsilon$ regime. The rigorous lower bound is within a factor of $1.27$. *Practical meaning:* the false-complex gap can be read off the **simple** model's fit. It is half the per-participant noncentrality of the score test for the extra parameter.

**Theorem 2.6 (local mechanism theorem: why $\Lambda\ne0$).** Assume:

1. the truth is the small-heterogeneity path of Theorem 1.4 with $\varepsilon\mapsto p_\varepsilon(y\mid w)$ of class $C^3$ near 0 (true under D3 if $E\lvert V\rvert^3<\infty$), so $p_\varepsilon=p_0(1+\varepsilon^2h+O(\varepsilon^3))$;
2. $p_0\in\mathcal Q_S\subseteq\mathcal Q_K$; the simple mean structure represents $\bar\theta(w)$;
3. hypotheses H1–H2 of [`smooth_observable_extension.md`](smooth_observable_extension.md) hold for both models at $p_0$: regular $C^3$ observable charts with injective derivative, and local completeness of the closure. The tangent spaces satisfy $\mathcal T_S\subseteq\mathcal T_K$ in $L^2(Hp_0)$, with orthogonal projections $P_S,P_K$.

Let $d=P_Kh-P_Sh$, $r_M=h-P_Mh$ and $\mathcal A=\frac1T\sum_t(I-E_0[\,\cdot\mid Y_{-t},W])$. Then for all small $\varepsilon\ne0$ the projections are unique and
$$R_M(\varepsilon)=\tfrac{\varepsilon^4}2\lVert r_M\rVert^2+O(\varepsilon^5),\qquad\Delta_J(\varepsilon)=\tfrac{\varepsilon^4}2\lVert d\rVert^2+O(\varepsilon^5),$$
$$\Delta_C(\varepsilon)=\tfrac{\varepsilon^4}2L+O(\varepsilon^5),\qquad L=\langle d,\mathcal Ad\rangle+2\langle r_K,\mathcal Ad\rangle .$$
Thus, for all sufficiently small $\varepsilon\ne0$: $d\ne0$ gives (M1), $r_K\ne0$ gives (M2), and $L>0$ gives (M3).

*Proof.*
1. **Localization of laws.** $\mathrm{KL}_H(p_\varepsilon\Vert p_0)=O(\varepsilon^4)\to0$. By compactness and lower semicontinuity, every global minimizer over the closure converges to $p_0$ (Proof 1 of the smooth extension). By H2 it eventually lies in the chart.
2. **Stationary branch.** Let $\Phi_M(\theta,\varepsilon)=\nabla_\theta\mathrm{KL}_H(p_\varepsilon\Vert q_M(\theta))=-E_{p_\varepsilon}[s_M(\theta)]$. It is $C^2$ near $(0,0)$, and $\partial_\theta\Phi_M(0,0)=G_M$ is positive definite (H1). Because $E_0s_M=0$ and the $O(\varepsilon)$ term of $p_\varepsilon$ vanishes, $\Phi_M(0,\varepsilon)=-\varepsilon^2E_0[hs_M]+O(\varepsilon^3)$. The implicit function theorem gives a unique local zero $\theta_M(\varepsilon)$ with $\theta_M'(0)=0$. Inserting it into $\Phi_M=0$ gives $\lvert\theta_M\rvert\le C(\varepsilon^2+\lvert\theta_M\rvert^2)$, hence $\theta_M(\varepsilon)=\varepsilon^2G_M^{-1}E_0[hs_M]+O(\varepsilon^3)$. Local strict convexity makes it the unique minimizer in the chart, hence the global one. Therefore $q_M^\star/p_0=1+\varepsilon^2P_Mh+O(\varepsilon^3)$.
3. **Risks.** Take normalized laws with $p/p_0=1+a$ and $q/p_0=1+b$, where $a,b=O(\varepsilon^2)$. The expansion $(1+a)\log\frac{1+a}{1+b}=(a-b)+\tfrac12(a-b)^2+O(\lvert a\rvert^3+\lvert b\rvert^3)$ and conditional normalization give $\mathrm{KL}_H(p\Vert q)=\tfrac12\lVert a-b\rVert^2+O(\varepsilon^6)$; this yields $R_M$. Nesting gives $r_S=r_K+d$ with $r_K\perp d$, which yields $\Delta_J$.
4. **Conditional risks.** Marginalizing over $Y_t$ replaces a first-order coefficient by $E_0[\,\cdot\mid Y_{-t},W]$. The chain rule (Lemma 2.2) then gives $C_M=\tfrac{\varepsilon^4}2\langle r_M,\mathcal Ar_M\rangle+O(\varepsilon^5)$; substitute $r_S=r_K+d$. $\square$

*Role:* explains what $\Lambda$ measures: the component of the omission direction $h$ that lies in $K$'s extra tangent direction but not in $S$'s.

**Corollary 2.7 (homogeneous candidates: a weighted-least-squares criterion).** Take homogeneous candidates with logit Jacobians $\mathbf J_S$ and $\mathbf J_K=[\mathbf J_S,e]$ at $p_0$, of full column rank. Stack over $(w,t)$ and set
$$\Omega=\mathrm{diag}\{H(w)\sigma'_t(w)\},\qquad\mathbf a=(a_t(w))\ \text{(Cor. 1.5)},\qquad\mathbf M_S=I-\mathbf J_S(\mathbf J_S^\top\Omega\mathbf J_S)^{-1}\mathbf J_S^\top\Omega ,$$
with $\mathbf M_K$ defined in the same way from $\mathbf J_K$. Then:

- **(a)** The tangent spaces consist of first-order functions $\sum_tc_t(w)(y_t-\pi^0_t)$, with inner product $c^\top\Omega c'$. Hence $P_Mh=P_Mh_A$ ($h_D$ is orthogonal to every first-order function), and $P_M$ acts on $\mathbf a$ by $\Omega$-weighted least squares.
- **(b)** $\Lambda=\varepsilon^2\langle\mathbf a,\mathbf M_Se\rangle_\Omega+O(\varepsilon^3)$. For one extra parameter (Frisch–Waugh–Lovell),
  $$\Delta_J=\frac{\varepsilon^4}2\,\frac{\langle\mathbf a,\mathbf M_Se\rangle_\Omega^2}{\langle e,\mathbf M_Se\rangle_\Omega}+o(\varepsilon^4).$$
- **(c)** $R_K=\tfrac{\varepsilon^4}2\big(\lVert\mathbf M_K\mathbf a\rVert_\Omega^2+\lVert h_D\rVert^2\big)+o(\varepsilon^4)$, where $\lVert h_D\rVert^2=\sum_wH(w)v(w)^2\sum_{t<u}\beta_t^2\beta_u^2\sigma'_t\sigma'_u$, which is positive under D4.
- **(d)** $\mathcal Ad=d/T$, so $L=\lVert d\rVert^2/T>0$ whenever $d\ne0$.

In words: **the complex model wins iff its extra logit signature has nonzero weighted partial covariance with the attenuation pattern $\tfrac12v\beta_t^2(1-2\pi_t)$, after partialling out the simple model's own logit signatures.** If $e$ lies in the span of the simple model's signatures on the whole design (design absorption), then $\mathbf M_Se=0$ and there is no gap for any context law.

*Proof.*
- (a) Product-family scores are $\sum_t(\partial\eta_t/\partial\phi)(y_t-\pi_t)$, and independence under $p_0$ gives the inner-product formula. $h_D$ is a sum of products of two distinct centered coordinates, orthogonal to every first-order function. The projection of $h_A=\sum_ta_t(y_t-\pi_t)$ is therefore the $\Omega$-weighted least-squares projection of $\mathbf a$.
- (b) Theorem 2.6 plus the one-column Frisch–Waugh–Lovell identity; also $\Lambda=\varepsilon^2\langle h-P_Sh,s_e\rangle+O(\varepsilon^3)=\varepsilon^2\langle\mathbf a-P_S\mathbf a,e\rangle_\Omega+O(\varepsilon^3)$.
- (c) Pythagoras.
- (d) For first-order $f$, $(I-E_0[\,\cdot\mid Y_{-t}])f=c_t(y_t-\pi_t)$, so $\mathcal Af=f/T$.
- H1–H2 hold for full-rank affine-logit product families: near an interior point, the observable image is an open piece of an embedded affine family in logit coordinates. $\square$

Numerically (check L1; $T=3$, two context-retaining cells, skewed and symmetric $V$), the exact $R_S$, $R_K$, $\Delta_J$ and $\Lambda$ converge to these formulas. At $\varepsilon=0.006$ the ratios are within about 2% for skewed $V$ (error $O(\varepsilon)$) and within 0.1% for symmetric $V$ (error $O(\varepsilon^2)$). In that design $\lVert d\rVert^2=4.7\times10^{-4}$ versus $\lVert h_D\rVert^2=1.37$. The complex model removes only a sliver of the simple model's misfit; most of it is dependence that no homogeneous model can absorb.

---

## Part III. From population gaps to BIC, Bayes factors and trial LOO

**Setup.**

- Cells are $j=(w,y)$; there are $N=\lvert\mathcal W\rvert2^T$ of them, with $r_j=H(w)p(y\mid w)>0$ and empirical frequencies $\hat r_j$.
- For a law $q$, $\ell(q)=\sum_jr_j\log q_j$ and $\hat\ell_n(q)=\sum_j\hat r_j\log q_j$.
- $\ell_M^\star=\sup_{\mathcal Q_M}\ell=-R_M-\mathrm{Ent}_P(Y\mid W)$, so $\Delta_J=\ell_K^\star-\ell_S^\star$; and $\ell_{M,n}(\phi)=n\hat\ell_n(q_M(\phi))$.
- Independence across participants is used; independence of a participant's trials never is.

**Lemma 3.1 (cell frequencies).** $P(\max_j\lvert\hat r_j-r_j\rvert>u)\le2N\exp(-2nu^2)$.

*Proof.* Hoeffding's inequality for each indicator mean, plus a union bound. $\square$

**Lemma 3.2 (uniform law of large numbers on law space).**

- **(a)** $\sup_{\mathcal Q_M}\hat\ell_n\to_p\ell_M^\star$.
- **(b)** If every candidate cell is at least $\underline q>0$ (for example on compact parameter boxes), then $\sup_{\mathcal Q_M}\lvert\hat\ell_n-\ell\rvert\le\bar\ell\,\lVert\hat r-r\rVert_1$, where $\bar\ell=\log(1/\underline q)$.

*Proof.* (b) is immediate. For (a), use small-cell exclusion. On $\{\hat r\ge r_{\min}/2\}$, any $q$ with a cell below $\epsilon_0$ has $\hat\ell_n(q)\le(r_{\min}/2)\log\epsilon_0$, which is below $\ell_M^\star-2$ for small $\epsilon_0$. On the set of laws with all cells $\ge\epsilon_0$, apply (b) ([L4 of the separation attempt](primary_separation_attempt_2026-09-08.md)). $\square$

**Theorem 3.3 (BIC).** Let $D_n=\sup\ell_{K,n}-\sup\ell_{S,n}$ and $\kappa=k_K-k_S$.

- **(a) Exact threshold.** $K$ has smaller BIC iff $2D_n>\kappa\log n$.
- **(b) Limit.** $D_n/n\to_p\Delta_J$, so $(\mathrm{BIC}_K-\mathrm{BIC}_S)/n\to_p-2\Delta_J$, and $P(\text{BIC selects }K)\to1$ when $\Delta_J>0$.
- **(c) Quantitative bound** (cell floor $\underline q$). If $g_n=\Delta_J-\kappa\log n/(2n)>0$, then
  $$P(\text{BIC does not select }K)\le2N\exp\{-ng_n^2/(2\bar\ell^2N^2)\}.$$

*Proof.* (a) is algebra. (b) By Lemma 3.2(a), $D_n/n=\sup_{\mathcal Q_K}\hat\ell_n-\sup_{\mathcal Q_S}\hat\ell_n\to_p\ell_K^\star-\ell_S^\star=\Delta_J$. (c) With a cell floor, a supremum over a set moves by at most the sup-norm error, so $\lvert D_n/n-\Delta_J\rvert\le2U_n$ with $U_n=\max_M\sup_{\mathcal Q_M}\lvert\hat\ell_n-\ell\rvert\le\bar\ell N\max_j\lvert\hat r_j-r_j\rvert$ (Lemma 3.2(b)). Failure forces $2U_n\ge g_n$; apply Lemma 3.1. $\square$

BIC is treated as a computed criterion; no claim is made that it approximates the log evidence. That would need regular geometry, which latent hierarchies can violate.

**Theorem 3.4 (Bayes factor).** $n^{-1}\log m_M\to_p\ell_M^\star$. Hence $n^{-1}\log\mathrm{BF}_{KS}\to_p\Delta_J$ and $P(\mathrm{BF}_{KS}>1)\to1$ when $\Delta_J>0$.

*Quantitative version (cell floor).* Let $V=\{\phi:\ell(q_K(\phi))>\ell_K^\star-\Delta_J/2\}$ and $\pi_V=\Pi_K(V)>0$. If $g_n'=\Delta_J/2-\log(1/\pi_V)/n>0$, then
$$P(\mathrm{BF}_{KS}\le1)\le2N\exp\{-ng_n'^2/(2\bar\ell^2N^2)\}.$$

*Proof.*
- Upper bound: $m_M\le\exp(n\sup\hat\ell_n)$, because the prior is a probability measure.
- Lower bound: for $\delta>0$ let $V_\delta$ be a law-neighbourhood of the optimum on which $\ell>\ell_M^\star-\delta$ and cells are bounded below. T2 gives $\Pi(V_\delta)>0$, and $m_M\ge\Pi(V_\delta)\exp\{n(\ell_M^\star-\delta-\sup_{V_\delta}\lvert\hat\ell_n-\ell\rvert)\}$, where the last supremum tends to 0 in probability by Lemma 3.2(b) because cells are bounded below on $V_\delta$.
- Divide logs by $n$, let $n\to\infty$, then let $\delta\downarrow0$.
- The quantitative bound follows as in Theorem 3.3 from $\log\mathrm{BF}_{KS}\ge\log\pi_V+n(\Delta_J/2-2U_n)$. $\square$

No Laplace approximation or regularity is needed for the exponential rate. A sharper $\tfrac\kappa2\log n$ correction would need them.

**Lemma 3.5 (exact single-response deletion).**
$$p_M(y_{it}\mid D_{-it})=\int\frac{q_M(y_i\mid W_i;\phi)}{q_{M,-t}(y_{i,-t}\mid W_i;\phi)}\,\Pi_M(d\phi\mid D_{-it})=\frac{m_M(D)}{m_M(D_{-it})},$$
where $\Pi_M(\cdot\mid D_{-it})$ uses $q_{M,-t}(y_{i,-t})$ for participant $i$ and full response vectors for everyone else. The participant effect is learned from the retained responses ([L3 of the separation attempt](primary_separation_attempt_2026-09-08.md)). $\square$

**Lemma 3.6 (uniform deletion stability).** Under T1–T3,
$$\max_{i,t}\Big\lvert p_M(y_{it}\mid D_{-it})-\frac{q_M^\star(y_i\mid W_i)}{q^\star_{M,-t}(y_{i,-t}\mid W_i)}\Big\rvert\to_p0,$$
and with probability tending to one every prediction exceeds $q^\star_{\min}/2$, where $q^\star_{\min}>0$ is the smallest cell of $q_M^\star$.

*Proof sketch* ([L5](primary_separation_attempt_2026-09-08.md)):
1. Lemma 3.2 plus uniqueness gives a likelihood gap $g$ outside any law-neighbourhood $U$ of $q_M^\star$. Let $V$ be a smaller neighbourhood with positive prior mass on which $\ell\ge\ell_M^\star-g/4$. On events with probability tending to one, the full posterior puts mass at most $\Pi(V)^{-1}e^{-3ng/4}$ outside $U$.
2. Deleting a whole participant changes every cell frequency by at most $1/(n-1)$, deterministically. One frequency event therefore controls all $n$ participant-deleted posteriors $\Pi_{-i}$; no union bound over separate events is needed.
3. The response-deleted posterior is $\Pi_{-i}$ tilted by $q_{-t}(y_{i,-t})\le1$. Its normalizer is at least $(q^\star_{\min}/2)\,\Pi_{-i}(V_0)$, so $\Pi_{-it}(U^c)\le2\Pi_{-i}(U^c)/(q^\star_{\min}\Pi_{-i}(V_0))$.
4. The prediction functional is continuous near $q_M^\star$, with denominator bounded below. $\square$

**Theorem 3.7 (exact trial LOO).** Under T1–T3, $(\mathrm{ELPD}_K-\mathrm{ELPD}_S)/(nT)\to_p\Delta_C$. Hence $(\mathrm{LOOIC}_K-\mathrm{LOOIC}_S)/(nT)\to_p-2\Delta_C$, and $P(\text{trial LOO selects }K)\to1$ when $\Delta_C>0$.

*Proof.* Lemma 3.6 and the Lipschitz property of $\log$ on $[q^\star_{\min}/2,1]$ give $\mathrm{ELPD}_M/(nT)=n^{-1}\sum_iH_M(W_i,Y_i)+o_p(1)$, where
$$H_M(w,y)=T^{-1}\sum_t\log\frac{q_M^\star(y\mid w)}{q^\star_{M,-t}(y_{-t}\mid w)}$$
is a bounded function of the participant cell. The cell law of large numbers (Lemma 3.1) gives convergence to $EH_M$, and the true conditional entropy cancels in the $K-S$ difference, leaving $\Delta_C$. A participant's trials are never treated as independent. $\square$

**Corollary 3.8 (systematic false-complex selection; spurious significance and estimates).** Assume (M1) and (M3), with T1–T3.

- **(a)** $P(\text{all three select }K)\ge1-\sum(\text{failure probabilities})\to1$. No independence among the criteria is assumed.
- **(b)** The likelihood-ratio statistic for $\rho=1$ is $2D_n=2n\Delta_J+o_p(n)\to\infty$. Any test that rejects "no distortion" when $2D_n$ exceeds a fixed critical value (for example a $\chi^2$ quantile) rejects with probability tending to one.
- **(c)** Suppose $\rho$ is a continuous function of the law near $q_K^\star$ (identifiable from the observable law) and T3 holds. Then $\hat\rho_{\rm MLE}\to_p\rho_K^\star$, and the posterior of $\rho$ concentrates at $\rho_K^\star\ne1$. The analyst estimates a "distortion" that is purely an artifact of omission.

*Proof.* (a) Union bound over Theorems 3.3, 3.4 and 3.7. (b) Theorem 3.3(b). (c) Law-space consistency: with probability tending to one, empirical near-maximizers lie in any neighbourhood $U$ of the unique optimal law (Lemma 3.2 plus the gap outside $U$), and so does posterior mass (Lemma 3.6, step 1). Compose with the continuous map from law to $\rho$. $\square$

**Corollary 3.9 (context-aware dominance when context is measured).** Suppose $C$ has finite support and is observed. Apply Part III with $W'=(W,C)$. Then $R'_{S^C}=0$ and $R'_K=R_K+I(Y;C\mid W)>0$ (Proposition 1.6), so BIC and BF prefer $S^C$ with probability tending to one.

Trial LOO prefers $S^C$ as well, provided $K$'s conditional predictions differ from the truth's on a set of positive probability. This holds whenever $U\equiv0$ and $p(y_t\mid w,c)$ varies with $c$ for some $t$. In that case the truth's conditionals given $(w,c)$ are the marginals $p(y_t\mid w,c)$, while $K$'s do not depend on $c$. $\square$

**Remark 3.10 (finite samples: what the limits do and do not say).** Theorems 3.3–3.7 are first-order statements; at realistic $n$ the gap competes with penalties and noise. The following heuristics use standard regular misspecified-likelihood expansions and are **not theorems** (check I1, witness of Part V).

1. **Noise.** The pseudo-true log-likelihood ratio $\sum_i\log\{q_K^\star(Y_i\mid W_i)/q_S^\star(Y_i\mid W_i)\}$ is approximately $N(n\Delta_J,n\sigma^2)$, with $\sigma=0.0355$ per participant. In the local regime $\sigma^2\approx2\Delta_J$; here $0.00126$ versus $0.00140$.
2. **Fitting bonus.** Refitting adds an expected in-sample bonus $b=\tfrac12[\mathrm{tr}(\mathbf G_K^{-1}V_K)-\mathrm{tr}(\mathbf G_S^{-1}V_S)]=0.449$ to $D_n$. Here $V$ is the participant-score covariance, and the traces are $2$ for $K$ and $1.103$ for $S$.
3. **Penalties.**
   - BIC: $\tfrac\kappa2\log n$.
   - Trial LOO: $\mathrm{tr}(\mathbf G_K^{-1}V^{\rm trial}_K)-\mathrm{tr}(\mathbf G_S^{-1}V^{\rm trial}_S)=2-1.009$, a Takeuchi-type penalty with trial-level score variance.
   - BF (Laplace): $\tfrac\kappa2\log n-c_0$, with $c_0=\log\frac{\pi_K(\theta_K^\star,\delta_K^\star)}{\pi_S(\theta_S^\star)}+\tfrac12\log2\pi-\tfrac12\log\frac{\det\mathbf G_K}{\mathbf G_S}=-0.052+0.919+1.537=2.40$. The large last term reflects weak identification of the extra parameter: its partial information is $0.046$ per participant.

| Participants | BIC | BF (Laplace) | trial LOO (TIC) | Pilot, 10 replicates: BIC / BF / LOO |
|---:|---:|---:|---:|---|
| 1,000 | 0.02 | 0.53 | 0.56 | 1/10 / 7/10 / 8/10 |
| 10,000 | 0.79 | 0.93 | 0.97 | not run |

These approximations explain the pilot's otherwise puzzling ordering ([`minimal_ambiguity_validation.md`](minimal_ambiguity_validation.md)). At these sample sizes BF and trial LOO have $O(1)$ effective penalties and select the false complex model far more often than BIC, whose penalty grows like $\tfrac12\log n$. The expected likelihood gain $n\Delta_J$ first exceeds BIC's penalty at $n\approx6{,}300$; trial LOO reaches 80% selection near $n\approx3{,}200$. The Laplace BF figure is unreliable at small $n$, where the $\delta$ posterior is truncated by the prior box. Rule of thumb: $O(1)$-penalty criteria need $n\approx2z^2/\Delta_J$, and BIC additionally needs $n\Delta_J>\tfrac\kappa2\log n$. Because $\Delta_J\propto\varepsilon^4$ for homogeneous simple models and is $O(\varepsilon^6)$ or smaller for hierarchical ones (Proposition 4.3), the required $n$ grows like $\varepsilon^{-4}$ and at least $\varepsilon^{-6}$, respectively.

By contrast, the rigorous bound of Theorem 3.3(c) needs $n\approx2.7\times10^{10}$ for at most 5% failure: valid but uninformative.

---

## Part IV. Boundaries: when the mechanism switches off

**Proposition 4.1 (representable heterogeneity: no gap).** If $p\in\overline{\mathcal Q}_S$, then $R_S=R_K=0$ and $\Delta_J=\Delta_C=0$. Examples:

- $\gamma=0$ with a representable residual;
- Gaussian context with affine mean and constant variance, fitted by a normal shared-effect $S$ ([L1 of the separation attempt](primary_separation_attempt_2026-09-08.md)).

First-order criteria are then silent; finite-sample preferences are governed by penalties and priors. $\square$

**Proposition 4.2 (observable absorption: no gap for any context law).** If $\mathcal Q_K=\mathcal Q_S$, then $\Delta_J=0$ for every data-generating process. Locally, if $e\in\mathrm{col}(\mathbf J_S)$ on the whole design (Corollary 2.7), then $\mathbf M_Se=0$ and $d=0$ for every $h$. Existing instances: the two-trial opposite-side design and the full-support all-$\rho$ absorption ([design audit](design_absorption_audit_2026-09-08.md)). The eight-trial calibrated design breaks absorption ([manifest](cognitive_design_manifest.md)). $\square$

**Proposition 4.3 (a free-variance random effect absorbs the leading term).** Suppose:

- $S$ contains a normal working random effect on $\Theta$ with free variance, the same kernel, and a mean structure that represents $\bar\theta(w)$;
- the heterogeneity is homoskedastic: $\mathrm{Var}(\Theta\mid W=w)=\varepsilon^2\bar v$.

Then $R_S=O(\varepsilon^6)$ ($O(\varepsilon^8)$ if $V$ is symmetric with $EV^4<\infty$), hence $\Delta_J\le R_S=O(\varepsilon^6)$. Against a hierarchical simple model the false-complex advantage is at least two orders smaller in $\varepsilon$ than the $\varepsilon^4$ advantage against a homogeneous one.

*Proof.*
1. Compare with the $S$ law of mean $\bar\theta(w)$ and variance $\varepsilon^2\bar v$. Its density ratio to $p_0$ is $1+\tfrac12\varepsilon^2\bar v\,g''/g+O(\varepsilon^4)$, because odd normal moments vanish.
2. The truth's ratio is $1+\tfrac12\varepsilon^2\bar v\,g''/g+(\varepsilon^3/6)\kappa_3g'''/g+O(\varepsilon^4)$, with $\kappa_3=EV^3$.
3. The two ratios differ by $O(\varepsilon^3)$, or by $O(\varepsilon^4)$ if $\kappa_3=0$. The KL expansion in step 3 of Theorem 2.6 gives $\mathrm{KL}=O(\varepsilon^6)$ (respectively $O(\varepsilon^8)$).
4. Finally $R_S\le\mathrm{KL}$ and $\Delta_J\le R_S$. $\square$

Numerically (check H1): $\mathrm{KL}/\varepsilon^6\to1.32$ (skewed $V$) and $\mathrm{KL}/\varepsilon^8\to2.80$ (symmetric $V$), versus homogeneous $R_S/\varepsilon^4\to0.99$–$1.04$. At $\varepsilon=0.1$ the hierarchical bound is $1.2\times10^{-6}$ (skewed) or $2.5\times10^{-8}$ (symmetric), against about $10^{-4}$ for a homogeneous $S$.

*Interpretation:* the hierarchical route (the PI's G1 pair) must rely on one of two things. Either the context mixture has a non-Gaussian **shape** (skewness or multimodality, for example a binary context with a large effect), or there is heteroskedasticity across retained covariates, which is subject to Proposition 4.4.

**Proposition 4.4 (parity obstruction for context-dependent dispersion).** Assume:

- $Z=\pm1$ with $H(\pm1)=\tfrac12$ and a common design;
- both candidates retain $Z$ through a latent mean $\mu_0+\mu_1Z$;
- $S$ is hierarchical with constant working variance $\sigma^2$, and $K$ adds one global parameter;
- the truth is $S$'s working law with mean $\mu_0$ and variance $\bar v+\lambda Z$ (context-dependent dispersion, the M3 structure).

At the $Z$-symmetric baseline $\mu_1=0$, under H1–H2 there, $\Delta_J(\lambda)=o(\lambda^2)$ while $R_S(\lambda)=\tfrac{\lambda^2}2\lVert h-P_Sh\rVert^2+o(\lambda^2)$.

*Proof.* The baseline laws coincide across $Z$. Then:

- $h=Z\,s_{\sigma^2}(y)$ is $Z$-odd;
- the scores of $\mu_0$, $\sigma^2$ and $K$'s extra parameter are $Z$-even;
- the score of $\mu_1$ is $Z\,s_{\mu_0}(y)$.

With equal weights, $Z$-odd and $Z$-even functions are orthogonal. So $P_Kh$ and $P_Sh$ both equal the projection of $h$ onto $\mathrm{span}\{Zs_{\mu_0}\}$, and $d=0$. Apply the first-order version of Theorem 2.6, with perturbation $\lambda h$ in place of $\varepsilon^2h$. $R_S>0$ to leading order iff $s_{\sigma^2}\notin\mathrm{span}\{s_{\mu_0}\}$, which holds generically. $\square$

Numerically (check H2, $T=3$): $\lVert d\rVert^2\approx3\times10^{-33}$, while $\lVert h-P_Sh\rVert^2=0.142$ and the extra score is not absorbed ($\lVert s_e-P_Ss_e\rVert^2=0.079$). With $\mu_1=0.5$, $\lVert d\rVert^2=0.0049$.

*Implication for the M2/M3-versus-M4 plan:* under context symmetry, a context-free distortion parameter cannot mimic context-dependent dispersion to first order. Omitted dispersion makes $S$ wrong without favouring $K$. Asymmetry ($\mu_1\ne0$ or unequal context weights) or higher-order effects are needed.

**Proposition 4.5 (trial LOO can disagree with BIC and BF).** There are nested families with $\Delta_J>0>\Delta_C$ at the global joint fits (Lemma 2.2). Under T1–T3, BIC and BF then select $K$ while trial LOO selects $S$, each with probability tending to one. "All three criteria agree" therefore requires (M3) separately whenever participant effects are present. $\square$

**Remark 4.6 (zero gaps and shrinking effects).** When $\Delta_J=0$ the first-order theorems are silent; the pilot's context-null cells are of this kind. The same holds in the symmetric boundary where $\Theta$ is symmetric about the indifference point: in the witness's design, all marginals then equal $1/2$ exactly, and $S$ matches them. If $\varepsilon=\varepsilon_n\to0$, selection still follows when $n\Delta_J(\varepsilon_n)$ outgrows $\log n$ (BIC) and the $\sqrt n$ fluctuation scale. A uniform-in-$\varepsilon$ version of Part III is not proved here.

---

## Part V. The explicit ambiguity witness

**Theorem 5.1.** Use the setup of [`minimal_ambiguity_proof.md`](minimal_ambiguity_proof.md) §1–2:

- $T=2$ gain-only ambiguity trials with widths $1/2$ and $1$, so $x=(1,2)$;
- fixed $\tau=4$, intercept and side effect fixed at 0;
- truth $\theta_i=C_i\log3$ with $C\sim\mathrm{Bern}(1/2)$, and $\rho=1$;
- $S$: logit $-\theta x_t$; $K$: logit $\delta(\rho)-\theta x_t$, with $\delta(\rho)=4[w(1/2;\rho)-1/2]$;
- uniform priors on $\theta\in[0,2]$ and $\rho\in[\rho_L,\rho_U]$.

All hypotheses of Theorem 0(a) hold, with the values below.

| Quantity | Value | Result |
|---|---|---|
| Cells $(00,10,01,11)$ | $(37,19,13,11)/80$ | Lemma 1.1 |
| $\mathrm{Cov}(Y_1,Y_2)$; multi-information $I_P$ | $1/40$; $0.006270$ | Prop. 1.3 |
| Kernel logits at $\bar\theta=\tfrac12\log3$ | $(-0.549,-1.099)$ | Cor. 1.5 |
| True marginal logits (attenuation) | $(-0.511,-0.847)$, shifts $(+0.038,+0.251)$ | Cor. 1.5 |
| $\theta_S^\star$ | $0.4429$ (interior, unrestricted) | Lemma 2.1 |
| $(\theta_K^\star,\delta_K^\star)$ | $(\log\tfrac75,\log\tfrac{21}{25})=(0.3365,-0.1744)$ | exact marginal match |
| $\rho_K^\star$ | $0.663$ (inverse-S) | Cor. 3.8(c) |
| Extra-score drift $\Lambda$ ($\delta$ coordinate) | $-0.00802$ | Thm. 2.4 |
| $R_S$; $R_K$ | $0.006968$; $0.006270=I_P$ | (M2) |
| $\Delta_J$ | $6.985\times10^{-4}$ per participant | (M1) |
| $\Lambda^2/(2\bar B)\le\Delta_J$; $\Lambda^2/(2\mathcal I_{\rho\mid S})$ | $6.42\times10^{-4}$; $6.97\times10^{-4}$ | Prop. 2.5 |
| $\Delta_C$ | $3.493\times10^{-4}$ per trial $=\Delta_J/2$ | Lemma 2.3, (M3) |
| $I(Y;C\mid W)$ | $0.1293$ | Prop. 1.6 |
| Local $\varepsilon^4$ formula at $\varepsilon=\tfrac12\log3$ | $\Delta_J\approx1.08\times10^{-3}$ (exact/local $=0.65$) | Cor. 2.7 |

**Transfer conditions.**

- The compact boxes keep every candidate cell at or above $\sigma(-9/2)^2$, so T1 holds and Theorem 3.3(c) applies.
- The uniform priors are proper with positive density (T2).
- Strict concavity in $(\theta,\delta)$ gives unique optimal laws (T3).

Hence conclusions 1–6 of Theorem 0 hold. $\square$

On this design distortion is observationally an offset, because both trials use $p=1/2$. The witness demonstrates false-complex selection, not identification of probability distortion ([M1 review](proof_reviews/review_minimal_ambiguity.md)).

---

## Part VI. What it would take: gap ledger and recommended architecture

### Status of each step in this draft

| Step | Status here | What remains |
|---|---|---|
| Lemma 1.1, Lemma 1.2, Prop. 1.6 | Proved (standard) | — |
| Prop. 1.3 (dependence; homogeneous models false) | Proved | Review |
| Thm. 1.4, Cor. 1.5 (attenuation + dependence) | Proved; checked numerically (E1) | Review; general (non-logistic) kernels need bounded third derivatives |
| Lemmas 2.1–2.3, Thm. 2.4 | Proved | Review |
| Prop. 2.5 (gap from drift) | Lower bound proved; asymptotic form via Thm. 2.6 | Review; non-affine $\rho$ paths need an extra curvature term |
| Thm. 2.6 | Proved conditional on H1–H2 (adapts the reviewed smooth extension) | Verify H1–H2 for each application |
| Cor. 2.7 (WLS criterion) | Proved; checked numerically (L1) | Evaluate on RAID-like designs once coding is resolved |
| Lemmas 3.1–3.2, Thms. 3.3–3.4 | Proved, with explicit exponential bounds | Sharper constants are optional |
| Lemma 3.5, Lemma 3.6, Thm. 3.7 | Restated from existing author proofs (sketch for 3.6) | Independent review of L3–L6 |
| Cor. 3.8–3.9 | Proved | — |
| Remark 3.10 | Heuristic only | Confirm by predeclared simulation |
| Props. 4.1, 4.2, 4.5 | Proved / cited | — |
| Props. 4.3, 4.4 | Proved (4.4 conditional on H1–H2 at the baseline); checked (H1, H2) | Review |
| Thm. 5.1 | Proved (exact plus numerics) | Already author-reviewed in the M1 review |

### Recommended final architecture

1. **Theorem A (homogeneous candidates; complete).** Theorem 0 with case (a). It is proved here for finite designs. The witness shows it is not vacuous, and Corollary 2.7 makes the mechanism condition checkable on any finite design, including RAID once coded. This is the strongest unconditional statement available now. It already goes all the way from omission to systematic misselection by BIC, BF and trial LOO.
2. **Theorem B (hierarchical candidates; conditional).** Theorem 0 with case (b), with Propositions 4.3–4.5 as the honest boundary: the effect is higher-order and parity-constrained. Making B unconditional for the G1 pair requires:
   1. H1–H2 on a non-absorbed design (the eight-trial manifest is the natural candidate);
   2. a context law with skew or multimodality, or asymmetric heteroskedasticity, giving $\Lambda\ne0$ at the **hierarchical** $S$ projection;
   3. $L>0$, or a direct conditional computation;
   4. uniqueness of the optimal laws.
3. **Transfer theorems.** Complete for finite support and fixed $T$ (Part III).
4. **Simulation.** Report finite-$n$ behaviour, guided by the rule of thumb in Remark 3.10, rather than asymptotic claims.

### Open problems

- **O1. Hierarchical cognitive witness** (above). The hardest item, and the most important for the M1–M5 empirical suite.
- **O2. Continuous designs and covariates.** Needs a Glivenko–Cantelli argument for integrated log-likelihoods, with envelopes, in place of cell counts.
- **O3. Growing task length $T$.** For homogeneous candidates with fixed design composition, $\Delta_J$ grows linearly in $T$ and $\Delta_C=\Delta_J/T$ is $T$-invariant (Lemma 2.3); misselection persists for each $T$. For hierarchical candidates, a conjecture: retained trials reveal $\theta_i$, so $K$'s trial-conditional advantage shrinks as $T$ grows ($\Delta_C(T)\to0$ when $S$'s kernel is correct), while the joint gap depends on how the shape of $F$ mismatches $S$'s working family. The research specification's target ("even as behavioral-task length increases") therefore likely holds for homogeneous or inflexible candidates. It needs a separate theorem, or a revised target, for hierarchical ones.
- **O4. Fitted-score uncertainty for trial LOO.** Needs a cluster CLT including fitting effects.
- **O5. Shrinking effects.** Uniformity in $\varepsilon$, and finite-sample rates for LOO.
- **O6. Independent review** of the results that are new in this draft: Thm. 1.4, Thm. 2.4, Prop. 2.5, Cor. 2.7 and Props. 4.3–4.4.

---

## Appendix A. Verification summary

Run `python3 scripts/verify_central_theorem_draft.py` (dependency-free). Every check passed on 2026-10-02; its output is in [`logs/theory_checks/2026-10-02_central_theorem_draft.json`](../logs/theory_checks/2026-10-02_central_theorem_draft.json).

| Check | What it verifies |
|---|---|
| I1 | Exact rational cells and covariance; projections; $R_K=I_P$; direct conditional gap $=\Delta_J/2$; drift and Prop. 2.5 bounds; $\rho_K^\star$; Prop. 1.6 identity; Remark 3.10 heuristics |
| E1 | Thm. 1.4 closed form against exact mixtures (remainder orders 1 and 2); finite-difference check of $\tfrac12v\,g''/g$; zero means and cross-moment; exact positive covariances |
| L1 | Thm. 2.6 and Cor. 2.7 for homogeneous candidates: risk, gap, multi-information and drift ratios converge to 1; $\Delta_C=\Delta_J/T$; Lemma 2.3 identity; Prop. 2.5 bound in every row |
| H1 | Prop. 4.3: hierarchical comparator KL scales as $\varepsilon^6$ (skewed) and $\varepsilon^8$ (symmetric), against $\varepsilon^4$ for homogeneous $S$ |
| H2 | Prop. 4.4: $d=0$ at the $Z$-symmetric baseline with $S$ false and the extra score unabsorbed; $d\ne0$ when the symmetry is broken |

These checks test algebra and orders of magnitude. They do not certify global optimality in general, prove a theorem, or replace review.

## Appendix B. Background references

All entries are background only, **not yet verified against source** under [`literature_verification_policy.md`](literature_verification_policy.md). None closes a proof obligation above.

- Chesher, A. (1984). Testing for neglected heterogeneity. *Econometrica*, 52(4), 865–872. Neglected-heterogeneity direction (Thm. 1.4).
- Cox, D. R. (1983). Some remarks on overdispersion. *Biometrika*, 70(1), 269–274. Small-dispersion mixture expansions.
- White, H. (1982). Maximum likelihood estimation of misspecified models. *Econometrica*, 50(1), 1–25. Pseudo-true KL projections.
- Vuong, Q. H. (1989). Likelihood ratio tests for model selection and non-nested hypotheses. *Econometrica*, 57(2), 307–333. Log-likelihood-ratio normal approximation (Remark 3.10).
- Sin, C.-Y., & White, H. (1996). Information criteria for selecting possibly misspecified parametric models. *Journal of Econometrics*, 71(1–2), 207–225. BIC-type selection under misspecification.
- Berk, R. H. (1966). Limiting behavior of posterior distributions when the model is incorrect. *Annals of Mathematical Statistics*, 37(1), 51–58. Posterior concentration at KL minimizers.
- Kass, R. E., & Raftery, A. E. (1995). Bayes factors. *Journal of the American Statistical Association*, 90(430), 773–795. Laplace approximation (Remark 3.10).
- Vehtari, A., Gelman, A., & Gabry, J. (2017). Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC. *Statistics and Computing*, 27(5), 1413–1432.
- Zeger, S. L., Liang, K.-Y., & Albert, P. S. (1988). Models for longitudinal data: A generalized estimating equation approach. *Biometrics*, 44(4), 1049–1060. Attenuation of population-averaged logistic effects.
- Neuhaus, J. M., Kalbfleisch, J. D., & Hauck, W. W. (1991). A comparison of cluster-specific and population-averaged approaches for analyzing correlated binary data. *International Statistical Review*, 59(1), 25–35.
- Estes, W. K. (1956). The problem of inference from curves based on group data. *Psychological Bulletin*, 53(2), 134–140. Averaging artifacts in cognitive data.
- Heathcote, A., Brown, S., & Mewhort, D. J. K. (2000). The power law repealed: The case for an exponential law of practice. *Psychonomic Bulletin & Review*, 7(2), 185–207.
- Prelec, D. (1998). The probability weighting function. *Econometrica*, 66(3), 497–527.
- Hoeffding, W. (1963). Probability inequalities for sums of bounded random variables. *Journal of the American Statistical Association*, 58(301), 13–30.
