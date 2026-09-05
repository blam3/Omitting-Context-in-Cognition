#!/usr/bin/env python3
"""Build docs/project_map.html, the interactive map of this repository.

Curated content (what each file is, why you would read it, status, tour order,
progress tables) lives in docs/project_map_data.json and is maintained by hand.
Mechanical facts (line counts, last-commit dates, commit counts, totals) are
re-derived from disk and git on every build, so the page cannot silently drift
away from the repository.

Usage:
    python3 scripts/build_project_map.py            # or: make project-map
    python3 scripts/build_project_map.py --fragment PATH

The default output is a standalone HTML document. --fragment additionally writes
the same page without the <!doctype>/<html>/<head>/<body> wrapper, for hosts that
supply their own document shell.

Drift warnings are printed but do not fail the build: a repository file that is
missing from the curated data is reported here and also rendered on the page in
an "Unmapped" lane, so the picture is never quietly incomplete.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "docs" / "project_map_data.json"
TEMPLATE = REPO / "scripts" / "project_map_template.html"
OUTPUT = REPO / "docs" / "project_map.html"
PLACEHOLDER = "__PROJECT_MAP_DATA__"

DOCUMENT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{body}
</html>
"""


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True, check=True
    ).stdout


def tracked_files() -> list[str]:
    return [line for line in git("ls-files").splitlines() if line]


def line_count(path: str) -> int:
    full = REPO / path
    if not full.is_file():
        return 0
    try:
        with full.open("rb") as handle:
            return sum(1 for _ in handle)
    except OSError:
        return 0


def git_history() -> tuple[dict[str, dict], int, str, str]:
    """One log pass: last-touched date and commit count for every path."""
    log = git("log", "--date=short", "--name-only", "--pretty=format:@@%H|%ad")
    stats: dict[str, dict] = defaultdict(lambda: {"last": "", "commits": 0})
    commits = 0
    latest = ""
    date = ""
    first = ""
    for line in log.splitlines():
        if line.startswith("@@"):
            _, date = line[2:].split("|", 1)
            commits += 1
            latest = latest or date
            first = date
        elif line.strip():
            entry = stats[line.strip()]
            entry["commits"] += 1
            if not entry["last"]:
                entry["last"] = date
    return dict(stats), commits, latest, first


def curated_paths(nodes: list[dict]) -> dict[str, str]:
    """Map every curated file path to the id of the node that presents it."""
    owned: dict[str, str] = {}
    for node in nodes:
        if node.get("path"):
            owned[node["path"]] = node["id"]
        for member in node.get("members", []):
            owned[member["path"]] = node["id"]
    return owned


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fragment",
        metavar="PATH",
        help="also write the page without a document wrapper, for embedding hosts",
    )
    args = parser.parse_args()

    data = json.loads(DATA.read_text())
    nodes = data["nodes"]
    owned = curated_paths(nodes)
    files = tracked_files()
    history, total_commits, latest_commit, first_commit = git_history()

    warnings: list[str] = []

    missing = sorted(path for path in owned if path not in set(files))
    for path in missing:
        warnings.append(f"curated node references a path that is not tracked: {path}")

    unmapped = sorted(path for path in files if path not in owned)
    if unmapped:
        for path in unmapped:
            warnings.append(f"tracked file is missing from the map: {path}")
        data["lanes"].append(
            {
                "id": "unmapped",
                "title": "Unmapped",
                "blurb": "Tracked files with no curated entry yet. Add them to docs/project_map_data.json.",
            }
        )
        nodes.append(
            {
                "id": "unmapped_group",
                "lane": "unmapped",
                "label": f"Not yet described ({len(unmapped)})",
                "kind": "group",
                "status": "stub",
                "what": "These files are tracked by git but have no entry in the curated map data.",
                "why": "Describe them in docs/project_map_data.json and rebuild.",
                "members": [
                    {"path": path, "label": path.rsplit("/", 1)[-1], "what": ""}
                    for path in unmapped
                ],
            }
        )

    # Mechanical facts, attached per path.
    stats: dict[str, dict] = {}
    for path in files:
        entry = history.get(path, {"last": "", "commits": 0})
        stats[path] = {
            "lines": line_count(path),
            "last": entry["last"],
            "commits": entry["commits"],
        }

    for node in nodes:
        paths = [node["path"]] if node.get("path") else []
        paths += [member["path"] for member in node.get("members", [])]
        node["file_count"] = len(paths)
        node["lines"] = sum(stats.get(p, {}).get("lines", 0) for p in paths)
        dates = [stats.get(p, {}).get("last", "") for p in paths]
        node["last"] = max([d for d in dates if d], default="")

    data["files"] = stats
    data["repo_stats"] = {
        "tracked": len(files),
        "commits": total_commits,
        "latest_commit": latest_commit,
        "first_commit": first_commit,
        "lines": sum(entry["lines"] for entry in stats.values()),
        "directories": len({p.rsplit("/", 1)[0] for p in files if "/" in p}),
        "generated_from": git("rev-parse", "--short", "HEAD").strip(),
    }

    template = TEMPLATE.read_text()
    if PLACEHOLDER not in template:
        print(f"error: {TEMPLATE} has no {PLACEHOLDER} placeholder", file=sys.stderr)
        return 1
    payload = json.dumps(data, separators=(",", ":")).replace("</", "<\\/")
    fragment = template.replace(PLACEHOLDER, payload)
    OUTPUT.write_text(DOCUMENT.format(body=fragment))
    if args.fragment:
        Path(args.fragment).write_text(fragment)

    for warning in warnings:
        print(f"drift: {warning}", file=sys.stderr)
    print(
        f"wrote {OUTPUT.relative_to(REPO)} "
        f"({len(nodes)} nodes, {len(files)} tracked files, {len(warnings)} drift warnings)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
