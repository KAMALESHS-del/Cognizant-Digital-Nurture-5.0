# Web Framework Foundations

Web frameworks provide the basic structure and tools required to build **websites, web applications, and backend services** efficiently.

Instead of writing everything from scratch, developers use frameworks that provide features such as **URL routing, request handling, database connectivity, authentication, and API development**.

---

## 1. What is a Web Framework?

A **web framework** is a software framework that helps developers build web applications using predefined tools, libraries, and structures.

### Without a Framework

```text
Client
  ↓
Server
  ↓
Manually handle:
- URL
- Request
- Database
- Authentication
- Response
```

### With a Framework

```text
Client
  ↓
Web Framework
  ↓
Routing
  ↓
Business Logic
  ↓
Database
  ↓
Response
```

### Example

When a user visits:

```text
https://example.com/products
```

The framework:

1. Receives the request.
2. Identifies the URL.
3. Calls the appropriate function.
4. Fetches data from the database.
5. Sends a response to the user.

---

# 2. Client–Server Architecture

Most web applications follow the **Client–Server Model**.

### Client

The client is usually:

* Web browser
* Mobile application
* Desktop application

Examples:

```text
Google Chrome
Firefox
Mobile App
```

### Server

The server:

* Receives requests
* Processes business logic
* Communicates with databases
* Sends responses

### Architecture

```text
        Request
Client ─────────────► Server
  ▲                    │
  │                    │
  └────── Response ────┘
                       │
                       ▼
                   Database
```

### Example

A user logs into an application:

```text
1. User enters username and password
2. Client sends login request
3. Server validates the credentials
4. Server checks the database
5. Server sends success/failure response
```

---

# 3. HTTP Fundamentals

**HTTP (HyperText Transfer Protocol)** is used for communication between clients and web servers.

### Request

The client sends a request:

```text
Client ───────► Server
```

### Response

The server sends a response:

```text
Server ───────► Client
```

---

## HTTP Request Structure

```text
GET /users HTTP/1.1
Host: example.com
```

A request contains:

* HTTP method
* URL
* Headers
* Body

---

## HTTP Response Structure

```text
HTTP/1.1 200 OK
Content-Type: application/json
```

A response contains:

* Status code
* Headers
* Response body

---

# 4. HTTP Methods

HTTP methods define the operation that should be performed.

| Method | Purpose              |
| ------ | -------------------- |
| GET    | Retrieve data        |
| POST   | Create new data      |
| PUT    | Update complete data |
| PATCH  | Update partial data  |
| DELETE | Delete data          |

### Example

```text
GET     /users       → Get all users
POST    /users       → Create a user
PUT     /users/1    → Update user
DELETE  /users/1    → Delete user
```

---

# 5. HTTP Status Codes

Status codes indicate the result of a request.

### 2xx – Success

```text
200 OK
201 Created
204 No Content
```

### 3xx – Redirection

```text
301 Moved Permanently
302 Found
```

### 4xx – Client Error

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
```

### 5xx – Server Error

```text
500 Internal Server Error
503 Service Unavailable
```

---

# 6. Routing

**Routing** maps a URL to a specific function.

### Example

```text
URL: /home
        ↓
home() function
```

### Flask Example

```python
from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "Welcome to Home Page"
```

When the user visits:

```text
http://localhost:5000/home
```

The `home()` function is executed.

---

# 7. Request and Response

A web framework processes a request and returns a response.

### Request

```text
GET /products
```

### Processing

```text
Server:
1. Receive request
2. Process logic
3. Access database
4. Prepare response
```

### Response

```json
{
    "product": "Laptop",
    "price": 800
}
```

---

# 8. Middleware

**Middleware** is software that processes requests and responses before they reach the main application logic.

### Flow

```text
Request
   ↓
Middleware
   ↓
Application
   ↓
Middleware
   ↓
Response
```

### Common Uses

* Authentication
* Logging
* Error handling
* CORS
* Security
* Request processing

### Example

```text
User Request
     ↓
Authentication Middleware
     ↓
Check Login
     ↓
Application
```

---

# 9. Templates

Templates are used to generate dynamic HTML pages.

### Example

```html
<h1>Welcome, {{ name }}</h1>
```

If:

```text
name = "King"
```

The output becomes:

```text
Welcome, King
```

Frameworks commonly use template engines such as:

* Django Templates
* Jinja2

---

# 10. Database Integration

Web applications often need databases to store data.

### Example

```text
User Registration
        ↓
Web Framework
        ↓
Database
        ↓
User Information Stored
```

### Common Databases

* MySQL
* PostgreSQL
* SQLite
* MongoDB

### Example Data

```text
User ID: 101
Name: John
Email: john@example.com
```

---

# 11. APIs

An **API (Application Programming Interface)** allows different applications to communicate with each other.

### Example

```text
Mobile App
    │
    ▼
   API
    │
    ▼
Backend Server
    │
    ▼
Database
```

### Example API Response

```json
{
    "id": 1,
    "name": "John",
    "email": "john@example.com"
}
```

Python frameworks commonly used for APIs:

* Django REST Framework
* Flask
* FastAPI

---

# 12. MVC and MVT Architecture

## MVC

MVC stands for:

* **Model** – Data and database
* **View** – User interface
* **Controller** – Application logic

```text
User
 ↓
Controller
 ↓
Model
 ↓
Database
```

---

## Django MVT

Django uses **MVT**:

* **Model** – Database structure
* **View** – Business logic
* **Template** – User interface

```text
User
 ↓
URL
 ↓
View
 ↓
Model
 ↓
Database
```

The result is then sent to the:

```text
Template
```

---

# 13. Authentication and Authorization

### Authentication

Authentication answers:

> **Who are you?**

Example:

```text
Username + Password
```

### Authorization

Authorization answers:

> **What are you allowed to do?**

Example:

```text
Admin → Delete Users
User  → View Profile
```

### Authentication Flow

```text
User
 ↓
Login
 ↓
Server
 ↓
Validate Credentials
 ↓
Database
 ↓
Access Granted / Denied
```

---

# 14. Sessions and Cookies

### Cookie

A cookie stores small pieces of information in the user's browser.

Example:

```text
user_id = 101
```

### Session

A session stores user information during a browsing session.

Example:

```text
Login
  ↓
Session Created
  ↓
User Accesses Pages
  ↓
Logout
  ↓
Session Destroyed
```

---

# 15. REST API Fundamentals

REST stands for **Representational State Transfer**.

A REST API uses HTTP methods to perform operations.

### Example: Student API

| Operation       | Method | URL           |
| --------------- | ------ | ------------- |
| Get students    | GET    | `/students`   |
| Get one student | GET    | `/students/1` |
| Add student     | POST   | `/students`   |
| Update student  | PUT    | `/students/1` |
| Delete student  | DELETE | `/students/1` |

---

# 16. Django, Flask, and FastAPI

| Framework | Main Purpose                 |
| --------- | ---------------------------- |
| Django    | Complete web applications    |
| Flask     | Lightweight web applications |
| FastAPI   | High-performance APIs        |

### Django

```text
Large Web Applications
        ↓
     Django
```

### Flask

```text
Small and Flexible Applications
        ↓
      Flask
```

### FastAPI

```text
Fast REST APIs and Microservices
        ↓
     FastAPI
```

---

# 17. Basic Backend Application Flow

```text
User
  ↓
Browser / Mobile App
  ↓
HTTP Request
  ↓
Web Framework
  ↓
URL Router
  ↓
Business Logic
  ↓
Database
  ↓
Response
  ↓
Client
