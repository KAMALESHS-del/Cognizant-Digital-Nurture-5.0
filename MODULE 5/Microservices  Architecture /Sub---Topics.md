# Monolith vs Microservices, Service Decomposition, Inter-service Communication, API Gateway, Service Discovery (with Real Examples)

....................................................................

# 1. Monolith vs Microservices

## Monolithic Architecture

### Definition

A **Monolithic Architecture** is a software architecture where the entire application is built as a **single, unified application**. All modules such as user management, products, orders, and payments are part of one codebase and are deployed together.

### Architecture

```text
                Client
                   │
                   ▼
        Monolithic Application
   ┌────────────────────────────┐
   │ User Module                │
   │ Product Module             │
   │ Order Module               │
   │ Payment Module             │
   └────────────────────────────┘
                   │
                   ▼
             Single Database
```

### Real-Life Example

A **College Management System** where student management, attendance, fees, exams, and reports are all contained in one application.

### Advantages

* Easy to develop initially
* Simple deployment
* Easy communication between modules
* Suitable for small projects

### Disadvantages

* Difficult to scale
* Large codebase
* One failure may affect the whole application
* Entire application must be redeployed for small changes

....................................................................

## Microservices Architecture

### Definition

A **Microservices Architecture** divides a large application into **small, independent services**, where each service performs a specific business function and communicates using APIs.

### Architecture

```text
                 Client
                    │
                    ▼
              API Gateway
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
 User Service  Product Service  Order Service
      │             │             │
      ▼             ▼             ▼
 User DB      Product DB      Order DB
```

### Real-Life Example

An **Online Shopping Website** where login, products, orders, payments, and notifications are separate services.

### Advantages

* Independent deployment
* Better scalability
* Easier maintenance
* Fault isolation
* Different technologies can be used

### Disadvantages

* More complex architecture
* Network communication overhead
* Difficult debugging
* More infrastructure required

....................................................................

## Comparison Table

| Feature        | Monolithic           | Microservices                      |
| -------------- | -------------------- | ---------------------------------- |
| Structure      | Single application   | Multiple independent services      |
| Deployment     | Entire application   | Individual services                |
| Database       | Single database      | Separate database for each service |
| Scalability    | Entire application   | Individual services                |
| Maintenance    | Difficult            | Easier                             |
| Failure Impact | Whole application    | Only affected service              |
| Technology     | Usually one language | Multiple languages/frameworks      |

....................................................................

# 2. Service Decomposition

## Definition

**Service Decomposition** is the process of breaking a large application into **small, independent services**, where each service handles a single business function.

### Example

Suppose an Online Shopping System initially has:

```text
Shopping System
│
├── Login
├── Products
├── Orders
├── Payment
├── Delivery
├── Notifications
```

After decomposition:

```text
User Service

Product Service

Order Service

Payment Service

Delivery Service

Notification Service
```

Each service has its own:

* Business logic
* Database
* API

### Real-Life Example

A **Hospital Management System** can be divided into:

```text
Patient Service

Doctor Service

Appointment Service

Billing Service

Pharmacy Service

Laboratory Service
```

Each team develops and maintains its own service independently.

### Benefits

* Easier maintenance
* Independent deployment
* Better scalability
* Faster development
* Better fault isolation

....................................................................

# 3. Inter-service Communication

## Definition

**Inter-service Communication** is the process by which different microservices exchange information with each other.

There are two common communication methods.

....................................................................

## A. Synchronous Communication (REST API)

Services communicate directly using HTTP requests.

### Architecture

```text
Order Service
      │
 REST API Request
      │
      ▼
Payment Service
      │
 REST API Response
      │
      ▼
Order Service
```

### Real-Life Example

When a customer places an order:

1. Order Service sends payment details.
2. Payment Service processes the payment.
3. Payment Service returns success or failure.

....................................................................

## B. Asynchronous Communication (Message Queue)

Services communicate using a message broker.

### Architecture

```text
Order Service
      │
      ▼
Message Queue
      │
      ▼
Notification Service
```

Popular message brokers:

* RabbitMQ
* Apache Kafka
* Amazon SQS

### Real-Life Example

After payment succeeds:

* Order Service sends a message.
* Notification Service receives it.
* Customer receives an email or SMS.

The Order Service does not wait for the notification to finish.

....................................................................

## Comparison

| Feature       | REST API       | Message Queue             |
| ------------- | -------------- | ------------------------- |
| Communication | Direct         | Through broker            |
| Response      | Immediate      | Delayed (asynchronous)    |
| Best For      | Login, Payment | Email, Notifications      |
| Speed         | Fast           | Good for background tasks |

....................................................................

# 4. API Gateway

## Definition

An **API Gateway** is the **single entry point** for all client requests in a microservices architecture.

Instead of clients communicating with each service directly, they communicate with the API Gateway.

### Architecture

```text
                Client
                   │
                   ▼
             API Gateway
      ┌────────┼────────┐
      ▼        ▼        ▼
User Service Product Service Order Service
```

### Functions of API Gateway

* Request routing
* Authentication
* Authorization
* Load balancing
* Rate limiting
* Logging
* Request aggregation

### Real-Life Example

A mobile shopping app requests:

```text
Home Page
```

The API Gateway collects data from:

* User Service
* Product Service
* Offer Service

and sends a single response to the app.

### Advantages

* Simplifies client communication
* Improves security
* Reduces client complexity
* Centralized request handling

....................................................................

# 5. Service Discovery

## Definition

**Service Discovery** is a mechanism that helps microservices find and communicate with each other automatically, even if service locations or IP addresses change.

Instead of hardcoding addresses, services register themselves with a **Service Registry**.

### Architecture

```text
            Service Registry
           (Service Discovery)
          ┌────────┼────────┐
          ▼        ▼        ▼
     User     Product    Payment
    Service    Service    Service

             ▲
             │
       Order Service
```

The Order Service asks the Service Registry where the Payment Service is located before sending a request.

....................................................................

## How Service Discovery Works

### Step 1

A service starts.

```text
Payment Service Started
```

..................................................................

### Step 2

It registers itself.

```text
Payment Service

IP: 192.168.1.10

Port: 8000
```

..................................................................

### Step 3

Another service wants to communicate.

```text
Order Service

↓

Ask Registry

↓

Where is Payment Service?
```

..................................................................

### Step 4

Registry returns the address.

```text
192.168.1.10:8000
```

Order Service sends the request successfully.

....................................................................

## Popular Service Discovery Tools

* Netflix Eureka
* Consul
* Apache ZooKeeper
* Kubernetes Service Discovery

....................................................................

## Real-Life Example

Imagine a hotel reception.

Instead of remembering every room number, guests ask the receptionist where a room is located.

```text
Guest

↓

Reception

↓

Room Number
```

The **Reception** acts like the **Service Registry**, helping guests find the correct room.

....................................................................

# Summary Table

| Concept                     | Purpose                                 | Real-Life Example                      |
| --------------------------- | --------------------------------------- | -------------------------------------- |
| Monolithic Architecture     | Single application with all modules     | College Management System              |
| Microservices Architecture  | Independent services                    | Amazon, Netflix                        |
| Service Decomposition       | Split application into smaller services | Hospital Management System             |
| Inter-service Communication | Services exchange information           | Order Service ↔ Payment Service        |
| API Gateway                 | Single entry point for requests         | Mobile shopping app                    |
| Service Discovery           | Finds service locations automatically   | Order Service locating Payment Service |

....................................................................

# Interview / Exam Questions

### 1. What is the difference between Monolithic and Microservices Architecture?

A monolithic application is built as one large application, whereas a microservices application is divided into multiple small, independent services that communicate through APIs.

### 2. What is Service Decomposition?

Service decomposition is the process of breaking a large application into smaller, independent services based on business functions.

### 3. How do microservices communicate?

Microservices communicate using synchronous methods (REST APIs, gRPC) or asynchronous methods (message queues such as RabbitMQ or Kafka).

### 4. What is an API Gateway?

An API Gateway is the single entry point for client requests. It routes requests to the appropriate microservices and provides features such as authentication, load balancing, and rate limiting.

### 5. What is Service Discovery?

Service Discovery is a mechanism that allows services to register themselves and enables other services to locate them dynamically through a service registry.

....................................................................

# Key Points to Remember

* **Monolithic Architecture** = One large application.
* **Microservices Architecture** = Many small, independent services.
* **Service Decomposition** splits a large application into business-focused services.
* **Inter-service Communication** can be synchronous (REST/gRPC) or asynchronous (message queues).
* **API Gateway** is the single entry point for all client requests.
* **Service Discovery** automatically locates services without hardcoding their addresses.

