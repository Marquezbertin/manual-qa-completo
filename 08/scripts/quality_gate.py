# 08/scripts/quality_gate.py
"""Quality gate reproduzível: decide PASS/FAIL de lint, cobertura e segurança.

Execute:  python quality_gate.py
"""
from __future__ import annotations


def evaluate(
    lint_errors: int,
    coverage_pct: float,
    high_vulns: int,
    threshold: float = 80.0,
) -> dict:
    results = {
        "lint": "PASS" if lint_errors == 0 else "FAIL",
        "coverage": "PASS" if coverage_pct >= threshold else "FAIL",
        "security": "PASS" if high_vulns == 0 else "FAIL",
    }
    results["overall"] = "PASS" if all(v == "PASS" for v in results.values()) else "FAIL"
    return results


if __name__ == "__main__":
    cenarios = [
        ("Release boa", 0, 92.0, 0),
        ("Cobertura baixa", 0, 71.0, 1),
        ("Lint sujo", 3, 88.0, 0),
    ]
    for nome, le, cov, hv in cenarios:
        print(nome, "->", evaluate(le, cov, hv))
