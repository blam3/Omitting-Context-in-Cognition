# Omitted-context mixture lemma

Status: short proof draft, locally checked on 2026-09-05; independent acceptance pending. Claim C-002. General primary conditioning remains on both trial features and covariates; rejected A-006 is not reinstated.

## Lemma 1.1: finite-response conditional mixture

Let $Y$ have finite support, and let the latent parameter $\Theta=h(Z,C,U)$ take values in a standard Borel space. Assume the regular conditional law $F_{\Theta\mid X,Z}$ exists, and the measurable probability kernel satisfies

$$P(Y=y\mid X,Z,\Theta)=p(y\mid X,\Theta;\eta^*)\quad\text{almost surely}.$$

Then, for $(X,Z)$-almost every $(x,z)$,

$$P(Y=y\mid X=x,Z=z)=\int p(y\mid x,\theta;\eta^*)\,dF_{\Theta\mid X,Z}(\theta\mid x,z).$$

**Proof.** Apply the tower property to $1_{\{Y=y\}}$:

$$E[1_{\{Y=y\}}\mid X,Z]
=E[E[1_{\{Y=y\}}\mid X,Z,\Theta]\mid X,Z]
=E[p(y\mid X,\Theta;\eta^*)\mid X,Z].$$

Represent the last conditional expectation using the stated conditional distribution. The kernel is bounded, hence integrable; finite outcome support allows one common null set. $\square$

## Corollary 1.2: exogenous design

If additionally $\Theta\perp X\mid Z$, replace $F_{\Theta\mid X,Z}$ by $F_{\Theta\mid Z}$ in the display. This follows by substitution. A genuinely deterministic common design is a special case; merely treating an observed design as fixed, or calling assignment non-adaptive, does not establish independence. Adaptive assignment or dependence on an unrecorded baseline trait can violate it.

## Participant-level version and scope

For a deterministic common design $x_{1:T}$, suppose the trial kernels above hold and the responses are mutually conditionally independent given **$(\Theta,Z)$** (A-011). Then, for $Z$-almost every $z$, the likelihood for a new participant is

$$P(Y_{1:T}=y_{1:T}\mid Z=z)=\int\prod_{t=1}^T p(y_t\mid x_t,\theta;\eta^*)\,dF_{\Theta\mid Z}(\theta\mid z).$$

Apply the same argument to the finite vector $Y_{1:T}$. The integral encloses the product. The product of separately marginalized trial probabilities is generally not this joint likelihood. Other designs require the appropriate joint conditional kernel and mixing distribution; the single-trial result does not silently establish conditional trial independence. Independence given $\Theta$ alone need not survive conditioning on $Z$; see the explicit counterexample and repair in [the 2026-09-06 review](proof_reviews/review_01_KL.md).

The identity alone proves neither observable complexity nor model-selection superiority. A Bernoulli mixture at one predictor value remains Bernoulli. The main work is showing that a restricted response function or joint law cannot represent the marginal distribution. [PROOF_PACKAGE.md](../PROOF_PACKAGE.md) supplies an explicit two-trial construction and separate BIC, BF and leave-one-participant-out corollaries. Gaussian heterogeneity is an [optional example](optional_gaussian_heterogeneity.md), not a dependency.
