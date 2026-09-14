# Project files and synchronization

Recovered 2026-09-13. The normal local folder and this Codex task use `/Users/brendanlam/Documents/GitHub/Omitting-Context-in-Cognition`. GitHub: https://github.com/blam3/Omitting-Context-in-Cognition/tree/main.

## Start here

| Artifact | Location |
|---|---|
| Current minimal ambiguity proof | [Proof](docs/minimal_ambiguity_proof.md) |
| Proof review | [Review](docs/proof_reviews/review_minimal_ambiguity.md) |
| Bayesian / trial LOO validation and full pilot results | [Validation](docs/minimal_ambiguity_validation.md) |
| Earlier finite benchmark proof package | [Package](PROOF_PACKAGE.md) |
| Primary theorem specification | [Specification](docs/primary_theorem_specification.md) |
| General perturbation and conditional-risk proofs | [Joint](docs/context_score_perturbation_2026-09-09.md), [conditional](docs/trial_conditional_perturbation_2026-09-09.md), [smooth extension](docs/smooth_observable_extension.md) |
| Gaussian constructive draft (historical assumption IDs) | [Gaussian draft](docs/proofs/L2_gaussian_constructive_heterogeneity.md) |
| Current roadmap and machine-readable progress | [Roadmap](docs/proof_roadmap.md), [state](registries/proof_progress.json) |
| Study 1 rewrite | [Word](docs/prospectus/Study1_rewrite.docx), [Markdown](docs/prospectus/Study1_rewrite.md) |
| Manuscript and supplement | [Main](manuscript/main.tex), [supplement](manuscript/supplement_proofs.tex) |

## Why files were missing

The normal folder was on `main`. Newer Codex work was committed to `agent/general-context-proof-20260909` in `/private/tmp/ocecm-proof-progress-20260909` and had not been pushed or merged. The task titled “Audit proofs and theorems” also displayed an obsolete project directory, `autonomous_loop_researcher_starter`, although its commands worked in the temporary proof checkout. Codex task history is a record of work, not a separate live file store.

## Preserved parallel versions

Complete source snapshots preserve divergent GitHub/local work without treating incompatible theorem assumptions, registries or code as one approved scientific model. Unzip to inspect their original folder structure. Exact commits are in [the manifest](docs/archive/branch_snapshots/manifest.json).

- [Formal theorem strategy](docs/archive/branch_snapshots/formal-theorem-strategy.zip): `docs/theorems/T-003` through `T-007`, Lean attenuation algebra, coherence checks, and supporting files.
- [KL proof and score screen](docs/archive/branch_snapshots/kl-score-screen.zip): `docs/proofs/L3_kl_dominance.md`, `docs/proofs/reviews/L1_mixture_lemma_claude_review.md`, and R score-screen work.
- [Interactive project map](docs/archive/branch_snapshots/project-map.zip): `docs/project_map.html`, its data and generator.
- [Gaussian draft and original assumption registers](docs/archive/branch_snapshots/gaussian-heterogeneity.zip).

The minimal proof branch supplies the newer PI decisions when merge conflicts involve scientific workflow. Earlier main versions remain in Git history. Historical snapshots and the Gaussian draft retain their original status and assumption numbering; synchronization does not approve or reconcile their scientific claims. Older STATUS/context pages may describe previous milestones; use the current roadmap and progress JSON for active work.

## Ongoing use

Use the normal project folder for new work. The temporary proof checkout is synchronized at this checkpoint, but subsequent branch edits still require commit, merge and push to appear on GitHub main. This operation is a one-time reconciliation, not automatic synchronization.
