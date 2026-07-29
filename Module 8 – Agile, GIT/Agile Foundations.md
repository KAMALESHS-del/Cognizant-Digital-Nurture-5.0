
---

# 1. Agile Manifesto

## Definition

The **Agile Manifesto** is a set of **4 values and 12 principles** that help software teams develop products faster while adapting to changing customer needs.

It was introduced in **2001** by 17 software developers.

---

## Four Agile Values

### 1. Individuals and interactions over processes and tools

**Meaning:**
People working together are more important than following strict processes.

**Example:**

Instead of filling many documents, developers discuss requirements directly with the client.

---

### 2. Working software over comprehensive documentation

**Meaning:**
A working application is more valuable than hundreds of pages of documentation.

**Example:**

Instead of spending one month writing documents, the team builds a working login page in one week.

---

### 3. Customer collaboration over contract negotiation

**Meaning:**
Customers continuously provide feedback during development.

**Example:**

Customer asks to change button color.

Agile Team:

> Changes it in next sprint.

Waterfall:

> Must modify documents first.

---

### 4. Responding to change over following a plan

**Meaning:**
Requirements may change anytime.

Agile welcomes changes.

**Example**

Customer wants Dark Mode after development starts.

Agile team adds it in the next sprint.

---

## Simple Example

Building an Online Shopping App

Week 1

* Login Page

Week 2

* Product Page

Week 3

* Cart

Week 4

* Payment

Customer gives feedback every week.

---

# 2. Agile vs Waterfall

| Agile                          | Waterfall                               |
| ------------------------------ | --------------------------------------- |
| Flexible                       | Fixed                                   |
| Incremental development        | Sequential development                  |
| Customer involved continuously | Customer involved only at beginning/end |
| Changes are easy               | Changes are difficult                   |
| Testing happens continuously   | Testing after development               |
| Fast delivery                  | Slow delivery                           |

---

## Example

### Waterfall

Requirement

↓

Design

↓

Coding

↓

Testing

↓

Deployment

Problem:
If customer changes requirements after coding, the team must redo many phases.

---

### Agile

Sprint 1 → Login

Sprint 2 → Dashboard

Sprint 3 → Payment

Sprint 4 → Reports

Customer reviews every sprint.

Changes can be added easily.

---

## Interview Question

**Which model is better?**

Answer:

* Agile for changing requirements
* Waterfall for fixed requirements like government projects

---

# 3. Iterative Development

## Definition

Iterative Development means building software **step by step** instead of developing everything at once.

Each iteration improves the product.

---

## Example

Building a Food Delivery App

Iteration 1

* Login

Iteration 2

* Restaurant List

Iteration 3

* Cart

Iteration 4

* Payment

Iteration 5

* Tracking

Each version works independently.

---

## Advantages

* Early feedback
* Fewer bugs
* Easier testing
* Faster delivery
* Better customer satisfaction

---

## Real-Life Example

Microsoft Word

Version 1

Basic typing

↓

Version 2

Spell Check

↓

Version 3

Auto Save

↓

Version 4

Cloud Sync

Each release improves the previous one.

---

# 4. Roles in Agile Teams

An Agile team consists of different members working together.

---

## A. Product Owner (PO)

### Responsibilities

* Understand customer needs
* Prioritize features
* Maintain Product Backlog
* Accept completed work

### Example

Customer wants:

* Login
* Payment
* Coupons

Product Owner decides:

1. Login
2. Payment
3. Coupons

---

## B. Scrum Master

### Responsibilities

* Removes obstacles
* Conducts Scrum meetings
* Helps team follow Agile practices
* Protects team from interruptions

### Example

Developers cannot access the server.

Scrum Master contacts the infrastructure team and resolves the issue.

---

## C. Development Team

Includes

* Frontend Developers
* Backend Developers
* Testers
* UI Designers
* DevOps Engineers

Responsibilities

* Design
* Develop
* Test
* Deliver software

---

## D. Stakeholders

Examples

* Customer
* Manager
* Business Analyst

They review progress and provide feedback.

---

## Team Structure Example

```
Customer
      │
Product Owner
      │
Scrum Master
      │
-------------------------
| Developer             |
| Tester                |
| UI Designer           |
| DevOps Engineer       |
-------------------------
```

---

# 5. Estimation Techniques

Software teams estimate the effort required to complete tasks.

---

## A. Story Points

Story points measure **effort, complexity, and risk**, not time.

Common values:

```
1
2
3
5
8
13
21
```

### Example

| Task            | Story Points |
| --------------- | ------------ |
| Login Page      | 2            |
| Registration    | 3            |
| Payment Gateway | 8            |
| Chat Feature    | 13           |

Higher story points indicate greater effort or complexity.

---

## B. Planning Poker

Each team member secretly selects a story point card.

Cards

```
1 2 3 5 8 13 21
```

### Example

Task:

Build Payment Module

Developer A → 5

Developer B → 8

Tester → 8

Discussion happens.

Final estimate → 8 Story Points

---

## C. T-Shirt Sizing

Tasks are estimated using sizes.

| Size | Meaning    |
| ---- | ---------- |
| XS   | Very Small |
| S    | Small      |
| M    | Medium     |
| L    | Large      |
| XL   | Very Large |

### Example

| Feature           | Size |
| ----------------- | ---- |
| Login             | S    |
| Registration      | M    |
| Search            | L    |
| AI Recommendation | XL   |

---

## D. Time-Based Estimation

Tasks are estimated in hours or days.

### Example

| Task      | Estimate |
| --------- | -------- |
| Login     | 4 Hours  |
| Dashboard | 2 Days   |
| Payment   | 3 Days   |

---

# Sprint Example

Suppose a team has these tasks:

| Feature   | Story Points |
| --------- | ------------ |
| Login     | 2            |
| Signup    | 3            |
| Dashboard | 5            |
| Cart      | 8            |
| Payment   | 13           |

Total = **31 Story Points**

If the team's sprint capacity is **20 Story Points**, they may include:

* Login (2)
* Signup (3)
* Dashboard (5)
* Cart (8)

Total = **18 Story Points**

The **Payment** feature (13 points) is moved to the next sprint.

---

# Advantages of Agile

* Faster software delivery
* Continuous customer feedback
* Easy to accommodate changes
* Better product quality
* Improved teamwork
* Reduced project risk
* Frequent testing and bug fixing

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Agile?

**Answer:** Agile is a software development methodology that delivers software in small, iterative increments while continuously incorporating customer feedback.

### 2. What are the four Agile Manifesto values?

**Answer:**

* Individuals and interactions over processes and tools
* Working software over comprehensive documentation
* Customer collaboration over contract negotiation
* Responding to change over following a plan

### 3. Agile vs Waterfall?

**Answer:** Agile is iterative, flexible, and supports continuous feedback, while Waterfall follows a fixed sequence of phases with limited flexibility for changes.

### 4. What is Iterative Development?

**Answer:** Iterative development builds software in small, working versions, improving it with each iteration based on feedback.

### 5. Who are the key Agile team members?

**Answer:** Product Owner, Scrum Master, Development Team, and Stakeholders.

### 6. What are Story Points?

**Answer:** Story points estimate the effort, complexity, and risk of a task rather than the actual time required.

### 7. What is Planning Poker?

**Answer:** Planning Poker is a collaborative estimation technique where team members independently choose story point values, discuss differences, and agree on a final estimate.

### 8. Why is Agile preferred?

**Answer:** Agile enables faster delivery, adapts easily to changing requirements, improves collaboration, and ensures continuous customer feedback, leading to higher-quality software.

---

## Quick Revision (1-Minute)

| Topic                 | Key Point                                                                        |
| --------------------- | -------------------------------------------------------------------------------- |
| Agile Manifesto       | 4 values, customer-focused, adaptable                                            |
| Agile vs Waterfall    | Agile is iterative and flexible; Waterfall is sequential and rigid               |
| Iterative Development | Build software step by step with feedback                                        |
| Product Owner         | Prioritizes requirements and manages the backlog                                 |
| Scrum Master          | Facilitates Agile practices and removes blockers                                 |
| Development Team      | Designs, develops, tests, and delivers the product                               |
| Story Points          | Estimate effort, not time                                                        |
| Planning Poker        | Team-based estimation using story point cards                                    |
| T-Shirt Sizing        | Estimates work as XS, S, M, L, XL                                                |
| Sprint                | A fixed time period (typically 1–4 weeks) to deliver a working product increment |

