# Module: Scrum Framework (Cognizant Technical Assessment)

Scrum is the **most widely used Agile framework** for developing software in small, manageable iterations called **Sprints**. It helps teams deliver high-quality products through collaboration, transparency, and continuous improvement.

---

# What is Scrum?

**Definition:**

Scrum is an Agile framework used to manage and complete complex software projects by dividing the work into short, fixed-length iterations called **Sprints** (usually **2–4 weeks**).

### Example

Suppose a team is developing an **Online Food Delivery App**.

Instead of building the entire application at once, they divide it into sprints.

* Sprint 1 → Login & Registration
* Sprint 2 → Restaurant Listing
* Sprint 3 → Cart & Checkout
* Sprint 4 → Payment & Order Tracking

At the end of every sprint, a working version of the application is delivered.

---

# Scrum Framework Overview

```text
Product Backlog
       │
       ▼
Sprint Planning
       │
       ▼
Sprint Backlog
       │
       ▼
Sprint (2–4 Weeks)
       │
 ┌───────────────┐
 │ Daily Standup │
 └───────────────┘
       │
       ▼
Working Product Increment
       │
       ▼
Sprint Review
       │
       ▼
Sprint Retrospective
       │
       ▼
Next Sprint
```

---

# 1. Scrum Roles

There are **three main Scrum roles**.

## A. Product Owner (PO)

### Responsibilities

* Represents the customer.
* Defines product requirements.
* Creates and prioritizes the Product Backlog.
* Accepts completed work.
* Maximizes product value.

### Example

Customer requests:

* Login
* Search Products
* Online Payment
* Wishlist

The Product Owner decides the priority:

1. Login
2. Search
3. Payment
4. Wishlist

---

## B. Scrum Master

### Responsibilities

* Ensures Scrum practices are followed.
* Removes blockers for the team.
* Facilitates Scrum meetings.
* Coaches the team in Agile principles.

### Example

The development team cannot deploy because the server is unavailable.

The Scrum Master coordinates with the infrastructure team to resolve the issue.

---

## C. Development Team

Includes:

* Frontend Developers
* Backend Developers
* Testers
* UI/UX Designers
* DevOps Engineers

### Responsibilities

* Design
* Develop
* Test
* Deliver working software

### Example

For an e-commerce application:

Frontend Developer:

* Creates the login page.

Backend Developer:

* Develops the authentication API.

Tester:

* Tests login functionality.

DevOps Engineer:

* Deploys the application.

---

# Scrum Team Example

```text
Customer
     │
Product Owner
     │
Scrum Master
     │
--------------------------------
| Developers                  |
| Testers                     |
| UI Designer                 |
| DevOps Engineer             |
--------------------------------
```

---

# 2. Sprint Planning

## Definition

Sprint Planning is the meeting where the team decides **what work will be completed during the upcoming sprint**.

Usually held at the beginning of every sprint.

### Activities

* Review Product Backlog
* Select high-priority items
* Estimate work
* Define Sprint Goal
* Create Sprint Backlog

---

### Example

Product Backlog

* Login
* Signup
* Dashboard
* Payment
* Chat

Sprint Capacity = 15 Story Points

Selected for Sprint

* Login
* Signup
* Dashboard

Payment and Chat remain in the Product Backlog for future sprints.

---

## Output

Sprint Backlog

* Login
* Signup
* Dashboard

---

# 3. Daily Standup (Daily Scrum)

## Definition

A Daily Standup is a **15-minute meeting** held every day during the sprint.

Purpose:

* Share progress
* Identify blockers
* Plan today's work

---

### Every team member answers three questions:

1. What did I complete yesterday?
2. What will I work on today?
3. Is there any blocker?

---

### Example

Developer

Yesterday:

* Completed Login API

Today:

* Develop Registration API

Blocker:

* Database connection issue

Scrum Master works to resolve the blocker.

---

## Benefits

* Better communication
* Quick problem solving
* Daily progress tracking
* Increased accountability

---

# 4. Sprint Review

## Definition

Sprint Review is conducted **at the end of the sprint** to demonstrate the completed work to stakeholders.

Purpose:

* Show completed features
* Gather customer feedback
* Update Product Backlog if needed

---

### Example

Completed:

* Login
* Registration
* Dashboard

Customer Feedback:

"Please add Google Login."

The Product Owner adds this requirement to the Product Backlog for a future sprint.

---

## Output

* Working product demonstration
* Customer feedback
* Updated Product Backlog

---

# 5. Sprint Retrospective

## Definition

Sprint Retrospective is held **after the Sprint Review**.

The team reflects on the sprint and identifies ways to improve.

Focus is on the **process**, not the product.

---

### Questions Discussed

* What went well?
* What didn't go well?
* What should we improve?

---

### Example

Went Well

* Completed all planned features.

Problems

* Testing started late.

Improvements

* Begin testing earlier in the next sprint.
* Improve communication between developers and testers.

---

## Benefits

* Continuous improvement
* Better teamwork
* Higher productivity
* Fewer repeated mistakes

---

# 6. Product Backlog

## Definition

The Product Backlog is a **prioritized list of all features, bug fixes, enhancements, and requirements** for the product.

Maintained by the **Product Owner**.

---

### Example

| Priority | Feature      |
| -------- | ------------ |
| 1        | Login        |
| 2        | Registration |
| 3        | Search       |
| 4        | Cart         |
| 5        | Payment      |
| 6        | Wishlist     |

The Product Backlog is continuously updated based on customer feedback and business needs.

---

# 7. Sprint Backlog

## Definition

The Sprint Backlog contains the **Product Backlog items selected for the current sprint**, along with the tasks needed to complete them.

Owned and managed by the **Development Team**.

---

### Example

Sprint 1 Backlog

| Task         | Status      |
| ------------ | ----------- |
| Login        | Completed   |
| Registration | In Progress |
| Dashboard    | Not Started |

The Sprint Backlog changes only if the team and Product Owner agree that adjustments are necessary.

---

# Product Backlog vs Sprint Backlog

| Product Backlog          | Sprint Backlog                        |
| ------------------------ | ------------------------------------- |
| All project requirements | Tasks selected for the current sprint |
| Managed by Product Owner | Managed by Development Team           |
| Updated continuously     | Used only during the current sprint   |
| Long-term planning       | Short-term execution                  |

---

# Complete Scrum Example

A team is developing an **Online Shopping Application**.

### Product Backlog

* Login
* Registration
* Product List
* Search
* Cart
* Payment
* Order History

### Sprint Planning

Sprint Goal:
Develop user authentication.

Sprint Backlog:

* Login
* Registration

### Daily Standup

Developer:

* Yesterday: Designed login page.
* Today: Connect login API.
* Blocker: API server unavailable.

### Sprint Review

The team demonstrates:

* Login
* Registration

Customer requests:

* Add "Login with Google."

This feature is added to the Product Backlog.

### Sprint Retrospective

The team decides:

* Start testing earlier.
* Improve code reviews.
* Reduce deployment delays.

---

# Scrum Ceremony Timeline

```text
Sprint Planning
      │
      ▼
Sprint Begins (2–4 Weeks)
      │
      ▼
Daily Standup (Every Day)
      │
      ▼
Sprint Ends
      │
      ▼
Sprint Review
      │
      ▼
Sprint Retrospective
      │
      ▼
Next Sprint
```

---

# Advantages of Scrum

* Delivers software faster
* Adapts easily to changing requirements
* Encourages teamwork and communication
* Provides continuous customer feedback
* Improves software quality through frequent testing
* Reduces project risk by delivering in small increments
* Supports continuous process improvement

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Scrum?

**Answer:** Scrum is an Agile framework that develops software in short iterations called sprints, delivering working software frequently.

### 2. Who are the three Scrum roles?

**Answer:** Product Owner, Scrum Master, and Development Team.

### 3. What is Sprint Planning?

**Answer:** A meeting where the team selects Product Backlog items, defines the Sprint Goal, and creates the Sprint Backlog.

### 4. What happens in the Daily Standup?

**Answer:** Team members discuss what they completed yesterday, what they will do today, and any blockers they face.

### 5. What is the purpose of the Sprint Review?

**Answer:** To demonstrate the completed product increment, gather stakeholder feedback, and update the Product Backlog if needed.

### 6. What is Sprint Retrospective?

**Answer:** A meeting where the Scrum team reflects on the sprint process and identifies improvements for future sprints.

### 7. What is a Product Backlog?

**Answer:** A prioritized list of all features, enhancements, bug fixes, and requirements maintained by the Product Owner.

### 8. What is a Sprint Backlog?

**Answer:** A list of Product Backlog items selected for the current sprint, along with the tasks required to complete them.

### 9. Difference between Product Backlog and Sprint Backlog?

**Answer:** The Product Backlog contains all future work for the product, while the Sprint Backlog contains only the work selected for the current sprint.

---

# Quick Revision (1-Minute)

| Topic                | Key Point                                       |
| -------------------- | ----------------------------------------------- |
| Scrum                | Agile framework using 2–4 week sprints          |
| Scrum Roles          | Product Owner, Scrum Master, Development Team   |
| Sprint Planning      | Select work and create Sprint Backlog           |
| Daily Standup        | 15-minute daily progress meeting                |
| Sprint Review        | Demonstrate completed work and collect feedback |
| Sprint Retrospective | Improve team process after each sprint          |
| Product Backlog      | Prioritized list of all project requirements    |
| Sprint Backlog       | Selected tasks for the current sprint           |

