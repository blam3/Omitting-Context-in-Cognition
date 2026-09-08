# Contributing

This repository is written to by three different workers: **Brendan on a local
machine**, **Claude Code** (cloud sessions), and **ChatGPT Codex**. Each works
from its own checkout, and only one of them is durable.

This document covers how those checkouts stay synchronized. It does not
restate the scientific governance rules — for those, see
[`loops/autonomous_researcher_loop.md`](loops/autonomous_researcher_loop.md),
[`docs/procedure_compliance.md`](docs/procedure_compliance.md), and
[`registries/README.md`](registries/README.md).

## The one rule

**GitHub is the only source of truth.** No checkout is authoritative, and no
work exists until it is pushed.

This matters because the three checkouts are not equally durable:

| Checkout | Durability | Visible to others? |
| --- | --- | --- |
| Local machine | Persistent | No — invisible to Claude and Codex until pushed |
| Claude Code session | **Ephemeral** — the container is wiped when the session ends | No |
| Codex session | **Ephemeral** | No |

Unpushed work in an agent session is lost, not merely delayed. Unpushed work
on the local machine is invisible, which is how divergence starts.

## Branch naming

`main` is the trunk. Nothing is committed directly to it; everything lands
through a pull request.

| Prefix | Used by |
| --- | --- |
| `claude/<topic>` | Claude Code sessions |
| `codex/<topic>` | Codex sessions |
| `<initials>-patch-N` or `<topic>` | Local work |

Delete merged branches. A branch that is `0 ahead` of `main` contains nothing
and is only a source of confusion.

## Local workflow

Start every local session by taking whatever the agents landed while you were
away:

```bash
git checkout main
git pull origin main
```

End every local session by pushing, even if the work is unfinished:

```bash
git status --short          # confirm nothing unexpected is staged
git add -A
git commit -m "..."
git push -u origin <branch-name>
```

An unfinished commit on a branch is recoverable. An uncommitted working tree
is not visible to anyone else, and blocks the next agent session from starting
on current code.

## Agent workflow

Before starting a Claude or Codex session, **push your local work first.**
Agent sessions clone fresh from GitHub, so anything sitting uncommitted on
your machine is invisible to them. Starting an agent on a stale `main`
produces conflicts that were entirely avoidable.

Agents should:

1. Branch from the latest `origin/main`.
2. Keep each PR to one bounded, reviewable task.
3. Complete the procedure-compliance section of
   [`.github/pull_request_template.md`](.github/pull_request_template.md).
4. Push before the session ends.

## Checking whether you are in sync

From any checkout:

```bash
git fetch origin
git rev-list --left-right --count origin/main...HEAD
```

The output is two numbers, `behind` and `ahead`:

| Output | Meaning | Action |
| --- | --- | --- |
| `0  0` | In sync | Nothing to do |
| `N  0` | Behind only | `git pull origin main` |
| `0  N` | Ahead only | `git push` |
| `N  M` | Diverged | Push your branch, open a PR, merge deliberately |

Only the last case needs care. Do not resolve divergence with a force-push —
it destroys whichever side is not yours.

## What never gets committed

[`.gitignore`](.gitignore) enforces most of this, but the boundaries are
worth stating directly, because a sync mistake is the likeliest way to breach
them:

- **Restricted RAID data.** `data_raw_secure/`, `data_processed_secure/`,
  `results_secure/`, and `scratch_secure/` stay local. Participant-level
  outputs never leave the machine that is licensed to hold them.
- **Secrets.** `.env` is ignored; [`.env.example`](.env.example) is the
  committed template. Never commit a filled-in copy.
- **Build and run artifacts.** `results/`, `cache/`, rendered PDFs, and
  serialized objects (`*.rds`, `*.parquet`) are regenerated, not tracked.

If you are unsure whether a file is safe to push, check `git status` before
committing rather than after.
