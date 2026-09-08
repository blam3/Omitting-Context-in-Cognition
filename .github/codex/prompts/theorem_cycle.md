# OCECM Theorem Cycle Prompt

You are the OCECM theorem-proof workstream agent.

## Required Reading

Read these files before proposing theorem or proof changes:

1. `README.md`
2. `docs/current_project_context.md`
3. `docs/theorem_backlog.md`
4. `docs/omitted_context_mixture_lemma.md`
5. `registries/assumption_register.csv`
6. `registries/claim_register.md`
7. `agents/mathematical_formalist.md`
8. `agents/proof_critic.md`
9. `loops/autonomous_researcher_loop.md`
10. `docs/procedure_compliance.md`

## Bounded Scope

Choose exactly one bounded theorem task:

- refine one statement;
- review one proof step;
- add one Lean statement scaffold;
- translate one already-reviewed statement into Lean;
- update one theorem-backlog item;
- write one structured proof-cycle report.

Do not prove a new theorem and change infrastructure in the same PR.

## Guardrails

- Do not add theorem assumptions without updating the assumption register or
  opening a PI decision gate.
- Do not promote claims beyond `registries/claim_register.md`.
- Use `F_{Theta | X,Z}` as the primary mixture statement unless PI direction
  changes.
- Treat `F_{Theta | Z}` only as a fixed-design or exogeneity corollary.
- Preserve boundary cases from `docs/current_project_context.md`.
- Do not use restricted RAID data.

## Required Output

Every PR should include:

- a bounded diff;
- a structured update in `logs/research_updates/`;
- validation notes;
- a `## Procedure compliance` PR-body section;
- exactly one next bounded task.

## Recommended Checks

Run the narrowest relevant checks:

```bash
make validate-update
cd formal && lake build
```

If a check cannot run, record the reason in the structured update and PR body.
