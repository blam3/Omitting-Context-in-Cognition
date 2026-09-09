# Primary additive-context route: moment and Gaussian conditions

Status updated 2026-09-08: A-003 is now the PI-approved primary formal route. The historical filename is retained for link stability. The additive equation and context moments are approved; residual and Gaussian sufficient conditions below remain explicit proposals unless separately adopted. This is not yet an observable model-selection theorem. See pi_decisions_2026-09-08.md.

Let $\Theta=\alpha_0+\alpha_1 Z+\gamma C+u$, with finite conditional second moments. Define $m(z)=E[C\mid z]$ and $v(z)=\operatorname{Var}(C\mid z)$. Linearity of conditional expectation and expansion of the squared centered sum give

$$E[\Theta\mid z]=\alpha_0+\alpha_1 z+\gamma m(z)+E[u\mid z],$$
$$\operatorname{Var}(\Theta\mid z)=\gamma^2v(z)+\operatorname{Var}(u\mid z)+2\gamma\operatorname{Cov}(C,u\mid z).$$

Thus if $E[u\mid z]=0$, $\operatorname{Var}(u\mid z)=\sigma_u^2$ and $\operatorname{Cov}(C,u\mid z)=0$, the mean is $\alpha_0+\alpha_1 z+\gamma m(z)$ and the variance is $\gamma^2v(z)+\sigma_u^2$. Gaussianity is unnecessary for these moment identities. Nonconstant $v(z)$ gives nonconstant variance only if $\gamma\ne0$ (with nonconstancy understood on the support, up to null sets).

For the stronger normal-distribution conclusion, one sufficient specification is $C\mid z\sim N(m(z),v(z))$ and $u\mid z\sim N(0,\sigma_u^2)$, independent conditional on $Z=z$. The conditional characteristic function of $\Theta$ is then the product

$$e^{it(\alpha_0+\alpha_1z)}e^{it\gamma m(z)-t^2\gamma^2v(z)/2}e^{-t^2\sigma_u^2/2},$$

which is the characteristic function of $N(\alpha_0+\alpha_1z+\gamma m(z),\gamma^2v(z)+\sigma_u^2)$. This calculation uses the normal characteristic-function formula and its uniqueness, not an unstated independence inference.

Without the residual conditions, $u=-\gamma(C-m(z))$ cancels the context variance. Even a valid latent-variance result does not itself prove a strict observable KL gap. The finite benchmark establishes the latter for a different binary-context/quadratic-model construction. The primary route must now establish observable separation for its own specified candidates; the benchmark cannot supply that conclusion automatically.
