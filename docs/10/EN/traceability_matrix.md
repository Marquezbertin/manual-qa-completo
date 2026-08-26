# Traceability Matrix

Links requirements → test cases → result.

| Req ID | Requirement | Test Case | Status | Bugs |
|--------|-------------|-----------|--------|------|
| REQ-01 | Valid login | TC-LOGIN-001 | Pass | - |
| REQ-02 | Invalid password | TC-LOGIN-002 | Pass | - |
| REQ-03 | Logout | TC-LOGIN-003 | Fail | BUG-120 |
| REQ-04 | Recover password | TC-PWD-001 | Pass | - |

Coverage = (Reqs with test / total Reqs) × 100
```
Coverage = 4/4 = 100%
Defect Leakage = prod bugs / total
```
