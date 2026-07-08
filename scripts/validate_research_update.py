#!/usr/bin/env python3
"""Lightweight validator for autonomous researcher update JSON files.

This intentionally avoids third-party dependencies so CI can run in a minimal
Python environment. It checks the project-specific required shape from
schemas/research_update.schema.json, but it is not a full JSON Schema engine.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

VALID_TRACKS = {
    "theorem",
    "simulation",
    "empirical",
    "manuscript",
    "governance",
    "infrastructure",
}

VALID_CHECK_STATUSES = {"pass", "fail", "not_run", "not_applicable"}

REQUIRED_TOP_LEVEL = {
    "cycle_title",
    "track",
    "completed",
    "why_it_matters",
    "checks_run",
    "decision_needed",
    "next_bounded_task",
}

PROCEDURE_COMPLIANCE_KEYS = {
    "operating_context_read",
    "bounded_task",
    "self_check_completed",
    "registry_reviewed",
    "structured_update_written",
    "validation_documented",
    "restricted_data_checked",
    "pi_decision_gate_checked",
    "claim_status_checked",
    "next_task_named",
}


def fail(message: str) -> None:
    print(f"research update validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_nonempty_string(obj: dict, key: str) -> None:
    if not isinstance(obj.get(key), str) or not obj[key].strip():
        fail(f"{key!r} must be a nonempty string")


def require_string_list(obj: dict, key: str) -> None:
    value = obj.get(key)
    if not isinstance(value, list) or len(value) == 0:
        fail(f"{key!r} must be a nonempty list")
    if not all(isinstance(item, str) and item.strip() for item in value):
        fail(f"all entries in {key!r} must be nonempty strings")


def validate_procedure_compliance(update: dict) -> None:
    """Validate optional procedure-compliance metadata when present.

    The field is optional for backward compatibility with older cycle logs, but
    autonomous PRs created after the PR-compliance template should include it.
    """

    if "procedure_compliance" not in update:
        return

    compliance = update["procedure_compliance"]
    if not isinstance(compliance, dict):
        fail("procedure_compliance must be an object")

    missing = PROCEDURE_COMPLIANCE_KEYS - set(compliance)
    if missing:
        fail(
            "procedure_compliance missing required fields: "
            + ", ".join(sorted(missing))
        )

    for key in sorted(PROCEDURE_COMPLIANCE_KEYS):
        if not isinstance(compliance.get(key), bool):
            fail(f"procedure_compliance.{key} must be true or false")

    if "notes" in compliance and not isinstance(compliance["notes"], str):
        fail("procedure_compliance.notes must be a string when present")


def validate_update(update: dict) -> None:
    missing = REQUIRED_TOP_LEVEL - set(update)
    if missing:
        fail(f"missing required fields: {', '.join(sorted(missing))}")

    require_nonempty_string(update, "cycle_title")
    require_nonempty_string(update, "next_bounded_task")

    if update.get("track") not in VALID_TRACKS:
        fail(f"track must be one of {sorted(VALID_TRACKS)}")

    require_string_list(update, "completed")
    require_string_list(update, "why_it_matters")

    checks = update.get("checks_run")
    if not isinstance(checks, list):
        fail("checks_run must be a list")
    for i, check in enumerate(checks):
        if not isinstance(check, dict):
            fail(f"checks_run[{i}] must be an object")
        if not isinstance(check.get("name"), str) or not check["name"].strip():
            fail(f"checks_run[{i}].name must be a nonempty string")
        if check.get("status") not in VALID_CHECK_STATUSES:
            fail(f"checks_run[{i}].status must be one of {sorted(VALID_CHECK_STATUSES)}")

    decision = update.get("decision_needed")
    if not isinstance(decision, dict):
        fail("decision_needed must be an object")
    if not isinstance(decision.get("needed"), bool):
        fail("decision_needed.needed must be true or false")
    if decision["needed"] and not str(decision.get("question", "")).strip():
        fail("decision_needed.question must be nonempty when a decision is needed")

    validate_procedure_compliance(update)


def main(argv: list[str]) -> int:
    if len(argv) not in {2, 3}:
        print(
            "usage: validate_research_update.py <update.json> [schema.json]",
            file=sys.stderr,
        )
        return 2

    update_path = Path(argv[1])
    with update_path.open("r", encoding="utf-8") as f:
        update = json.load(f)

    validate_update(update)
    print(f"validated research update: {update_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
