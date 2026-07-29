# Module: Git & GitHub Workflow (Cognizant Technical Assessment)

Git and GitHub are essential tools used by software developers for **version control**, **team collaboration**, and **code management**. These topics are frequently asked in Cognizant technical assessments and interviews.

---

# What is Git?

## Definition

**Git** is a **Distributed Version Control System (DVCS)** used to track changes in source code and allow multiple developers to work on the same project without overwriting each other's work.

### Advantages

* Tracks code changes
* Supports collaboration
* Maintains version history
* Easy rollback to previous versions
* Supports branching and merging

---

# What is GitHub?

## Definition

**GitHub** is a cloud-based platform that hosts Git repositories and provides collaboration features such as Pull Requests, Issues, and Code Reviews.

### Example

A team developing an **Online Shopping Application** stores the project on GitHub.

* Developer A → Login Module
* Developer B → Payment Module
* Developer C → Cart Module

GitHub combines everyone's work safely.

---

# Git Workflow

```text
Create Repository
        │
        ▼
Clone Repository
        │
        ▼
Create Branch
        │
        ▼
Write Code
        │
        ▼
Git Add
        │
        ▼
Git Commit
        │
        ▼
Git Push
        │
        ▼
Pull Request
        │
        ▼
Code Review
        │
        ▼
Merge into Main Branch
```

---

# 1. Git Basics

## Important Git Commands

### Initialize Repository

```bash
git init
```

Creates a new Git repository.

---

### Clone Repository

```bash
git clone https://github.com/user/project.git
```

Downloads an existing repository from GitHub.

---

### Check Status

```bash
git status
```

Shows:

* Modified files
* Untracked files
* Files ready to commit

---

### Add Files

Single file

```bash
git add index.html
```

All files

```bash
git add .
```

Moves files to the staging area.

---

### Commit Changes

```bash
git commit -m "Added login page"
```

Saves changes in the local repository.

---

### Push Changes

```bash
git push origin main
```

Uploads commits to GitHub.

---

### Pull Latest Changes

```bash
git pull origin main
```

Downloads the latest changes from GitHub.

---

### View Commit History

```bash
git log
```

Displays previous commits.

---

## Example

Developer edits:

```text
login.html
```

Workflow

```text
git add .
      ↓
git commit -m "Added Login Page"
      ↓
git push origin main
```

---

# 2. Branching Strategies

## What is a Branch?

A **branch** is an independent line of development that allows developers to work on new features or bug fixes without affecting the main code.

---

## Common Branches

```text
main
 │
 ├── feature/login
 │
 ├── feature/payment
 │
 └── bugfix/navbar
```

---

## Why Use Branches?

* Parallel development
* Safer experimentation
* Easy bug fixing
* Cleaner collaboration

---

## Create Branch

```bash
git branch feature-login
```

---

## Switch Branch

```bash
git checkout feature-login
```

Or

```bash
git switch feature-login
```

---

## Create and Switch Together

```bash
git checkout -b feature-login
```

---

## Example

Developer A

```text
feature-login
```

Developer B

```text
feature-payment
```

Both work independently.

After testing, both branches merge into **main**.

---

## Popular Branching Strategies

### Git Flow

Branches:

* main
* develop
* feature/*
* release/*
* hotfix/*

Used in large projects.

---

### GitHub Flow

Simple workflow:

```text
main
   │
Feature Branch
   │
Pull Request
   │
Merge
```

Best for continuous deployment.

---

# 3. Pull Requests (PR)

## Definition

A **Pull Request (PR)** is a request to merge code from one branch into another after review.

---

## Why Use Pull Requests?

* Code review
* Team discussion
* Automated testing
* Better code quality

---

## Example

Developer completes:

```text
feature-login
```

Creates:

**Pull Request**

Reviewer checks:

* Code quality
* Bugs
* Naming
* Performance

If approved

↓

Merge into **main**

---

## Pull Request Workflow

```text
Feature Branch
      │
      ▼
Pull Request
      │
      ▼
Code Review
      │
      ▼
Approval
      │
      ▼
Merge
```

---

# 4. Merge vs Rebase

Both combine changes from different branches, but they work differently.

---

## Merge

Creates a **merge commit** and preserves branch history.

Example

```text
main
  A──B──C
        \
         D──E (feature)
              \
               M (Merge Commit)
```

Command

```bash
git merge feature-login
```

### Advantages

* Preserves history
* Safe for shared branches
* Easy to understand

---

## Rebase

Moves feature commits on top of the latest main branch, creating a cleaner, linear history.

Example

Before

```text
main
A──B──C

feature
     D──E
```

After Rebase

```text
main
A──B──C──D'──E'
```

Command

```bash
git rebase main
```

### Advantages

* Cleaner commit history
* Easier to read logs

**Note:** Avoid rebasing branches that have already been shared with others, as it rewrites commit history.

---

# Merge vs Rebase Comparison

| Merge                    | Rebase                            |
| ------------------------ | --------------------------------- |
| Creates a merge commit   | Rewrites commit history           |
| Preserves branch history | Produces a linear history         |
| Safe for shared branches | Best for local, unshared branches |
| Easier to understand     | Cleaner commit history            |

---

# 5. Conflict Resolution

## What is a Merge Conflict?

A merge conflict occurs when two developers modify the **same part of the same file**, and Git cannot determine which change should be kept automatically.

---

## Example

Developer A

```text
button color = Blue
```

Developer B

```text
button color = Green
```

When merging, Git reports a conflict.

---

## Conflict Markers

```text
<<<<<<< HEAD
Button Color = Blue
=======
Button Color = Green
>>>>>>> feature-login
```

Developer manually edits the file:

```text
Button Color = Blue
```

(or chooses Green or combines both, depending on the requirement)

---

## Resolve Conflict

```bash
git add .
git commit
```

Conflict is resolved.

---

## Tips

* Pull the latest changes frequently.
* Keep branches short-lived.
* Communicate with teammates.
* Make small, focused commits.

---

# 6. Tags & Releases

## What is a Tag?

A **tag** is a permanent label pointing to a specific commit, commonly used to mark software versions.

---

## Example

```text
v1.0
```

Initial Release

```text
v1.1
```

Bug Fix Release

```text
v2.0
```

Major Update

---

## Create Tag

```bash
git tag v1.0
```

---

## Push Tag

```bash
git push origin v1.0
```

---

## List Tags

```bash
git tag
```

---

## What is a Release?

A **release** is a published version of the software, often created from a Git tag and accompanied by release notes.

Example:

Version **v1.0**

Features:

* Login
* Registration
* Dashboard

Users can download this stable version.

---

# Complete GitHub Workflow Example

Suppose a team is building a **Student Management System**.

### Step 1

Clone repository

```bash
git clone https://github.com/company/student-system.git
```

---

### Step 2

Create branch

```bash
git checkout -b feature-login
```

---

### Step 3

Develop Login Page

---

### Step 4

Commit changes

```bash
git add .
git commit -m "Added login functionality"
```

---

### Step 5

Push branch

```bash
git push origin feature-login
```

---

### Step 6

Create Pull Request

Reviewer checks:

* Code quality
* Functionality
* Tests

---

### Step 7

Merge into **main**

---

### Step 8

Create Release

```bash
git tag v1.0
git push origin v1.0
```

The application version **v1.0** is ready for deployment.

---

# Advantages of Git & GitHub

* Version control
* Team collaboration
* Easy rollback
* Parallel development using branches
* Code review through Pull Requests
* Release management with tags
* Safe backup in the cloud
* Supports CI/CD workflows

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Git?

**Answer:** Git is a distributed version control system that tracks changes in source code and enables collaborative software development.

### 2. What is GitHub?

**Answer:** GitHub is a cloud platform for hosting Git repositories and supporting collaboration through features like Pull Requests, code reviews, and issue tracking.

### 3. What is a Git branch?

**Answer:** A branch is an independent line of development that allows developers to work on features or bug fixes without affecting the main branch.

### 4. What is a Pull Request?

**Answer:** A Pull Request is a request to merge changes from one branch into another after review and approval.

### 5. Difference between Merge and Rebase?

| Merge                    | Rebase                   |
| ------------------------ | ------------------------ |
| Preserves branch history | Creates a linear history |
| Adds a merge commit      | Rewrites commit history  |
| Safe for shared branches | Best for local branches  |

### 6. What is a merge conflict?

**Answer:** A merge conflict occurs when Git cannot automatically combine changes because multiple developers modified the same part of a file.

### 7. What is a Git tag?

**Answer:** A Git tag is a permanent reference to a specific commit, usually used to mark software versions such as **v1.0** or **v2.0**.

### 8. What is a release?

**Answer:** A release is a published version of the software created from a tagged commit and often includes release notes.

---

# Quick Revision (1-Minute)

| Topic          | Key Point                                                         |
| -------------- | ----------------------------------------------------------------- |
| Git            | Distributed version control system                                |
| GitHub         | Cloud platform for Git repositories                               |
| Git Basics     | `init`, `clone`, `add`, `commit`, `push`, `pull`, `status`, `log` |
| Branch         | Independent line of development                                   |
| Pull Request   | Request to merge reviewed code                                    |
| Merge          | Combines branches with a merge commit                             |
| Rebase         | Replays commits for a cleaner history                             |
| Merge Conflict | Happens when Git cannot merge changes automatically               |
| Tag            | Labels a specific commit (e.g., `v1.0`)                           |
| Release        | Published software version based on a tag                         |


