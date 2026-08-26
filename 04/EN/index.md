# Module 04: Manual and Exploratory Testing

## 4.1 Manual vs Exploratory Testing

| Aspect | Manual (Scripted) | Exploratory |
|--------|-------------------|-------------|
| Preparation | Detailed test cases | Session charter |
| Execution | Follows exact steps | Free, intuition-based |
| When to use | Regression, compliance | New features, hidden bugs |
| Advantage | Reproducible | Finds unexpected defects |

## 4.2 Structured Test Case

Every test case should have:
- **ID** unique
- **Preconditions**: required state before starting
- **Steps**: numbered actions
- **Test data**: values used
- **Expected result**: what should happen
- **Actual result**: what happened (filled during execution)
- **Status**: Pass / Fail / Blocked / Not Run

Example:
```
ID: TC-LOGIN-001
Precondition: Registered user (user@test.com / Pass123)
Steps:
  1. Access /login
  2. Enter valid email
  3. Enter valid password
  4. Click "Sign in"
Expected result: Redirect to /dashboard with user name
```

## 4.3 Session-Based Test Management (SBTM)

Structured exploratory testing methodology (James Bach / Jon Bach):
- **Charter**: session mission ("Explore the checkout screen looking for usability issues")
- **Time**: 60-90 min session, no interruptions
- **Opportunities**: bugs, questions, risks found
- **Bug**: reported defects
- **Test Notes**: free annotations
- **Debrief**: quick post-session review

Charter template:
```
Charter: Explore password recovery flow checking error messages
Areas: /forgot-password, email, SMS
Duration: 60 min
```

## 4.4 Test Checklists (Heuristics)

Practical checklist for web feature acceptance:
- [ ] Required fields validated
- [ ] Formatting (SSN, phone, date) accepts and rejects invalid
- [ ] Clear error messages in English
- [ ] Loading states displayed
- [ ] Responsive (mobile/tablet/desktop)
- [ ] Basic accessibility (contrast, focus, screen reader)
- [ ] Error logs don't expose sensitive data

## 4.5 Complete Bug Report

A good bug report saves time for the whole team.

| Field | Description |
|-------|-------------|
| **Title** | Failure summary (what happens) |
| **Environment** | Browser, OS, build version |
| **Steps to reproduce** | Numbered and exact |
| **Expected result** | What should happen |
| **Actual result** | What happened |
| **Severity** | Critical / High / Medium / Low (business impact) |
| **Priority** | Urgent / High / Medium / Low (fix urgency) |
| **Evidence** | Screenshot, video, logs |
| **Attachments** | `.har`, console log |

### Real example (anonymized)
```
Title: "Checkout" button disappears after card error
Environment: Chrome 120 / Windows 11 / Build 2.3.1
Steps:
  1. Add item to cart
  2. Go to checkout
  3. Enter invalid card (1234 5678 9012 3456)
  4. Submit
Expected result: Error message and button remains visible
Actual result: Error screen and button disappears (impossible to retry)
Severity: High (blocks sale)
Priority: High
Evidence: screenshot_error.png
```

## 4.6 Usability Testing and Nielsen Heuristics

**Nielsen's 10 heuristics (1994)**:
1. Visibility of system status
2. Match between system and real world
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, recover from errors
10. Help and documentation

## 4.7 Citations and References

- **Bach, J. & Bach, J. (2004)** — Session-Based Test Management
- **Nielsen, J. (1994)** — "10 Heuristics for User Interface Design"
- **ISTQB®** — "Test Techniques" (manual testing)
- **Kaner, C. (2008)** — Exploratory Testing

---

## 4.8 Next Steps

At the end of this module, the reader should be able to:
1. Write structured test cases
2. Create an exploratory session charter
3. Build an acceptance checklist
4. Write a complete and useful bug report
5. Apply Nielsen's heuristics

---

> **Next module**: [Module 05: Automated Testing](05/PT/indice.md)