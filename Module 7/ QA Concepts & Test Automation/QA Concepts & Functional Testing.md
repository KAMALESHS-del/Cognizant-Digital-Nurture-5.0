# Module: QA Concepts & Functional Testing

## Overview

Quality Assurance (QA) is a systematic process that ensures software products meet specified requirements and are free from defects. QA focuses on preventing issues throughout the software development lifecycle, while testing is used to identify defects before software is released. Functional testing verifies that each feature works according to the requirements.

---

# 1. QA Roles & Responsibilities

## What is Quality Assurance (QA)?

Quality Assurance (QA) is the process of ensuring that software is developed according to quality standards and meets customer expectations. QA aims to prevent defects rather than just finding them.

### Objectives of QA

* Ensure software meets business requirements.
* Improve software quality.
* Reduce defects before release.
* Increase customer satisfaction.
* Follow standard development processes.

### Responsibilities of a QA Engineer

* Understand project requirements.
* Create test plans and test cases.
* Execute manual and automated tests.
* Report and track bugs.
* Verify bug fixes.
* Perform regression testing.
* Work closely with developers and business analysts.
* Maintain testing documentation.
* Ensure software quality before release.

### Skills Required

* Analytical thinking
* Problem-solving
* Communication skills
* Knowledge of SDLC and STLC
* Automation basics
* Attention to detail

---

# 2. Types of Testing

Software testing is broadly divided into:

## A. Functional Testing

Functional testing verifies that software functions according to the specified requirements.

### Types

### Unit Testing

* Tests individual functions or methods.
* Performed by developers.

**Example**

```text
Calculator.add(2,3) → Expected = 5
```

---

### Integration Testing

Tests interaction between multiple modules.

Example:

```text
Login Module + Database
```

Checks whether login credentials are correctly verified from the database.

---

### System Testing

Entire application is tested as one complete system.

Example:
Testing an online shopping website from login to payment.

---

### Acceptance Testing (UAT)

Performed by clients or end users.

Purpose:

* Ensure software satisfies business needs.

Example:
Customer checks whether all required features work before deployment.

---

### Smoke Testing

Basic testing performed after a new build.

Purpose:

* Check whether major functionalities work.

Example:

* Login works
* Home page opens
* Database connection successful

---

### Sanity Testing

Checks whether a specific bug fix or feature works properly.

Example:
Developer fixes password reset.

QA verifies only password reset functionality.

---

### Regression Testing

Ensures old functionalities continue working after new changes.

Example:
Adding Wishlist should not break Cart functionality.

---

## B. Non-Functional Testing

Tests quality attributes rather than functionality.

### Performance Testing

Checks speed and response time.

Example:
Can website load within 2 seconds?

---

### Load Testing

Tests application under expected users.

Example:
1000 users accessing simultaneously.

---

### Stress Testing

Tests application beyond normal limits.

Example:
10,000 users accessing at once.

---

### Security Testing

Checks for vulnerabilities.

Example:
SQL Injection
Cross-Site Scripting (XSS)

---

### Usability Testing

Checks whether software is easy to use.

Example:
Navigation should be simple.

---

### Compatibility Testing

Checks application on different:

* Browsers
* Devices
* Operating Systems

---

### Reliability Testing

Measures consistent performance over time.

---

# 3. Test Levels

Testing is performed at different levels.

## Level 1: Unit Testing

* Individual components
* Done by developers

Example:
Testing login validation method.

---

## Level 2: Integration Testing

Tests communication between modules.

Example:
Payment Gateway + Banking API

---

## Level 3: System Testing

Tests the entire application.

Example:
Complete Online Banking System

---

## Level 4: Acceptance Testing

Done by customer.

Purpose:
Verify business requirements.

---

### Test Level Diagram

```text
Acceptance Testing
        ▲
System Testing
        ▲
Integration Testing
        ▲
Unit Testing
```

---

# 4. Black-Box vs White-Box Testing

| Feature           | Black-Box Testing                                 | White-Box Testing                |
| ----------------- | ------------------------------------------------- | -------------------------------- |
| Knowledge of code | Not required                                      | Required                         |
| Focus             | Functionality                                     | Internal code                    |
| Tester            | QA Engineer                                       | Developer                        |
| Based on          | Requirements                                      | Program logic                    |
| Objective         | Validate outputs                                  | Validate code paths              |
| Techniques        | Equivalence Partitioning, Boundary Value Analysis | Statement, Branch, Path Coverage |

---

## Black-Box Testing

Tests software without seeing source code.

### Example

Requirement:

```text
Password must contain 8 characters.
```

Test Cases:

* 6 characters → Fail
* 8 characters → Pass
* 12 characters → Pass

---

## White-Box Testing

Tests internal program logic.

Example

```python
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

Test cases:

* age = 20
* age = 15

Both branches are tested.

---

# 5. Defect Lifecycle & Management

A defect (bug) is any difference between expected and actual software behavior.

## Defect Lifecycle

```text
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed
```

If the issue still exists:

```text
Retest
 ↓
Reopened
 ↓
Assigned
 ↓
Fixed
 ↓
Verified
 ↓
Closed
```

---

## Defect Status Explanation

### New

QA discovers a bug.

---

### Assigned

Bug is assigned to a developer.

---

### Open

Developer starts working.

---

### Fixed

Developer fixes the issue.

---

### Retest

QA tests the fix.

---

### Verified

Bug is confirmed fixed.

---

### Closed

Issue is officially closed.

---

### Reopened

Bug still exists after fixing.

---

### Rejected

Developer determines it is not a valid bug.

---

### Duplicate

Bug has already been reported.

---

### Deferred

Bug fix is postponed to a future release.

---

## Defect Report Example

| Field           | Example                                 |
| --------------- | --------------------------------------- |
| Defect ID       | BUG-101                                 |
| Module          | Login                                   |
| Severity        | High                                    |
| Priority        | High                                    |
| Status          | Open                                    |
| Reported By     | QA Engineer                             |
| Assigned To     | Developer                               |
| Expected Result | User should log in successfully         |
| Actual Result   | Login fails despite correct credentials |

---

# Severity vs Priority

| Severity          | Priority                              |
| ----------------- | ------------------------------------- |
| Impact of the bug | Urgency to fix                        |
| Technical impact  | Business urgency                      |
| Set by QA         | Usually decided by QA/Project Manager |

### Example

* Login page crashes → High Severity, High Priority
* Logo misalignment → Low Severity, Low Priority
* Typo on homepage before product launch → Low Severity, High Priority

---

# Software Testing Life Cycle (STLC)

```text
Requirement Analysis
        ↓
Test Planning
        ↓
Test Case Design
        ↓
Environment Setup
        ↓
Test Execution
        ↓
Defect Reporting
        ↓
Retesting
        ↓
Regression Testing
        ↓
Test Closure
```

---

# Real-Time Example

**Application:** Online Banking System

**Feature:** Money Transfer

**Functional Test Cases**

* Transfer money with sufficient balance.
* Transfer money with insufficient balance.
* Transfer to an invalid account.
* Verify transaction history updates correctly.

**Non-Functional Test Cases**

* Response time under 2 seconds.
* Support 10,000 concurrent users.
* Prevent unauthorized access.
* Work correctly across Chrome, Firefox, Edge, and Safari.

---

# Interview Questions

1. What is Quality Assurance?
2. Difference between QA and QC.
3. Explain Functional Testing.
4. What is Non-Functional Testing?
5. Difference between Smoke and Sanity Testing.
6. What are the four levels of testing?
7. Difference between Black-Box and White-Box Testing.
8. Explain the Defect Lifecycle.
9. Difference between Severity and Priority.
10. What is Regression Testing?
11. What is User Acceptance Testing (UAT)?
12. What is the Software Testing Life Cycle (STLC)?
13. What is the purpose of Compatibility Testing?
14. What is the difference between Load Testing and Stress Testing?
15. What information is included in a defect report?

---

# Key Points to Remember

* QA focuses on **preventing defects**, while testing focuses on **finding defects**.
* Functional testing checks **what the software does**; non-functional testing checks **how well it performs**.
* The four test levels are **Unit, Integration, System, and Acceptance**.
* Black-box testing validates functionality without viewing the source code; white-box testing verifies internal code logic.
* Common functional tests include **Smoke, Sanity, Regression, and UAT**.
* Non-functional testing includes **Performance, Load, Stress, Security, Usability, Compatibility, and Reliability** testing.
* A defect typically moves through **New → Assigned → Open → Fixed → Retest → Verified → Closed**.
* **Severity** measures the impact of a defect, while **Priority** determines how urgently it should be fixed.
* The **STLC** consists of Requirement Analysis, Test Planning, Test Case Design, Environment Setup, Test Execution, Defect Reporting, Retesting, Regression Testing, and Test Closure.

