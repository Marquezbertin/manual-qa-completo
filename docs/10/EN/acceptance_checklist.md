# Acceptance Checklist

```
FUNCTIONALITY
  [ ] Main flows work (happy path)
  [ ] Edge cases handled
  [ ] Clear error messages (English)

DATA VALIDATION
  [ ] Required fields validated
  [ ] Masks/formats (SSN, phone, date)
  [ ] Basic SQL injection / XSS blocked

UI / UX
  [ ] Responsive (mobile/tablet/desktop)
  [ ] Loading/error/empty states
  [ ] Accessibility (focus, contrast)

SECURITY
  [ ] No secrets in logs/console
  [ ] Logout invalidates session
  [ ] Sensitive data masked

PERFORMANCE
  [ ] Acceptable response time (< SLA)
  [ ] No obvious memory leak

DATA / ENVIRONMENT
  [ ] Tested build = accepted build
  [ ] Test data anonymized
```
