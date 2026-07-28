# Microservices Architecture (with Real Examples)

....................................................................

# 1. What is Microservices Architecture?

## Definition

**Microservices Architecture** is a software architecture where a large application is divided into **small, independent services**. Each service performs a specific business function and communicates with other services through APIs.

Each microservice can be developed, deployed, updated, and scaled independently.

### Exam Definition

> **Microservices Architecture** is an architectural style in which an application is built as a collection of small, independent services that communicate with each other using APIs.

### Real-Life Example

An **Online Shopping Application** can be divided into several microservices:

```text
Online Shopping System
        │
        ├── User Service
        ├── Product Service
        ├── Order Service
        ├── Payment Service
        └── Delivery Service
```

Each service performs only one specific task.

....................................................................

# 2. Microservices Architecture Diagram

```text
               Client
                  │
                  ▼
            API Gateway
                  │
   ┌──────────────┼──────────────┐
   ▼              ▼              ▼
User Service   Product Service  Order Service
   │              │              │
   ▼              ▼              ▼
User DB      Product DB      Order DB
                  │
                  ▼
          Payment Service
                  │
                  ▼
             Payment DB
```

Each service has its own database and communicates through APIs.

....................................................................

# 3. Characteristics of Microservices

### 1. Independent Services

Each service works independently.

Example:

* Login Service
* Payment Service
* Notification Service

If the Notification Service fails, the Login Service can still work.

..................................................................

### 2. Single Responsibility

Each service performs only one business function.

Example:

```text
Authentication Service → User Login

Payment Service → Payment Processing

Inventory Service → Stock Management
```

..................................................................

### 3. Independent Deployment

Each service can be updated without affecting other services.

### Real-Life Example

A food delivery app updates only the **Payment Service** to support a new payment method without redeploying the whole application.

..................................................................

### 4. Scalability

Each service can be scaled separately.

Example:

During a sale:

```text
Product Service
      ▲
Increase Servers

Payment Service
      ▲
Increase Servers

User Service
      ▲
No Change
```

Only the busy services are scaled.

..................................................................

### 5. Technology Independence

Different services can use different programming languages and databases.

Example:

| Service              | Technology         |
| -------------------- | ------------------ |
| User Service         | Python (Flask)     |
| Product Service      | Java (Spring Boot) |
| Payment Service      | Node.js            |
| Notification Service | Go                 |

....................................................................

# 4. Components of Microservices Architecture

### API Gateway

Acts as the single entry point for all client requests.

Functions:

* Receives requests
* Routes requests
* Authentication
* Rate limiting
* Load balancing

### Example

```text
Client
   │
   ▼
API Gateway
   │
   ├── User Service
   ├── Product Service
   └── Order Service
```

..................................................................

### Service Registry

Keeps track of available microservices.

Example:

```text
User Service
Payment Service
Order Service
Inventory Service
```

..................................................................

### Database

Each microservice has its own database.

Example:

```text
User Service
      │
   User Database

Order Service
      │
  Order Database
```

This prevents tight coupling between services.

....................................................................

# 5. Communication Between Microservices

Microservices communicate using APIs or messaging systems.

### REST API Communication

```text
Order Service
      │
REST API
      │
Payment Service
```

Example:

The Order Service sends payment information to the Payment Service.

..................................................................

### Message Queue Communication

```text
Order Service
      │
Message Queue
      │
Notification Service
```

Example:

After an order is placed, a message is sent to the Notification Service to email the customer.

....................................................................

# 6. Monolithic vs Microservices

| Feature         | Monolithic             | Microservices           |
| --------------- | ---------------------- | ----------------------- |
| Structure       | Single application     | Multiple small services |
| Deployment      | Entire application     | Individual services     |
| Scalability     | Entire application     | Individual services     |
| Maintenance     | Difficult              | Easier                  |
| Fault Isolation | Low                    | High                    |
| Technology      | Usually one technology | Multiple technologies   |

....................................................................

# 7. Real-World Example – Amazon

Amazon uses many microservices.

```text
Amazon
   │
   ├── User Service
   ├── Product Service
   ├── Cart Service
   ├── Order Service
   ├── Payment Service
   ├── Shipping Service
   └── Recommendation Service
```

If the **Recommendation Service** fails, customers can still browse products and place orders.

....................................................................

# 8. Real-World Example – Netflix

Netflix is built using microservices.

```text
Netflix
   │
   ├── User Profile Service
   ├── Movie Catalog Service
   ├── Recommendation Service
   ├── Streaming Service
   └── Billing Service
```

Each service handles a specific responsibility independently.

....................................................................

# 9. Advantages of Microservices

* Easy to develop and maintain
* Independent deployment
* High scalability
* Better fault isolation
* Faster development by multiple teams
* Technology flexibility
* Easier testing of individual services
* Improved reliability

....................................................................

# 10. Disadvantages of Microservices

* More complex architecture
* Difficult service management
* Network communication overhead
* More challenging debugging
* Data consistency can be difficult
* Requires monitoring and orchestration tools

....................................................................

# 11. Microservices Workflow Example

Suppose a customer orders a mobile phone online.

```text
Customer
    │
    ▼
API Gateway
    │
    ▼
Order Service
    │
    ├──► Product Service
    │       │
    │       ▼
    │   Check Stock
    │
    ├──► Payment Service
    │       │
    │       ▼
    │   Process Payment
    │
    └──► Notification Service
            │
            ▼
      Send Confirmation Email
```

Each service performs its own task independently.

....................................................................

# 12. Microservices in Python

Python frameworks commonly used to build microservices:

* **Flask** – Lightweight microservices and REST APIs
* **FastAPI** – High-performance APIs with async support
* **Django** (with Django REST Framework) – Larger REST-based services

Example using Flask:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/product")
def product():
    return jsonify({
        "id": 101,
        "name": "Laptop",
        "price": 800
    })

app.run(debug=True)
```

This service exposes product information and can operate independently from other services.

....................................................................

# Summary Table

| Concept              | Description                        | Example                      |
| -------------------- | ---------------------------------- | ---------------------------- |
| Microservice         | Small independent service          | Payment Service              |
| API Gateway          | Entry point for all requests       | Routes requests to services  |
| Independent Database | Each service owns its data         | User DB, Order DB            |
| REST Communication   | Services communicate via HTTP APIs | Order → Payment              |
| Message Queue        | Asynchronous communication         | Order → Notification         |
| Scalability          | Scale only required services       | Product Service during sales |

....................................................................

# Interview / Exam Questions

### 1. What is Microservices Architecture?

Microservices Architecture is a software design approach in which an application is divided into small, independent services that communicate using APIs.

### 2. What is the main advantage of microservices?

The main advantage is that each service can be developed, deployed, and scaled independently.

### 3. What is an API Gateway?

An API Gateway is the single entry point that receives client requests and routes them to the appropriate microservice.

### 4. How do microservices communicate?

They communicate using REST APIs, gRPC, or message queues such as RabbitMQ or Apache Kafka.

### 5. What is the difference between Monolithic and Microservices Architecture?

A monolithic application is built as one large unit, while a microservices application is divided into multiple small, independent services.

....................................................................

# Key Points to Remember

* **Microservices = Many small independent services.**
* Each service performs **one specific business function**.
* Services communicate through **REST APIs or messaging systems**.
* Each service can have its **own database**.
* **API Gateway** is the entry point for client requests.
* Microservices provide **better scalability, flexibility, and fault isolation** than monolithic architectures.

