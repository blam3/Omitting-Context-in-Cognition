# Autonomous Loop Researcher Architecture

## Design principle

Use a manager-led multi-agent system, not a decentralized swarm. The principal investigator agent orchestrates specialized agents, records decisions, and routes tasks through approval gates.

## Core state objects

Each loop iteration should read and update these project ledgers:

| Ledger | File | Purpose |
|---|---|---|
| Research spec | `docs/research_spec.md` | Stable project definition |
| Assumption registry | `docs/assumption_registry.md` | Approved assumptions only |
| Claim registry | `docs/claim_registry.md` | Conjectures, theorems, empirical claims, citation status |
| Proof log | `docs/proof_review_log.md` | Proof attempts, gaps, counterexamples |
| Simulation registry | `simulations/run_registry.csv` | Simulation runs, seeds, status |
| Approval log | `docs/approval_log.md` | Human approvals and rejected proposals |
| Error reports | `logs/error_reports/` | Failed loops after repeated repair attempts |

## Recommended orchestration pattern

```text
User goal
  ↓
Principal Investigator Agent
  ↓
Task packet
  ↓
Specialized agent
  ↓
Structured output
  ↓
Verifier or critic agent
  ↓
Approval gate if necessary
  ↓
Git branch / issue / PR / local artifact
```

## Loop stopping criteria

A loop must stop when one of the following occurs:

1. The task is complete and verified.
2. The task requires human approval.
3. The loop has failed 10 repair attempts.
4. A tool execution would exceed safety or compute limits.
5. The agent proposes a new assumption, estimand, interpretive claim, or literature claim.
6. The agent attempts deletion or an expensive cluster job.

## Minimum viable autonomous loop

Start with the following:

1. PI agent creates a task packet.
2. Simulation Architect proposes one simulation design cell.
3. Code Engineer implements the DGM and smoke simulation.
4. Reproducibility Auditor runs tests.
5. Reviewer 2 Agent critiques whether the simulation actually tests the claim.
6. PI agent writes a GitHub issue or PR summary.

Only after this works should you add the proof loop and literature loop.
