# Module: Microsoft Azure (Cognizant Technical Assessment)

Microsoft Azure is a **cloud computing platform** that provides services for hosting applications, databases, storage, serverless computing, DevOps, monitoring, networking, and AI. Many enterprises use Azure because it integrates well with Microsoft technologies.

---

# What is Microsoft Azure?

## Definition

**Microsoft Azure** is a cloud computing platform developed by **Microsoft** that provides on-demand cloud services such as:

* Virtual Machines
* Web App Hosting
* Databases
* Storage
* Serverless Computing
* DevOps
* Monitoring
* Networking

It follows a **pay-as-you-go** pricing model.

---

## Real-Life Example

Suppose a company develops an **Online Shopping Application**.

Instead of buying physical servers:

* **App Service** → Hosts the web application
* **Azure SQL Database** → Stores customer data
* **Blob Storage** → Stores product images
* **Azure Functions** → Processes uploaded images
* **Azure DevOps** → Manages code and CI/CD
* **Application Insights** → Monitors application performance

---

# Azure Architecture Example

```text
                Users
                  │
                  ▼
            Azure App Service
                  │
        ┌─────────┴──────────┐
        ▼                    ▼
 Azure SQL Database     Azure Functions
        │                    │
        └─────────┬──────────┘
                  ▼
            Blob Storage
                  │
                  ▼
      Application Insights
                  ▲
                  │
          Azure DevOps (CI/CD)
```

---

# 1. Azure App Service

## Definition

**Azure App Service** is a **Platform as a Service (PaaS)** used to host web applications, REST APIs, and mobile backends.

Developers upload code, and Azure manages:

* Servers
* Operating System
* Scaling
* Security
* Load balancing

---

## Features

* Automatic scaling
* HTTPS support
* Deployment slots
* Custom domains
* Continuous deployment

---

## Example

A company builds an **Employee Portal**.

Developer uploads the application.

↓

Azure App Service hosts it.

↓

Users access the website through the internet.

---

## Supported Technologies

* ASP.NET
* Java
* Python
* Node.js
* PHP
* Ruby

---

## Advantages

* Easy deployment
* Automatic updates
* Built-in security
* Auto scaling

---

# 2. Azure SQL Database

## Definition

**Azure SQL Database** is a fully managed relational database service.

It is based on Microsoft SQL Server.

---

## Features

* Automatic backups
* High availability
* Automatic updates
* Built-in security
* Auto scaling

---

## Example

Online Banking System

Customer details

↓

Stored in Azure SQL Database

Azure automatically performs:

* Backup
* Recovery
* Security updates

---

## Advantages

* No database server management
* Reliable
* Secure
* Highly available

---

# 3. Blob Storage

## Definition

**Azure Blob Storage** is an object storage service used to store unstructured data.

Examples:

* Images
* Videos
* PDFs
* Documents
* Audio files
* Backup files

---

## Example

Shopping Application

Customer uploads a product image.

↓

Image stored in Blob Storage.

↓

Database stores only the image URL.

---

## Storage Types

* Block Blob
* Append Blob
* Page Blob

---

## Advantages

* Massive storage capacity
* Secure
* Cost-effective
* Fast access

---

# 4. Azure Functions

## Definition

Azure Functions is a **serverless computing** service.

It allows developers to run code automatically when an event occurs.

Developers do not manage servers.

---

## Event Examples

* File uploaded
* Timer event
* HTTP request
* Database update
* Queue message

---

## Example

Customer uploads an image.

↓

Blob Storage triggers Azure Function.

↓

Function compresses the image.

↓

Compressed image stored again.

---

## Advantages

* No server management
* Automatic scaling
* Pay only when code runs
* Event-driven execution

---

# 5. Azure DevOps

## Definition

Azure DevOps is a platform that supports the complete software development lifecycle.

It provides tools for:

* Project management
* Source control
* Build automation
* Testing
* Deployment

---

## Azure DevOps Services

### Azure Boards

* Agile planning
* Sprint management
* Backlogs

---

### Azure Repos

Git repositories for source code.

---

### Azure Pipelines

CI/CD pipelines

Automatically:

* Build
* Test
* Deploy

---

### Azure Test Plans

Manage manual and exploratory testing.

---

### Azure Artifacts

Store packages and dependencies.

---

## Example

Developer pushes code to Azure Repos.

↓

Azure Pipeline starts automatically.

↓

Build

↓

Test

↓

Deploy to Azure App Service.

---

# Azure DevOps Workflow

```text
Developer
     │
     ▼
Azure Repos
     │
     ▼
Azure Pipeline
     │
 ┌───┼────┐
 ▼   ▼    ▼
Build Test Deploy
     │
     ▼
Azure App Service
```

---

## Benefits

* Continuous Integration (CI)
* Continuous Deployment (CD)
* Automated testing
* Faster releases

---

# 6. Application Insights

## Definition

Application Insights is an Azure monitoring service that tracks application health and performance.

---

## Monitors

* Response time
* Failed requests
* Exceptions
* Performance
* User activity
* Availability

---

## Example

Website response time increases.

↓

Application Insights detects slow performance.

↓

Developer investigates.

↓

Performance issue fixed.

---

## Features

* Live Metrics
* Performance Monitoring
* Error Tracking
* Dependency Monitoring
* Usage Analytics

---

## Benefits

* Detects issues early
* Improves performance
* Helps troubleshoot errors
* Enhances user experience

---

# Complete Azure Example

Suppose a company develops an **Online Food Delivery Application**.

### Step 1

Application deployed to **Azure App Service**.

### Step 2

Customer data stored in **Azure SQL Database**.

### Step 3

Food images uploaded to **Blob Storage**.

### Step 4

Blob upload triggers **Azure Functions** to resize images.

### Step 5

Developers use **Azure DevOps** to build, test, and deploy automatically.

### Step 6

**Application Insights** monitors performance and reports errors.

---

# Azure Services Summary

| Service              | Purpose                                              |
| -------------------- | ---------------------------------------------------- |
| Azure App Service    | Host web apps and APIs                               |
| Azure SQL Database   | Managed relational database                          |
| Blob Storage         | Store files such as images, videos, and documents    |
| Azure Functions      | Serverless event-driven code execution               |
| Azure DevOps         | Project management, Git repositories, CI/CD, testing |
| Application Insights | Monitor application performance and diagnose issues  |

---

# Azure vs AWS

| Azure Service        | Similar AWS Service                                           |
| -------------------- | ------------------------------------------------------------- |
| Azure App Service    | Elastic Beanstalk                                             |
| Azure SQL Database   | Amazon RDS                                                    |
| Blob Storage         | Amazon S3                                                     |
| Azure Functions      | AWS Lambda                                                    |
| Azure DevOps         | AWS CodePipeline / CodeBuild / CodeCommit (combined services) |
| Application Insights | Amazon CloudWatch                                             |

---

# Advantages of Microsoft Azure

* Easy application deployment
* Managed cloud services
* Automatic scaling
* High availability
* Strong security
* Built-in monitoring
* Excellent integration with Microsoft products
* Supports DevOps and CI/CD

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Microsoft Azure?

**Answer:** Microsoft Azure is a cloud computing platform that provides services such as computing, databases, storage, networking, serverless computing, DevOps, and monitoring.

---

### 2. What is Azure App Service?

**Answer:** Azure App Service is a Platform as a Service (PaaS) that hosts web applications, REST APIs, and mobile backends without requiring server management.

---

### 3. What is Azure SQL Database?

**Answer:** Azure SQL Database is a fully managed relational database service based on Microsoft SQL Server, offering automatic backups, updates, and high availability.

---

### 4. What is Blob Storage?

**Answer:** Blob Storage is Azure's object storage service used to store unstructured data such as images, videos, documents, and backups.

---

### 5. What are Azure Functions?

**Answer:** Azure Functions is a serverless computing service that executes code automatically in response to events such as HTTP requests, file uploads, or timers.

---

### 6. What is Azure DevOps?

**Answer:** Azure DevOps is a platform that provides tools for Agile planning, source control, CI/CD pipelines, testing, and package management throughout the software development lifecycle.

---

### 7. What is Application Insights?

**Answer:** Application Insights is Azure's monitoring service that tracks application performance, errors, availability, and user activity to help diagnose and resolve issues.

---

### 8. Difference between Azure App Service and Azure Functions?

| Azure App Service                    | Azure Functions                              |
| ------------------------------------ | -------------------------------------------- |
| Hosts full web applications and APIs | Runs small pieces of event-driven code       |
| Application runs continuously        | Code runs only when triggered                |
| Suitable for websites and REST APIs  | Suitable for background tasks and automation |

---

# Quick Revision (1-Minute)

| Topic                | Key Point                                                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Microsoft Azure      | Cloud computing platform by Microsoft                                                                                         |
| Azure App Service    | Host web apps and APIs (PaaS)                                                                                                 |
| Azure SQL Database   | Managed SQL database                                                                                                          |
| Blob Storage         | Object storage for files                                                                                                      |
| Azure Functions      | Serverless event-driven computing                                                                                             |
| Azure DevOps         | Agile planning, Git, CI/CD, testing                                                                                           |
| Application Insights | Monitor performance, errors, and application health                                                                           |
| Azure vs AWS         | App Service ↔ Elastic Beanstalk, Blob Storage ↔ S3, SQL Database ↔ RDS, Functions ↔ Lambda, Application Insights ↔ CloudWatch |


