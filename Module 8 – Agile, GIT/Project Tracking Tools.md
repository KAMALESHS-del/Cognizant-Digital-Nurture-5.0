
Project Tracking Tools help Agile teams **plan, assign, track, and manage software development work**. They improve collaboration, monitor project progress, and ensure tasks are completed on time.

Common Project Tracking Tools:

* Jira
* Azure Boards
* GitHub Projects

---

# What are Project Tracking Tools?

## Definition

Project Tracking Tools are software applications used to:

* Plan project work
* Track task progress
* Assign work to team members
* Monitor sprint progress
* Report project status

---

## Example

Suppose a team is developing an **Online Shopping Application**.

Tasks:

* Login
* Registration
* Search
* Cart
* Payment

Instead of using Excel, the team uses **Jira** or **Azure Boards** to manage these tasks.

---

# Agile Project Workflow

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
Assign Tasks
       │
       ▼
Development
       │
       ▼
Testing
       │
       ▼
Done
```

---

# 1. Jira Basics

## What is Jira?

**Jira** is one of the most popular Agile project management tools developed by **Atlassian**.

It is mainly used for:

* Sprint Planning
* Bug Tracking
* Task Management
* Agile Reporting
* Scrum and Kanban Boards

---

## Features of Jira

* Product Backlog
* Sprint Backlog
* Scrum Board
* Kanban Board
* Issue Tracking
* Reports and Dashboards
* Burndown Charts

---

## Example

Project:

Online Banking System

Jira Board

| To Do  | In Progress | Testing | Done         |
| ------ | ----------- | ------- | ------------ |
| Login  | Dashboard   | Payment | Registration |
| Search |             |         |              |

Developers simply move tasks between columns as work progresses.

---

## Jira Issue Types

| Issue Type | Description                 |
| ---------- | --------------------------- |
| Epic       | Large feature or project    |
| Story      | User requirement            |
| Task       | General work item           |
| Bug        | Defect to fix               |
| Sub-task   | Smaller task within a story |

---

### Example

Epic

Shopping Application

↓

Story

User Login

↓

Sub-task

* Design Login Page
* Create Login API
* Write Unit Tests

---

# 2. Azure Boards

## What is Azure Boards?

Azure Boards is an Agile project management tool that is part of **Azure DevOps**.

It helps teams:

* Plan work
* Track tasks
* Manage backlogs
* Track bugs
* Run Scrum and Kanban projects

---

## Features

* Product Backlog
* Sprint Planning
* Kanban Boards
* Dashboards
* Work Items
* Reporting

---

## Example

Azure Board

```text
To Do → In Progress → Testing → Done
```

Task

Payment Module

Moves across the board until completed.

---

## Work Item Types

* Epic
* Feature
* User Story
* Task
* Bug

---

# Jira vs Azure Boards

| Jira                       | Azure Boards                           |
| -------------------------- | -------------------------------------- |
| Developed by Atlassian     | Part of Azure DevOps                   |
| Popular for Agile projects | Integrated with Azure services         |
| Supports Scrum & Kanban    | Supports Scrum & Kanban                |
| Strong plugin ecosystem    | Strong Microsoft ecosystem integration |

---

# 3. GitHub Projects

## What is GitHub Projects?

GitHub Projects is a project management feature integrated with GitHub repositories.

It helps developers manage:

* Tasks
* Pull Requests
* Issues
* Releases

---

## Example

Columns

```text
To Do
↓

In Progress
↓

Review
↓

Done
```

Each issue or pull request appears as a card and moves through the workflow.

---

## Features

* Kanban-style boards
* Linked Pull Requests
* Linked Issues
* Automation rules
* Milestones
* Labels

---

## Example

Task

Develop Login API

↓

Developer creates Pull Request

↓

GitHub automatically links it to the project board

↓

Reviewer approves

↓

Card moves to Done

---

# Jira vs GitHub Projects

| Jira                    | GitHub Projects               |
| ----------------------- | ----------------------------- |
| Advanced Agile planning | Lightweight project tracking  |
| Separate application    | Built into GitHub             |
| Extensive reports       | Basic reporting               |
| Supports Scrum & Kanban | Mainly Kanban-style workflows |

---

# 4. User Stories

## Definition

A **User Story** is a short description of a feature written from the perspective of the end user.

---

## Standard Format

```text
As a <user>,
I want <feature>,
So that <benefit>.
```

---

## Example 1

As a customer,

I want to log in using my email and password,

So that I can access my account securely.

---

## Example 2

As a student,

I want to download my marksheet,

So that I can print it.

---

## Characteristics of Good User Stories

* Simple
* Clear
* Valuable
* Testable
* Small enough to complete within a sprint

---

# 5. Acceptance Criteria

## Definition

Acceptance Criteria define the conditions that must be satisfied for a User Story to be considered complete.

They help developers and testers understand exactly what is expected.

---

## Example

User Story

As a customer,

I want to log in,

So that I can access my account.

---

Acceptance Criteria

✔ User can log in with valid credentials.

✔ Invalid password shows an error message.

✔ Empty fields are not accepted.

✔ Password is hidden while typing.

✔ Login redirects to the dashboard after success.

---

## Benefits

* Removes ambiguity
* Helps QA create test cases
* Ensures everyone understands the requirements

---

# 6. Story Points

## Definition

Story Points measure the **relative effort, complexity, and risk** involved in completing a User Story.

They **do not represent hours or days**.

---

## Fibonacci Scale

```text
1 2 3 5 8 13 21
```

Higher value = More effort.

---

## Example

| User Story     | Story Points |
| -------------- | ------------ |
| Login          | 2            |
| Registration   | 3            |
| Product Search | 5            |
| Shopping Cart  | 8            |
| Online Payment | 13           |

---

## Planning Poker Example

Task

Payment Gateway

Developer A

8

Developer B

13

Tester

8

After discussion,

Final Estimate

8 Story Points

---

# Complete Example

A team is developing an **Online Food Delivery Application**.

### Product Backlog

* Login
* Restaurant List
* Search
* Cart
* Payment

### User Story

As a customer,

I want to search restaurants,

So that I can quickly find nearby food options.

### Acceptance Criteria

* Search returns matching restaurants.
* Results update within 2 seconds.
* Empty search shows all restaurants.
* No matching results display a helpful message.

### Story Points

Search Feature = **5 Story Points**

### Tracking

The story is added to **Jira**.

Workflow

```text
To Do
↓

In Progress
↓

Testing
↓

Done
```

The Scrum Master tracks progress throughout the sprint.

---

# Advantages of Project Tracking Tools

* Better task organization
* Easy sprint planning
* Improved team collaboration
* Clear visibility of project progress
* Faster bug tracking
* Better reporting and dashboards
* Supports Agile methodologies
* Increases productivity

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Jira?

**Answer:** Jira is an Agile project management and issue-tracking tool used for sprint planning, task management, bug tracking, and Scrum/Kanban workflows.

---

### 2. What is Azure Boards?

**Answer:** Azure Boards is an Agile planning tool within Azure DevOps that helps teams manage backlogs, user stories, tasks, bugs, and sprint progress.

---

### 3. What is GitHub Projects?

**Answer:** GitHub Projects is a project management feature integrated with GitHub that organizes issues, pull requests, and tasks using Kanban-style boards.

---

### 4. What is a User Story?

**Answer:** A User Story is a short description of a feature from the user's perspective, usually written as: *As a..., I want..., So that...*.

---

### 5. What are Acceptance Criteria?

**Answer:** Acceptance Criteria are the specific conditions that a feature must satisfy before it is considered complete and accepted.

---

### 6. What are Story Points?

**Answer:** Story Points estimate the relative effort, complexity, and risk of implementing a User Story. They are not based on time.

---

### 7. Difference between Jira, Azure Boards, and GitHub Projects?

| Tool            | Best Use                                                        |
| --------------- | --------------------------------------------------------------- |
| Jira            | Advanced Agile project management, Scrum, and Kanban            |
| Azure Boards    | Agile planning integrated with Azure DevOps                     |
| GitHub Projects | Lightweight task management integrated with GitHub repositories |

---

# Quick Revision (1-Minute)

| Topic               | Key Point                                       |
| ------------------- | ----------------------------------------------- |
| Jira                | Agile project management and issue tracking     |
| Azure Boards        | Agile planning tool in Azure DevOps             |
| GitHub Projects     | Kanban-style project tracking in GitHub         |
| User Story          | Describes a feature from the user's perspective |
| User Story Format   | As a... I want... So that...                    |
| Acceptance Criteria | Conditions that define when a story is complete |
| Story Points        | Measure effort, complexity, and risk (not time) |
| Common Workflow     | To Do → In Progress → Testing/Review → Done     |

