# docs/04/scripts/triage.py
"""Helper de triagem: mapeia (Severidade, Prioridade) -> SLA de resolução (horas).

Execute:  python triage.py
"""
from __future__ import annotations

SEVERITY_SLA = {
    ("Crítico", "Urgente"): 4,
    ("Crítico", "Alta"): 8,
    ("Alto", "Urgente"): 8,
    ("Alto", "Alta"): 24,
    ("Médio", "Alta"): 48,
    ("Médio", "Média"): 72,
    ("Baixo", "Média"): 120,
    ("Baixo", "Baixa"): 240,
}


def sla_horas(severidade: str, prioridade: str) -> int:
    """Retorna o SLA em horas; 999 se combinação não mapeada."""
    return SEVERITY_SLA.get((severidade, prioridade), 999)


if __name__ == "__main__":
    casos = [
        ("Crítico", "Urgente"),
        ("Alto", "Alta"),
        ("Médio", "Média"),
        ("Baixo", "Baixa"),
    ]
    print("SLA de resolução (horas):")
    for sev, pri in casos:
        print(f"  {sev:8s} / {pri:8s}: {sla_horas(sev, pri)}h")

