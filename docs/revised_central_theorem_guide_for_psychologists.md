# A psychologist's guide to the central theorem

*How leaving context out of a cognitive model can make standard model comparison prefer a false, more complex model — explained one equation at a time.*

Date: 2026-10-29. This guide accompanies the **revised manuscript**, [`manuscript/revised/revised_central_theorem.tex`](../manuscript/revised/revised_central_theorem.tex) (compiled: [PDF](../manuscript/revised/revised_central_theorem.pdf)), with the 29 October audit fixes applied. Every result is referred to by the number it has there (Lemma 2.2, Theorem 4.1, …). It replaces the earlier guide, which followed a superseded draft.

**Status.** The manuscript has been checked by its authors, by an independent audit, and by computer, but not yet by an outside mathematician. Where the guide says "proved", read "proved in the manuscript, pending external review."

---

## How to read this guide

The theorem is not one result but a short chain. Each link takes something established earlier and turns it into something new. For every equation the guide tells you:

1. **What it says** in ordinary words.
2. **What each symbol means.**
3. **What job it does in the argument.**

One small example — the *witness* — runs through the guide. All its numbers can be checked with a calculator. When a general statement feels abstract, return to the witness: the general step is always the same idea with more symbols.

You need only three things: what a probability is, what an average is, and the idea of fitting a model by making its predictions match data. Part 1 builds everything else. Skip any item you already know.

**The map of the chain:**

| Step | Manuscript | What it establishes |
|---|---|---|
| 1 | Lemma 2.1 | Omitting context turns each person's data into a *mixture* |
| 2 | Lemmas 2.1–2.2 | The mixture creates within-person dependence, so every model without person-level effects is wrong |
| 3 | Theorem 3.1 | An exact example in which the false complex model wins |
| 4 | Theorem 4.1 | Why BIC, Bayes factors and leave-one-out all follow the population winner |
| 5 | Theorem 5.1, Prop. 5.3 | A general test for when the complex model wins, and how much it wins by |
| 6 | Lemma 6.1, Theorem 6.2 | *Why* it wins: the shape that omitted context gives the data, and a regression-like criterion |
| 7 | Section 7 | What changes when the models include person-level (random) effects |
| 8 | Corollary 8.1 | The context-aware simple model is correct and wins when context is measured |

---

## Part 0. The claim in plain words

Cognitive models describe decisions with a few psychological parameters. In ambiguity tasks, each person typically gets an **ambiguity aversion** parameter: how much they dislike options whose probabilities are unknown.

Suppose a person's **context** — socioeconomic resources, how uncertain their environment has been — shifts their ambiguity aversion, and suppose the model leaves context out. The manuscript proves:

> When context shifts a cognitive parameter but is left out of the model, the data take on a shape the true, simple cognitive model cannot reproduce. A more complex model — for example one with **probability distortion** — can sometimes reproduce part of that shape. When it can, BIC, Bayes factors and trial-level leave-one-out cross-validation all prefer the complex model, and the preference becomes **certain** as the number of participants grows. The complex model is still wrong: the process that generated the data has no distortion at all. The simple model *with context included* is exactly right and beats it.

Three qualifications are built into the theorem and are as important as the headline:

- **It can happen, not it must happen.** Whether a given complex model gains depends on the task design and on how its extra parameter interacts with the shape omission creates (Steps 5–6).
- **The fully proved case is models without person-level effects.** For models with random effects, the manuscript proves the selection result *conditional* on two inequalities that still need to be established for the project's specific models (Step 7).
- **The example shows false complexity, not true distortion.** In the minimal example, "probability distortion" acts as a simple shift; the example shows that an unnecessary parameter gets selected, not that people distort probabilities.

---

## Part 1. The toolkit

### 1.1 The latent parameter θ and the choice rule

**Ambiguity aversion** is written $\theta$ ("theta"). Upper-case $\Theta$ means the parameter as something that varies across people; lower-case $\theta$ means one value.

The manuscript's equation (1) says the probability of choosing the ambiguous option on trial $t$ is

$$\Pr(Y_t=1\mid\Theta=\theta,W=w,C)=\pi_t(\theta,w)=\operatorname{expit}\{\kappa_t(w)-\beta_t(w)\theta\}.$$

- $Y_t=1$ means the ambiguous option was chosen on trial $t$; $Y_t=0$ means the other option.
- $W$ is everything the researcher **does** record: the trial design and any covariates in the model. $C$ is the context, which the models **omit**.
- $\kappa_t$ ("kappa") collects everything that makes the ambiguous option attractive apart from ambiguity (payoffs, stated probabilities, screen side).
- $\beta_t$ ("beta") is how much ambiguity trial $t$ carries. A more averse person (larger $\theta$) finds the option less attractive, and more so on more ambiguous trials.
- $\operatorname{expit}(x)=1/(1+e^{-x})$ turns any score into a probability: a score of 0 gives 0.5, large positive scores approach 1, large negative scores approach 0. It is the familiar S-curve of logistic regression. Its inverse is the **logit** (log-odds), $\operatorname{logit}(p)=\log\{p/(1-p)\}$.

The vertical bar "$\mid$" means "given." Notice that $C$ appears to the right of the bar but not on the right-hand side of the equation: **context affects choices only through $\theta$.**

### 1.2 The latent equation

$$\Theta=a_0+a_1Z+\gamma C+U.$$

A person's aversion is a baseline $a_0$, plus an effect of a recorded covariate $Z$, plus an effect $\gamma$ ("gamma") of context $C$, plus everything else $U$ (individual differences the model does not explain). The theorem is about what happens when $\gamma C$ is real but the model leaves it out.

### 1.3 The two candidate models

- The **simple model $S$** uses the true choice rule above, but without context.
- The **complex model $K$** adds one parameter $\rho$ ("rho"): probability weighting $w(p;\rho)=\exp\{-(-\log p)^\rho\}$ (Prelec, 1998). With $\rho=1$ there is no distortion, $w(p;1)=p$, and $K$ is exactly $S$. We say $S$ is **nested** in $K$: $K$ is $S$ plus a knob that can be switched off.

Each model is a **family** of possible response distributions, written $\mathcal Q_S$ and $\mathcal Q_K$. Each setting of a model's parameters picks out one member of the family. Nesting means $\mathcal Q_S\subseteq\mathcal Q_K$: every distribution $S$ can produce, $K$ can produce too.

Two kinds of model matter:

- **Homogeneous** models give everyone the same parameters. They have no person-level or random effects, and they treat one person's responses as independent coin flips.
- **Hierarchical** models give each person their own $\theta$, drawn from a population distribution (a random effect).

### 1.4 KL divergence: one number for "how wrong a model is"

The manuscript measures how far a model's predictions are from the truth with the **Kullback–Leibler (KL) divergence**:

$$\operatorname{KL}(p\Vert q)=\sum_yp(y)\log\frac{p(y)}{q(y)}.$$

- $p(y)$ is the true probability of response pattern $y$; $q(y)$ is the model's probability for the same pattern; the sum runs over all possible patterns.
- $-\log q(y)$ measures how surprised the model is when $y$ happens. KL is the **average extra surprise** the model suffers, compared with someone who knows the truth, when patterns occur at their true rates.

Three facts are used throughout:

1. KL is never negative, and it is **zero only when the model's predictions equal the truth exactly.**
2. It is measured in **nats**. A difference of $\Delta$ nats per participant means each new participant multiplies the evidence for the better model by about $e^{\Delta}$; over $n$ participants, by about $e^{n\Delta}$.
3. KL is what the log-likelihood estimates. A model's average log-likelihood per participant equals a constant shared by all models, minus that model's KL. So **the model with smaller KL is the one whose likelihood pulls ahead as data accumulate.** This is the bridge from population quantities to data-based criteria (Step 4).

The manuscript's $\operatorname{KL}_H$ is just KL averaged over the recorded cells $w$, weighted by how common each cell is ($H(w)$).

### 1.5 The two target quantities

Equation (2) defines each model's **risk**, the smallest KL it can achieve, and the **joint advantage** of the complex model:

$$R_M=\min_{q\in\overline{\mathcal Q_M}}\operatorname{KL}_H(p\Vert q),\qquad\Delta_J=R_S-R_K.$$

- The bar over $\mathcal Q_M$ means the **closure**: the family plus anything it can approach arbitrarily closely. Including these limits guarantees a best fit exists. The best fit is called the model's **projection** $q_M^\star$ (the star means "best").
- **$R_M=0$ exactly when the truth is in (the closure of) the model.** So "$R_K>0$" means "the complex model is wrong."
- $\Delta_J>0$ means the complex model fits whole response patterns strictly better. The "$J$" is for **joint**: it concerns all of a person's responses together.

Equation (3) defines a second target, needed for leave-one-out:

$$C_M=\frac1T\sum_{t=1}^T\mathbb E\,\operatorname{KL}\{p(Y_t\mid Y_{-t},W)\Vert q_M^\star(Y_t\mid Y_{-t},W)\},\qquad\Delta_C=C_S-C_K.$$

- $Y_{-t}$ means "all of the person's responses except trial $t$."
- $p(Y_t\mid Y_{-t},W)$ is the true probability of the response on trial $t$ **once you know their other responses**. $C_M$ is how badly the best-fitting model predicts one held-out response, given the rest, averaged over trials ($\frac1T\sum_t$) and over people ($\mathbb E$, "expected value").
- $\Delta_C>0$ means the complex model predicts held-out single responses better. The "$C$" is for **conditional**.

The best-fitting model is chosen for the joint target and then *scored* on the conditional one; it is never refitted to it.

### 1.6 The three selection criteria (Section 1)

All likelihoods are **participant** likelihoods: the probability of a person's whole response pattern. $n$ counts participants, not trials, because only participants are independent of each other.

$$\mathrm{BIC}_M=-2\sup_\phi\ell_{M,n}(\phi)+k_M\log n .$$

$\ell_{M,n}(\phi)$ is the log-likelihood at parameter values $\phi$ ("phi"); "sup" means its best achievable value; $k_M$ is the number of parameters. Lower BIC is better. The term $k_M\log n$ penalizes parameters.

$$m_M(D)=\int e^{\ell_{M,n}(\phi)}\,\Pi_M(d\phi),\qquad\mathrm{BF}_{KS}=\frac{m_K(D)}{m_S(D)}.$$

The **evidence** $m_M$ is the likelihood averaged over the prior $\Pi_M$. The integral sign $\int\cdots\Pi_M(d\phi)$ means "average over parameter values, weighted by the prior." The **Bayes factor** $\mathrm{BF}_{KS}$ is the ratio of the two evidences; above 1 favors $K$.

$$\mathrm{ELPD}_M=\sum_{i=1}^n\sum_{t=1}^T\log\widehat p_M(y_{it}\mid D_{-it}),\qquad\mathrm{LOOIC}_M=-2\,\mathrm{ELPD}_M .$$

**Trial-level leave-one-out**: for each person $i$ and trial $t$, delete *only that one response*, refit to everything else (including that person's other responses), and record the log-probability given to the deleted response. ELPD sums these; LOOIC rescales by $-2$, so lower is better.

### 1.7 "With probability tending to one"

The conclusions say a criterion picks $K$ "with probability tending to one as $n\to\infty$." In words: **as you recruit more participants, the chance that the criterion picks the complex model gets as close to 100% as you like.** It does not say how many participants that takes (Part 9).

---

## Part 2. Step 1 — Omitting context makes each person's data a mixture (Lemma 2.1)

$$p(y\mid w)=\int\prod_{t=1}^T\pi_t(\theta,w)^{y_t}\{1-\pi_t(\theta,w)\}^{1-y_t}\,F_w(d\theta).$$

**What it says.** If you do not know someone's context, the probability of their response pattern is an **average**: take the pattern probability each kind of person would produce, and weight it by how common that kind of person is.

**Piece by piece:**

- $y=(y_1,\dots,y_T)$ is a whole response pattern, such as "ambiguous on trial 1, other option on trial 2."
- $\pi_t^{y_t}(1-\pi_t)^{1-y_t}$ is shorthand for "$\pi_t$ if they chose ambiguous, $1-\pi_t$ if not."
- $\prod_{t=1}^T$ ("product") means multiply across trials. For a person whose $\theta$ is known, trials are independent, so pattern probability is the product of trial probabilities.
- $\int\cdots F_w(d\theta)$ means average over people with the recorded characteristics $w$, weighting each $\theta$ by how common it is. $F_w$ is the distribution of $\theta$ in that group. It is shaped by context **and** by $U$.

**The subtle point.** The average is taken over the **product**: first compute whole-pattern probabilities for each kind of person, then average. Averaging each trial first and multiplying afterwards gives a different, wrong answer. That difference is exactly what creates the dependence in Step 2.

The lemma also records how context feeds into the spread of $\theta$:

$$\operatorname{Var}(\Theta\mid W)=\gamma^2\operatorname{Var}(C\mid W)+\operatorname{Var}(U\mid W)+2\gamma\operatorname{Cov}(C,U\mid W).$$

The variability of aversion among people who look the same on recorded variables has three sources: context ($\gamma^2$ times its variance), everything else ($U$), and how the two co-vary. Remark 2.4 adds two cautions:

- Context does not automatically create spread: if $U$ happens to offset context exactly, the spread from context can cancel.
- Spread from $U$ alone produces the same mixture effect.

The theorem is therefore really about **unmodelled heterogeneity**, of which omitted context is one important source.

**Job in the argument.** This is the only place where "omitting context" enters the mathematics. Everything after is about the properties of this mixture.

---

## Part 3. Step 2 — The mixture makes responses within a person correlated (Lemmas 2.1–2.2)

### 3.1 The covariance equation

$$\operatorname{Cov}(Y_t,Y_u\mid w)=\tfrac12\,\mathbb E\big[\{\pi_t(\Theta)-\pi_t(\Theta')\}\{\pi_u(\Theta)-\pi_u(\Theta')\}\mid w\big].$$

**What it says.** Two responses from the same person co-vary positively, even though for any *given* person they are independent.

**Reading it.** $\Theta$ and $\Theta'$ are the aversions of two *different*, randomly chosen people with the same recorded characteristics. The brackets compare how the two differ on trial $t$ with how they differ on trial $u$. If person A is more averse than person B, A is less likely to choose the ambiguous option on **both** trials. The two differences have the same sign, so their product is positive, and so is the average.

**Intuition.** Choosing the safe option on trial 1 is a clue that the person is probably from the more averse context. That makes the safe option more likely on trial 2 too. Hidden differences between people appear as consistency within people. The lemma states the conditions: people must genuinely differ ("nondegenerate"), and both trials' choice probabilities must move in the same direction as $\theta$ changes. In the project's task, both hold on every ambiguous trial.

### 3.2 Splitting the misfit of a homogeneous model (Lemma 2.2)

A homogeneous model treats a person's responses as independent. For any such model $q$:

$$\operatorname{KL}_H(p\Vert q)=\sum_wH(w)I_w+\sum_{w,t}H(w)\operatorname{KL}(p_t\Vert q_t).$$

**What it says.** A homogeneous model's total misfit splits *exactly* into two parts:

- $I_w$, the **multi-information**, is the misfit caused purely by the within-person correlation. It is the KL between the true joint law and the product of its own trial marginals. No homogeneous model can touch it.
- $\operatorname{KL}(p_t\Vert q_t)$ is the misfit in each trial's **choice rate** ($p_t$ is the true rate on trial $t$, $q_t$ the model's), added over trials.

Two consequences follow immediately:

1. **Every homogeneous model is wrong, however many parameters it has.** Its risk is at least $\sum_wH(w)I_w$, which is positive whenever Step 1's mixture creates correlation.
2. **When comparing two homogeneous models, the correlation part cancels.** The whole contest between $S$ and $K$ is about who matches the trial-by-trial choice rates better.

### 3.3 The exact leave-one-out identity

Lemma 2.2's second equation does the same split for the held-out-response target:

$$\mathbb E\operatorname{KL}\{p(Y_t\mid Y_{-t},W)\Vert q_t(Y_t\mid W)\}=I(Y_t;Y_{-t}\mid W)+\sum_wH(w)\operatorname{KL}(p_t\Vert q_t).$$

$I(Y_t;Y_{-t}\mid W)$ is how much the other responses tell you about response $t$. A homogeneous model ignores this information, and that part again cancels between $S$ and $K$. Averaging over trials gives the key identity:

$$\Delta_C=\Delta_J/T\qquad\text{exactly, for homogeneous models.}$$

In words: the per-trial predictive advantage is the per-person advantage spread evenly over the $T$ trials. **For homogeneous models, the joint and conditional advantages always have the same sign.**

---

## Part 4. Step 3 — An exact example in which the false complex model wins (Theorem 3.1)

This is the manuscript's centerpiece. It proves the whole phenomenon with nothing more than arithmetic and Step 2.

### 4.1 The setup

- **Task.** Two trials. Trial 1 carries a little ambiguity and trial 2 twice as much: in the model's units, $x_1=1$ and $x_2=2$. The probability of choosing the ambiguous option is $\operatorname{expit}(-x_t\theta)$.
- **Truth.** Two equally common contexts:
  - $C=0$: $\theta=0$. These people are indifferent and choose ambiguous with probability $1/2$ on both trials.
  - $C=1$: $\theta=\log3\approx1.10$. These people choose ambiguous with probability $\operatorname{expit}(-\log3)=1/4$ on trial 1 and $\operatorname{expit}(-2\log3)=1/10$ on trial 2.

  **There is no probability distortion anywhere.**
- **Simple model $S$:** one shared $\theta$; predictions $\operatorname{expit}(-x_t\theta)$; $\theta\in[0,2]$.
- **Complex model $K$:** shared $\theta$ plus Prelec distortion $\rho$. Both trials use the stated probability $1/2$, so distortion acts here as a shift $\delta$ added to both scores, $\delta=4\{w(1/2;\rho)-1/2\}$, which is zero when $\rho=1$. Predictions: $\operatorname{expit}(\delta-x_t\theta)$. The prior allows $\delta$ between $-1/2$ and $1/2$ (equivalently $\rho$ between about 0.053 and 2.06), as in the project's pilot simulations.

### 4.2 What the researcher sees

Apply Step 1: half the people are context 0 and half context 1. Order the patterns as (trial 1, trial 2), with 1 = ambiguous:

| Pattern | Context-0 person | Context-1 person | Mixture |
|---|---|---|---|
| (0,0) | 1/4 | $(3/4)(9/10)=27/40$ | **37/80** |
| (1,0) | 1/4 | $(1/4)(9/10)=9/40$ | **19/80** |
| (0,1) | 1/4 | $(3/4)(1/10)=3/40$ | **13/80** |
| (1,1) | 1/4 | $(1/4)(1/10)=1/40$ | **11/80** |

The last column is equation (8) of the manuscript. It is all the data can ever reveal when context is not recorded.

### 4.3 Correlation: both models are wrong

- Trial 1 is chosen ambiguously $19/80+11/80=3/8$ of the time; trial 2, $13/80+11/80=3/10$.
- If responses were independent, "ambiguous on both" would occur $3/8\times3/10=9/80$ of the time. It occurs $11/80$.
- The covariance is therefore $1/40>0$.

By Step 2, every homogeneous model — $S$, $K$, or anything else homogeneous — is wrong, with risk at least $I(Y_1;Y_2)=0.00627$ nats per participant.

### 4.4 Why the simple model cannot match the choice rates

To match both rates, $S$ would need $\operatorname{logit}(3/10)=2\operatorname{logit}(3/8)$, because trial 2's score is exactly twice trial 1's. But $\operatorname{logit}(3/8)=\log(3/5)\approx-0.511$ and $\operatorname{logit}(3/10)=\log(3/7)\approx-0.847$, and $-0.847\neq2\times(-0.511)$.

Put differently: trial 1 alone implies an aversion of $0.511$, trial 2 alone implies $0.424$. *The data look as if people become less averse as ambiguity increases* (Part 7 explains why). One $\theta$ cannot do both. $S$ compromises at $\theta_S^\star=0.4429$, predicting rates 0.391 (too high) and 0.292 (too low).

### 4.5 Why the complex model can

$K$ has two knobs, $\theta$ and $\delta$. Two equations in two unknowns, $\delta-\theta=\log(3/5)$ and $\delta-2\theta=\log(3/7)$, give

$$\theta_K^\star=\log(7/5)=0.3365,\qquad\delta_K^\star=\log(21/25)=-0.1744,$$

which matches both choice rates **exactly**. In weighting terms, $\delta_K^\star$ corresponds to $\rho_K^\star=0.663$: a clear inverse-S distortion, produced by data that contain no distortion at all.

### 4.6 The verdict in numbers

By Step 2's split, $K$'s only misfit is the unavoidable correlation part, while $S$ also misses the choice rates:

| Quantity | Value (nats per participant) |
|---|---|
| $R_K=I(Y_1;Y_2)$ | 0.0062696 |
| $R_S$ | 0.0069681 |
| $\Delta_J=R_S-R_K$ | 0.0006985 |
| $\Delta_C=\Delta_J/2$ (per trial) | 0.0003493 |

So $0<R_K<R_S$ (the complex model is less wrong, but wrong) and $\Delta_C>0$. Step 4 turns this into a statement about BIC, Bayes factors and leave-one-out. Because $\rho_K^\star\neq1$, an analyst would also *estimate* a distortion near 0.663, and a test of "no distortion" would eventually reject.

**The interpretive limitation.** Both trials here use the same stated probability, so distortion is indistinguishable from a simple shift. The witness proves that an unnecessary parameter gets selected; it does not show that the shift *is* probability weighting in any psychological sense.

---

## Part 5. Step 4 — Why all three criteria follow the population winner (Theorem 4.1)

$$\frac{\mathrm{BIC}_K-\mathrm{BIC}_S}{n}\xrightarrow{p}-2\Delta_J,\qquad\frac1n\log\mathrm{BF}_{KS}\xrightarrow{p}\Delta_J,\qquad\frac{\mathrm{LOOIC}_K-\mathrm{LOOIC}_S}{nT}\xrightarrow{p}-2\Delta_C.$$

**Notation.** The arrow with a $p$ ("converges in probability") means: as $n$ grows, the left side gets arbitrarily close to the right side, with probability approaching one.

**What it says.** Divide each criterion's difference by the amount of data, and it settles down to a population quantity:

- the BIC difference per participant approaches $-2\Delta_J$;
- the log Bayes factor per participant approaches $\Delta_J$;
- the LOOIC difference per trial approaches $-2\Delta_C$.

So if $\Delta_J>0$ and $\Delta_C>0$, **all three criteria pick $K$ with probability tending to one.** The same likelihood limit makes the likelihood-ratio statistic for "no distortion" grow like $2n\Delta_J$, so any test with a fixed critical value rejects eventually.

**Why each limit holds.**

- **BIC.** The best log-likelihood grows like $n$ times the population fit, so the log-likelihood gain of $K$ over $S$ grows like $n\Delta_J$. The penalty $(k_K-k_S)\log n$ grows far more slowly. $K$ has the lower BIC exactly when $2\times$gain$>(k_K-k_S)\log n$, which eventually always holds.
- **Bayes factor.** The evidence is a prior-weighted average of likelihoods. It is at most the best likelihood, and at least the likelihood near the best fit times the prior weight there. Both bounds grow like $e^{n\times\text{population fit}}$, so the Bayes factor grows like $e^{n\Delta_J}$. This needs only that the prior puts *some* weight near the best fit; no approximation formula (such as Laplace's) is used.
- **Trial LOO.** The exact predictive probability for one deleted response is

  $$\widehat p_M(y_{it}\mid D_{-it})=\frac{m_M(D)}{m_M(D_{-it})}=\int q_M(y_{it}\mid y_{i,-t},W_i;\phi)\,\Pi_M(d\phi\mid D_{-it}).$$

  This is equation (13). In words: the prediction is the model's conditional probability for the held-out response given the person's other responses, averaged over the posterior fitted without that response. It equals a ratio of two evidences. As $n$ grows, deleting one response barely changes the posterior, so each prediction approaches the best-fitting model's conditional probability. Averaging their logs gives $C_M$, and comparing models gives $\Delta_C$.

**What the conditions mean.** The task has finitely many configurations; every response pattern has positive probability; priors are proper and give some weight near the best fit; and, for LOO, each model has a single best-fitting distribution. Nesting is **not** required, which matters for Step 8.

**What the appendix adds (Lemmas A.1–A.4).** The appendix proves each step in full. Conceptually:

- **A.1, small-cell exclusion.** A model that predicts some pattern as nearly impossible pays a huge log-likelihood penalty whenever that pattern occurs, so near-best fits never do this. On the remaining models, observed pattern frequencies settle on true ones at a rate given by Hoeffding's inequality, $\Pr(\max_j|\hat r_j-r_j|>u)\le2Ne^{-2nu^2}$: the chance that any of the $N$ pattern frequencies is off by more than $u$ shrinks exponentially in $n$.
- **A.2, evidence.** This turns the "at most / at least" bounds above into a limit.
- **A.3, deletion stability.** Removing one participant changes every pattern frequency by at most $1/(n-1)$. So a *single* good-data event makes the posterior concentrate for every possible deletion at once, without assuming anything about the deletions separately. Removing one response rather than a whole person reweights the posterior by a factor bounded away from zero, which keeps the conclusion.
- **A.4, the LOO limit.** Predictions stay away from zero, so their logs behave, and averaging over participants (not trials) gives the limit. **A person's trials are never treated as independent.**

---

## Part 6. Step 5 — A general test for when the complex model wins (Theorem 5.1, Proposition 5.3)

The witness is one example. Theorem 5.1 gives a condition that can be checked for any homogeneous pair.

### 6.1 The drift Λ

$$\Lambda=\sum_{w,t}H(w)\,e_t(w)\,\{p_t(1\mid w)-q^\star_{St}(1\mid w)\}.$$

- $p_t(1\mid w)-q^\star_{St}(1\mid w)$ is the simple model's **residual** on trial $t$: the true choice rate minus the rate its best fit predicts.
- $e_t(w)$ is the **design signature** of the extra knob: how much nudging $\rho$ away from "off" changes trial $t$'s score. It depends only on the task. For Prelec weighting it depends on the stated probabilities and payoffs.
- The sum weights each trial by how common its cell is ($H(w)$). $\Lambda$ ("Lambda") is thus a weighted inner product of "where the simple model gets it wrong" with "where the extra knob has leverage."

**What it says.** Stand at the simple model's best fit and nudge the extra knob slightly. $\Lambda$ is the slope of the complex model's fit in that direction (formally, the derivative of KL is $-\Lambda$). If the slope is not zero, a small nudge improves fit, so $R_K<R_S$. If, in addition, the truth is a mixture as in Step 2, both models are wrong and $\Delta_C=\Delta_J/T>0$. Then Theorem 4.1 applies and all three criteria select the false complex model.

**Familiar statistics.** $\Lambda$ is the population version of the **score test** (Rao's test) for "no distortion." The theorem says: *the complex model wins whenever omitted context gives the standard test for its extra parameter a non-zero signal.*

**In the witness.** The extra knob shifts both trials equally, $e=(1,1)$ in the $\delta$ coordinate. The residuals are $0.375-0.391=-0.016$ and $0.300-0.292=+0.008$, so $\Lambda\approx-0.008$. It is negative, predicting that $K$ moves the knob in the negative direction; it does ($\delta_K^\star<0$, i.e. $\rho<1$).

### 6.2 Sufficient, not necessary (Remark 5.2)

$\Lambda\ne0$ guarantees an advantage, but $\Lambda=0$ does **not** rule one out. The manuscript's example uses the same task with a family whose shift is $-\rho^2$. At $\rho=0$ the knob's slope is zero (since $\rho^2$ is flat at 0), so $\Lambda=0$. Yet the family still contains every negative shift, including the witness's best one, so it wins by the same $\Delta_J=0.0007$. A zero slope means the first-order test is silent, not that there is no effect.

### 6.3 How big the advantage is at least (Proposition 5.3)

$$\Delta_J\ge\frac{\Lambda_\delta^2}{2B}.$$

- $\Lambda_\delta$ is the drift measured in the $\delta$ coordinate.
- $B$ is a bound on how sharply the fit can curve along the most efficient direction. That direction moves the extra knob while adjusting the simple model's own parameters to compensate, like holding other predictors fixed in a regression. The $\tfrac14$ in $B$'s definition comes from the fact that a Bernoulli variance $\pi(1-\pi)$ is at most $1/4$.

**What it says.** A parabola with starting slope $\Lambda$ and curvature at most $B$ must dip at least $\Lambda^2/(2B)$ below its starting point. So the complex model gains at least that much. The conditions: the simple fit is interior, the step stays in the parameter space all the way along, and both models' logits are affine in the parameters.

**In the witness.** The bound gives $0.000642$, against the true $0.000699$.

---

## Part 7. Step 6 — Why the complex model wins: the shape of omitted context (Lemma 6.1, Theorem 6.2)

Step 5 says *when*; Step 6 says *why*, in terms of what omission does to the data. It works in the regime where people differ only modestly.

### 7.1 Writing the spread

$$\Theta\mid w=\bar\theta(w)+\varepsilon V_w,\qquad\mathbb EV_w=0,\quad\operatorname{Var}(V_w)=v(w).$$

A person's aversion is the group average $\bar\theta(w)$ ("theta-bar") plus a deviation. $V_w$ is the standardized deviation and $\varepsilon$ ("epsilon") a dial for its size, so $\varepsilon^2v(w)$ is the actual variance of aversion in the group (the Step 1 variance). Small $\varepsilon$ means people differ modestly.

### 7.2 The shape of the averaged distribution (Lemma 6.1)

$$p_\varepsilon(y\mid w)=p_0(y\mid w)\{1+\varepsilon^2(h_A+h_D)+O(\varepsilon^3)\}.$$

**What it says.** The averaged distribution equals what an *average* person would produce ($p_0$), corrected by a term proportional to the variance of aversion ($\varepsilon^2$). "$O(\varepsilon^3)$" means "smaller terms that shrink at least as fast as $\varepsilon^3$." The correction has two pieces that never interfere with each other (they are "orthogonal"):

$$h_A=\sum_ta_t(w)(y_t-\pi_{t0}),\qquad a_t(w)=\tfrac12v(w)\,\beta_t(w)^2\,(1-2\pi_{t0}),$$

$$h_D=v(w)\sum_{t<u}\beta_t\beta_u(y_t-\pi_{t0})(y_u-\pi_{u0}).$$

- $h_D$, the **dependence** piece, is Step 2's correlation in small-spread form: covariance $\approx\varepsilon^2v\beta_t\beta_u\pi'_{t0}\pi'_{u0}$, where $\pi'=\pi(1-\pi)$.
- $h_A$, the **attenuation** piece, changes each trial's choice rate.

**Where attenuation comes from: averaging a curved function.** If a function is a straight line, averaging its output over a spread of inputs gives the same answer as plugging in the average input. If it is curved, it does not, and the difference is approximately

$$\tfrac12\times(\text{spread of inputs})\times(\text{curvature}).$$

This is a form of Jensen's inequality. The S-curve bends upward below 50% and downward above 50%. **Averaging over people who differ therefore pulls every trial's choice rate toward 50%.** On the logit scale, trial $t$'s rate moves by $\varepsilon^2a_t$. Each factor in $a_t$ has a meaning:

| Factor | Meaning |
|---|---|
| $\tfrac12$ | from the curved-function rule |
| $v(w)$ (times $\varepsilon^2$) | the more people differ, the bigger the pull |
| $\beta_t^2$ | trials carrying more ambiguity spread people's scores more, and the pull grows with the **square** of the ambiguity load |
| $1-2\pi_{t0}$ | positive below 50% (rate pushed up), negative above (pushed down): always toward 50% |

The $\beta_t^2$ is the crux. The simple model's own changes are proportional to $\beta_t$ (aversion multiplies the ambiguity load), but omission produces changes proportional to $\beta_t^2$. **That is a bend the simple model cannot produce with its own parameters**, unless some other parameter happens to absorb it.

**In the witness.** The average person ($\bar\theta=0.55$) would choose ambiguous at 0.366 on trial 1 and 0.250 on trial 2. The observed rates are 0.375 and 0.300: both pulled toward 50%, trial 2 (double ambiguity) far more. On the logit scale the shifts are $+0.038$ and $+0.251$. That is the "people seem less averse on more ambiguous trials" pattern of Part 4.

### 7.3 The regression-like criterion (Theorem 6.2)

$$\Delta_J(\varepsilon)=\frac{\varepsilon^4}{2}\,\frac{\langle a,\tilde e\rangle_\Omega^2}{\langle\tilde e,\tilde e\rangle_\Omega}+o(\varepsilon^4),\qquad\tilde e=M_Se .$$

This looks dense but is a familiar regression idea.

- $a$ is the attenuation pattern: one number per trial and cell, saying how far omission bends that trial's choice rate.
- $e$ is the extra knob's design signature (Step 5).
- $M_S$ means "remove whatever the simple model's own parameters can already reproduce." $\tilde e$ is the extra knob's signature **after partialling out** the simple model, like taking residuals from regressing it on the simple model's predictors.
- $\langle\cdot,\cdot\rangle_\Omega$ is a weighted inner product (a covariance-like sum across trials and cells). The weights $\Omega=\operatorname{diag}\{H(w)\pi_{t0}(1-\pi_{t0})\}$ give more say to common cells and to trials whose choices are more variable (nearer 50%).
- $o(\varepsilon^4)$ means "terms that vanish faster than $\varepsilon^4$."

**What it says.** For modest spread, **the complex model's advantage is the squared partial covariance between the attenuation pattern and its extra knob, divided by the knob's residual variance, times $\varepsilon^4/2$.** That is the structure of an incremental $R^2$, the Frisch–Waugh–Lovell logic familiar from "controlling for covariates." The theorem also gives each model's risk:

$$R_M(\varepsilon)=\frac{\varepsilon^4}{2}\big\{\lVert M_Ma\rVert_\Omega^2+\lVert h_D\rVert^2\big\}+o(\varepsilon^4),$$

i.e. the unexplained part of the attenuation plus the dependence part, which no homogeneous model removes.

Three consequences:

1. **The effect can be predicted from the design before collecting data.** Compute $a$ and $\tilde e$; if their weighted covariance is zero, the knob cannot exploit omitted context at leading order.
2. **The effect scales as $\varepsilon^4$.** Halve the spread of aversion and the advantage drops sixteenfold. This is why the advantage is small in realistic settings.
3. **Absorption is only a leading-order statement (Remark 6.3).** If the knob's signature can be reproduced by the simple model's own parameters, $\tilde e=0$ and the leading term vanishes. But this does *not* prove there is no advantage at all. As in the $-\rho^2$ example, a knob can be invisible to first order yet still matter. The advantage is exactly zero for every truth only when the two families can produce exactly the same positive distributions.

---

## Part 8. Step 7 — Models with person-level effects (Section 7)

So far the models gave everyone the same parameters. Real cognitive models usually include random effects, letting each person have their own $\theta$. That changes the picture in four ways.

### 8.1 Selection still follows the two gaps (Theorem 7.1)

$$R_S>R_K>0\quad\text{and}\quad C_S>C_K\quad\Longrightarrow\quad\text{BIC, BF and trial LOO all select the false complex model.}$$

This is Theorem 4.1 again: the transfer argument never assumed homogeneity. The catch is the boxed condition. For hierarchical models, **neither inequality follows automatically from omitting context**, and Step 2's identity $\Delta_C=\Delta_J/T$ no longer holds. Both must be established separately. For the project's specific hierarchical pair, they have not yet been.

### 8.2 The local formulas still hold at a regular point (Theorem 7.2)

For a truth that is a small perturbation of a law the simple model can produce, $p_\varepsilon=p_0\{1+\varepsilon^kh+o(\varepsilon^k)\}$:

$$R_M=\tfrac12\varepsilon^{2k}\lVert r_M\rVert^2+o(\varepsilon^{2k}),\quad\Delta_J=\tfrac12\varepsilon^{2k}\lVert d\rVert^2+o(\varepsilon^{2k}),\quad\Delta_C=\tfrac12\varepsilon^{2k}\{\langle d,\mathcal Ad\rangle+2\langle r_K,\mathcal Ad\rangle\}+o(\varepsilon^{2k}).$$

**The symbols:**

- $h$ is the direction in which the truth departs from $p_0$, and $\varepsilon^k$ its size.
- $P_Mh$ is the part of that departure model $M$ can follow; $r_M=h-P_Mh$ is the part it cannot; $d=P_Kh-P_Sh$ is the extra part only the complex model can follow.
- $\mathcal A$ is an averaging operator: "the part of a quantity not predictable from the person's other responses." It turns joint quantities into held-out-response quantities.

**What it says.**

- Each model's misfit is half the squared size of what it cannot follow.
- The joint advantage is half the squared size of what only $K$ can follow.
- The held-out advantage is the same idea filtered through $\mathcal A$, plus a cross term.

So $d\ne0$ gives a joint advantage, $r_K\ne0$ makes $K$ wrong, and the bracket being positive gives a conditional advantage. **The bracket can be negative:** a joint advantage does not imply a held-out advantage.

The conditions matter. The best fits must be near a regular, interior point of each model; in particular the random-effect variance must not be zero.

### 8.3 Two obstacles

**The zero-variance boundary (Remark 7.3).** A random-effect variance cannot be negative. At variance zero the model sits on an edge, and the calculus behind Theorem 7.2 breaks down there. The local theorem does not cover expansions around "no person differences."

**Random effects absorb the leading term (Proposition 7.4).** If the simple model already has a normal random effect with a free variance, it can match the mean and variance of aversion. What is left for the complex model is only the **shape** of the variation: lopsidedness (skew) or clumping into types. Then

$$R_S=O(\varepsilon^6)\quad(\text{or }O(\varepsilon^8)\text{ if the deviations are symmetric}),\qquad\Delta_J\le R_S,\qquad\Delta_C\le R_S .$$

Halve the spread and the advantage against a homogeneous model falls 16-fold, but against such a hierarchical model 64-fold or more. **This is the main reason the hierarchical case is hard.**

**Balanced contexts and context-dependent spread (Proposition 7.5, Remark 7.6).** Suppose context changes how *variable* aversion is, the contexts are balanced, and they are otherwise alike. Then the perturbation is "odd" (it flips sign between contexts), while a distortion parameter that ignores context has an "even" signature (the same in both). Odd and even directions are orthogonal, so $d=0$: the simple model is wrong, but the complex model gains nothing at leading order.

The proposition requires the extra parameter's signature to be even. Remark 7.6 shows why: an extra parameter written as "variance $=v+\delta Z$" has an odd signature and can fit context-dependent variance exactly.

### 8.4 An explicit reversal (Proposition 7.7)

The manuscript gives two-trial laws (cells ordered as in the witness) with

| | $(0,0)$ | $(1,0)$ | $(0,1)$ | $(1,1)$ |
|---|---|---|---|---|
| truth $p$ | 0.27 | 0.33 | 0.28 | 0.12 |
| simple $s$ | 0.11 | 0.19 | 0.12 | 0.58 |
| direction $k$ | 0.68 | 0.06 | 0.05 | 0.21 |

$K$ is the segment from $s$ toward $k$. Its best fit moves 28% of the way ($\lambda^\star=0.282$), giving $\Delta_J=0.098>0$ but $\Delta_C=-0.052<0$. BIC and Bayes factors would choose $K$; trial LOO would choose $S$.

**Why the two targets disagree.** By the chain rule (Lemma 2.2's logic), joint misfit equals misfit to the retained responses plus misfit in predicting the held-out one.

- **Marginals.** The truth's choice rates are 0.45 and 0.40; $S$ predicts 0.77 and 0.70. Moving toward $k$ brings them down to 0.63 and 0.58, a large gain on the "retained responses" part: 0.151 per trial.
- **Dependence.** The truth is **negatively** dependent: after an ambiguous choice on trial 1, trial 2 is ambiguous only 27% of the time, against 51% after a safe choice. $K$'s fit is strongly **positively** dependent (76% versus 27%), so its held-out predictions get worse.

The joint gain (0.098) is smaller than the marginal gain (0.151), and the difference is the conditional loss ($-0.052$). This example is abstract — not a cognitive model — but it proves that "$\Delta_J>0$ implies $\Delta_C>0$" is false in general.

---

## Part 9. Step 8 — The context-aware model wins when context is measured (Lemma 2.3, Corollary 8.1)

$$\mathbb E_{W,C}\operatorname{KL}\{p(Y\mid W,C)\Vert q(Y\mid W)\}=I(Y;C\mid W)+\operatorname{KL}_H(p\Vert q).$$

**What it says.** Suppose context *is* measured, and judge a context-blind model by how well it predicts each person given their context. Its misfit is its ordinary misfit plus $I(Y;C\mid W)$. That is the **mutual information** between responses and context: how much knowing someone's context sharpens predictions of their responses. No context-blind model can recover it, however complex.

**In the witness.** $I(Y;C\mid W)=0.129$ nats per participant, while the complex model's advantage over $S$ is $0.0007$. **The complex model recovers about half a percent of what omitting context costs; including context recovers all of it.**

**Corollary 8.1** turns this into selection. If the context-aware simple model is correctly specified — including any person differences that $U$ requires — then BIC and Bayes factors prefer it to the context-blind complex model with probability tending to one, and so does trial LOO when best fits are unique.

The trial-LOO part rests on a neat fact. If two response distributions agree on every "probability of this response given all the others," they are the same distribution: you can walk from any pattern to any other by changing one response at a time, and the ratio of the two distributions cannot change along the way. So a context-blind model that is wrong about the joint distribution must also be wrong about some held-out predictions.

The caution in Remark 8.2 matters for interpretation. Including context makes the simple model correct only if the remaining person differences ($U$) are also modelled adequately.

---

## Part 10. What the theorem does and does not say

| Claim | Status in the manuscript |
|---|---|
| Omitting context can make all three criteria choose a false complex model | **Proved** by an exact example (Theorem 3.1) |
| A checkable condition for homogeneous models (non-zero drift Λ) | **Proved**; sufficient, not necessary |
| The design-level "partial covariance with attenuation" explanation | **Proved** as a small-spread (leading-order) result |
| Selection with random-effect models | **Proved conditionally**: requires $R_S>R_K>0$ and $C_S>C_K$, not yet shown for the project's models |
| Random effects shrink the effect to order $\varepsilon^6$ or smaller | **Proved** (Proposition 7.4) |
| More participants always help | **False here**: more participants make the wrong choice *more* certain |
| More trials per person | **Not covered**; for random-effect models with trial LOO the effect may fade as trials accumulate |

**On sample sizes.** "With probability tending to one" says nothing about how many participants are needed. In the witness the advantage is only 0.0007 nats per participant. The project's analyses suggest:

- BIC needs several thousand participants before the expected likelihood gain exceeds its penalty;
- Bayes factors and trial LOO are more vulnerable at moderate sizes;
- the pilot found trial LOO choosing the complex model in 8 of 10 simulated data sets of 1,000 participants, against 1 of 10 for BIC.

**The open problem.** Constructing a convincing hierarchical example for the project's probability-distortion comparison. Part 8.3 says what it would need: lopsided or clumped context effects, or unbalanced contexts; a regular point with positive random-effect variance; and direct verification of both gaps rather than reliance on leading-order formulas.

---

## Glossary of symbols

| Symbol | Read as | Meaning |
|---|---|---|
| $\theta$, $\Theta$ | theta | Ambiguity aversion (one value; varying across people) |
| $C$, $U$ | — | Omitted context; other unexplained individual differences |
| $W$, $w$, $H(w)$ | — | Recorded design and covariates; a cell; its share of participants |
| $Y_t$, $y$, $Y_{-t}$ | — | Response on trial $t$ (1 = ambiguous); a whole pattern; all responses except $t$ |
| $T$, $n$ | — | Trials per person; number of participants |
| $\operatorname{expit}$, $\operatorname{logit}$ | — | S-curve from score to probability; its inverse (log-odds) |
| $\kappa_t$, $\beta_t$, $\pi_t$ | kappa, beta, pi | Non-ambiguity attractiveness; ambiguity load; choice probability |
| $\pi'$ | pi-prime | $\pi(1-\pi)$, the variance of a single choice |
| $\rho$, $\delta$ | rho, delta | Distortion parameter (1 = none); the shift it produces in the witness |
| $S$, $K$, $S_C$ | — | Simple, complex, and context-aware simple models |
| $\mathcal Q_M$, $\overline{\mathcal Q_M}$ | — | A model's family of distributions; its closure (family plus limits) |
| $\operatorname{KL}(p\Vert q)$ | KL divergence | Average extra surprise of $q$ when the truth is $p$ (nats) |
| $R_M$, $q_M^\star$ | risk, projection | Best achievable misfit; the best-fitting distribution |
| $\Delta_J$, $\Delta_C$ | Delta | Complex model's advantage on whole patterns (per person) and on held-out responses (per trial) |
| $C_M$ | — | Misfit in predicting one held-out response from the rest |
| $I_w$, $I(\cdot;\cdot)$ | (multi-/mutual) information | Misfit from within-person dependence; information one quantity carries about another |
| $\Lambda$, $e_t$ | Lambda | Drift (score-test signal) of the extra parameter; its design signature |
| $\varepsilon^2v(w)$ | epsilon | Variance of aversion among people who look alike on recorded variables |
| $a_t$, $h_A$, $h_D$ | — | Attenuation of trial $t$; attenuation and dependence parts of omission's effect |
| $M_S$, $\tilde e$, $\Omega$ | — | "Partial out the simple model"; the residualized signature; weights |
| $d$, $r_M$, $\mathcal A$ | — | Part only $K$ can follow; part $M$ cannot follow; "unpredictable from the other responses" operator |
| $\xrightarrow{p}$ | converges in probability | Gets arbitrarily close, with probability tending to one |
| $O(\cdot)$, $o(\cdot)$ | big-O, little-o | At most proportional to; vanishing faster than |

## Further reading

- The manuscript: [`manuscript/revised/revised_central_theorem.pdf`](../manuscript/revised/revised_central_theorem.pdf).
- The audit and its numerical checks: [`audit_revised_central_theorem_2026-10-29.md`](audit_revised_central_theorem_2026-10-29.md).
- Background, not yet verified against sources under the project's literature policy: Estes (1956) on inferences from averaged group data; Chesher (1984) on neglected heterogeneity; Prelec (1998) on probability weighting.
