# Module: CI/CD Pipelines & Responsible Use of GitHub Copilot (Cognizant Technical Assessment)

CI/CD is one of the most important DevOps practices. It helps teams **automatically build, test, and deploy applications** whenever developers make changes to the source code.

---

# What is CI/CD?

## Definition

**CI/CD** stands for:

* **CI – Continuous Integration**
* **CD – Continuous Delivery / Continuous Deployment**

It automates software development, testing, and deployment.

---

## Real-Life Example

Suppose a developer updates the **Login Feature**.

Without CI/CD:

* Developer writes code.
* Manually builds the application.
* Manually tests it.
* Manually deploys it.
* Slow and error-prone.

With CI/CD:

* Developer pushes code to GitHub.
* Pipeline automatically:

  * Builds the application.
  * Runs tests.
  * Deploys to staging.
  * After approval, deploys to production.

---

# CI/CD Workflow

```text
Developer
     │
     ▼
Push Code to GitHub
     │
     ▼
Continuous Integration (CI)
     │
 ┌───────────────┐
 │ Build         │
 │ Run Tests     │
 │ Code Quality  │
 └───────────────┘
     │
     ▼
Continuous Delivery (CD)
     │
Deploy to Staging
     │
Manual Approval
     │
     ▼
Deploy to Production
```

---

# Continuous Integration (CI)

## Definition

Continuous Integration is the practice of **frequently merging code into a shared repository** where automated builds and tests run immediately.

### Objectives

* Detect bugs early
* Ensure code integrates correctly
* Reduce merge conflicts

---

## Example

Developer A updates Login.

Developer B updates Registration.

Both push code to GitHub.

CI automatically:

* Builds the application.
* Runs unit tests.
* Reports any failures.

---

## Benefits

* Faster feedback
* Better code quality
* Easier collaboration
* Early bug detection

---

# Continuous Delivery (CD)

## Definition

Continuous Delivery automatically prepares software for release.

Deployment to production usually requires **manual approval**.

---

## Workflow

```text
Build
   │
Test
   │
Deploy to Staging
   │
Manual Approval
   │
Deploy to Production
```

---

# Continuous Deployment

## Definition

Continuous Deployment goes one step further.

If all tests pass, the application is **automatically deployed to production** without manual approval.

---

# Continuous Delivery vs Continuous Deployment

| Continuous Delivery               | Continuous Deployment           |
| --------------------------------- | ------------------------------- |
| Manual approval before production | Automatic production deployment |
| Lower release risk                | Faster releases                 |
| Common in enterprise applications | Common in mature DevOps teams   |

---

# 1. Pipeline Concepts

## Definition

A **Pipeline** is an automated sequence of steps that builds, tests, and deploys software.

---

## Pipeline Stages

```text
Source Code
      │
      ▼
Build
      │
      ▼
Unit Test
      │
      ▼
Integration Test
      │
      ▼
Package
      │
      ▼
Deploy
```

---

## Benefits

* Automation
* Consistent deployments
* Faster releases
* Fewer manual errors

---

# Typical Pipeline

```text
Git Commit
     │
     ▼
Build
     │
     ▼
Run Tests
     │
     ▼
Security Scan
     │
     ▼
Create Artifact
     │
     ▼
Deploy
```

---

# 2. GitHub Actions Workflows

## Definition

**GitHub Actions** is GitHub's automation service used to build CI/CD pipelines directly from a GitHub repository.

Workflow files are stored in:

```text
.github/workflows/
```

---

## Example Workflow

```yaml
name: Build Application

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Java
        uses: actions/setup-java@v4

      - name: Build
        run: mvn clean package
```

---

## Workflow Explanation

* Trigger on push to `main`
* Checkout repository
* Install Java
* Build the application

---

## Benefits

* Built into GitHub
* Easy automation
* Supports many programming languages
* Large marketplace of reusable actions

---

# GitHub Actions Workflow

```text
Push Code
     │
     ▼
GitHub Actions
     │
 ┌─────────────┐
 │ Build       │
 │ Test        │
 │ Deploy      │
 └─────────────┘
```

---

# 3. Azure Pipelines

## Definition

**Azure Pipelines** is a CI/CD service in **Azure DevOps**.

It automates:

* Build
* Test
* Package
* Deployment

---

## Example

Developer pushes code.

↓

Azure Pipeline starts automatically.

↓

Build

↓

Run Tests

↓

Deploy to Azure App Service.

---

## Azure Pipeline Example

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
- script: mvn clean package
```

---

## Benefits

* Supports multiple platforms
* Integrates with Azure DevOps
* Automated deployment
* Enterprise-ready

---

# Azure Pipeline Workflow

```text
Git Push
    │
    ▼
Azure Pipeline
    │
Build
    │
Test
    │
Deploy
```

---

# GitHub Actions vs Azure Pipelines

| GitHub Actions                | Azure Pipelines          |
| ----------------------------- | ------------------------ |
| Built into GitHub             | Part of Azure DevOps     |
| Great for GitHub repositories | Strong Azure integration |
| Uses YAML workflows           | Uses YAML pipelines      |
| Large Actions marketplace     | Rich enterprise features |

---

# 4. Build & Deploy Stages

## Build Stage

Compiles the application and prepares it for deployment.

Example:

Java

```bash
mvn clean package
```

Node.js

```bash
npm install
npm run build
```

---

## Test Stage

Runs automated tests.

Examples:

* Unit Tests
* Integration Tests
* Code Quality Checks

---

## Package Stage

Creates deployable artifacts.

Examples:

* JAR
* WAR
* Docker Image
* ZIP Package

---

## Deploy Stage

Deploys the application.

Examples:

* AWS
* Azure
* Google Cloud
* Kubernetes

---

# Build Pipeline Example

```text
Source Code
      │
      ▼
Compile
      │
      ▼
Run Tests
      │
      ▼
Package
      │
      ▼
Deploy
```

---

# 5. Environment Promotion

## Definition

Environment Promotion is the process of moving the same application build through multiple environments before production.

---

## Common Environments

```text
Development
      │
      ▼
Testing
      │
      ▼
Staging
      │
      ▼
Production
```

---

## Example

Developer completes Login feature.

↓

Deploy to Development

↓

QA tests

↓

Deploy to Staging

↓

Business approval

↓

Deploy to Production

---

## Benefits

* Safer deployments
* Better testing
* Reduced production failures
* Consistent releases

---

# Environment Promotion Workflow

```text
Developer
     │
     ▼
Development
     │
     ▼
Testing
     │
     ▼
Staging
     │
     ▼
Production
```

---

# 6. Responsible Use of GitHub Copilot

## What is GitHub Copilot?

**GitHub Copilot** is an AI-powered coding assistant that suggests code, documentation, tests, and explanations while you write software.

It helps improve developer productivity but should always be used responsibly.

---

## Good Practices

* Use Copilot as a coding assistant, not a replacement for understanding.
* Review every generated suggestion before accepting it.
* Test generated code thoroughly.
* Follow your project's coding standards.
* Check for security issues and performance problems.
* Ensure generated code matches licensing and organizational policies.

---

## Avoid

* Accepting code without reading it.
* Sharing confidential company data or secrets in prompts.
* Assuming generated code is always correct.
* Skipping code reviews because AI generated the code.

---

## Example

**Poor Practice**

Developer accepts Copilot-generated database code without testing.

Result:

Application crashes due to a missing null check.

**Good Practice**

Developer reviews the code, adds validation, runs unit tests, and submits it for peer review before merging.

---

# Complete Example

A company develops an **Online Banking Application**.

### Step 1

Developer pushes code to GitHub.

### Step 2

GitHub Actions starts automatically.

### Step 3

Application is built.

### Step 4

Unit and integration tests run.

### Step 5

A Docker image is created.

### Step 6

The application is deployed to the **Development** environment.

### Step 7

After QA testing, the same build is promoted to **Staging**.

### Step 8

Following approval, it is deployed to **Production**.

### Step 9

The developer uses **GitHub Copilot** to generate boilerplate code but reviews, tests, and refines it before committing.

---

# CI/CD Summary

| Topic                       | Purpose                                                      |
| --------------------------- | ------------------------------------------------------------ |
| Continuous Integration (CI) | Automatically build and test code after changes              |
| Continuous Delivery         | Prepare software for release with approval before production |
| Continuous Deployment       | Automatically deploy to production after successful tests    |
| Pipeline                    | Automated build, test, and deployment workflow               |
| GitHub Actions              | GitHub-based CI/CD automation                                |
| Azure Pipelines             | Azure DevOps CI/CD service                                   |
| Build Stage                 | Compile source code                                          |
| Test Stage                  | Execute automated tests                                      |
| Package Stage               | Create deployable artifact                                   |
| Deploy Stage                | Release application to an environment                        |
| Environment Promotion       | Move builds from Dev → Test → Staging → Production           |
| GitHub Copilot              | AI coding assistant that requires review and testing         |

---

# Advantages of CI/CD

* Faster software delivery
* Automated testing
* Early bug detection
* Consistent deployments
* Reduced manual effort
* Higher software quality
* Easier rollback and recovery
* Better collaboration

---

# Cognizant Technical Assessment – Important Questions

### 1. What is CI/CD?

**Answer:** CI/CD is a DevOps practice that automates building, testing, and deploying software. CI stands for Continuous Integration, while CD stands for Continuous Delivery or Continuous Deployment.

---

### 2. What is Continuous Integration (CI)?

**Answer:** Continuous Integration is the practice of frequently merging code into a shared repository where automated builds and tests verify the changes.

---

### 3. What is the difference between Continuous Delivery and Continuous Deployment?

| Continuous Delivery                        | Continuous Deployment                                      |
| ------------------------------------------ | ---------------------------------------------------------- |
| Requires manual approval before production | Deploys automatically to production after successful tests |

---

### 4. What is a pipeline?

**Answer:** A pipeline is an automated sequence of stages that builds, tests, packages, and deploys an application.

---

### 5. What is GitHub Actions?

**Answer:** GitHub Actions is GitHub's built-in automation platform for creating CI/CD workflows using YAML files stored in the repository.

---

### 6. What is Azure Pipelines?

**Answer:** Azure Pipelines is a CI/CD service within Azure DevOps that automates application build, testing, and deployment.

---

### 7. What is Environment Promotion?

**Answer:** Environment Promotion is the controlled movement of the same application build through Development, Testing, Staging, and Production environments.

---

### 8. How should GitHub Copilot be used responsibly?

**Answer:**

* Review all generated code.
* Test suggestions thoroughly.
* Follow coding and security standards.
* Do not expose confidential information in prompts.
* Treat Copilot as an assistant, not an authority.

---

# Quick Revision (1-Minute)

| Topic                 | Key Point                                          |
| --------------------- | -------------------------------------------------- |
| CI                    | Automatically build and test code changes          |
| CD                    | Deliver or deploy applications automatically       |
| Pipeline              | Build → Test → Package → Deploy                    |
| GitHub Actions        | CI/CD automation built into GitHub                 |
| Azure Pipelines       | CI/CD service in Azure DevOps                      |
| Build Stage           | Compile source code                                |
| Test Stage            | Run automated tests                                |
| Package Stage         | Create deployable artifact                         |
| Deploy Stage          | Release application                                |
| Environment Promotion | Dev → Test → Staging → Production                  |
| GitHub Copilot        | AI assistant—always review and test generated code |

