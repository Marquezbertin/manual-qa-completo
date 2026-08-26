# run_all.py
"""Executa todos os scripts standalone do manual de QA.

Uso:
    python run_all.py            # só os scripts sem dependências
    python run_all.py --suites   # também roda as suítes pytest (M05, M06)
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

STANDALONE = [
    "docs/03/scripts/estimate.py",
    "docs/04/scripts/triage.py",
    "docs/07/scripts/percentile.py",
    "docs/08/scripts/quality_gate.py",
    "docs/09/scripts/kpi.py",
]

SUITES = [
    "06/scripts",  # API (precisa requests + jsonschema)
    "05/scripts",  # UI  (precisa playwright + chromium)
]


def run(cmd: list[str]) -> bool:
    print(f"\n$ {' '.join(cmd)}")
    try:
        subprocess.run(cmd, cwd=ROOT, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def main() -> int:
    failures = 0
    for script in STANDALONE:
        if not run([sys.executable, script]):
            failures += 1

    if "--suites" in sys.argv:
        for suite in SUITES:
            if not run([sys.executable, "-m", "pytest", "-q", suite]):
                failures += 1

    print("\n" + ("TUDO OK" if failures == 0 else f"{failures} falha(s)"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

