# Primary roadmap: minimal ambiguity comparison

Updated 2026-09-12 under explicit user direction. This replaces the general/hierarchical priority. Authoritative proof: `minimal_ambiguity_proof.md`. State: `../registries/proof_progress.json`.

## Contract

Exactly one fitted global ambiguity parameter versus ambiguity plus probability distortion. Fix shared sensitivity and other nuisance constants identically. Two specified ambiguity trials; shared binary context changes true ambiguity; no true distortion. Keep context-aware and context-null controls. Primary prediction target remains exact single-trial LOO. Independent sampling unit is the participant.

The direct author proof establishes strict joint separation, positive complex residual risk, and separate BIC/BF/trial-LOO corollaries. Review remains required. The small gap does not promise ordinary-sample-size wins. Do not change seeds, priors or model scope to manufacture favorable outcomes.

## Remaining daily goals

| Item | Exit artifact | Backup |
|---|---|---|
| M1 Review minimal proof | `proof_reviews/review_minimal_ambiguity.md`: task mapping, parameter counts, KL decomposition, global fits, priors and single-response deletion. | Repair a named defect; same-LLM review is not external verification. |
| M2 Validate computation | `minimal_ambiguity_validation.md`: deterministic evidence/posterior quadrature, exact trial deletion and a predeclared small fixed-seed pilot with all outcomes. | Refine numerical accuracy before adding simulations. Preserve unfavorable results. |
| M3 Write concise proof | `minimal_ambiguity_manuscript.md`: main theorem, three corollaries, scope and controls. | Use reviewed Markdown; no formatting detours. |
| M4 Final audit | `proof_reviews/minimal_final_verdict.md`: proof and numerical provenance, remaining issues, optional extensions. | Work only named gaps; await PI acceptance once review-ready. |

Each run closes one bounded artifact, within roughly 60 minutes. After two distinct unsuccessful attacks, checkpoint the exact gap. Two no-progress runs require a changed route. Never add general machinery merely to keep working. Update state and a schema-valid log after each run.

## Deferred work

General smooth-family theorems, eight-trial calibration/latent inversion, hierarchical empirical parameterizations, Gaussian constructions and a full Lean probability library are optional extensions. They are not M1–M4 dependencies. Preserve prior files. Reopen only for a named main-proof defect or a user request. Small Lean certificates may assist verification but are not mandatory detours. The previous roadmap is in `archive/proof_roadmap_before_minimal_2026-09-12.md`.

## Scheduled execution

Use the existing 9 AM America/New_York heartbeat. Synchronized working folder: `/Users/brendanlam/Documents/GitHub/Omitting-Context-in-Cognition`. Set explicit workdir. The former `/private/tmp/ocecm-proof-progress-20260909` checkout is retained as a synchronized checkpoint; use the normal project folder for durable files. Do not fall back to an older roadmap.

Read current state, proof, latest log and git status. Notify only meaningful results, corrections or required decisions. Commit local artifacts for persistence; do not merge or publish without authorization. Stop routine work when awaiting PI acceptance.
