# docs/09/scripts/kpi.py
"""Cálculo de KPIs de qualidade de forma reproduzível.

Execute:  python kpi.py
"""
from __future__ import annotations


def defect_density(defeitos: int, kloc: float) -> float:
    return defeitos / kloc


def defect_leakage(em_prod: int, total: int) -> float:
    return em_prod / total * 100


def coverage(testados: int, total: int) -> float:
    return testados / total * 100


def mttr(horas_correcao: list[float]) -> float:
    return sum(horas_correcao) / len(horas_correcao)


if __name__ == "__main__":
    print(f"Defect Density : {defect_density(12, 2):.1f} / KLOC")
    print(f"Defect Leakage: {defect_leakage(2, 20):.0f}%")
    print(f"Cobertura     : {coverage(48, 50):.0f}%")
    print(f"MTTR          : {mttr([2, 4, 6, 6]):.1f} h")

