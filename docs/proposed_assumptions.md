# Proposed Assumptions

Agents may append proposed assumptions here. They must not move them into `assumption_registry.md` without human approval.

## A-006 Trial-design exogeneity for simplified mixture

For the omitted-context mixture lemma to use
`dF_{theta|Z}(theta|z)` rather than `dF_{theta|X,Z}(theta|x,z)`,
trial features `X_it` are fixed by design or assigned independently of
`theta_i` conditional on `Z_i`.

Rationale: Issue #4 proposes the simplified `theta | Z` mixture display, but
the direct conditional law of total probability gives a mixture over
`theta | X,Z`. The simplified display is appropriate only under a fixed-design
convention or conditional trial-design exogeneity.
