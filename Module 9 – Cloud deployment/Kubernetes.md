
**Kubernetes (K8s)** is an open-source **container orchestration platform** used to deploy, manage, scale, and monitor containerized applications. It automates many tasks involved in running applications across multiple servers.

> **Remember:** Docker creates and runs containers, while Kubernetes manages many containers across one or more machines.

---

# What is Kubernetes?

## Definition

**Kubernetes (K8s)** is a platform that:

* Deploys containerized applications
* Automatically scales applications
* Restarts failed containers
* Distributes traffic using load balancing
* Manages application updates

It was originally developed by **Google** and is now maintained by the **Cloud Native Computing Foundation (CNCF)**.

---

## Real-Life Example

Suppose an **Online Shopping Application** has:

* Frontend
* Backend
* MySQL Database

Using Docker:

Each component runs inside a container.

Using Kubernetes:

* Runs all containers
* Restarts failed containers automatically
* Scales the application during high traffic
* Balances user requests

---

# Kubernetes Architecture

```text
                 Users
                   │
                   ▼
               Service
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
      Pod 1                Pod 2
 (Frontend App)      (Frontend App)
        │
        ▼
   Deployment
        │
        ▼
 Kubernetes Cluster
```

---

# Important Kubernetes Components

| Component  | Purpose                      |
| ---------- | ---------------------------- |
| Pod        | Smallest deployable unit     |
| Deployment | Manages Pods                 |
| Service    | Exposes Pods to users        |
| ConfigMap  | Stores configuration         |
| Secret     | Stores sensitive information |
| kubectl    | Command-line management tool |

---

# 1. Pods

## Definition

A **Pod** is the **smallest deployable unit** in Kubernetes.

A Pod usually contains:

* One container
* Shared network
* Shared storage (if required)

---

## Example

Shopping Application

```text
Pod
│
├── Spring Boot Container
```

Sometimes a Pod contains multiple containers.

Example

```text
Pod
│
├── Application Container
└── Logging Container
```

---

## Pod Features

* Smallest Kubernetes object
* Has its own IP address
* Containers inside a Pod communicate easily
* Can be recreated automatically if it fails

---

## Create Pod

```bash
kubectl run nginx --image=nginx
```

---

## View Pods

```bash
kubectl get pods
```

---

# 2. Deployments

## Definition

A **Deployment** manages Pods automatically.

It ensures:

* Desired number of Pods
* Automatic restart
* Rolling updates
* Rollback support

---

## Example

Requirement:

Always run **3 application Pods**.

Deployment automatically creates:

```text
Deployment
     │
     ▼
 ┌────┬────┬────┐
 ▼    ▼    ▼
Pod1 Pod2 Pod3
```

If Pod2 crashes:

```text
Pod2 ❌

Deployment

↓

Creates New Pod2 ✔
```

---

## Deployment Benefits

* High availability
* Auto healing
* Easy updates
* Easy rollback

---

## Create Deployment

```bash
kubectl create deployment myapp --image=nginx
```

---

## Scale Deployment

```bash
kubectl scale deployment myapp --replicas=5
```

Now Kubernetes runs **5 Pods**.

---

# 3. Services

## Definition

A **Service** provides a **stable network endpoint** for accessing Pods.

Since Pod IP addresses can change, a Service provides a consistent way to reach them.

---

## Example

Without Service

```text
User

↓

Pod IP Changes

↓

Application Breaks
```

With Service

```text
User

↓

Service

↓

Pod1
Pod2
Pod3
```

Users connect to the Service, not directly to Pods.

---

## Types of Services

### ClusterIP

Accessible only inside the cluster.

---

### NodePort

Accessible using the node's IP and a port.

---

### LoadBalancer

Accessible from the internet using a cloud load balancer.

---

## Benefits

* Load balancing
* Stable access
* High availability

---

# 4. ConfigMaps

## Definition

A **ConfigMap** stores **non-sensitive configuration data** separately from application code.

Examples:

* Database host
* Application mode
* API URL

---

## Example

Instead of hardcoding:

```text
DB_HOST = mysql.company.com
```

Store it inside a ConfigMap.

Application reads it at runtime.

---

## Benefits

* Easy configuration updates
* Environment-specific settings
* No code changes required

---

# 5. Secrets

## Definition

A **Secret** stores **sensitive information** securely.

Examples:

* Passwords
* API Keys
* Database credentials
* Tokens

---

## Example

Store:

```text
Database Password

MyPassword123
```

Inside a Secret instead of the application code.

Application retrieves it securely.

---

## Difference: ConfigMap vs Secret

| ConfigMap                   | Secret                |
| --------------------------- | --------------------- |
| Non-sensitive configuration | Sensitive information |
| API URL                     | Password              |
| Database Host               | API Token             |
| Port Number                 | Secret Key            |

---

# 6. kubectl Basics

## Definition

**kubectl** is the command-line tool used to interact with Kubernetes clusters.

---

## Common Commands

### View Cluster

```bash
kubectl cluster-info
```

---

### View Nodes

```bash
kubectl get nodes
```

---

### View Pods

```bash
kubectl get pods
```

---

### View Deployments

```bash
kubectl get deployments
```

---

### Create Deployment

```bash
kubectl create deployment myapp --image=nginx
```

---

### Scale Deployment

```bash
kubectl scale deployment myapp --replicas=4
```

---

### Delete Pod

```bash
kubectl delete pod pod-name
```

---

### Describe Pod

```bash
kubectl describe pod pod-name
```

Displays:

* Events
* Status
* Configuration
* Errors

---

# 7. Managed Kubernetes Services

Cloud providers offer managed Kubernetes services, where they handle the control plane, upgrades, and maintenance.

---

## Amazon EKS (Elastic Kubernetes Service)

AWS-managed Kubernetes service.

Features:

* Automatic control plane management
* AWS integration
* High availability

---

## Azure AKS (Azure Kubernetes Service)

Microsoft Azure's managed Kubernetes service.

Features:

* Easy deployment
* Azure integration
* Automatic upgrades

---

## Google GKE (Google Kubernetes Engine)

Google Cloud's managed Kubernetes service.

Features:

* High performance
* Automatic scaling
* Google-managed infrastructure

---

## Comparison

| Service | Cloud Provider        |
| ------- | --------------------- |
| EKS     | Amazon Web Services   |
| AKS     | Microsoft Azure       |
| GKE     | Google Cloud Platform |

---

# Kubernetes Workflow

```text
Developer
     │
     ▼
Docker Image
     │
     ▼
Deployment
     │
     ▼
Pods
     │
     ▼
Service
     │
     ▼
Users
```

---

# Complete Example

Suppose a company develops an **Online Food Delivery Application**.

### Step 1

Create a Docker image.

↓

### Step 2

Push the image to a container registry.

↓

### Step 3

Create a Kubernetes Deployment with **3 Pods**.

↓

### Step 4

Create a **LoadBalancer Service**.

↓

### Step 5

Users access the application through the Service.

↓

### Step 6

If one Pod crashes:

Kubernetes automatically creates a replacement Pod.

↓

### Step 7

Database password is stored in a **Secret**.

API URL is stored in a **ConfigMap**.

---

# Kubernetes Objects Summary

| Object     | Purpose                                   |
| ---------- | ----------------------------------------- |
| Pod        | Runs one or more containers               |
| Deployment | Manages Pods and replicas                 |
| Service    | Provides stable access and load balancing |
| ConfigMap  | Stores configuration settings             |
| Secret     | Stores sensitive data                     |
| kubectl    | Command-line management tool              |

---

# Advantages of Kubernetes

* Automatic scaling
* Self-healing (restarts failed Pods)
* Load balancing
* Rolling updates
* Easy rollback
* High availability
* Efficient resource utilization
* Cloud portability

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Kubernetes?

**Answer:** Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.

---

### 2. What is a Pod?

**Answer:** A Pod is the smallest deployable unit in Kubernetes and usually contains one or more closely related containers that share networking and storage.

---

### 3. What is a Deployment?

**Answer:** A Deployment manages Pods by maintaining the desired number of replicas, performing rolling updates, and automatically replacing failed Pods.

---

### 4. What is a Service?

**Answer:** A Service provides a stable network endpoint for accessing Pods and distributes traffic among them.

---

### 5. Difference between ConfigMap and Secret?

| ConfigMap                          | Secret                       |
| ---------------------------------- | ---------------------------- |
| Stores non-sensitive configuration | Stores sensitive information |
| Example: API URL                   | Example: Password or API key |

---

### 6. What is `kubectl`?

**Answer:** `kubectl` is the command-line tool used to create, manage, inspect, and troubleshoot Kubernetes resources.

---

### 7. What are EKS, AKS, and GKE?

**Answer:**

* **EKS** – Amazon Elastic Kubernetes Service (AWS)
* **AKS** – Azure Kubernetes Service (Microsoft Azure)
* **GKE** – Google Kubernetes Engine (Google Cloud)

These are managed Kubernetes services that simplify cluster management.

---

### 8. Difference between Docker and Kubernetes?

| Docker                      | Kubernetes                                  |
| --------------------------- | ------------------------------------------- |
| Creates and runs containers | Manages and orchestrates containers         |
| Runs on a single host       | Can manage containers across multiple hosts |
| Containerization platform   | Container orchestration platform            |

---

# Quick Revision (1-Minute)

| Topic                | Key Point                                       |
| -------------------- | ----------------------------------------------- |
| Kubernetes           | Container orchestration platform                |
| Pod                  | Smallest deployable unit                        |
| Deployment           | Manages Pods and replicas                       |
| Service              | Stable network access and load balancing        |
| ConfigMap            | Stores non-sensitive configuration              |
| Secret               | Stores passwords, tokens, and keys securely     |
| `kubectl`            | Command-line tool for Kubernetes                |
| EKS                  | Managed Kubernetes on AWS                       |
| AKS                  | Managed Kubernetes on Azure                     |
| GKE                  | Managed Kubernetes on Google Cloud              |
| Docker vs Kubernetes | Docker runs containers; Kubernetes manages them |
