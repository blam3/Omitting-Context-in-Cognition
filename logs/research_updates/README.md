# Structured Research Updates

Every autonomous researcher cycle should write a machine-readable update file here.

## File naming

Use:

```text
YYYY-MM-DDTHHMMSSZ_short-title.json
```

Example:

```text
2026-07-04T043000Z_update-loop-context.json
```

## Required schema

Each update should conform to:

```text
schemas/research_update.schema.json
```

The minimal required fields are:

- `cycle_title`
- `track`
- `completed`
- `why_it_matters`
- `checks_run`
- `decision_needed`
- `next_bounded_task`

## Validation

Run:

```bash
make validate-update
```

By default this validates `logs/research_updates/example_update.json` with a lightweight no-dependency validator.

## Confidentiality rule

Research updates must not include restricted participant-level RAID values or any private credentials, file paths, or API keys.
