# Theorem Statements

One file per result. Each carries a machine-readable `theorem-meta` block that
`scripts/check_coherence.py` validates against the registries.

| File | Result | Status |
|---|---|---|
| (`../omitted_context_mixture_lemma.md`) | T-001 mixture representation; T-002 exogenous-design corollary | proof-critic-review / corollary-only |
| `T-003_gaussian_constructive.md` | Gaussian constructive heterogeneity, with a sharp iff | proof-draft |
| `T-004_kl_dominance.md` | when the KL inequality actually holds | proof-draft |
| `T-005_loo_predictive.md` | trial-level LOO estimator-to-population bridge | statement-draft (T-005b is a sketch) |
| `T-006_bayes_factor_deferred.md` | why Bayes factors are not a theorem target | deferred |
| `T-007_finite_sample_selection.md` | finite-sample thresholds, singular-case corrected | proof-draft |

Nothing here is accepted. As of D-006 (2026-09-09) there are **no open decision
gates**; every result is blocked on proof-critic review instead. See
`../theorem_backlog.md` for the route, `../approval_log.md` for the decisions,
and `../../loops/proof_loop.md` for the four-part gate into the supplement.

## Citations are unverified

The results here cite standard sources by name (White; Vuong; Takeuchi; Kleijn
and van der Vaart; Watanabe; Chernoff; Self and Liang; Vehtari and colleagues;
Meng and Wong). Every one is recorded in `../citation_claim_map.csv` with status
`unverified` — no DOI has been confirmed. Under
`../literature_verification_policy.md` they may not enter the manuscript in that
state. Verifying them is a prerequisite for any of these results reaching the
supplement, alongside proof-critic review.

## The `theorem-meta` block

```
<!-- theorem-meta
id: T-004
title: ...
claim: C-004
status: statement-draft
assumptions: A-001, A-002, A-003, A-007, A-008, A-009
depends_on: T-001, T-003
approval: D-001
-->
```

`assumptions` is what this result *establishes or requires directly*.
`depends_on` is what it inherits from. The checker computes the transitive
closure and fails if the body cites an assumption that is in neither — which is
how a downstream result quietly consuming an upstream assumption gets caught.

## The `coherence-allow` marker

A file that *discusses* forbidden notation rather than using it declares:

```
<!-- coherence-allow: F_Theta_given_Z, bare_delta_ell -->
```

Use it sparingly and only where the forbidden form is quoted in order to
correct or retire it. Notation rules live in `../notation_registry.md`.
