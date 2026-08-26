# docs/07/scripts/percentile.py
"""Cálculo de percentis (p95/p99) de tempos de resposta via nearest-rank.

Demonstra por que a média esconde a cauda longa. Execute: python percentile.py
"""
from __future__ import annotations

import math


def percentile(tempos: list[float], q: int) -> float:
    """Percentil q (1-100) pelo método nearest-rank (índice = ceil(q% * N))."""
    s = sorted(tempos)
    if not s:
        return 0.0
    idx = math.ceil(q / 100 * len(s)) - 1
    idx = max(0, min(idx, len(s) - 1))
    return s[idx]


if __name__ == "__main__":
    tempos = [100, 120, 130, 140, 150, 160, 170, 180, 190, 1000]
    media = sum(tempos) / len(tempos)
    print(f"Média : {media:.0f} ms  (distorcida pelo outlier)")
    print(f"p95   : {percentile(tempos, 95):.0f} ms")
    print(f"p99   : {percentile(tempos, 99):.0f} ms")

