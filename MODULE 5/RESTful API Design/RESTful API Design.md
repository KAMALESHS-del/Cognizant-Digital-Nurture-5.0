# RESTful API Design (with Real Examples)

..................................................................

# 1. What is a RESTful API?

## Definition

**REST (Representational State Transfer)** is an architectural style for designing web services that allows different applications to communicate over the internet using the **HTTP protocol**.

A **RESTful API** is an API that follows REST principles and uses HTTP methods such as **GET, POST, PUT, PATCH, and DELETE** to perform operations on resources.

### Exam Definition

> A RESTful API is a web service that follows REST architecture and uses HTTP methods to perform Create, Read, Update, and Delete (CRUD) operations on resources.

### Real-Life Example

Consider an **Online Shopping Application**.

* Mobile App (Client)
* Backend Server (REST API)
* Database

When the customer opens the app:

```text
Customer
     │
     ▼
Mobile App
     │
HTTP Request
     ▼
REST API
     │
Database
     │
HTTP Response
     ▼
Customer
```

..................................................................

# 2. What is a Resource?

A **Resource** is any object or data managed by the API.

Examples:

* Student
* Employee
* Product
* Customer
* Order

### Example URLs

```text
/students
/products
/orders
/users
```

Each URL represents a resource.

### Real-Life Example

In a **College Management System**:

```text
/students
```

represents all students.

```text
/students/101
```

represents the student whose ID is 101.

..................................................................

# 3. HTTP Methods (CRUD Operations)

REST APIs use HTTP methods to perform different operations.

| HTTP Method | CRUD Operation | Description                 | Example                |
| ----------- | -------------- | --------------------------- | ---------------------- |
| GET         | Read           | Retrieve data               | Get all students       |
| POST        | Create         | Add new data                | Add a student          |
| PUT         | Update         | Replace existing data       | Update student details |
| PATCH       | Partial Update | Update only selected fields | Update student email   |
| DELETE      | Delete         | Remove data                 | Delete a student       |

### Example

```text
GET    /students
```

Returns all students.

```text
POST   /students
```

Creates a new student.

```text
PUT    /students/101
```

Updates the student with ID 101.

```text
DELETE /students/101
```

Deletes the student with ID 101.

..................................................................

# 4. HTTP Request and Response

A REST API works through requests and responses.

### Request

```http
GET /students HTTP/1.1
Host: example.com
```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
[
  {
    "id": 101,
    "name": "King"
  }
]
```

### Real-Life Example

A mobile banking app requests the account balance.

```text
Customer
    │
GET /balance
    │
Server
    │
Balance Returned
```

..................................................................

# 5. REST API Architecture

```text
Client (Browser/Mobile App)
            │
            ▼
      HTTP Request
            │
            ▼
      REST API Server
            │
            ▼
        Database
            │
            ▼
      HTTP Response
            │
            ▼
Client
```

### Real-Life Example

Food Delivery App

```text
Customer
      │
      ▼
Order Food
      │
      ▼
REST API
      │
      ▼
Restaurant Database
      │
      ▼
Order Confirmation
```

..................................................................

# 6. REST Constraints (Principles)

REST APIs follow six important principles.

## 1. Client–Server

The client and server are separate.

Example:

* Mobile App = Client
* Backend = Server

### Benefit

Both can be developed independently.

..................................................................

## 2. Stateless

Each request contains all the information needed to process it.

The server does not remember previous requests.

### Example

```text
GET /profile
Authorization: Bearer Token
```

Every request sends the authentication token.

### Real-Life Example

Every ATM transaction requires the card and PIN. The ATM does not remember your previous transaction.

..................................................................

## 3. Cacheable

Responses may be cached to improve performance.

### Example

```text
GET /products
```

Product lists may be cached for faster loading.

..................................................................

## 4. Uniform Interface

The API follows consistent URL naming.

Good examples:

```text
/students
/students/10
/products
/orders
```

Bad examples:

```text
/getStudent
/deleteStudent
/createStudent
```

..................................................................

## 5. Layered System

Clients do not know whether they communicate directly with the server or through proxies, gateways, or load balancers.

```text
Client
   │
Load Balancer
   │
API Server
   │
Database
```

..................................................................

## 6. Code on Demand (Optional)

The server may send executable code such as JavaScript to the client.

This constraint is optional and not used by every REST API.

..................................................................

# 7. URL Design Best Practices

Good REST URLs:

```text
/students
/students/101
/products
/orders
/customers
```

Avoid:

```text
/getStudent
/addStudent
/deleteProduct
```

Use **nouns** instead of verbs.

..................................................................

# 8. HTTP Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 204  | No Content            |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 500  | Internal Server Error |

### Example

Creating a student successfully:

```http
HTTP/1.1 201 Created
```

Deleting successfully:

```http
HTTP/1.1 204 No Content
```

..................................................................

# 9. JSON in REST APIs

REST APIs commonly exchange data in **JSON (JavaScript Object Notation)**.

### Student Example

```json
{
    "id": 101,
    "name": "King",
    "course": "Python"
}
```

### Multiple Students

```json
[
  {
    "id": 101,
    "name": "King"
  },
  {
    "id": 102,
    "name": "Rahul"
  }
]
```

..................................................................

# 10. CRUD Example Using REST API

### Get All Students

```http
GET /students
```

Response

```json
[
  {
    "id":1,
    "name":"King"
  }
]
```

..................................................................

### Get One Student

```http
GET /students/1
```

Response

```json
{
  "id":1,
  "name":"King"
}
```

..................................................................

### Create Student

```http
POST /students
```

Request Body

```json
{
  "name":"King",
  "course":"Python"
}
```

Response

```http
201 Created
```

..................................................................

### Update Student

```http
PUT /students/1
```

Request Body

```json
{
  "name":"King",
  "course":"Java"
}
```

..................................................................

### Delete Student

```http
DELETE /students/1
```

Response

```http
204 No Content
```

..................................................................

# 11. RESTful API Example Using Flask

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/students", methods=["GET"])
def students():
    return jsonify([
        {"id":1, "name":"King"},
        {"id":2, "name":"Rahul"}
    ])

app.run(debug=True)
```

Output

```json
[
  {
    "id":1,
    "name":"King"
  },
  {
    "id":2,
    "name":"Rahul"
  }
]
```

..................................................................

# 12. RESTful API Example Using FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
def get_students():
    return [
        {"id":1, "name":"King"},
        {"id":2, "name":"Rahul"}
    ]
```

Open in browser:

```text
http://127.0.0.1:8000/students
```

Output

```json
[
  {
    "id":1,
    "name":"King"
  },
  {
    "id":2,
    "name":"Rahul"
  }
]
```

..................................................................

# 13. Real-World REST API Examples

### Online Shopping

| HTTP Method | URL            | Action               |
| ----------- | -------------- | -------------------- |
| GET         | `/products`    | View all products    |
| GET         | `/products/10` | View product details |
| POST        | `/products`    | Add a product        |
| PUT         | `/products/10` | Update product       |
| DELETE      | `/products/10` | Remove product       |

..................................................................

### Student Management System

| HTTP Method | URL           | Action                 |
| ----------- | ------------- | ---------------------- |
| GET         | `/students`   | View all students      |
| POST        | `/students`   | Add a student          |
| PUT         | `/students/5` | Update student details |
| DELETE      | `/students/5` | Delete student         |

..................................................................

# Advantages of RESTful APIs

* Simple and easy to understand
* Platform independent
* Uses standard HTTP methods
* Supports JSON and XML
* Scalable and lightweight
* Easy integration with web and mobile applications
* Widely supported by modern frameworks

..................................................................

# Disadvantages of RESTful APIs

* Stateless nature may require sending authentication data with every request
* Not ideal for real-time communication (WebSockets are better for chat/live updates)
* Large responses can increase network usage

..................................................................

# Interview / Exam Questions

### 1. What is a RESTful API?

A RESTful API is a web service that follows REST principles and uses HTTP methods to perform CRUD operations on resources.

### 2. What is a resource in REST?

A resource is any data or object (such as a student, product, or order) that can be accessed through a unique URL.

### 3. Which HTTP methods are commonly used in REST?

**GET, POST, PUT, PATCH, and DELETE.**

### 4. Why is REST called stateless?

Because each request contains all the information required to process it, and the server does not store client session state between requests.

### 5. Why is JSON commonly used in REST APIs?

JSON is lightweight, human-readable, easy to parse, and supported by most programming languages.

..................................................................

# Key Points to Remember

* **REST = Representational State Transfer**
* **RESTful APIs use HTTP methods** for CRUD operations.
* **Resources** are identified using URLs (e.g., `/students`, `/products`).
* **JSON** is the most common data format.
* **Stateless communication** means each request is independent.
* Use **nouns** in URLs (e.g., `/students`) rather than verbs (e.g., `/getStudents`).
* Common status codes: **200, 201, 204, 400, 401, 404, 500**.

