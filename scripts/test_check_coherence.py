#!/usr/bin/env python3
"""Self-test for scripts/check_coherence.py.

A checker that never fails is worthless. This builds minimal repository
fixtures that each violate exactly one rule and asserts the checker rejects
them, then asserts it accepts a clean fixture.
"""
import pathlib
import subprocess
import sys
import tempfile

CHECKER = pathlib.Path(__file__).resolve().parent / "check_coherence.py"

REGISTER = (
    "assumption_id,track,short_name,assumption_text,status,decision_status,"
    "review_owner,source_or_rationale,proof_or_analysis_dependency,last_updated\n"
    "A-001,theorem,ok,text,approved,approved,PI,r,d,2026-09-08\n"
    "A-002,theorem,gated,text,proposed,decision_needed,PI,r,d,2026-09-08\n"
    "A-006,theorem,rejected one,text,rejected,PI_rejected,PI,r,d,2026-09-08\n"
)
CLAIMS = "| Claim ID | Claim |\n|---|---|\n| C-002 | x |\n"

CLEAN = """<!-- theorem-meta
id: T-001
title: base
claim: C-002
status: proof-critic-review
assumptions: A-001
depends_on:
-->

Body uses A-001 only.
"""


def build(tmp: pathlib.Path, files: dict):
    (tmp / "registries").mkdir(parents=True, exist_ok=True)
    (tmp / "docs" / "theorems").mkdir(parents=True, exist_ok=True)
    (tmp / "registries" / "assumption_register.csv").write_text(REGISTER)
    (tmp / "registries" / "claim_register.md").write_text(CLAIMS)
    for rel, text in files.items():
        (tmp / rel).write_text(text)


def run(tmp: pathlib.Path):
    return subprocess.run(
        [sys.executable, str(CHECKER), "--repo", str(tmp)],
        capture_output=True, text=True,
    )


CASES = [
    ("clean fixture passes", {"docs/theorems/a.md": CLEAN}, 0, ""),
    (
        "assumption leak is caught",
        {"docs/theorems/a.md": CLEAN.replace("Body uses A-001 only.", "Body silently uses A-002.")},
        1, "assumption leak",
    ),
    (
        "rejected assumption is caught",
        {"docs/theorems/a.md": CLEAN.replace("assumptions: A-001", "assumptions: A-001, A-006")},
        1, "REJECTED",
    ),
    (
        "unknown claim is caught",
        {"docs/theorems/a.md": CLEAN.replace("claim: C-002", "claim: C-999")},
        1, "absent from the claim register",
    ),
    (
        "missing dependency is caught",
        {"docs/theorems/a.md": CLEAN.replace("depends_on:\n", "depends_on: T-404\n")},
        1, "has no theorem-meta block",
    ),
    (
        "dependency cycle is caught",
        {
            "docs/theorems/a.md": CLEAN.replace("depends_on:\n", "depends_on: T-002\n"),
            "docs/theorems/b.md": CLEAN.replace("id: T-001", "id: T-002")
                                       .replace("depends_on:\n", "depends_on: T-001\n"),
        },
        1, "dependency cycle",
    ),
    (
        "duplicate theorem id is caught",
        {"docs/theorems/a.md": CLEAN, "docs/theorems/b.md": CLEAN},
        1, "declared in more than one file",
    ),
    (
        "accepted-on-open-gate is caught",
        {"docs/theorems/a.md": CLEAN.replace("status: proof-critic-review", "status: accepted")
                                    .replace("assumptions: A-001", "assumptions: A-001, A-002")
                                    .replace("A-001 only.", "A-001 and A-002.")},
        1, "open gates",
    ),
    (
        "F_{Theta|Z} outside T-002 is caught",
        {"docs/theorems/a.md": CLEAN + "\nThe law $F_{\\Theta \\mid Z}(\\theta)$ is primary.\n"},
        1, "F_Theta_given_Z",
    ),
    (
        "eta as a model index is caught",
        {"docs/theorems/a.md": CLEAN + "\nTake $\\eta \\in M_S$ minimising the risk.\n"},
        1, "eta_model_index",
    ),
    (
        "bare Delta-ell is caught",
        {"docs/theorems/a.md": CLEAN + "\nSelection favours it when $2n\\Delta\\ell > 2\\Delta k$.\n"},
        1, "bare_delta_ell",
    ),
    (
        "coherence-allow marker suppresses a rule",
        {"docs/theorems/a.md": CLEAN + "\n<!-- coherence-allow: eta_model_index -->\n"
                                       "\nDiscussing $\\eta \\in M_S$ as retired notation.\n"},
        0, "",
    ),
]


def main() -> int:
    failures = []
    for name, files, want_code, want_text in CASES:
        with tempfile.TemporaryDirectory() as td:
            tmp = pathlib.Path(td)
            build(tmp, files)
            res = run(tmp)
            out = res.stdout + res.stderr
            if res.returncode != want_code:
                failures.append(f"{name}: expected exit {want_code}, got {res.returncode}\n{out}")
            elif want_text and want_text not in out:
                failures.append(f"{name}: expected {want_text!r} in output\n{out}")
            else:
                print(f"  ok  {name}")

    if failures:
        print("\nSELF-TEST FAILURES:\n" + "\n\n".join(failures), file=sys.stderr)
        return 1
    print(f"\nOK: {len(CASES)} coherence-checker self-tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
