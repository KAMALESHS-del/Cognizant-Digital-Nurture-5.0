

Docker is one of the most popular **containerization platforms** used to package applications and their dependencies into lightweight, portable containers. It ensures that applications run consistently across development, testing, and production environments.

---

# What is Containerization?

## Definition

**Containerization** is the process of packaging an application along with its libraries, dependencies, and configuration files into a **container**.

A container can run consistently on any system that has Docker installed.

---

## Real-Life Example

Suppose you develop a **Java Spring Boot Application**.

Without Docker:

* Your computer has Java 21.
* Another developer has Java 17.
* The application works on your machine but fails on theirs.

With Docker:

The application, Java version, libraries, and dependencies are packaged together.

Result:

**"It works the same everywhere."**

---

# Why Docker?

Without Docker

```text
Developer PC
      │
      ▼
Works Fine
      │
      ▼
Testing Server
      │
      ▼
Missing Dependencies
      │
      ▼
Application Fails
```

With Docker

```text
Docker Image
      │
      ▼
Developer PC
      │
      ▼
Testing Server
      │
      ▼
Production Server
      │
      ▼
Works Everywhere
```

---

# Docker Architecture

```text
Docker Client
      │
docker commands
      │
      ▼
Docker Engine
      │
 ┌───────────────┐
 │ Docker Images │
 └───────────────┘
        │
        ▼
 Docker Containers
```

---

# 1. Docker Concepts

## What is Docker?

**Docker** is an open-source platform used to build, package, distribute, and run applications inside containers.

---

## Key Components

### Docker Engine

Runs and manages containers.

---

### Docker Image

A **read-only template** containing:

* Application code
* Runtime
* Libraries
* Dependencies

Images are used to create containers.

---

### Docker Container

A **running instance of a Docker image**.

Containers are lightweight and isolated.

---

### Docker Registry

Stores Docker images.

Popular registry:

* Docker Hub

---

## Example

Shopping Application

Docker Image

↓

Create Container

↓

Application runs inside the container.

---

# Difference: Image vs Container

| Docker Image               | Docker Container             |
| -------------------------- | ---------------------------- |
| Blueprint/template         | Running instance of an image |
| Read-only                  | Read-write while running     |
| Can create many containers | Executes the application     |

---

# Docker Workflow

```text
Dockerfile
      │
      ▼
Docker Image
      │
      ▼
Docker Container
      │
      ▼
Running Application
```

---

# 2. Dockerfile

## Definition

A **Dockerfile** is a text file containing instructions to build a Docker image.

---

## Basic Dockerfile

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

---

## Explanation

### FROM

Specifies the base image.

```dockerfile
FROM python:3.12
```

---

### WORKDIR

Sets the working directory.

```dockerfile
WORKDIR /app
```

---

### COPY

Copies project files into the image.

```dockerfile
COPY . .
```

---

### RUN

Executes commands during image creation.

```dockerfile
RUN pip install -r requirements.txt
```

---

### CMD

Runs when the container starts.

```dockerfile
CMD ["python","app.py"]
```

---

# Build Docker Image

```bash
docker build -t myapp .
```

---

# Run Docker Container

```bash
docker run myapp
```

---

# 3. Docker Images & Containers

## Create Image

```bash
docker build -t shopping-app .
```

---

## List Images

```bash
docker images
```

---

## Run Container

```bash
docker run shopping-app
```

---

## List Running Containers

```bash
docker ps
```

---

## List All Containers

```bash
docker ps -a
```

---

## Stop Container

```bash
docker stop container-id
```

---

## Remove Container

```bash
docker rm container-id
```

---

## Remove Image

```bash
docker rmi shopping-app
```

---

# Example

Developer creates

```text
Docker Image
```

↓

Runs

```text
3 Containers
```

Container 1

Frontend

Container 2

Backend

Container 3

Database

---

# 4. Docker Compose

## Definition

**Docker Compose** is a tool used to define and run **multiple containers** using a single configuration file (`docker-compose.yml` or `compose.yaml`).

---

## Example

Shopping Application

Needs:

* Frontend
* Backend
* MySQL Database

Instead of starting each container manually,

Docker Compose starts all of them together.

---

## Sample Compose File

```yaml
version: "3.9"

services:
  web:
    build: .
    ports:
      - "8080:8080"

  database:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: password
```

---

## Start Containers

```bash
docker compose up
```

---

## Stop Containers

```bash
docker compose down
```

---

# Docker Compose Architecture

```text
docker-compose.yml
          │
          ▼
---------------------------
| Web Container           |
| Database Container      |
| Redis Container         |
---------------------------
```

---

# 5. Multi-Stage Builds

## Definition

A **Multi-stage Build** uses multiple `FROM` statements in one Dockerfile to create smaller and more secure images.

The first stage builds the application, and the final stage contains only the files needed to run it.

---

## Example

```dockerfile
# Build Stage
FROM maven:3.9 AS builder

WORKDIR /app
COPY . .
RUN mvn package

# Runtime Stage
FROM eclipse-temurin:21-jre

COPY --from=builder /app/target/app.jar app.jar

CMD ["java","-jar","app.jar"]
```

---

## Advantages

* Smaller image size
* Faster deployment
* Better security
* Removes unnecessary build tools

---

## Example Flow

```text
Build Stage
      │
Compile Java
      │
      ▼
Create JAR
      │
      ▼
Runtime Stage
      │
Only Copy JAR
      │
      ▼
Small Docker Image
```

---

# 6. Docker Best Practices

## A. Use Official Base Images

Example

```dockerfile
FROM python:3.12
```

Official images are generally maintained and secure.

---

## B. Keep Images Small

Use lightweight images when possible.

Example

```dockerfile
FROM node:20-alpine
```

Smaller images download faster.

---

## C. Use Multi-stage Builds

Removes unnecessary build dependencies.

---

## D. Use `.dockerignore`

Avoid copying unnecessary files.

Example

```text
.git
node_modules
*.log
```

---

## E. Avoid Running as Root

Create a non-root user when possible to improve security.

---

## F. Cache Layers Efficiently

Copy dependency files first to maximize Docker's build cache.

Example

```dockerfile
COPY package*.json ./
RUN npm install

COPY . .
```

---

## G. Use Environment Variables

Avoid hardcoding values.

Example

```dockerfile
ENV PORT=8080
```

---

## H. Keep One Main Process Per Container

Example

* Web Server → One Container
* Database → Another Container

---

# Complete Docker Example

Suppose a company develops an **Online Food Delivery Application**.

### Step 1

Create a Dockerfile.

### Step 2

Build the image.

```bash
docker build -t food-app .
```

### Step 3

Run the container.

```bash
docker run -p 8080:8080 food-app
```

### Step 4

Create a Docker Compose file.

Services:

* Frontend
* Backend
* MySQL Database

### Step 5

Start all services.

```bash
docker compose up
```

Application is ready to use.

---

# Docker Commands Summary

| Command                 | Purpose                          |
| ----------------------- | -------------------------------- |
| `docker build -t app .` | Build an image                   |
| `docker images`         | List images                      |
| `docker run app`        | Run a container                  |
| `docker ps`             | List running containers          |
| `docker stop <id>`      | Stop a container                 |
| `docker rm <id>`        | Remove a container               |
| `docker rmi app`        | Remove an image                  |
| `docker compose up`     | Start multiple services          |
| `docker compose down`   | Stop and remove Compose services |

---

# Advantages of Docker

* Consistent environments
* Fast deployment
* Lightweight containers
* Efficient resource usage
* Easy scaling
* Simplifies DevOps workflows
* Portable across operating systems
* Works well with Kubernetes and cloud platforms

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Docker?

**Answer:** Docker is a containerization platform that packages applications and their dependencies into portable containers that run consistently across different environments.

---

### 2. What is containerization?

**Answer:** Containerization is the process of packaging an application with all its dependencies so it can run reliably on any system with a container runtime like Docker.

---

### 3. What is a Dockerfile?

**Answer:** A Dockerfile is a text file containing instructions to build a Docker image, such as selecting a base image, copying files, installing dependencies, and defining the startup command.

---

### 4. Difference between Docker Image and Docker Container?

| Docker Image              | Docker Container                   |
| ------------------------- | ---------------------------------- |
| Read-only template        | Running instance of an image       |
| Used to create containers | Executes the application           |
| Immutable                 | Has a writable layer while running |

---

### 5. What is Docker Compose?

**Answer:** Docker Compose is a tool that uses a YAML file to define and run multiple containers together as a single application.

---

### 6. What are Multi-stage Builds?

**Answer:** Multi-stage builds use multiple `FROM` statements in a Dockerfile to separate the build environment from the runtime environment, producing smaller and more secure images.

---

### 7. Name some Docker best practices.

**Answer:**

* Use official base images.
* Keep images small.
* Use multi-stage builds.
* Add a `.dockerignore` file.
* Avoid running containers as the root user.
* Use environment variables for configuration.
* Optimize Docker layer caching.
* Run one main process per container.

---

# Quick Revision (1-Minute)

| Topic             | Key Point                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------- |
| Docker            | Containerization platform                                                                |
| Containerization  | Package app with dependencies                                                            |
| Docker Image      | Read-only template                                                                       |
| Docker Container  | Running instance of an image                                                             |
| Dockerfile        | Instructions to build an image                                                           |
| Docker Compose    | Manage multiple containers with YAML                                                     |
| Multi-stage Build | Smaller, optimized Docker images                                                         |
| Best Practices    | Official images, `.dockerignore`, non-root user, small images, one process per container |

