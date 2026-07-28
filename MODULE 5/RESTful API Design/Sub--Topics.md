# REST Principles, HTTP Methods & Status Codes, Resource Modelling, Versioning, Pagination, Filtering (with Real Examples)

................................................................................................................................

# 1. REST Principles

## Definition

**REST (Representational State Transfer)** is an architectural style used to design web services. REST APIs follow a set of principles that make them simple, scalable, and efficient.

## REST Principles

### 1. Client–Server

The client and server are separate.

* **Client:** Browser, Mobile App
* **Server:** REST API

### Example

```text
Mobile App
      │
      ▼
 REST API Server
      │
      ▼
   Database
```

**Real-Life Example:**
A food delivery app sends requests to the server to place orders. The mobile app (client) and backend server work independently.

................................................................................................................................

### 2. Stateless

Each request must contain all the information needed to process it.

The server does **not remember previous requests**.

### Example

```http
GET /profile
Authorization: Bearer eyJhbGci...
```

Every request includes the authentication token.

**Real-Life Example:**
An ATM requires your card and PIN for each new session. It does not remember your previous transaction.

................................................................................................................................

### 3. Cacheable

Responses can be stored temporarily (cached) to improve performance.

### Example

```http
GET /products
```

Product data can be cached so users don't need to download the same information repeatedly.

**Real-Life Example:**
An online shopping app stores product images locally so they load faster the next time.

................................................................................................................................

### 4. Uniform Interface

REST APIs should use consistent URL patterns.

Good URLs:

```text
/students
/students/101
/products
/orders
```

Bad URLs:

```text
/getStudent
/createStudent
/deleteStudent
```

**Real-Life Example:**
An e-commerce website consistently uses `/products`, `/customers`, and `/orders`.

................................................................................................................................

### 5. Layered System

A client does not know whether it communicates directly with the server or through intermediaries.

```text
Client
   │
Load Balancer
   │
API Server
   │
Database
```

**Real-Life Example:**
When watching a video on a streaming platform, your request may pass through multiple servers before reaching the main server.

................................................................................................................................

### 6. Code on Demand (Optional)

The server may send executable code (such as JavaScript) to the client.

**Real-Life Example:**
A website sends JavaScript to the browser for form validation.

................................................................................................................................

# 2. HTTP Methods & Status Codes

## HTTP Methods

HTTP methods define the action to perform on a resource.

| Method | Purpose               | Example           |
| ------ | --------------------- | ----------------- |
| GET    | Retrieve data         | View all students |
| POST   | Create new data       | Add a student     |
| PUT    | Replace existing data | Update student    |
| PATCH  | Partially update data | Update email only |
| DELETE | Delete data           | Remove student    |

### Example

```http
GET /students
```

Returns all students.

```http
POST /students
```

Adds a new student.

```http
PUT /students/10
```

Updates student 10.

```http
DELETE /students/10
```

Deletes student 10.

### Real-Life Example

For an online shopping application:

| Method | URL         | Action         |
| ------ | ----------- | -------------- |
| GET    | /products   | View products  |
| POST   | /products   | Add product    |
| PUT    | /products/5 | Update product |
| DELETE | /products/5 | Delete product |

................................................................................................................................

## HTTP Status Codes

Status codes indicate the result of an HTTP request.

### Success (2xx)

| Code | Meaning    |
| ---- | ---------- |
| 200  | OK         |
| 201  | Created    |
| 204  | No Content |

### Client Errors (4xx)

| Code | Meaning      |
| ---- | ------------ |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not Found    |

### Server Errors (5xx)

| Code | Meaning               |
| ---- | --------------------- |
| 500  | Internal Server Error |
| 503  | Service Unavailable   |

### Example

```http
HTTP/1.1 200 OK
```

```http
HTTP/1.1 201 Created
```

```http
HTTP/1.1 404 Not Found
```

**Real-Life Example:**
If a customer searches for a product that doesn't exist, the server returns **404 Not Found**.

................................................................................................................................

# 3. Resource Modelling

## Definition

A **resource** is any object or data that the API manages. Each resource is identified by a unique URL.

### Examples of Resources

* Student
* Product
* Employee
* Order
* Customer

### Resource URLs

```text
/students
/products
/orders
/customers
```

### Individual Resource

```text
/students/101
```

Returns details of the student with ID 101.

### Resource Relationship Example

```text
/customers/5/orders
```

Returns all orders placed by customer 5.

### Real-Life Example

In a Library Management System:

```text
/books
/books/25
/authors
/members
```

Each URL represents a different resource.

### Good Resource Design

```text
/products
/products/20
/orders
/orders/5
```

Avoid:

```text
/getProducts
/deleteOrder
```

Use **nouns**, not verbs.

................................................................................................................................

# 4. Versioning

## Definition

**API Versioning** allows developers to introduce new features without breaking existing applications.

### URL Versioning

```text
/api/v1/students
/api/v2/students
```

### Example

Version 1

```json
{
  "name": "King"
}
```

Version 2

```json
{
  "id": 1,
  "name": "King",
  "email": "king@example.com"
}
```

### Why Versioning?

* Supports old applications
* Adds new features safely
* Prevents compatibility issues

### Real-Life Example

A banking mobile app continues using **v1** while a new app version uses **v2** with additional features.

................................................................................................................................

# 5. Pagination

## Definition

**Pagination** divides a large dataset into smaller pages to improve performance and reduce response size.

### Without Pagination

```text
GET /students
```

Returns 50,000 student records.

### With Pagination

```text
GET /students?page=1&limit=10
```

Returns only the first 10 students.

### Example

```text
Page 1
Student 1
Student 2
...
Student 10

Page 2
Student 11
Student 12
...
Student 20
```

### JSON Response

```json
{
  "page": 1,
  "limit": 10,
  "total": 100,
  "data": [
    {"id":1,"name":"King"},
    {"id":2,"name":"Rahul"}
  ]
}
```

### Real-Life Example

An e-commerce website displays **10 products per page** instead of loading all products at once.

................................................................................................................................

# 6. Filtering

## Definition

**Filtering** allows users to retrieve only the data that matches specific conditions.

### Example URLs

```text
/products?category=Laptop
```

Returns only laptops.

```text
/products?price=500
```

Returns products priced at 500.

```text
/students?department=CSE
```

Returns only CSE students.

### Multiple Filters

```text
/products?category=Laptop&brand=HP
```

Returns only HP laptops.

### JSON Response

```json
[
  {
    "id": 1,
    "name": "HP Laptop",
    "price": 500
  }
]
```

### Real-Life Example

In an online shopping app, customers filter products by:

* Brand
* Price
* Rating
* Color
* Size

instead of viewing every product.

................................................................................................................................

# Summary Table

| Concept            | Purpose                     | Real-Life Example        |
| ------------------ | --------------------------- | ------------------------ |
| REST Principles    | Define REST architecture    | Food delivery app        |
| HTTP Methods       | Perform CRUD operations     | Student management       |
| Status Codes       | Show request results        | 200 OK, 404 Not Found    |
| Resource Modelling | Represent data as resources | `/students`, `/products` |
| Versioning         | Maintain API compatibility  | `/api/v1`, `/api/v2`     |
| Pagination         | Split large data into pages | 10 products per page     |
| Filtering          | Return selected data only   | Filter laptops by brand  |

................................................................................................................................

# Interview / Exam Questions

### 1. What are REST principles?

REST principles are architectural constraints such as Client–Server, Stateless, Cacheable, Uniform Interface, Layered System, and Code on Demand that guide the design of RESTful APIs.

### 2. What are HTTP methods?

HTTP methods are operations used to interact with resources, including **GET, POST, PUT, PATCH, and DELETE**.

### 3. What is resource modelling?

Resource modelling is the process of representing application data as resources identified by unique URLs.

### 4. Why is API versioning important?

API versioning allows new features to be added while keeping older client applications working without changes.

### 5. What is pagination?

Pagination divides large datasets into smaller pages to improve performance and reduce response size.

### 6. What is filtering?

Filtering allows clients to retrieve only the records that match specified conditions, such as category, price, or department.

................................................................................................................................

# Key Points to Remember

* **REST** follows six main principles.
* **HTTP methods** perform CRUD operations.
* **Status codes** indicate the result of requests.
* **Resources** are represented using nouns (e.g., `/students`, `/products`).
* **Versioning** helps maintain backward compatibility.
* **Pagination** improves performance by limiting records returned.
* **Filtering** retrieves only relevant data based on query parameters.

.................................................................................................................................
