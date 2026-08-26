# docs/11/scripts/secret_scan.py
"""Detecta segredos óbvios no código (chaves AWS, chaves privadas, senhas).

Exemplo de "secret scanning" em SAST leve. Execute: python secret_scan.py
"""
from __future__ import annotations

import re

PATTERNS = {
    "AWS_KEY": re.compile(r"AKIA[0-9A-Z]{16}"),
    "PRIVATE_KEY": re.compile(r"-----BEGIN .*PRIVATE KEY-----"),
    "PASSWORD": re.compile(r"password\s*=\s*['\"]?[^\s'\"]{6,}"),
}


def scan(text: str) -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    for name, pat in PATTERNS.items():
        for m in pat.finditer(text):
            hits.append((name, m.group(0)[:20]))
    return hits


if __name__ == "__main__":
    sample = 'aws_key=AKIAIOSFODNN7EXAMPLE password="supersecret123"'
    encontrados = scan(sample)
    if encontrados:
        print("Segredos encontrados:")
        for nome, trecho in encontrados:
            print(f"  [{nome}] {trecho}")
    else:
        print("Nenhum segredo encontrado.")

