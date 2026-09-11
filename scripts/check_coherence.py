#!/usr/bin/env python3
"""Cross-result coherence checker for the OCECM theorem package.

Single-pass drafting of an interdependent theorem route drifts in two ways that
prose review reliably misses:

  1. NOTATION DRIFT   - the same symbol silently changes meaning between files
                        (eta as kernel parameter vs. model index; per-observation
                        vs. total log score; the primary F_{Theta|X,Z} mixing law
                        vs. the corollary-only F_{Theta|Z} display).
  2. ASSUMPTION LEAK  - a downstream result consumes an assumption that neither
                        it nor any result it depends on ever established.

This script fails CI on both. It is stdlib-only on purpose: it must run before
any heavyweight toolchain is available.

Usage:  python3 scripts/check_coherence.py [--repo ROOT]
"""

from __future__ import annotations

import argparse
import csv
import pathlib
import re
import sys

META_RE = re.compile(r"<!--\s*theorem-meta\s*\n(.*?)-->", re.DOTALL)
FENCE_RE = re.compile(r"^[ \t]*(```|~~~).*?^[ \t]*\1[ \t]*$", re.DOTALL | re.MULTILINE)
ALLOW_RE = re.compile(r"<!--\s*coherence-allow:\s*([^>]*?)-->")

VALID_STATUS = {
    "backlog", "statement-draft", "proof-draft", "proof-critic-review",
    "accepted", "decision-gated", "corollary-only", "deferred",
}

# ---------------------------------------------------------------- notation ---
# Each rule: (allow-key, compiled pattern, human-readable reason).
NOTATION_RULES = [
    (
        "F_Theta_given_Z",
        re.compile(r"F_\{?\\?[Tt]heta\s*\\?[|]?\s*(\\mid|\|)\s*Z\s*\}?"),
        "F_{Theta|Z} is corollary-only (T-002). A-006 is rejected; the primary "
        "mixing law is F_{Theta|X,Z}. See docs/notation_registry.md section 3.",
    ),
    (
        "eta_model_index",
        re.compile(r"\\eta\s*\\in\s*M_|\\psi\s*\\in\s*M_|\\inf_\{\\?(eta|psi)"),
        "eta is the choice-kernel parameter and psi is retired; model classes are "
        "indexed by beta_S and beta_K. See docs/notation_registry.md section 4.",
    ),
    (
        "bare_delta_ell",
        re.compile(r"\\Delta\\ell(?!\^\{\\?\*?\}|\^\*)"),
        "write \\Delta\\ell^{*} for the population per-observation gap; the "
        "realised sample quantity is D_n. See docs/notation_registry.md section 5.",
    ),
    (
        "k_as_complexity",
        re.compile(r"effective (?:number of )?(?:parameters|complexity)\s*[=:]\s*k"),
        "nominal parameter counts are not complexity under singularity (D-004); "
        "report p_loo / p_waic.",
    ),
]

ID_REFS = {
    "A": re.compile(r"\bA-\d{3}\b"),
    "C": re.compile(r"\bC-\d{3}\b"),
    "T": re.compile(r"\bT-\d{3}\b"),
}


class Problem(list):
    def add(self, path, msg):
        self.append(f"{path}: {msg}")


def strip_fences(text: str) -> str:
    """Blank out fenced code blocks, preserving line numbering.

    Documentation that *shows* a theorem-meta block or a retired symbol must not
    be read as declaring or using one.
    """
    return FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def parse_meta(block: str) -> dict:
    out = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if key in {"assumptions", "depends_on", "approval"}:
            out[key] = [v.strip() for v in val.split(",") if v.strip()]
        else:
            out[key] = val
    return out


def load_registries(root: pathlib.Path, problems: Problem):
    assumptions = {}
    apath = root / "registries" / "assumption_register.csv"
    if apath.exists():
        with apath.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("assumption_id"):
                    assumptions[row["assumption_id"].strip()] = row
    else:
        problems.add(str(apath), "missing assumption register")

    claims = set()
    cpath = root / "registries" / "claim_register.md"
    if cpath.exists():
        claims = set(re.findall(r"\|\s*(C-\d{3})\s*\|", cpath.read_text(encoding="utf-8")))
    else:
        problems.add(str(cpath), "missing claim register")
    return assumptions, claims


def collect_theorems(root: pathlib.Path, problems: Problem):
    theorems = {}
    for path in sorted(root.glob("docs/**/*.md")):
        raw = path.read_text(encoding="utf-8")
        text = strip_fences(raw)
        for block in META_RE.findall(text):
            meta = parse_meta(block)
            tid = meta.get("id")
            if not tid:
                problems.add(str(path), "theorem-meta block without an id")
                continue
            if tid in theorems:
                problems.add(str(path), f"{tid} declared in more than one file "
                                        f"(also {theorems[tid]['path']})")
                continue
            meta["path"] = path.relative_to(root).as_posix()
            meta["body"] = text
            theorems[tid] = meta
    return theorems


def effective_assumptions(tid, theorems, seen=None):
    """Own assumptions plus everything inherited transitively via depends_on."""
    seen = seen or set()
    if tid in seen or tid not in theorems:
        return set()
    seen.add(tid)
    meta = theorems[tid]
    acc = set(meta.get("assumptions", []))
    for dep in meta.get("depends_on", []):
        acc |= effective_assumptions(dep, theorems, seen)
    return acc


def find_cycle(theorems):
    colour = {}

    def visit(node, stack):
        if colour.get(node) == 1:
            return stack[stack.index(node):] + [node]
        if colour.get(node) == 2 or node not in theorems:
            return None
        colour[node] = 1
        for dep in theorems[node].get("depends_on", []):
            cyc = visit(dep, stack + [node])
            if cyc:
                return cyc
        colour[node] = 2
        return None

    for node in theorems:
        cyc = visit(node, [])
        if cyc:
            return cyc
    return None


def check_notation(root: pathlib.Path, problems: Problem):
    targets = sorted(root.glob("docs/**/*.md")) + sorted(root.glob("manuscript/*.tex"))
    for path in targets:
        text = strip_fences(path.read_text(encoding="utf-8"))
        allowed = set()
        for grp in ALLOW_RE.findall(text):
            allowed |= {a.strip() for a in grp.split(",") if a.strip()}
        for line_no, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith(("<!--", "|---", "- `")):
                continue
            for key, pattern, reason in NOTATION_RULES:
                if key in allowed:
                    continue
                if pattern.search(line):
                    problems.add(
                        f"{path.relative_to(root).as_posix()}:{line_no}",
                        f"notation drift [{key}]: {reason}",
                    )


def check_lean_sync(root: pathlib.Path, theorems, problems: Problem):
    camel = {
        "backlog": "backlog", "statement-draft": "statementDraft",
        "proof-draft": "proofDraft", "proof-critic-review": "proofCriticReview",
        "accepted": "accepted", "decision-gated": "decisionGated",
        "corollary-only": "corollaryOnly", "deferred": "deferred",
    }
    for path in sorted(root.glob("formal/OCECM/*.lean")):
        text = path.read_text(encoding="utf-8")
        for label, status in re.findall(
            r'label\s*:=\s*"(T-\d{3})[^"]*"\s*\n\s*claimId[^\n]*\n\s*assumptionIds[^\n]*\n\s*'
            r"status\s*:=\s*TheoremStatus\.(\w+)", text
        ):
            if label not in theorems:
                problems.add(path.name, f"Lean card {label} has no theorem-meta in docs/")
                continue
            want = camel.get(theorems[label].get("status", ""), "?")
            if status != want:
                problems.add(
                    path.name,
                    f"Lean card {label} status '{status}' disagrees with docs "
                    f"status '{theorems[label].get('status')}' (expected '{want}')",
                )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    root = pathlib.Path(ap.parse_args().repo).resolve()

    problems = Problem()
    assumptions, claims = load_registries(root, problems)
    theorems = collect_theorems(root, problems)

    if not theorems:
        problems.add("docs/", "no theorem-meta blocks found")

    for tid, meta in sorted(theorems.items()):
        where = meta["path"]

        status = meta.get("status", "")
        if status not in VALID_STATUS:
            problems.add(where, f"{tid} has invalid status '{status}'")

        claim = meta.get("claim", "")
        if claim and claim not in claims:
            problems.add(where, f"{tid} cites {claim}, absent from the claim register")

        for aid in meta.get("assumptions", []):
            row = assumptions.get(aid)
            if row is None:
                problems.add(where, f"{tid} cites {aid}, absent from the assumption register")
            elif row.get("status", "").strip() == "rejected":
                problems.add(where, f"{tid} cites {aid}, which is REJECTED in the register")

        for dep in meta.get("depends_on", []):
            if dep not in theorems:
                problems.add(where, f"{tid} depends on {dep}, which has no theorem-meta block")

        # Assumption leak: any A-id named in the body must be established by this
        # result or inherited from one it depends on.
        eff = effective_assumptions(tid, theorems)
        body = re.sub(META_RE, "", meta["body"])
        for aid in sorted(set(ID_REFS["A"].findall(body))):
            if aid in eff:
                continue
            if aid in assumptions and assumptions[aid].get("status", "").strip() == "rejected":
                continue  # discussing a rejected assumption is allowed
            problems.add(
                where,
                f"assumption leak: {tid} uses {aid} in its body but neither declares "
                f"it nor inherits it via depends_on {meta.get('depends_on', [])}",
            )

        # A statement may not be manuscript-ready while it rests on an open gate.
        if status == "accepted":
            open_gates = [a for a in eff
                          if assumptions.get(a, {}).get("decision_status", "").strip()
                          == "decision_needed"]
            if open_gates:
                problems.add(where, f"{tid} is 'accepted' but depends on open gates {open_gates}")

    cyc = find_cycle(theorems)
    if cyc:
        problems.add("docs/theorems", f"dependency cycle: {' -> '.join(cyc)}")

    check_notation(root, problems)
    check_lean_sync(root, theorems, problems)

    if problems:
        print(f"FAIL: {len(problems)} coherence problem(s)\n", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print(f"OK: {len(theorems)} theorem(s) coherent "
          f"({', '.join(sorted(theorems))}); notation and Lean cards in sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
