# Módulo 11: Testes de Segurança (OWASP)

## 11.1 Por que testar segurança?

Uma falha de segurança pode custar dados de clientes, multas (LGPD/GDPR, PCI-DSS) e reputação. Segurança não é opcional: deve ser **shift-left** — testada desde o design, não só em produção.

> *"Secure by design"* — projetar já considerando ameaças (Threat Modeling).

## 11.2 OWASP Top 10 (2021)

Lista das 10 vulnerabilidades web mais críticas:

1. **Broken Access Control** — falta de restrição de acesso
2. **Cryptographic Failures** — dados sensíveis sem criptografia
3. **Injection** — SQL, XSS, comando OS
4. **Insecure Design** — falta de controles no design
5. **Security Misconfiguration** — defaults inseguros, exposição de erros
6. **Vulnerable and Outdated Components** — libs com CVE conhecida
7. **Identification and Authentication Failures** — auth fraca
8. **Software and Data Integrity Failures** — pipelines sem assinatura
9. **Security Logging and Monitoring Failures** — sem auditoria
10. **Server-Side Request Forgery (SSRF)** — requisições forjadas

## 11.3 Tipos de Teste de Segurança

| Tipo | Abordagem | Exemplo de ferramenta |
|------|-----------|----------------------|
| **SAST** | código estático | Bandit, Semgrep |
| **DAST** | app em execução | OWASP ZAP |
| **Dependency Scan** | libs vulneráveis | pip-audit, Dependency-Check |
| **Secret Scan** | segredos no código | Gitleaks, TruffleHog |
| **Penetration Test** | ataque real | equipe de red team |

## 11.4 Exemplo Executável: Secret Scanner

O script `docs/11/scripts/secret_scan.py` detecta segredos óbvios (chaves AWS, chaves privadas, senhas) via regex — sem dependências:

```python
import re
PATTERNS = {
    "AWS_KEY": re.compile(r"AKIA[0-9A-Z]{16}"),
    "PRIVATE_KEY": re.compile(r"-----BEGIN .*PRIVATE KEY-----"),
    "PASSWORD": re.compile(r"password\s*=\s*['\"]?[^\s'\"]{6,}"),
}
def scan(text):
    return [(n, m.group(0)[:20]) for n, p in PATTERNS.items()
            for m in p.finditer(text)]
```

Execute: `python docs/11/scripts/secret_scan.py`

## 11.5 Boas Práticas

- **Validação de entrada** contra injection (use ORMs/parametrized queries)
- **Princípio do menor privilégio** (RBAC)
- **Segredos em cofre** (Vault, AWS Secrets Manager) — nunca no código/log
- **HTTPS/TLS** em todas as transações
- **Atualização de dependências** e escaneamento contínuo (CI)
- **Logs sem dados sensíveis**

## 11.6 Citações e Referências

- **OWASP Top 10 (2021)** — https://owasp.org/www-project-top-ten/
- **OWASP Testing Guide** — https://owasp.org/www-project-web-security-testing-guide/
- **OWASP ASVS** — Application Security Verification Standard
- **OWASP ZAP** — https://www.zaproxy.org/

---

## 11.7 Próximos Passos

Ao final deste módulo, o leitor deverá:
1. Explicar o OWASP Top 10 (2021)
2. Diferenciar SAST, DAST e secret scanning
3. Rodar um secret scanner básico
4. Aplicar boas práticas de segurança no CI
5. Integrar dependência/segurança em pipelines

---

> **Volte a qualquer módulo** para aprofundar. Bom QA seguro! 🔒

