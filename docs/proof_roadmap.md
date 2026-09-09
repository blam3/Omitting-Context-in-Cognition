# Daily proof roadmap

## Operative revision — 2026-09-08

Latest user direction: P-G1 (specification sections 2–3) is approved for theorem development. Prioritize the general theorem. The synthetic pair is a supporting construction, pursued when it closes a general proof obligation or establishes nonvacuity. Next bounded artifact: `docs/general_theorem_architecture.md`, mapping mechanism-to-observable-separation conditions, distinct joint/conditional gaps, criterion transfer lemmas, and the precise role of the example. Distinguish proved results from proposals and avoid assuming the central separation conclusion. Preserve all current absorption obstructions; after this architecture task, select the highest-value open general obligation rather than automatically extending the example.

The PI has changed the primary route: A-003 additive context model, trial-level LOO, and M4 probability distortion. Read `docs/pi_decisions_2026-09-08.md` and `docs/bayesian_comparison_plan.md` first. The current `registries/proof_progress.json` takes precedence over the historical ten-run schedule below. Do not restore Gaussian-optional or primary-LOPO defaults from that schedule.

G1 specification is complete at author-draft level in `docs/primary_theorem_specification.md`; proposed conditions are not approvals. Next: G2_observable_separation, with separate joint and conditional KL gaps. G2b_primary_BIC and G3_trial_LOO follow G2; G4_primary_BF branches from G2 independently of the trial-conditional gap; G5_primary_review requires both BIC and BF/LOO, then G6_primary_computation and G7_primary_manuscript. Dependencies require artifacts, not authorization alone. If a new substantive condition is necessary, present its exact statement for decision while progressing independent authorized work.

The older D1/D2 reviews remain completed benchmark work; D3–D10 remain available secondary benchmark tasks. Do not mark the primary project complete when that older chain closes. Primary completion requires reviewed additive-context scope (or an explicit PI-approved limitation), probability-distortion specification and evidence, trial-level prediction validation, criterion-specific results, and PI acceptance. Historical benchmark mathematics and proof hashes should be preserved. The attempt limits, truthful reporting and compute policy below continue to apply.

The first G2 attempt is recorded in `docs/primary_separation_attempt_2026-09-08.md`: exact shared-effect representability and two-trial distortion absorption block those routes. The full existing support is now audited in `docs/design_absorption_audit_2026-09-08.md` and is absorbed for every rho. A complete richer support manifest is not yet specified; obtain or explicitly specify it before its global positive-scale audit. Do not rerun the failed pair, infer missing lotteries from the scaffold, or remove nuisance terms. Conditional P-G3 score/evidence limits are author drafts only, not positive primary-selection results.

## Historical September 5 roadmap (secondary finite benchmark)


Updated: 2026-09-05. Operational owner: the LLM running the daily proof task.

Daily heartbeat: `daily-cognitive-model-proof-progress`, active at 9:00 AM America/New_York. This is the default time used while the optional scheduling preference remained unanswered. The automation follows this file and the progress state; change the existing automation rather than creating a duplicate.

## Objective and definition of done

Complete a reviewable theorem package demonstrating that an omitted-context cognitive mechanism can induce strict **observable participant-level** KL superiority of a false complex candidate over a simple context-omitting candidate, with distinct BIC, BF and new-participant LOO corollaries. Preserve the comparison with the correct contextual mechanism and the cases where no superiority occurs.

The bounded completion inventory is T-001, T-002, T-004, T-005, T-006, T-007 and T-008 in `docs/theorem_backlog.md`, including their L1–L3 technical dependencies. T-003 Gaussian heterogeneity is optional and must not block completion. An extension to the structural ambiguity task is a separate planned work item; it must receive either a complete scoped proof or a documented counterexample/blockage decision, not an indefinite promise. Generalization to every cognitive model is not a goal.

Completion requires:

1. Every main statement has explicit variables, information available to each candidate, population target, sampling unit, assumptions, parameter space, prior (when needed), convergence mode and boundary cases.
2. Every load-bearing obligation has a local derivation or an inspected source with its hypotheses checked. No “standard arguments” stand in for a missing step.
3. A separate adversarial review accepts the full dependency chain, or identifies issues that are repaired and re-reviewed. Author self-check and structural lint alone do not count as independent review.
4. The simulation baseline contains the generating structural terms; fixed-parameter and no-context controls are distinguished; numerical criterion code uses participant joint likelihoods and matching deletion units.
5. The proof and model-recovery checks pass, finite-sample evidence is reported without cherry-picking, and manuscript/SI text agrees with the registries. Final scientific support remains subject to PI acceptance.
6. Every extension that remains unproved is explicitly outside the accepted theorem. Optional work does not keep the completion flag false forever.

## Current baseline: work completed on day zero

- Corrected the shared GLM baseline and added a fixed-parameter control and direct representation checks.
- Shortened the mixture lemma and separated an optional corrected Gaussian example.
- Selected linear utility sensitivity versus quadratic utility curvature, with two trials and one shared binary context per participant.
- Wrote a full local proof of $0<R_K<R_S$, BIC, BF with proper uniform priors, exact participant LOO and simultaneous asymptotic selection in `PROOF_PACKAGE.md`.
- Derived finite-state uniform convergence, likelihood localization, BF integral bounds and concentration uniform over all participant deletions, rather than assuming them.
- Added reproducible numerical checks in `scripts/verify_constructive_theory.py`.

**Scientific caution from the calculations:** the explicit example has a small positive gap (about 0.000699 nats per participant). The three fixed-seed finite-sample datasets are checks of computation, not evidence that complex models usually win at ordinary sample sizes; all three currently favor the simple candidate. Do not change the seed or replace the example merely to manufacture a favorable demonstration. A preregistered sensitivity study may investigate how the gap depends on declared DGM parameters.

## Daily operating contract

Read, in order: this file; `registries/proof_progress.json`; `PROOF_PACKAGE.md` sections linked by the active obligation; assumption/claim registers; latest research update; `git status --short`. Inspect changes since the last run before reusing a proof conclusion. The actual project path is `/Users/brendanlam/Documents/GitHub/Omitting-Context-in-Cognition`; the old `autonomous_loop_researcher_starter` path is absent. If the path moves, resolve the saved project location rather than creating an empty replacement repository.

Recompute readiness from dependencies: when every dependency is complete with valid evidence, move a pending item to `ready`. Choose **one ready work item** from the state file. A daily goal is a verifiable artifact, not a time promise or a number of tokens. Each run should close an obligation, establish a counterexample, or record a specific failed approach and advance to a viable fallback. Do not merely re-summarize the plan.

Suggested per-run budget: 5 minutes orientation, 30 minutes focused proof work, 15 minutes adversarial checking or a small numerical experiment, and 10 minutes recording state and the next exact action. This is a work cap, not a command to wait out unused time. Stop early when the bounded artifact is complete. If a lemma remains open, checkpoint its exact statement and the strongest established intermediate result.

The daily task may edit local proof drafts, tests, registries and roadmap within the user's authorized scientific scope. No routine reapproval for this constructive pair, its stated assumptions, the shared baseline repair, or these criterion corollaries. Document new scope rather than silently changing the main estimand/model. Do not select the final RAID model, access restricted data, run the 60,000-replication grid, publish, merge, or promote to final scientific support without the separate authorization those actions need.

## First ten runs: daily goals and exit artifacts

These are dependency-ordered work sessions, not guaranteed calendar completion dates. Skip a row already completed with valid evidence. If an earlier review exposes a gap, repair it before its dependent row.

| Run | Goal | Concrete exit artifact | Fallback if blocked |
|---|---|---|---|
| 1 | Adversarial review of T1 and L1: exact participant cells, strict KL infima, mechanistic and joint-distribution falsity | `docs/proof_reviews/review_01_KL.md`, covering every O1–O3 step with line anchors, examples and verdict | Exhaustively enumerate the four states and construct a counterexample to the precise failing implication; narrow that implication only |
| 2 | Adversarial review of L2 and C1, especially compactness, population interiority and probability bounds | `review_02_BIC.md` plus repaired equations if needed | Keep the exact realized BIC identity; isolate the minimum convergence lemma; do not assert a useful finite-sample threshold without its constants |
| 3 | Adversarial review of C2 evidence integration and prior normalization | `review_03_BF.md`, check both integral bounds and the interior event | Prove only $n^{-1}\log BF\to\Delta$ by finite-space upper/lower likelihood bounds if the sharper penalty expansion fails; label the narrower result |
| 4 | Adversarial review of L3/C3: delete whole persons, uniformity over all deletions, probability floor before taking logs | `review_04_LOPO.md` and explicit held-out-unit check | Use exact four-cell refits for diagnosis. If theory fails, isolate deletion lemma; fixed-training-fraction cross-validation is an explicitly different result, not a silent LOO substitute |
| 5 | Integration review of all core results; repair only review findings | `review_05_integration.md`, all obligations cross-referenced and closed, no stale assumptions | Freeze generalizations; make an issue ledger and work in dependency order until core consistency is restored |
| 6 | Map utility example into a fully specified ambiguity-choice task with reference payoff and known/estimated nuisance parameters made explicit | `docs/ambiguity_extension.md`: exact mapping with complete proof, or named obstruction and counterexample | Use an explicitly restricted two-trial ambiguity subdesign if valid; retain the utility theorem and explain the scientific limitation if no faithful mapping is available |
| 7 | Establish robustness/boundaries without losing simplicity: context-null, sufficient shared random effects, design dependence | `docs/proof_reviews/review_07_boundaries.md`; closed results or explicit negative results | Prefer a finite-support continuity argument over an unrestricted approximation theorem; do not expand the main claim to singular mixtures |
| 8 | Validate finite-sample computation on a predeclared small grid; compare exact participant refits/quadrature and proper-prior sensitivity | Seeded report with all cells, numerical convergence checks, MC uncertainty if estimating rates | If Bayesian computation is unstable, use the four-state sufficient counts and refined quadrature; keep the proof intact and report numerical limits. Cap the pilot before expensive work |
| 9 | Prepare concise manuscript/SI proof presentation from the reviewed package and verified references | Reviewable `manuscript/theory_draft.tex` or standalone draft; concise main proof and technical appendix, without claiming final acceptance | Keep the reviewed Markdown as the authoritative artifact if TeX tooling fails; no days spent on tool installation |
| 10 | Final adversarial audit, reproducibility and scope reconciliation | `docs/proof_reviews/final_verdict.md`, completed inventory, explicit deferred extensions, decision-ready scientific package | Produce a precise residual-issue packet. Continue only on an actionable named issue, not cosmetic rewriting |

Independent review means a distinct reviewer pass that attempts to disprove the statement without treating the author verdict as evidence. Prefer a separate human or fresh review task where available and authorized. A later pass by the same LLM may be useful but must be labeled “separate LLM review pass,” not human review or fully independent external verification. Do not spawn new sidebar tasks or subagents unless authorized by the user or applicable instructions.

## Anti-loop rules and backup ladder

- **Two attacks per obligation per run.** Before each attack record the exact missing statement and the route. After about 20 minutes without a new bound, counterexample, verified citation or calculation, checkpoint and change approach. “Think harder” is not a new approach.
- **Two no-progress runs trigger a fallback.** On the same blocker, two runs with no new mathematical evidence prohibit a third identical attempt. Choose the next documented route: exact finite-state enumeration → local analytic inequality → verified external theorem → explicitly weakened claim → counterexample/blockage record.
- **Three blocked runs require intervention or deferral.** If every authorized route has failed and no useful independent work remains, mark that obligation `blocked_needs_input`, ask one specific mathematical question, and do not send the same question daily. Continue another ready obligation if possible. Do not automatically weaken the central scientific claim to make a status green.
- **Failed attempts are durable.** Record the hypothesis tried, exact failure, artifact, and condition that would justify retrying. Revisit only after that condition changes.
- **No circular evidence.** Simulation agreement does not prove a theorem; a lint pass does not verify a proof; an assumption registry entry does not establish the assumption for an empirical model.
- **No criterion substitution.** BF is not BIC, LOO is not WAIC, and trial-wise prediction is not new-person prediction. Any replacement is an explicitly labeled backup claim.
- **No unbounded literature search.** After two targeted searches without a usable source, write the needed lemma precisely and try a local proof or bounded counterexample. Do not keep adding citations that do not close it.
- **No cosmetic progress.** Once a reviewed section is correct, do not rephrase it daily. Reopen it only if changed dependencies, a counterexample, or a review finding warrants it.
- **No seed shopping.** Preserve unfavorable results and the declared simulation grid. A small positive asymptotic gap need not imply practically common finite-sample selection.
- **No mandatory Gaussian or Lean detour.** Optional heterogeneity calculations and formalization wait until the mathematical package is closed. If formalization is later pursued, formalize one finite-state result first rather than building a general probability library.

## Required end-of-run checkpoint

Update `registries/proof_progress.json` with: current item/status, closed obligations, artifact paths, attempts and failed routes, consecutive no-progress count, exact next action, and any dependency changes. Append one schema-valid `logs/research_updates/<timestamp>_proof_daily.json`. Record tests actually run, not planned tests. Update a claim status only when its evidence warrants it; `supported_final` remains a scientific acceptance decision.

A user notification is warranted for a closed theorem/corollary, a material correction/counterexample, completion, a failure that changes the route, or an actionable question. Stay quiet when nothing actionable changed. The local checkpoint still gets written. When every required work item is complete and the final review packet is ready, mark `awaiting_pi_acceptance`; do not spend later daily runs rewriting the package. When accepted, mark `complete` and deactivate the monitor if the scheduling tool supports it. Do not archive the user's research task without a request.

## Daily automation prompt

Work in `/Users/brendanlam/Documents/GitHub/Omitting-Context-in-Cognition`. Follow `docs/proof_roadmap.md` and `registries/proof_progress.json` to advance the first ready proof obligation. Read the active proof, relevant assumption/claim registers, last update and current changes before editing. Complete one bounded, reviewable mathematical task; use the roadmap's attempt limits and fallback routes. Preserve participant joint likelihoods and the PI-approved primary single-trial holdout target; whole-person holdout is secondary. Follow the current scope decision over historical defaults. Update the progress state and write a schema-valid structured checkpoint with evidence, failed approaches and the next exact action. Do not repeat completed work, manufacture a positive result, silently change theorem assumptions/scope, or promote author drafts to final acceptance. Stay quiet unless there is a meaningful theorem result, material correction, completion, failure or required user action. If the package is awaiting PI acceptance or complete and no input has changed, do not rewrite it or send routine reminders.
