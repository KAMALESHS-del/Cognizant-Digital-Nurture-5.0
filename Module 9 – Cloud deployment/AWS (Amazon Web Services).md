# Module: AWS (Amazon Web Services) – Cognizant Technical Assessment

AWS (Amazon Web Services) is the **world's largest cloud computing platform**, offering services for computing, storage, databases, networking, security, monitoring, and serverless computing. AWS is widely used in software companies, including Cognizant projects.

---

# What is AWS?

## Definition

**AWS (Amazon Web Services)** is a cloud computing platform that provides on-demand IT resources such as:

* Virtual Servers
* Storage
* Databases
* Networking
* Security
* Monitoring
* Serverless Computing

Users pay only for the services they use (**Pay-as-you-go**).

---

## Real-Life Example

Suppose a company develops an **Online Shopping Application**.

Instead of buying physical servers, the company uses AWS:

* **EC2** → Runs the application
* **S3** → Stores product images
* **RDS** → Stores customer data
* **IAM** → Controls user permissions
* **CloudWatch** → Monitors application health
* **Lambda** → Executes background tasks
* **Elastic Beanstalk** → Deploys the application easily

---

# AWS Architecture Example

```text
                 Users
                   │
                   ▼
           Elastic Beanstalk
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
       EC2                 Lambda
         │
         ▼
        RDS
         │
         ▼
        S3
         │
         ▼
    CloudWatch (Monitoring)

IAM controls access to all services.
```

---

# 1. Amazon EC2 (Elastic Compute Cloud)

## Definition

**EC2** provides **virtual servers** (called instances) in the cloud.

It allows developers to run applications without owning physical hardware.

---

## Features

* Virtual Machines
* Multiple Operating Systems
* Auto Scaling
* High Availability
* Pay-as-you-go

---

## Example

A company launches a website.

Instead of purchasing a server,

they create an EC2 instance.

The website runs on that virtual server.

---

## Common Uses

* Host websites
* Run backend APIs
* Application servers
* Development environments

---

## Benefits

* Scalable
* Reliable
* Easy to launch
* Flexible configurations

---

# 2. Amazon S3 (Simple Storage Service)

## Definition

**S3** is an object storage service used to store files.

Examples:

* Images
* Videos
* Documents
* Backups
* Logs

---

## Example

Shopping App

Customer uploads a profile picture.

↓

Image stored in S3.

↓

Database stores only the image URL.

---

## Features

* Unlimited storage
* High durability
* Secure
* Versioning
* Backup support

---

## Common Uses

* Image hosting
* Video storage
* Backup
* Static website hosting

---

# 3. Amazon RDS (Relational Database Service)

## Definition

**RDS** is a managed relational database service.

Supported databases include:

* MySQL
* PostgreSQL
* MariaDB
* Oracle
* SQL Server

---

## Example

Online Banking Application

Customer information

↓

Stored in MySQL database

↓

Hosted on Amazon RDS

AWS automatically manages:

* Backups
* Updates
* Security
* Scaling

---

## Advantages

* Automatic backup
* Easy scaling
* High availability
* Reduced administration

---

# 4. IAM (Identity and Access Management)

## Definition

IAM controls **who can access AWS resources** and **what actions they can perform**.

---

## Components

### Users

Individual accounts.

Example:

Developer

---

### Groups

Collection of users.

Example:

Developers Group

---

### Roles

Temporary permissions assigned to AWS services or applications.

Example:

EC2 accesses S3 using an IAM Role.

---

### Policies

Documents defining permissions.

Example

Allow

* Read S3

Deny

* Delete S3 Bucket

---

## Example

Developer

↓

Allowed

* Launch EC2

Not Allowed

* Delete RDS Database

---

## Benefits

* Security
* Fine-grained access control
* Least privilege principle
* Multi-factor authentication (MFA) support

---

# 5. Elastic Beanstalk

## Definition

Elastic Beanstalk is a **Platform as a Service (PaaS)** that simplifies application deployment.

Developers upload code.

AWS automatically handles:

* EC2
* Load Balancer
* Auto Scaling
* Monitoring
* Deployment

---

## Example

Developer uploads Java application.

↓

Elastic Beanstalk creates

* EC2
* Load Balancer
* Auto Scaling

Application becomes available.

---

## Supported Languages

* Java
* Python
* Node.js
* .NET
* PHP
* Go
* Ruby

---

## Advantages

* Easy deployment
* Automatic scaling
* No infrastructure management

---

# 6. AWS Lambda (Serverless Computing)

## Definition

Lambda allows you to run code **without managing servers**.

Code executes only when an event occurs.

---

## Serverless Meaning

Developers write only the code.

AWS manages:

* Servers
* Scaling
* Infrastructure

---

## Example

Customer uploads an image.

↓

S3 triggers Lambda.

↓

Lambda resizes image.

↓

Stores resized version.

---

## Common Uses

* Image processing
* API backend
* Notifications
* File conversion
* Scheduled tasks

---

## Benefits

* No server management
* Automatic scaling
* Pay only for execution time

---

# 7. Amazon CloudWatch

## Definition

CloudWatch monitors AWS resources and applications.

It collects:

* CPU usage
* Memory usage (with additional configuration)
* Disk activity
* Logs
* Errors
* Network traffic

---

## Example

CPU reaches 90%.

↓

CloudWatch Alarm triggers.

↓

Administrator receives notification.

---

## Features

* Monitoring
* Metrics
* Dashboards
* Logs
* Alarms

---

## Benefits

* Early issue detection
* Performance monitoring
* Automatic alerts

---

# 8. AWS CLI (Command Line Interface)

## Definition

AWS CLI is a command-line tool used to manage AWS services directly from the terminal.

---

## Example Commands

### Configure AWS

```bash
aws configure
```

Enter:

* Access Key
* Secret Key
* Region
* Output Format

---

### List S3 Buckets

```bash
aws s3 ls
```

---

### Create S3 Bucket

```bash
aws s3 mb s3://my-bucket
```

---

### Upload File

```bash
aws s3 cp image.jpg s3://my-bucket
```

---

### Launch EC2 Instance

```bash
aws ec2 run-instances
```

---

## Advantages

* Automation
* Faster administration
* Script support
* Easy resource management

---

# Complete AWS Example

Suppose a company develops an **Online Food Delivery Application**.

### Step 1

Frontend and backend deployed using **Elastic Beanstalk**.

### Step 2

Application runs on **EC2**.

### Step 3

Customer data stored in **Amazon RDS (MySQL)**.

### Step 4

Food images stored in **Amazon S3**.

### Step 5

When a new image is uploaded,

**Lambda** automatically compresses it.

### Step 6

**CloudWatch** monitors CPU usage and application logs.

### Step 7

**IAM** ensures only authorized users can access AWS resources.

### Step 8

Developers use **AWS CLI** to upload files, deploy applications, and manage resources.

---

# AWS Services Summary

| Service           | Purpose                                               |
| ----------------- | ----------------------------------------------------- |
| EC2               | Virtual server for hosting applications               |
| S3                | Object storage for files, images, videos, and backups |
| RDS               | Managed relational database service                   |
| IAM               | Identity and access management for AWS resources      |
| Elastic Beanstalk | Easy application deployment and management            |
| Lambda            | Serverless code execution triggered by events         |
| CloudWatch        | Monitoring, logging, metrics, and alarms              |
| AWS CLI           | Command-line tool for managing AWS services           |

---

# Advantages of AWS

* Highly scalable
* Reliable and highly available
* Secure with IAM and encryption
* Pay-as-you-go pricing
* Global infrastructure
* Automatic scaling
* Managed services reduce operational effort
* Easy integration with DevOps and CI/CD

---

# Cognizant Technical Assessment – Important Questions

### 1. What is AWS?

**Answer:** AWS (Amazon Web Services) is a cloud computing platform that provides on-demand services such as computing, storage, databases, networking, monitoring, and security.

---

### 2. What is Amazon EC2?

**Answer:** Amazon EC2 provides virtual servers (instances) that allow users to run applications in the cloud without owning physical hardware.

---

### 3. What is Amazon S3?

**Answer:** Amazon S3 is an object storage service used to store and retrieve files such as images, videos, documents, and backups.

---

### 4. What is Amazon RDS?

**Answer:** Amazon RDS is a managed relational database service that supports databases like MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB.

---

### 5. What is IAM?

**Answer:** IAM (Identity and Access Management) controls who can access AWS resources and what actions they are permitted to perform using users, groups, roles, and policies.

---

### 6. What is Elastic Beanstalk?

**Answer:** Elastic Beanstalk is a Platform as a Service (PaaS) that simplifies application deployment by automatically managing infrastructure such as EC2 instances, load balancers, and scaling.

---

### 7. What is AWS Lambda?

**Answer:** AWS Lambda is a serverless computing service that runs code automatically in response to events without requiring server management.

---

### 8. What is Amazon CloudWatch?

**Answer:** Amazon CloudWatch is a monitoring service that collects metrics, logs, and events, and can trigger alarms when predefined conditions are met.

---

### 9. What is AWS CLI?

**Answer:** AWS CLI is a command-line interface that allows users to manage AWS services through terminal commands.

---

# Quick Revision (1-Minute)

| Topic             | Key Point                                 |
| ----------------- | ----------------------------------------- |
| AWS               | Cloud computing platform                  |
| EC2               | Virtual servers (instances)               |
| S3                | Object storage for files                  |
| RDS               | Managed relational database               |
| IAM               | User and permission management            |
| Elastic Beanstalk | Easy application deployment (PaaS)        |
| Lambda            | Serverless event-driven computing         |
| CloudWatch        | Monitoring, logs, and alarms              |
| AWS CLI           | Command-line tool to manage AWS resources |


