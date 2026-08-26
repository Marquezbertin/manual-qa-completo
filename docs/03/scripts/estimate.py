# docs/03/scripts/estimate.py
"""Estimativa de esforço de teste (PERT de 3 pontos) e cobertura de requisitos.

Execute:  python estimate.py
"""
from __future__ import annotations


def pert(o: float, r: float, p: float) -> float:
    """Estimativa ponderada: (Ot + 4*Rl + Ps) / 6."""
    return (o + 4 * r + p) / 6


def coverage(tested: int, total: int) -> float:
    """Cobertura de requisitos em porcentagem."""
    return tested / total * 100


if __name__ == "__main__":
    features = {
        "Login": (1, 2, 4),
        "Checkout": (3, 5, 10),
        "Relatórios": (2, 4, 9),
    }
    print("Estimativa por feature (dias PERT):")
    for name, (o, r, p) in features.items():
        print(f"  {name:12s}: {pert(o, r, p):.2f}")

    total = sum(pert(*v) for v in features.values())
    print(f"Total PERT: {total:.2f} dias")

    cov = coverage(40, 50)
    print(f"Cobertura de requisitos: {cov:.0f}%")

