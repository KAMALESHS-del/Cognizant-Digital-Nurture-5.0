# Module: Google Cloud Platform (GCP) – Cognizant Technical Assessment

Google Cloud Platform (GCP) is Google's cloud computing platform that provides services for computing, storage, databases, networking, serverless applications, AI, and DevOps. Many companies use GCP to build scalable and secure cloud applications.

---

# What is Google Cloud Platform (GCP)?

## Definition

**Google Cloud Platform (GCP)** is a cloud computing platform developed by **Google** that provides on-demand cloud services such as:

* Virtual Machines
* Application Hosting
* Databases
* Storage
* Serverless Computing
* Networking
* Monitoring
* Artificial Intelligence

Like other cloud platforms, GCP follows a **pay-as-you-go** pricing model.

---

## Real-Life Example

Suppose a company develops an **Online Shopping Application**.

Instead of buying physical servers:

* **Compute Engine** → Runs the application
* **Cloud SQL** → Stores customer information
* **Cloud Storage** → Stores product images
* **Cloud Functions** → Processes uploaded images
* **Cloud Run** → Runs containerized applications
* **gcloud CLI** → Manages cloud resources

---

# GCP Architecture Example

```text
                Users
                  │
                  ▼
             Cloud Run
                  │
       ┌──────────┴──────────┐
       ▼                     ▼
Compute Engine       Cloud Functions
       │                     │
       └──────────┬──────────┘
                  ▼
             Cloud SQL
                  │
                  ▼
           Cloud Storage
```

---

# 1. Compute Engine

## Definition

**Compute Engine** is GCP's **Infrastructure as a Service (IaaS)** that provides virtual machines (VMs) to run applications.

You can choose:

* Operating System
* CPU
* Memory
* Storage
* Network

---

## Features

* Virtual Machines
* Auto Scaling
* Load Balancing
* High Availability
* Custom Machine Types

---

## Example

A company launches an **Employee Management System**.

Instead of purchasing a physical server,

they create a **Compute Engine VM**.

The application runs on this virtual machine.

---

## Common Uses

* Web servers
* Backend APIs
* Development environments
* Enterprise applications

---

## Advantages

* Flexible
* Scalable
* High performance
* Easy to manage

---

# 2. Cloud Run

## Definition

**Cloud Run** is a **fully managed serverless platform** that runs containerized applications.

Developers package their application in a **Docker container**, and Cloud Run automatically:

* Deploys it
* Scales it
* Handles infrastructure

---

## Features

* Serverless
* Automatic scaling
* Supports Docker containers
* HTTPS enabled
* Pay only when used

---

## Example

A developer builds a **Node.js REST API**.

↓

Creates a Docker image.

↓

Deploys it to Cloud Run.

↓

Cloud Run automatically serves requests and scales based on traffic.

---

## Advantages

* No server management
* Automatic scaling
* Fast deployment
* Cost-effective

---

# 3. Cloud Storage

## Definition

**Cloud Storage** is GCP's object storage service for storing unstructured data.

Examples:

* Images
* Videos
* Documents
* Backups
* Audio files

---

## Example

Shopping Application

Customer uploads a product image.

↓

Image stored in **Cloud Storage**.

↓

Database stores only the image URL.

---

## Storage Classes

* Standard
* Nearline
* Coldline
* Archive

---

## Advantages

* Highly durable
* Secure
* Scalable
* Low-cost storage options

---

# 4. Cloud SQL

## Definition

**Cloud SQL** is GCP's managed relational database service.

Supported databases:

* MySQL
* PostgreSQL
* SQL Server

---

## Features

* Automatic backups
* High availability
* Automatic updates
* Data replication
* Security

---

## Example

Online Banking System

Customer account information

↓

Stored in MySQL database

↓

Hosted using **Cloud SQL**

Google automatically manages:

* Backups
* Maintenance
* Security patches

---

## Advantages

* Easy management
* Reliable
* Secure
* Highly available

---

# 5. Cloud Functions

## Definition

**Cloud Functions** is GCP's **serverless computing** service.

Functions execute automatically when triggered by an event.

---

## Event Examples

* HTTP request
* File upload
* Database change
* Message queue event
* Scheduled task

---

## Example

Customer uploads an image.

↓

Cloud Storage triggers **Cloud Functions**.

↓

Function resizes the image.

↓

Stores the resized image.

---

## Advantages

* No server management
* Event-driven
* Automatic scaling
* Pay only when executed

---

# 6. gcloud CLI

## Definition

**gcloud CLI** is the command-line interface used to manage Google Cloud resources.

Developers use it to:

* Create virtual machines
* Deploy applications
* Manage storage
* Configure projects
* View logs

---

## Common Commands

### Login

```bash
gcloud auth login
```

Logs in to your Google Cloud account.

---

### Set Project

```bash
gcloud config set project my-project
```

Sets the active project.

---

### List Compute Engine Instances

```bash
gcloud compute instances list
```

Displays all VM instances.

---

### Create Compute Engine VM

```bash
gcloud compute instances create my-vm
```

Creates a virtual machine.

---

### List Storage Buckets

```bash
gcloud storage buckets list
```

Displays available Cloud Storage buckets.

---

### Deploy Cloud Run

```bash
gcloud run deploy
```

Deploys an application to Cloud Run.

---

## Advantages

* Automates cloud management
* Supports scripting
* Faster administration
* Easy resource configuration

---

# Complete GCP Example

Suppose a company develops an **Online Food Delivery Application**.

### Step 1

Backend deployed to **Cloud Run**.

### Step 2

Some background services run on **Compute Engine**.

### Step 3

Customer information stored in **Cloud SQL**.

### Step 4

Food images uploaded to **Cloud Storage**.

### Step 5

Image uploads trigger **Cloud Functions**, which resize the images automatically.

### Step 6

Developers use **gcloud CLI** to deploy applications, create virtual machines, and manage cloud resources.

---

# GCP Services Summary

| Service         | Purpose                                            |
| --------------- | -------------------------------------------------- |
| Compute Engine  | Virtual machines for hosting applications          |
| Cloud Run       | Serverless platform for containerized applications |
| Cloud Storage   | Object storage for files and backups               |
| Cloud SQL       | Managed relational database                        |
| Cloud Functions | Serverless event-driven computing                  |
| gcloud CLI      | Command-line tool to manage GCP resources          |

---

# GCP vs AWS vs Azure

| GCP             | AWS                                                | Azure              |
| --------------- | -------------------------------------------------- | ------------------ |
| Compute Engine  | EC2                                                | Virtual Machines   |
| Cloud Run       | Elastic Beanstalk / App Runner (container hosting) | Azure App Service  |
| Cloud Storage   | Amazon S3                                          | Blob Storage       |
| Cloud SQL       | Amazon RDS                                         | Azure SQL Database |
| Cloud Functions | AWS Lambda                                         | Azure Functions    |
| gcloud CLI      | AWS CLI                                            | Azure CLI          |

---

# Advantages of Google Cloud Platform

* Easy deployment
* Global infrastructure
* Automatic scaling
* High security
* Managed services
* Serverless computing support
* Excellent support for containers (Docker, Kubernetes)
* Strong AI and machine learning services

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Google Cloud Platform (GCP)?

**Answer:** Google Cloud Platform is Google's cloud computing platform that provides services such as virtual machines, storage, databases, networking, serverless computing, and monitoring.

---

### 2. What is Compute Engine?

**Answer:** Compute Engine is GCP's Infrastructure as a Service (IaaS) that provides virtual machines for running applications in the cloud.

---

### 3. What is Cloud Run?

**Answer:** Cloud Run is a fully managed serverless platform that runs containerized applications with automatic scaling.

---

### 4. What is Cloud Storage?

**Answer:** Cloud Storage is GCP's object storage service used to store files such as images, videos, documents, and backups.

---

### 5. What is Cloud SQL?

**Answer:** Cloud SQL is a managed relational database service supporting MySQL, PostgreSQL, and SQL Server.

---

### 6. What is Cloud Functions?

**Answer:** Cloud Functions is a serverless service that executes code automatically in response to events like HTTP requests or file uploads.

---

### 7. What is gcloud CLI?

**Answer:** gcloud CLI is the command-line interface used to create, configure, deploy, and manage Google Cloud resources.

---

### 8. Difference between Compute Engine and Cloud Run?

| Compute Engine                     | Cloud Run                                         |
| ---------------------------------- | ------------------------------------------------- |
| Virtual machines                   | Serverless container platform                     |
| User manages VM                    | Google manages infrastructure                     |
| Best for long-running applications | Best for containerized, event-driven applications |
| More configuration options         | Easier deployment and automatic scaling           |

---

# Quick Revision (1-Minute)

| Topic                 | Key Point                                                                                                                                    |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Google Cloud Platform | Google's cloud computing platform                                                                                                            |
| Compute Engine        | Virtual machines (IaaS)                                                                                                                      |
| Cloud Run             | Serverless platform for containers                                                                                                           |
| Cloud Storage         | Object storage for files                                                                                                                     |
| Cloud SQL             | Managed relational database                                                                                                                  |
| Cloud Functions       | Event-driven serverless computing                                                                                                            |
| gcloud CLI            | Command-line tool for GCP management                                                                                                         |
| GCP vs AWS/Azure      | Compute Engine ↔ EC2 ↔ Azure VMs, Cloud Storage ↔ S3 ↔ Blob Storage, Cloud SQL ↔ RDS ↔ Azure SQL, Cloud Functions ↔ Lambda ↔ Azure Functions |

These Google Cloud Platform services are among the most frequently asked cloud computing topics in Cognizant technical assessments, interviews, and entry-level cloud, DevOps, and full-stack development roles.

