
Cloud Security & Monitoring are essential for protecting cloud resources, securing applications, monitoring system health, and controlling cloud costs. Every cloud platform (AWS, Azure, and Google Cloud) provides built-in security and monitoring services.

---

# What is Cloud Security?

## Definition

**Cloud Security** is the practice of protecting cloud infrastructure, applications, data, and services from unauthorized access, cyberattacks, and data loss.

Cloud security includes:

* Identity and Access Management (IAM)
* Data encryption
* Secure communication (HTTPS/TLS)
* Secrets management
* Monitoring and logging
* Cost management

---

## Real-Life Example

Suppose a company develops an **Online Banking Application**.

To secure it:

* **IAM** controls who can access cloud resources.
* **Secrets Manager** stores database passwords.
* **HTTPS/TLS** encrypts communication.
* **Logging & Monitoring** detect suspicious activities.
* **Cost Monitoring** tracks cloud spending.

---

# Cloud Security Architecture

```text
                 Users
                   │
             HTTPS / TLS
                   │
                   ▼
          Web Application
                   │
     ┌─────────────┼─────────────┐
     ▼             ▼             ▼
   IAM        Secrets Manager   Database
     │                           │
     └─────────────┬─────────────┘
                   ▼
          Logging & Monitoring
                   │
                   ▼
           Cost Monitoring
```

---

# 1. IAM Principles (Identity and Access Management)

## Definition

**IAM (Identity and Access Management)** controls:

* Who can access cloud resources
* What actions they can perform
* Which resources they can use

IAM improves security by granting only the required permissions.

---

## IAM Components

### Users

Individual accounts.

Example:

* Alice (Developer)
* Bob (Administrator)

---

### Groups

Collection of users with similar permissions.

Example:

* Developers
* Testers
* Administrators

---

### Roles

Temporary permissions assigned to users or services.

Example:

An application running on a server accesses cloud storage using an IAM Role.

---

### Policies

Rules defining permissions.

Example

Allow:

* Read Cloud Storage

Deny:

* Delete Database

---

# Principle of Least Privilege

## Definition

Users should receive **only the minimum permissions needed** to perform their work.

---

## Example

Developer

Allowed

* Deploy application
* Read logs

Not Allowed

* Delete production database

---

## Benefits

* Reduces security risks
* Prevents accidental changes
* Protects sensitive data

---

# Multi-Factor Authentication (MFA)

IAM often supports **MFA**.

Example:

Login requires:

* Password
* Mobile verification code

This provides stronger account security.

---

# 2. Secrets Management

## Definition

Secrets Management securely stores sensitive information instead of placing it in source code.

Examples of Secrets:

* Database passwords
* API Keys
* Access Tokens
* Encryption Keys
* OAuth Client Secrets

---

## Bad Practice

```python
password = "Admin123"
```

Password is visible to anyone reading the code.

---

## Good Practice

Store the password in a **Secrets Manager**.

Application retrieves it securely at runtime.

---

## Cloud Services

| Cloud Platform | Secrets Service     |
| -------------- | ------------------- |
| AWS            | AWS Secrets Manager |
| Azure          | Azure Key Vault     |
| Google Cloud   | Secret Manager      |

---

## Example

Shopping Application

↓

Database Password

↓

Stored securely in Secret Manager

↓

Application retrieves it when starting.

---

## Benefits

* Better security
* Easy secret rotation
* Centralized management
* Reduced risk of leaks

---

# 3. HTTPS / TLS

## What is HTTPS?

**HTTPS (HyperText Transfer Protocol Secure)** encrypts communication between a user's browser and a web server.

---

## What is TLS?

**TLS (Transport Layer Security)** is the protocol that provides encryption for HTTPS.

---

## HTTP vs HTTPS

| HTTP          | HTTPS         |
| ------------- | ------------- |
| Not encrypted | Encrypted     |
| Less secure   | Highly secure |
| Port 80       | Port 443      |

---

## Example

Without HTTPS

```text
User
 │
 ▼
Password ---------> Internet ---------> Server

Anyone intercepting traffic may read the password.
```

---

## With HTTPS/TLS

```text
User
 │
 ▼
Encrypted Password ======> Server

Attackers cannot easily read the encrypted data.
```

---

## Benefits

* Encrypts communication
* Protects passwords
* Prevents data tampering
* Improves user trust

---

# SSL vs TLS

| SSL            | TLS                     |
| -------------- | ----------------------- |
| Older protocol | Modern replacement      |
| Less secure    | More secure             |
| Obsolete       | Currently used by HTTPS |

> Modern websites use **TLS**, although people often still say "SSL certificate."

---

# 4. Logging & Monitoring

## Definition

Logging records system events.

Monitoring continuously observes system health and performance.

---

## Logging Example

Application Log

```text
09:30 User Login Successful

09:35 Product Added

09:40 Payment Failed
```

Logs help developers investigate issues.

---

## Monitoring Example

Monitor:

* CPU Usage
* Memory Usage
* Disk Usage
* Response Time
* Network Traffic
* Error Rate

---

## Cloud Monitoring Services

| Cloud Platform | Monitoring Service                   |
| -------------- | ------------------------------------ |
| AWS            | Amazon CloudWatch                    |
| Azure          | Application Insights / Azure Monitor |
| Google Cloud   | Cloud Monitoring and Cloud Logging   |

---

## Alert Example

CPU reaches **90%**.

↓

Monitoring service sends an alert.

↓

Operations team investigates.

---

## Benefits

* Detect failures early
* Improve performance
* Troubleshoot issues
* Increase application reliability

---

# Logging & Monitoring Workflow

```text
Application
      │
      ▼
Generate Logs
      │
      ▼
Monitoring Service
      │
      ▼
Alerts
      │
      ▼
Developer / Operations Team
```

---

# 5. Cost Management Basics

## Definition

Cloud Cost Management helps organizations monitor, optimize, and control cloud spending.

Since cloud providers charge based on usage, efficient management prevents unnecessary expenses.

---

## Cost Optimization Techniques

### A. Shut Down Unused Resources

Example:

Development virtual machines running overnight consume money.

Stop them when not in use.

---

### B. Delete Unused Storage

Remove:

* Old backups
* Unused virtual disks
* Temporary files

---

### C. Auto Scaling

Increase resources only when demand increases.

Reduce resources during low traffic.

---

### D. Monitor Usage

Review monthly cloud bills and dashboards.

---

### E. Choose the Right Service Size

Avoid using oversized virtual machines for small workloads.

---

# Example

Without Auto Scaling

```text
10 Virtual Machines

Running All Day

↓

Higher Cost
```

With Auto Scaling

```text
Morning

2 Virtual Machines

↓

Evening Peak

10 Virtual Machines

↓

Night

2 Virtual Machines

↓

Lower Cost
```

---

# Cloud Cost Tools

| Cloud Platform | Cost Tool             |
| -------------- | --------------------- |
| AWS            | AWS Cost Explorer     |
| Azure          | Azure Cost Management |
| Google Cloud   | Cloud Billing Reports |

---

# Complete Example

Suppose a company develops an **Online Food Delivery Application**.

### Step 1

Developers log in using **IAM** with the **Principle of Least Privilege**.

### Step 2

Database passwords are stored in a **Secrets Manager**.

### Step 3

Customers access the website over **HTTPS**, protected by **TLS** encryption.

### Step 4

The application writes logs for user logins, payments, and errors.

### Step 5

Cloud monitoring tracks CPU usage, response time, and availability. Alerts are sent when problems occur.

### Step 6

Auto Scaling adjusts server capacity based on demand, and cost management tools help control monthly cloud expenses.

---

# Cloud Security & Monitoring Summary

| Topic                        | Purpose                                           |
| ---------------------------- | ------------------------------------------------- |
| IAM                          | Manage users, roles, and permissions              |
| Principle of Least Privilege | Grant only the minimum required access            |
| Secrets Management           | Securely store passwords, API keys, and tokens    |
| HTTPS/TLS                    | Encrypt communication between clients and servers |
| Logging                      | Record system events                              |
| Monitoring                   | Track health, performance, and availability       |
| Cost Management              | Monitor and optimize cloud spending               |

---

# Advantages of Cloud Security & Monitoring

* Protects sensitive data
* Prevents unauthorized access
* Detects security threats quickly
* Improves application reliability
* Supports compliance requirements
* Optimizes cloud costs
* Enhances customer trust
* Reduces operational risks

---

# Cognizant Technical Assessment – Important Questions

### 1. What is IAM?

**Answer:** IAM (Identity and Access Management) is a security service that controls who can access cloud resources and what actions they are allowed to perform.

---

### 2. What is the Principle of Least Privilege?

**Answer:** It is the security principle of granting users and applications only the minimum permissions necessary to perform their tasks.

---

### 3. What is Secrets Management?

**Answer:** Secrets Management securely stores and manages sensitive information such as passwords, API keys, access tokens, and encryption keys instead of hardcoding them in applications.

---

### 4. What is HTTPS?

**Answer:** HTTPS is the secure version of HTTP that encrypts communication between a client and a server using TLS.

---

### 5. What is TLS?

**Answer:** TLS (Transport Layer Security) is the encryption protocol that secures data transmitted over HTTPS.

---

### 6. What is the difference between Logging and Monitoring?

| Logging                       | Monitoring                                          |
| ----------------------------- | --------------------------------------------------- |
| Records events and activities | Continuously observes system health and performance |
| Used for troubleshooting      | Used to detect issues and trigger alerts            |

---

### 7. Why is cloud cost management important?

**Answer:** Cloud cost management helps organizations track usage, eliminate waste, optimize resources, and reduce unnecessary cloud spending.

---

### 8. Name cloud services for monitoring and secrets management.

| Cloud Provider | Monitoring                           | Secrets Management  |
| -------------- | ------------------------------------ | ------------------- |
| AWS            | CloudWatch                           | AWS Secrets Manager |
| Azure          | Azure Monitor / Application Insights | Azure Key Vault     |
| Google Cloud   | Cloud Monitoring                     | Secret Manager      |

---

# Quick Revision (1-Minute)

| Topic              | Key Point                                               |
| ------------------ | ------------------------------------------------------- |
| Cloud Security     | Protect cloud resources and data                        |
| IAM                | Manage identities and permissions                       |
| Least Privilege    | Grant minimum required access                           |
| Secrets Management | Store passwords and keys securely                       |
| HTTPS              | Secure version of HTTP                                  |
| TLS                | Encrypts network communication                          |
| Logging            | Records system events                                   |
| Monitoring         | Tracks system health and sends alerts                   |
| Cost Management    | Monitor and optimize cloud spending                     |
| Common Goal        | Secure, reliable, and cost-efficient cloud applications |


