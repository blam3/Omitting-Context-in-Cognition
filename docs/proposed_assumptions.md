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

## A-009 Common comparison unit and design distribution

Status: proposed by the L3 KL dominance draft on 2026-09-01. Decision-gated;
not approved.

For the KL dominance bridge, the context-omitting simple class `M_S`, the
context-omitting complex class `M_K`, and the context-aware class `M_{S+C}`
are evaluated at the same declared comparison unit (trial or participant),
against the same omitted-context target law `p_0`, under the same
covariate/design distribution `P_V`; and `P_V` is the distribution of the
population to which the scientific claim generalizes.

Rationale: the divergence difference `delta_S - delta_K` is interpretable only
because a common conditional entropy term cancels. Evaluating the two classes
at different units or under different design distributions leaves
non-cancelling entropy terms and produces a difference with no meaning. See
counter-example CE-5 in `docs/proofs/L3_kl_dominance.md`.

## A-010 Kernel non-degeneracy for finite divergence

Status: proposed by the L3 KL dominance draft on 2026-09-01. Decision-gated;
not approved.

For the KL dominance bridge, there exist `epsilon` in `(0, 1/2)` and a finite
`T_max` such that every per-trial choice probability, under `p_0` and under
every candidate model used in the comparison, lies in `[epsilon, 1-epsilon]`
for `P_V`-almost every covariate value, and no participant contributes more
than `T_max` trials. The unit-level log densities are then uniformly bounded by
`T_max log(1/epsilon)`.

Rationale: without a uniform bound away from zero and one, the expected
divergence can be infinite for some candidates, and differences of infima are
ill-defined, so Theorem L3.2 fails as an identity. The bound is stated on the
per-trial kernel rather than on the unit-level density because at the
participant unit the response has `2^T` support points, so a unit-level bound
of this form is unsatisfiable for large `T` and would make the assumption
vacuous. Logistic and softmax choice kernels satisfy the per-trial bound on any
bounded parameter set, so the condition is a scope statement rather than a
restriction on the models the project intends to fit. See counter-example CE-4
in `docs/proofs/L3_kl_dominance.md`.
