# When leaving out context makes the wrong model win: a guided tour of the central theorem

*A companion to [`central_theorem_full_draft.md`](central_theorem_full_draft.md), written for psychologists who use cognitive models but do not work with mathematical statistics every day.*

> **Superseded (2026-10-29).** This guide follows the exploratory 2 October draft, several of whose claims were later corrected. Use [`revised_central_theorem_guide_for_psychologists.md`](revised_central_theorem_guide_for_psychologists.md), which follows the revised manuscript.

Date: 2026-10-28. **Status:** this guide explains an exploratory, not-yet-reviewed proof draft. It inherits that draft's status: the arguments have been checked by the author and by computer, but not by an independent reviewer. Where the guide says "proved," read "proved in the draft, pending review."

---

## How to use this guide

The theorem is a chain of about ten steps. Each step takes something established in the previous one and turns it into something new. The guide walks through the chain in order. For every equation it tells you three things:

1. **What it says**, in words.
2. **What each symbol means.**
3. **Why the step matters for the argument.**

The same small example runs through the whole guide. Every number in it can be checked with a calculator. When you get lost in the general version of a step, go back to the example; the general step is always the same idea with more symbols.

You need only three pieces of background: what a probability is, what an average is, and the idea of fitting a model by making its predictions match data. Everything else is built up as needed. Part 1 introduces the toolkit; skip any item you already know.

---

## Part 0. The claim in plain words

Cognitive models describe how a person makes decisions using a small number of psychological parameters. In decision-making under ambiguity, a common model gives each person an **ambiguity aversion** parameter: how much they dislike options whose probabilities are unknown.

Now suppose that something about people's lives (their context: for example, socioeconomic resources or how uncertain their environment has been) **shifts** their ambiguity aversion. People from one context tend to be more averse than people from another. Suppose also that the researcher does not include context in the model, perhaps because it was not measured or because standard practice ignores it.

The theorem says:

> When context shifts a cognitive parameter but is left out of the model, the data take on a shape that the true, simple cognitive model cannot reproduce. A more complex cognitive model, one with an extra mechanism such as **probability distortion**, can sometimes reproduce part of that shape. When it can, the three standard model-selection tools (BIC, Bayes factors, and leave-one-out cross-validation) will all prefer the complex model, and the preference becomes **certain** as the sample grows. The complex model is still wrong: the true process has no probability distortion at all. And the simple model *with context included* is exactly right and beats both.

The danger is a specific kind of scientific error. A researcher would conclude "people distort probabilities," would find a "significant" distortion parameter, and would have every standard tool agreeing. What actually happened is that people in different circumstances simply differ in ambiguity aversion.

The guide's job is to show *why* this happens, step by step, and *when* it does not.

---

## Part 1. The toolkit

### 1.1 Latent parameters and the symbol θ

A **latent parameter** is a quantity inside the model that describes a person but is not observed directly. Here it is ambiguity aversion, written $\theta$ (Greek "theta"). Upper-case $\Theta$ refers to the parameter as something that varies across people (a random variable); lower-case $\theta$ refers to one particular value.

### 1.2 How a cognitive model turns θ into a choice probability

On each trial a person chooses between an ambiguous option and a safer reference option. Write $Y_t=1$ if they choose the ambiguous option on trial $t$ and $Y_t=0$ otherwise. The model says the probability of choosing the ambiguous option is

$$P(Y_t=1\mid\theta)=\sigma\big(\eta_t(\theta)\big),\qquad \eta_t(\theta)=\kappa_t-\beta_t\,\theta .$$

**In words:** compute a "net attractiveness" score $\eta_t$ (Greek "eta") for the ambiguous option, then convert the score into a probability.

**The symbols:**

- $\kappa_t$ ("kappa") is everything about trial $t$ that makes the ambiguous option attractive *apart from* ambiguity: payoffs, stated probabilities, which side of the screen it appears on.
- $\beta_t$ ("beta") is how much ambiguity this trial contains, in units that matter for the decision. In the project's model it is proportional to the trial's ambiguity width. Trials with more ambiguity have larger $\beta_t$, so ambiguity aversion matters more on them.
- $\theta$ multiplies $\beta_t$ and is subtracted: a more averse person (larger $\theta$) finds the ambiguous option less attractive, and more so on more ambiguous trials.
- $\sigma(\cdot)$ is the **logistic function**, $\sigma(x)=1/(1+e^{-x})$. It turns any score into a probability between 0 and 1: a score of 0 gives 0.5, large positive scores approach 1, large negative scores approach 0. Plotted, it is the familiar S-shaped curve.

The inverse of $\sigma$ is the **logit** or log-odds, $\mathrm{logit}(p)=\log\{p/(1-p)\}$. If you have run a logistic regression, you have used this: the model is linear on the logit scale. Here, the logit of the choice probability is $\kappa_t-\beta_t\theta$, a straight line in $\theta$.

**Why it matters:** this is the "simple cognitive mechanism." It is the true model in the theorem. Nothing in reality is distorted; people differ only in $\theta$.

### 1.3 Probability distortion: the complex model's extra knob

The complex model adds **probability weighting**: instead of using a stated probability $p$, people act as if it were $w(p;\rho)$, where

$$w(p;\rho)=\exp\{-(-\ln p)^{\rho}\}.$$

This is Prelec's (1998) weighting function. The parameter $\rho$ ("rho") controls the distortion:

- $\rho=1$ gives $w(p;1)=p$: no distortion. The complex model then *is* the simple model.
- $\rho<1$ produces the classic inverse-S shape: small probabilities overweighted, moderate-to-large ones underweighted.

So the complex model $K$ is the simple model $S$ plus one extra knob $\rho$; turning the knob to 1 switches it off. This "the complex model contains the simple one" structure is called **nesting**, and it matters later.

### 1.4 The likelihood: how well a model's predictions match data

A model assigns a probability to every possible response pattern. The **likelihood** of a data set is the probability the model assigned to the patterns that actually occurred, multiplied across participants (participants are independent of one another). Because products of many small numbers are awkward, everyone works with the **log-likelihood**, the sum of the logs. Higher is better.

One point is easy to get wrong and important here. The unit is the **participant's whole response pattern**, not the single trial. One person's responses on different trials are not independent of each other (that is the whole story of Part 3), so we may not multiply single-trial probabilities across trials as if they were.

### 1.5 KL divergence: one number for "how wrong a model is"

To compare models we need a measure of how far each model's predictions are from the truth. The theorem uses the **Kullback–Leibler (KL) divergence**:

$$\mathrm{KL}(p\Vert q)=\sum_{y}p(y)\,\log\frac{p(y)}{q(y)} .$$

**The symbols:** $p(y)$ is the true probability of response pattern $y$; $q(y)$ is the model's predicted probability of the same pattern; the sum runs over every possible pattern.

**In words:** $-\log q(y)$ is how surprised the model is when pattern $y$ occurs. KL is the *average extra surprise* the model experiences, compared with someone who knew the true probabilities, when patterns occur at their true rates.

**Three facts about KL that the theorem uses:**

1. KL is never negative, and it is zero **only** when the model's predictions are exactly the truth.
2. It is measured in **nats** (natural-log units). A gap of $\Delta$ nats per participant means that, on average, each new participant multiplies the evidence for the better model by $e^{\Delta}$. Over $n$ participants, the factor is roughly $e^{n\Delta}$.
3. KL is exactly what the log-likelihood estimates. The average log-likelihood per participant equals a constant (which is the same for every model) minus that model's KL. So *the model with smaller KL is the model whose log-likelihood grows faster as data accumulate.* That one fact is the bridge between the population-level analysis (Parts 3–4) and the data-level criteria (Part 5).

We write $R_M$ ("risk" of model $M$) for the smallest KL that model $M$ can achieve with its best parameter values. $R_S$ is the simple model's best achievable misfit and $R_K$ the complex model's. The **false-complex advantage** is

$$\Delta_J=R_S-R_K .$$

The subscript $J$ stands for "joint": it measures fit to whole response patterns. If $\Delta_J>0$, the complex model fits the truth strictly better.

### 1.6 "With probability tending to one"

The theorem's conclusions are of the form "the probability that BIC picks the complex model tends to one as $n\to\infty$." This means: *as you recruit more participants, the chance that the criterion picks the complex model gets as close to 100% as you like.* It is not a promise about any particular sample size. Part 6 discusses what happens at realistic sample sizes.

---

## Part 2. The running example

Every step below is illustrated with this example, taken from the project's minimal proof.

**The task.** Every participant completes two trials. Both offer an ambiguous option and a sure option. Trial 1 has a little ambiguity and trial 2 has more. In the model's units, $\beta_1=1$ and $\beta_2=2$. The other trial features are arranged so that $\kappa_1=\kappa_2=0$. The choice probabilities are therefore $\sigma(-\theta)$ on trial 1 and $\sigma(-2\theta)$ on trial 2.

**The truth (the data-generating process).** There are two equally common contexts.

- Context $C=0$: ambiguity aversion $\theta=0$. These people are indifferent: they choose the ambiguous option with probability $\sigma(0)=1/2$ on both trials.
- Context $C=1$: ambiguity aversion $\theta=\log 3\approx1.10$. These people choose the ambiguous option with probability $\sigma(-\log3)=1/4$ on trial 1 and $\sigma(-2\log3)=1/10$ on trial 2.

Within a person, the two responses are independent coin flips with those probabilities. **There is no probability distortion anywhere in the truth.**

**The two candidate models.** Both ignore context.

- **Simple model $S$:** everyone shares one ambiguity aversion $\theta$. Predictions: $\sigma(-\theta)$ and $\sigma(-2\theta)$. One free parameter.
- **Complex model $K$:** shared $\theta$ plus probability distortion $\rho$. Both trials use the stated probability $1/2$, so distortion acts here as a shift $\delta$ added to both scores. Predictions: $\sigma(\delta-\theta)$ and $\sigma(\delta-2\theta)$, where $\delta=4\,[w(1/2;\rho)-1/2]$ is zero exactly when $\rho=1$. Two free parameters.

**The contextual model $S^C$** is the simple model with context included. It contains the truth exactly.

Keep these three models in mind; they are all we need.

---

## Part 3. Step 1: leaving out context turns each person's data into a mixture

### 3.1 The equation

$$p(y\mid w)=\int\prod_{t=1}^{T}\pi_t(\theta,w)^{y_t}\{1-\pi_t(\theta,w)\}^{1-y_t}\;F(d\theta\mid w).$$

*(Technical draft: Lemma 1.1.)*

**What it says.** If you do not know someone's context, the probability of their whole response pattern is an **average**. You take the pattern probability each possible kind of person would produce, and weight it by how common that kind of person is.

**Reading it piece by piece:**

- $y=(y_1,\dots,y_T)$ is a whole response pattern across the $T$ trials, such as "ambiguous on trial 1, sure on trial 2."
- $w$ stands for everything the researcher *does* record about the person and the task (design features and any covariates in the model). Conditioning on $w$ means "among people who look the same on everything recorded."
- $\pi_t(\theta,w)$ is the probability that a person with aversion $\theta$ chooses the ambiguous option on trial $t$.
- $\pi_t^{y_t}(1-\pi_t)^{1-y_t}$ is a compact way of writing "$\pi_t$ if they chose ambiguous, $1-\pi_t$ if they did not."
- $\prod_{t=1}^T$ (a capital Greek "pi") means *multiply across trials*. For a person whose $\theta$ is known, trials are independent coin flips, so the probability of the whole pattern is the product.
- $\int\cdots F(d\theta\mid w)$ means *average over people*, weighting each value of $\theta$ by how common it is among people with the same recorded characteristics $w$. $F(\cdot\mid w)$ is the distribution of aversion in that group. When there are only a few kinds of people, the integral is just a weighted sum.

**The one subtle point.** The averaging is applied to the *product*, not to each trial separately. You first compute the whole-pattern probability for each kind of person, then average. Averaging each trial first and then multiplying gives a different and wrong answer. That difference is precisely what creates the dependence in Step 2.

### 3.2 In the example

Half the people are context 0 and half are context 1, so the integral is "½ × (context-0 probability) + ½ × (context-1 probability)." For the four possible patterns (trial 1, trial 2):

| Pattern | Context 0 person | Context 1 person | Mixture (what the researcher sees) |
|---|---|---|---|
| sure, sure (0,0) | 1/4 | (3/4)(9/10) = 27/40 | 37/80 |
| ambiguous, sure (1,0) | 1/4 | (1/4)(9/10) = 9/40 | 19/80 |
| sure, ambiguous (0,1) | 1/4 | (3/4)(1/10) = 3/40 | 13/80 |
| ambiguous, ambiguous (1,1) | 1/4 | (1/4)(1/10) = 1/40 | 11/80 |

The last column is the only thing the data can ever reveal when context is not recorded. Everything that follows is about what this column looks like and which models can reproduce it.

**Why this step matters.** It is the only place where "omitting context" enters the mathematics. From here on, the theorem is entirely about the properties of this averaged distribution.

---

## Part 4. Step 2: the mixture leaves two fingerprints

Averaging over hidden differences between people changes the response distribution in two specific ways. The theorem calls them **dependence** and **attenuation**.

### 4.1 Fingerprint 1: responses within a person become correlated

*(Technical draft: Proposition 1.3.)*

$$\mathrm{Cov}(Y_t,Y_u\mid w)=\tfrac12\,E\Big[\big(\pi_t(\Theta)-\pi_t(\Theta')\big)\big(\pi_u(\Theta)-\pi_u(\Theta')\big)\Big]>0 .$$

**What it says.** Two responses from the same person are positively correlated, even though, for any *given* person, the responses are independent.

**Reading it:**

- $\mathrm{Cov}(Y_t,Y_u\mid w)$ is the covariance between the responses on trials $t$ and $u$ among people with recorded characteristics $w$.
- $\Theta$ and $\Theta'$ are the aversions of two *different*, randomly chosen people from that group. $E[\cdot]$ means "average over such pairs."
- The bracketed expression compares how the two people differ on trial $t$ with how they differ on trial $u$. If person A is more averse than person B, A is less likely to choose the ambiguous option on *both* trials. So the two differences have the same sign, their product is positive, and so is the average.

**Why it is true, in words.** Knowing that someone chose the sure option on trial 1 is a clue that they are probably from the more averse context. That makes it more likely they choose the sure option on trial 2 as well. Hidden differences between people show up as consistency within people.

**In the example.** Trial 1 is chosen ambiguously with probability $19/80+11/80=3/8$ and trial 2 with probability $13/80+11/80=3/10$. If the responses were independent, "ambiguous on both" would happen $3/8\times3/10=9/80$ of the time. It actually happens $11/80$ of the time. The covariance is $11/80-9/80=1/40$.

**The consequence: every homogeneous model is wrong, however complex.** A **homogeneous** model gives everyone the same parameters (no per-person or random effects). Such a model treats one person's responses as independent coin flips. However many parameters it has, it cannot produce correlation between a person's responses. Its KL can therefore never fall below a floor set by that correlation, called the **multi-information** $I$. In the example, $I=0.00627$ nats per participant. So *both* $S$ and $K$ are guaranteed to be false. Adding cognitive complexity cannot repair what omitting context did to the joint pattern.

### 4.2 Fingerprint 2: each trial's choice rate is pulled toward 50%

*(Technical draft: Theorem 1.4 and Corollary 1.5.)* This is the step that explains why a *specific* complex model can win.

The general result is an approximation for when people differ only modestly. Write each person's aversion as the group average plus a deviation:

$$\Theta=\bar\theta(w)+\varepsilon V,$$

- $\bar\theta(w)$ ("theta-bar") is the average aversion in the group;
- $V$ is a person's standardized deviation from it, with average 0 and variance $v(w)$;
- $\varepsilon$ ("epsilon") is a dial for how large the differences between people are, so that $\varepsilon^2 v(w)$ is the actual variance of aversion. When context is omitted, this variance includes the context effect: under the project's latent equation $\theta=a_0+a_1Z+\gamma C+u$, context contributes $\gamma^2\mathrm{Var}(C\mid w)$, with $\gamma$ the size of the context effect.

The theorem shows that the true, averaged distribution is

$$p_\varepsilon(y\mid w)\approx p_0(y\mid w)\,\{1+\varepsilon^2h(y,w)\},\qquad h=h_A+h_D .$$

**What it says.** The averaged distribution equals what an *average* person would produce ($p_0$), plus a correction proportional to how much people differ ($\varepsilon^2$). The correction has a fixed "shape" $h$, which splits into two pieces that never interfere with each other: $h_D$, the dependence piece (Fingerprint 1), and $h_A$, the attenuation piece. The attenuation piece is the one we need now.

**The idea behind it: averaging a curved function.** If a function is a straight line, averaging its output over a spread of inputs gives the same answer as plugging in the average input. If the function is curved, it does not. The difference is approximately

$$\tfrac12\times(\text{variance of the inputs})\times(\text{curvature of the function}).$$

This is a form of Jensen's inequality, and it is the whole engine of Fingerprint 2.

The S-shaped logistic curve is curved, and its curvature has a particular pattern. Below 50% it bends upward, so averaging pushes probabilities up. Above 50% it bends downward, so averaging pushes probabilities down. **Averaging over people who differ pulls every trial's choice rate toward 50%.**

**The equation for how much.** On the logit (log-odds) scale, the observed choice rate on trial $t$ is shifted from the average person's by about

$$\varepsilon^2a_t(w),\qquad a_t(w)=\tfrac12\,v(w)\,\beta_t^2\,\{1-2\pi^0_t(w)\}.$$

Each factor has a meaning:

- $\tfrac12$ comes from the curved-function rule above.
- $v(w)$, times $\varepsilon^2$: the more people differ, the bigger the shift.
- $\beta_t^2$, the trial's ambiguity load **squared**. On a trial with twice the ambiguity, the same differences in aversion produce twice the spread in scores and therefore four times the shift. This squared dependence is the crux: the shift is not proportional to $\beta_t$, which is the only pattern the simple model can produce.
- $1-2\pi^0_t$, where $\pi^0_t$ is the average person's choice probability. This is positive when $\pi^0_t<1/2$ (the rate is pushed up) and negative when $\pi^0_t>1/2$ (pushed down). Either way it points toward 50%.

**In the example.** The average person has $\bar\theta=\tfrac12\log3\approx0.55$. Such a person would choose the ambiguous option at rate $\sigma(-0.55)=0.366$ on trial 1 and $\sigma(-1.10)=0.250$ on trial 2. The observed rates are $0.375$ and $0.300$. Both moved toward 50%, but trial 2, with twice the ambiguity, moved far more. On the logit scale the shifts are $+0.038$ and $+0.251$.

**Why this breaks the simple model.** Suppose you ask, separately for each trial, what single aversion would produce the observed rate. Trial 1 gives $0.511$. Trial 2 gives $0.424$. *The data look as if people become less averse as ambiguity increases.* The simple model has one $\theta$ that must serve both trials, so it cannot do this. It is forced into a compromise ($\theta=0.443$), which predicts $0.391$ (too high) on trial 1 and $0.292$ (too low) on trial 2.

The complex model has an extra knob, $\delta$, that shifts both trials' scores together. With two knobs it can make the "effective aversion" differ between trials. It finds $\theta=0.336$ and $\delta=-0.174$, which reproduces both observed rates **exactly**. In the language of probability weighting, $\delta=-0.174$ corresponds to $\rho=0.663$: a clear inverse-S distortion, produced by data that contain no distortion at all. The extra knob has been spent absorbing the bend that omitted context created.

---

## Part 5. Step 3: separating the two kinds of misfit

*(Technical draft: Lemma 2.3.)*

$$\mathrm{KL}(p\Vert q)=I(p)+\sum_t\mathrm{KL}(p_t\Vert q_t)\qquad\text{(for any homogeneous model }q).$$

**What it says.** For a homogeneous model, total misfit splits exactly into two parts:

- **$I(p)$:** the misfit caused by the within-person correlation, which no homogeneous model can touch (Fingerprint 1);
- **$\sum_t\mathrm{KL}(p_t\Vert q_t)$:** the misfit in each trial's choice rate, added over trials. Here $p_t$ is the true rate on trial $t$ and $q_t$ the model's predicted rate (Fingerprint 2).

**Why it matters.** When we subtract the simple model's misfit from the complex model's, the first part is identical for both and cancels. *The entire competition between $S$ and $K$ is about who matches the trial-by-trial choice rates better.*

**In the example.**

- The complex model matches both choice rates exactly, so its only misfit is the unavoidable correlation part: $R_K=I=0.00627$.
- The simple model also misses the rates: $R_S=0.00697$.
- The false-complex advantage is $\Delta_J=0.00070$ nats per participant. Both models are wrong, but the complex one is less wrong.

---

## Part 6. Step 4: a single number that says whether the complex model wins

*(Technical draft: Theorem 2.4 and Proposition 2.5.)*

So far we have computed the advantage by fitting both models. The theorem gives a sharper tool: a number computed from the **simple model's fit alone** that says whether the complex model will win, and by roughly how much.

### 6.1 The drift Λ

$$\Lambda=\sum_w H(w)\sum_t e_t(w)\,\big(\bar p_{wt}-\pi^{S\star}_{wt}\big).$$

**Reading it:**

- $\bar p_{wt}-\pi^{S\star}_{wt}$ is the simple model's **residual** on trial $t$: the observed choice rate minus the rate the best-fitting simple model predicts.
- $e_t(w)$ is the complex model's extra knob's **design signature**: how much nudging the distortion knob away from "off" changes trial $t$'s score. It depends only on the task. In the project's model it depends on the stated probabilities and payoffs of the two options.
- $H(w)$ is the share of participants in recorded group $w$.
- $\Lambda$ ("Lambda") is therefore a weighted correlation between "where the simple model gets it wrong" and "where the extra knob has leverage."

**What it says.** Imagine standing at the simple model's best fit and nudging the extra knob slightly. $\Lambda$ is the slope of the complex model's log-likelihood in that direction. If the slope is not zero, nudging the knob one way improves fit, so the complex model must strictly beat the simple one ($\Delta_J>0$).

**Connection to familiar statistics.** $\Lambda$ is the population version of the **score test** (Rao's test) for "no distortion." So the theorem can be read as: *the complex model wins exactly when omitted context gives the standard test for its extra parameter a non-zero signal.*

**In the example.** The extra knob shifts both trials equally, $e=(1,1)$. The simple model's residuals are $0.375-0.391=-0.016$ on trial 1 and $0.300-0.292=+0.008$ on trial 2. So $\Lambda=-0.008$. It is negative, which predicts that the complex model will turn the knob in the negative direction. It does: $\delta=-0.174$, which corresponds to $\rho<1$. The sign of $\Lambda$ predicts the *direction* of the spurious distortion.

### 6.2 How big the advantage is

$$\Delta_J\approx\frac{\Lambda^2}{2\,\mathcal I_{\rho\mid S}} .$$

**Reading it:** $\mathcal I_{\rho\mid S}$ is the **partial information** about the extra knob: how sharply the data can pin it down *after* the simple model's own parameters have been adjusted. It plays the role of the variance of a predictor after other predictors have been partialled out in a regression.

**What it says.** The advantage is half the squared signal divided by the knob's informativeness. A strong signal on a knob the data can resolve well means a large advantage.

**In the example.** $\mathcal I=0.046$, so $\Lambda^2/(2\mathcal I)=0.000697$, against an exact advantage of $0.000699$: agreement to 0.3%. The draft also proves a guaranteed lower bound, $\Delta_J\ge\Lambda^2/(2\bar B)=0.000642$. The bound holds without any approximation.

---

## Part 7. Step 5: why the drift is non-zero, as a regression

*(Technical draft: Theorem 2.6 and Corollary 2.7.)*

Step 4 says the complex model wins if $\Lambda\ne0$. Step 5 says when that happens, in terms of the attenuation pattern from Step 2. When people differ modestly,

$$\Lambda\approx\varepsilon^2\,\big\langle\mathbf a,\ \mathbf M_S\,e\big\rangle_\Omega,\qquad \Delta_J\approx\frac{\varepsilon^4}{2}\,\frac{\langle\mathbf a,\mathbf M_Se\rangle_\Omega^2}{\langle e,\mathbf M_Se\rangle_\Omega}.$$

This looks dense, but it is a familiar regression idea.

- $\mathbf a$ is the attenuation pattern from Step 2: one number $a_t(w)$ per trial and group, saying how far omission bends that trial's choice rate.
- $e$ is the complex model's extra design signature from Step 4.
- $\mathbf M_S$ means "remove whatever the simple model's own parameters can already explain." In regression terms, it takes residuals after regressing on the simple model's predictors.
- $\langle\cdot,\cdot\rangle_\Omega$ is a weighted covariance across trials. The weights $\Omega$ give more say to trials and groups whose choices are more variable (nearer 50%) and more common.

**What it says.** The complex model wins **if and only if its extra knob is partially correlated with the attenuation pattern, after controlling for the simple model's own parameters.** The size of the advantage is like an incremental $R^2$: the squared partial covariance divided by the knob's residual variance. This is the Frisch–Waugh–Lovell logic of regression, which may be familiar from "controlling for covariates."

Three consequences:

1. **It is checkable in advance.** Given a task design, a researcher can compute $\mathbf a$ and $e$ and see whether a particular complex model is *capable* of exploiting omitted context, before collecting any data.
2. **Absorption.** If the extra knob's signature can be reproduced exactly by the simple model's existing parameters (intercepts, side biases, and so on), then $\mathbf M_Se=0$. The complex model then has no advantage whatever context does. The project found such designs earlier; this formula explains them.
3. **The effect scales with the fourth power of the context effect** ($\varepsilon^4$). Halving the spread of aversion across people cuts the advantage sixteenfold. This is why the advantage in realistic examples is small (Part 10).

A further detail from the draft: most of the simple model's misfit is the within-person correlation, which the complex model cannot fix either. In the draft's numerical check, the correlation part was about 3,000 times larger than the slice the complex model recovers. The complex model wins on a sliver, but a sliver is enough when sample sizes are large.

---

## Part 8. Step 6: leave-one-out scores a different target

*(Technical draft: Lemmas 2.2–2.3.)*

The project's primary predictive criterion is **trial-level leave-one-out (LOO)**. Each single response is held out in turn. The model is refit on everything else, *including that person's other responses*, and judged on how well it predicts the held-out response. This asks a different question from BIC and Bayes factors. They ask "how well does the model describe whole response patterns?"; LOO asks "how well does it predict one more response from someone we already know?"

The two targets are linked by the **chain rule** for KL:

$$\underbrace{\mathrm{KL}(\text{whole pattern})}_{\text{what BIC and BF measure}}=\underbrace{\mathrm{KL}(\text{the other responses})}_{\text{retained}}+\underbrace{E\,\mathrm{KL}(\text{held-out response}\mid\text{the rest})}_{\text{what trial LOO measures}} .$$

**What it says.** Misfit to a whole pattern equals misfit to part of the pattern, plus misfit in predicting the remaining response once you know the part. Trial LOO only sees the last term. We write $\Delta_C$ ("C" for conditional) for the complex model's advantage on that term, per trial.

**Why it matters.** In general, winning on whole patterns ($\Delta_J>0$) does **not** imply winning on held-out responses ($\Delta_C>0$). The project has an exact example where the ranking flips. This happens with models that include person-level (random) effects. Such models learn about the person from their other responses, and that can change which model predicts the next response better.

**But for homogeneous models it cannot flip.** A homogeneous model ignores a person's other responses when predicting a new one, since all people share the same parameters. Using the decomposition from Step 3, the theorem shows

$$\Delta_C=\frac{\Delta_J}{T}\qquad\text{exactly}.$$

In words: the per-trial predictive advantage is just the per-person advantage spread evenly over the $T$ trials. In the example, $\Delta_C=0.00070/2=0.00035$ nats per trial. For homogeneous models, then, all three criteria point the same way automatically.

---

## Part 9. Step 7: from population advantage to model selection

*(Technical draft: Part III.)* Steps 1–6 were about the population: what the best possible version of each model achieves. Step 7 shows that the three criteria computed from real data *discover* that population advantage as the sample grows. In everything that follows, $n$ is the number of participants; adding trials per person is a different matter (Part 11).

### 9.1 BIC

$$\mathrm{BIC}_M=-2\,\big(\text{maximized log-likelihood of }M\big)+k_M\log n .$$

Here $k_M$ is the number of parameters. Lower is better. The complex model has the lower BIC exactly when

$$2\times\big(\text{log-likelihood gain of }K\text{ over }S\big)>(k_K-k_S)\log n .$$

**What happens as $n$ grows.** The log-likelihood gain grows like $n\times\Delta_J$: each participant contributes, on average, the population advantage. The penalty grows only like $\log n$, which grows far more slowly than $n$. Eventually the gain overtakes the penalty, so BIC picks the complex model with probability tending to one. The draft also gives an explicit probability bound, but it is extremely conservative (Part 10).

### 9.2 Bayes factor

$$\mathrm{BF}_{KS}=\frac{m_K}{m_S},\qquad m_M=\int(\text{likelihood of }M\text{ at parameter values }\phi)\times(\text{prior probability of }\phi)\,d\phi .$$

Here $m_M$, the **marginal likelihood** or evidence, is the model's likelihood averaged over its prior. The theorem shows that

$$\frac1n\log\mathrm{BF}_{KS}\ \to\ \Delta_J .$$

In words: the Bayes factor grows roughly like $e^{n\Delta_J}$, so it eventually exceeds any threshold, whether 1, 3 or 100. The proof only needs the prior to put *some* weight near the best-fitting parameter values. It does not rely on any approximation such as the Laplace method.

### 9.3 Trial-level LOO

$$\mathrm{ELPD}_M=\sum_{\text{people }i}\ \sum_{\text{trials }t}\log p_M\big(y_{it}\mid\text{all data except }y_{it}\big).$$

ELPD is the "expected log predictive density": the total log-probability the model assigned to each held-out response. LOOIC is $-2\times$ELPD. The theorem shows that

$$\frac{\mathrm{ELPD}_K-\mathrm{ELPD}_S}{nT}\ \to\ \Delta_C .$$

The per-trial gain in predictive score converges to the per-trial population advantage. Two technical steps make this work. First, deleting one response barely changes what the model learns from everyone else, and this holds uniformly across all deletions. Second, predictions never come too close to zero, so their logs behave. Neither step requires treating a person's trials as independent.

### 9.4 The assembled theorem

> **Central theorem (Theorem 0 in the draft), in words.**
>
> Suppose context shifts a latent cognitive parameter and is omitted from two nested models, a simple one $S$ and a complex one $K$. Suppose also:
>
> - **(M1)** the complex model fits whole response patterns strictly better: $\Delta_J>0$;
> - **(M2)** it is nonetheless wrong: $R_K>0$;
> - **(M3)** it also predicts held-out responses better: $\Delta_C>0$.
>
> Then, as the number of participants grows:
>
> - BIC, the Bayes factor and trial-level LOO each choose the complex model with probability tending to one, and so do all three at once;
> - the standard test of "no distortion" rejects with probability tending to one;
> - the estimated distortion parameter settles on a value other than "none" (0.663 in the example);
> - when context is measured and included, the simple contextual model is exactly correct and beats the complex one on all three criteria.
>
> For homogeneous models, (M2) and (M3) are automatic, and (M1) holds whenever the drift $\Lambda$ of Step 4 is non-zero. The running example satisfies everything.

There are also some technical conditions, which hold in the example: finitely many task configurations, every response pattern possible, proper priors, and a unique best fit for each model.

### 9.5 What context costs, and what complexity buys

*(Technical draft: Proposition 1.6.)*

$$\text{misfit of a context-blind model when context is known}=\text{its misfit as computed above}+I(Y;C\mid w).$$

The last term, $I(Y;C\mid w)$, is the **mutual information** between responses and context: how much responses reveal about context, or equivalently how much knowing context would sharpen predictions of responses. No context-blind model can recover it, however complex. In the example it is $0.129$ nats per participant, while the complex model's advantage is $0.0007$. **The complex model recovers about half a percent of what omitting context costs. Including context recovers all of it.**

---

## Part 10. What this means at realistic sample sizes

The theorem is about the long run. In the example the advantage is small, $0.0007$ nats per participant, so the long run is long.

- **BIC.** The expected log-likelihood gain overtakes BIC's penalty at about **6,300 participants**. The project's pilot simulation found BIC choosing the complex model in only 1 of 10 data sets at 1,000 participants.
- **Bayes factors and trial LOO.** At these sample sizes their effective penalties stay roughly constant rather than growing with $n$. For the Bayes factor this happens because the distortion knob is weakly identified, which shrinks its effective penalty. Standard approximations predict they choose the complex model about 55% of the time at 1,000 participants and over 90% at 10,000. The pilot found 7 of 10 (Bayes factor) and 8 of 10 (LOO) at 1,000 participants. So *these* criteria are the more vulnerable ones at sample sizes typical of large studies.
- **A rule of thumb from the draft.** Criteria with constant penalties need about $2z^2/\Delta_J$ participants, where $z$ is the normal quantile for the desired selection rate. BIC additionally needs $n\Delta_J$ to exceed $\tfrac12\log n$.

These finite-sample figures are approximations, not theorems. The draft labels them as such.

---

## Part 11. When the mechanism switches off

*(Technical draft: Part IV.)* Knowing when the theorem does *not* apply is as important as the theorem itself. Each of the following breaks a specific step.

1. **The simple model can already represent the mixture.** For example, suppose aversion varies normally across people and the simple model includes a normally distributed random effect for $\theta$. Then the simple model is correct, both misfits are zero, and nothing favors the complex model. This breaks Step 3.
2. **Absorption.** The extra knob's design signature can be reproduced by the simple model's existing parameters across the whole task. The two models then make identical predictions, whatever context does. This breaks Step 5. The project found such designs; richer designs with known-probability calibration trials avoid it.
3. **Random effects absorb most of the effect.** *(Proposition 4.3.)* If the simple model includes a random effect with a free variance, that variance already accounts for "people differ," which is the $\varepsilon^2$ term in Step 2. What remains for the complex model to exploit is only the *shape* of the variation: lopsidedness (skew) or clumping into types. The advantage then shrinks from order $\varepsilon^4$ to at most $\varepsilon^6$ (skewed) or $\varepsilon^8$ (symmetric). If you halve the spread of aversion, the advantage against a homogeneous model falls by 16× but against such a hierarchical model by 64× or more. This is the main reason the project's hierarchical models have been hard to break.
4. **Balanced contexts and context-dependent spread.** *(Proposition 4.4.)* Suppose context changes how *variable* aversion is, rather than its average, and the contexts are balanced and otherwise alike. Then a distortion parameter that ignores context cannot imitate the effect at first order. The simple model is wrong, but the complex model is no better. Breaking the balance (different averages, or unequal group sizes) restores the possibility.
5. **LOO can disagree with BIC and Bayes factors.** With person-level effects, (M3) can fail even when (M1) holds (Step 6). BIC and Bayes factors then favor the complex model while trial LOO favors the simple one.
6. **Symmetric differences around indifference.** In the example's task, if aversion were spread symmetrically around zero (the indifference point), every choice rate would sit at exactly 50%. The simple model would match it, and there would be no advantage.

---

## Part 12. What is proved and what is still open

**Proved in the draft** (for a finite number of task configurations, a fixed number of trials, and sample size growing):

- Steps 1–9, for homogeneous models;
- the boundary results;
- the full example.

**Conditional (for models with random effects):** the local version holds if certain regularity conditions can be verified for the specific model and design, and if the drift and the LOO condition (M3) can be shown to hold. Constructing a convincing hierarchical example of the project's probability-distortion comparison is the main open problem. Points 3 and 4 of Part 11 explain why it is hard and what such an example would need: lopsided or clumped context effects, or unbalanced contexts.

**Other open questions:**

- **More trials per person.** For homogeneous models the per-trial advantage stays the same as trials are added, so the problem persists. For hierarchical models with trial-level LOO, it plausibly *vanishes* as trials accumulate, because each person's other responses increasingly reveal their own $\theta$. The project's research specification currently anticipates misselection "even as task length increases"; that target may need revising for hierarchical models.
- **Continuous covariates** and **uncertainty intervals** for LOO differences.
- **Independent review** of the new results.

---

## Glossary of symbols

| Symbol | Read as | Meaning |
|---|---|---|
| $\theta$, $\Theta$ | theta | Latent ambiguity aversion (lower case: one value; upper case: varying across people) |
| $C$ | — | Context (omitted from the candidate models) |
| $w$ | — | Everything recorded about a person and their task |
| $Y_t$, $y$ | — | Response on trial $t$ (1 = ambiguous option); a whole response pattern |
| $T$, $n$ | — | Number of trials per person; number of participants |
| $\sigma(x)$ | sigma | Logistic function, $1/(1+e^{-x})$; converts a score to a probability |
| $\mathrm{logit}(p)$ | — | Log-odds, $\log\{p/(1-p)\}$; inverse of $\sigma$ |
| $\eta_t$, $\kappa_t$, $\beta_t$ | eta, kappa, beta | Trial score; non-ambiguity attractiveness; ambiguity load of trial $t$ |
| $\pi_t$ | pi | Choice probability on trial $t$ |
| $\prod$, $\sum$, $\int$ | product, sum, integral | Multiply over; add over; weighted average over |
| $\rho$, $w(p;\rho)$ | rho | Probability-distortion parameter (1 = none); Prelec weighting function |
| $S$, $K$, $S^C$ | — | Simple model; complex model; simple model with context |
| $\mathrm{KL}(p\Vert q)$ | KL divergence | Average extra surprise of model $q$ when truth is $p$ (nats) |
| $R_M$ | risk | Best achievable KL of model $M$ |
| $\Delta_J$, $\Delta_C$ | Delta | Complex model's advantage on whole patterns (per person) and on held-out responses (per trial) |
| $I$ | multi-information | Misfit caused by within-person correlation; a floor for homogeneous models |
| $\varepsilon^2v(w)$ | epsilon | Variance of aversion among people with the same recorded characteristics |
| $a_t$ | — | Attenuation: how far omission bends trial $t$'s logit toward 0 |
| $e_t$ | — | Design signature of the complex model's extra parameter |
| $\Lambda$ | Lambda | Drift: score-test signal for the extra parameter at the simple model's fit |
| $\mathcal I_{\rho\mid S}$ | partial information | How sharply the data identify the extra parameter after the simple model's parameters are adjusted |
| $I(Y;C\mid w)$ | mutual information | How much responses reveal about context; what omitting context costs |

## Where to go next

- The full technical draft, with every proof: [`central_theorem_full_draft.md`](central_theorem_full_draft.md) (PDF: [`central_theorem_full_draft.pdf`](central_theorem_full_draft.pdf)).
- The minimal example as a standalone proof: [`minimal_ambiguity_proof.md`](minimal_ambiguity_proof.md).
- Pilot simulation results: [`minimal_ambiguity_validation.md`](minimal_ambiguity_validation.md).
- Background reading, not yet verified against the sources under the project's literature policy: Estes (1956) on inferences from averaged group data; Chesher (1984) on neglected heterogeneity; Prelec (1998) on probability weighting.
