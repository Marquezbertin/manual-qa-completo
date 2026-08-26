# Module 11: Security Testing (OWASP)

## 11.1 Why test security?

A security flaw can cost customer data, fines (LGPD/GDPR, PCI-DSS), and reputation. Security is not optional: it must be **shift-left** — tested from design, not only in production.

> *"Secure by design"* — consider threats during design (Threat Modeling).

## 11.2 OWASP Top 10 (2021)

The 10 most critical web vulnerabilities:

1. **Broken Access Control** — missing access restrictions
2. **Cryptographic Failures** — sensitive data without encryption
3. **Injection** — SQL, XSS, OS command
4. **Insecure Design** — missing design controls
5. **Security Misconfiguration** — insecure defaults, error exposure
6. **Vulnerable and Outdated Components** — libs with known CVE
7. **Identification and Authentication Failures** — weak auth
8. **Software and Data Integrity Failures** — unsigned pipelines
9. **Security Logging and Monitoring Failures** — no audit
10. **Server-Side Request Forgery (SSRF)** — forged requests

## 11.3 Types of Security Testing

| Type | Approach | Example tool |
|------|----------|--------------|
| **SAST** | static code | Bandit, Semgrep |
| **DAST** | running app | OWASP ZAP |
| **Dependency Scan** | vulnerable libs | pip-audit, Dependency-Check |
| **Secret Scan** | secrets in code | Gitleaks, TruffleHog |
| **Penetration Test** | real attack | red team |

## 11.4 Runnable Example: Secret Scanner

The script `docs/11/scripts/secret_scan.py` detects obvious secrets (AWS keys, private keys, passwords) via regex — no dependencies:

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

Run: `python docs/11/scripts/secret_scan.py`

## 11.5 Best Practices

- **Input validation** against injection (use ORMs/parameterized queries)
- **Least privilege** (RBAC)
- **Secrets in a vault** (Vault, AWS Secrets Manager) — never in code/logs
- **HTTPS/TLS** on all transactions
- **Dependency updates** and continuous scanning (CI)
- **Logs without sensitive data**

## 11.6 Citations and References

- **OWASP Top 10 (2021)** — https://owasp.org/www-project-top-ten/
- **OWASP Testing Guide** — https://owasp.org/www-project-web-security-testing-guide/
- **OWASP ASVS** — Application Security Verification Standard
- **OWASP ZAP** — https://www.zaproxy.org/

---

## 11.7 Next Steps

At the end of this module, the reader should be able to:
1. Explain the OWASP Top 10 (2021)
2. Differentiate SAST, DAST, and secret scanning
3. Run a basic secret scanner
4. Apply security best practices in CI
5. Integrate dependency/security scanning in pipelines

---

> **Return to any module** to deepen. Good and secure QA! 🔒

