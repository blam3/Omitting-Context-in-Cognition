# PR Procedure Compliance Audit Trail

## Purpose

Every autonomous-researcher pull request must include a `## Procedure compliance` section in the PR body. This turns the loop's operating procedure into a visible audit trail so reviewers can quickly detect skipped orientation, missing registry updates, hidden decision gates, or confidentiality risks.

The section complements, but does not replace, the structured JSON cycle report in `logs/research_updates/`.

## Required section title

Use this exact heading:

```markdown
## Procedure compliance
```

The repository includes a PR template at `.github/pull_request_template.md`. Autonomous agents should use that template unless a human maintainer intentionally overrides it.

## Required audit items

At minimum, the PR body must state whether the agent completed each item below:

1. Read the required operating context.
2. Scoped the work to one bounded, reviewable task.
3. Ran the self-check for assumptions, estimands, false-complex model choice, literature claims, causal claims, restricted data, expensive compute, and claim promotion.
4. Updated relevant registries or explicitly stated that no registry updates were needed.
5. Created or updated a structured cycle report in `logs/research_updates/`, or explained why the PR is exempt.
6. Ran applicable validation checks or documented why they could not be run.
7. Confirmed that no confidential RAID data, participant-level restricted outputs, secrets, or local-only files were committed.
8. Identified whether PI direction is needed, and asked exactly one concrete question if it is.
9. Kept scientific claims within the evidence status recorded in `registries/claim_register.md`.
10. Named the next bounded task.

## How to handle exceptions

A checkbox can remain unchecked only when the item is genuinely not applicable or impossible in the current environment. The reason must be recorded under `### Procedure compliance notes`.

Examples:

- R checks not run because R is not installed in the execution environment.
- No registry update needed because the PR only changes CI configuration.
- No structured cycle report needed because a human-only administrative PR is explicitly outside the autonomous-researcher loop.

Do not delete the checklist item. Leaving the item visible is what makes the audit trail reviewable.

## Enforcement

The workflow `.github/workflows/pr-procedure-compliance.yml` checks PR bodies for the required `## Procedure compliance` heading and core audit items. The workflow does not prove that the content is true; it verifies that the PR exposes the audit trail for human review.

## Reviewer guidance

When reviewing an autonomous-researcher PR, check the procedure-compliance section before the substantive diff:

- If the PR changes assumptions, claims, or model interpretation, confirm the relevant registry changed or the PI decision gate is explicit.
- If the PR touches empirical work, confirm no restricted RAID data or participant-level restricted outputs are included.
- If checks were skipped, verify that the reason is specific and plausible.
- If the PR asks for PI direction, ensure it asks one concrete question with actionable options.

## Non-goals

The compliance section is not a substitute for scientific review. A PR can pass the compliance workflow and still be scientifically wrong. The goal is to make procedural omissions visible early.