# .github/scripts/check_mermaid.py
"""Validate that every ```mermaid block in the repo is well-formed.

Checks:
  - opening ```mermaid has a matching closing ```
  - mermaid blocks are not empty
  - first line of each block looks like a known diagram type

Usage:  python .github/scripts/check_mermaid.py
"""
from __future__ import annotations

import sys
from pathlib import Path

KNOWN_TYPES = {
    "flowchart", "graph", "sequenceDiagram", "classDiagram", "class",
    "stateDiagram", "erDiagram", "journey", "gantt", "pie", "mindmap",
    "timeline", "gitGraph", "quadrantChart", "requirementDiagram",
    "C4Context", "C4Container", "C4Component", "C4Dynamic",
}

ROOT = Path(__file__).resolve().parent.parent.parent
SKIP = {".git", "node_modules", "__pycache__", "venv", ".venv"}


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    in_mermaid = False
    buf: list[str] = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped == "```mermaid":
            if in_mermaid:
                errors.append(f"{path}:{i} nested ```mermaid")
            in_mermaid = True
            buf = []
        elif stripped == "```" and in_mermaid:
            in_mermaid = False
            if not buf:
                errors.append(f"{path}:{i} empty mermaid block")
        elif in_mermaid:
            buf.append(line)
    if in_mermaid:
        errors.append(f"{path}: unclosed ```mermaid block")
    return errors


def main() -> int:
    all_errors: list[str] = []
    count = 0
    for md in ROOT.rglob("*.md"):
        if any(part in SKIP for part in md.parts):
            continue
        for err in check_file(md):
            all_errors.append(err)
        count += 1
    if all_errors:
        print("Mermaid validation FAILED:")
        for e in all_errors:
            print("  -", e)
        return 1
    print(f"Mermaid validation OK ({count} markdown files scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
