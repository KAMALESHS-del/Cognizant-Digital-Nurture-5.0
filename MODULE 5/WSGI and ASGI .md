# WSGI and ASGI

WSGI and ASGI are **interfaces between a Python web application and a web server**. They define how the server communicates with frameworks such as Django, Flask, and FastAPI.

---

## 1. WSGI

**WSGI** stands for:

> **Web Server Gateway Interface**

It is the traditional standard for connecting Python web applications with web servers.

### Architecture

```text
Client
  ↓
Web Server
  ↓
WSGI Server
  ↓
WSGI Application
  ↓
Python Web Framework
```

### Example

```text
Browser
   ↓
Nginx / Apache
   ↓
Gunicorn
   ↓
Django / Flask
```

### WSGI Application

A basic WSGI application:

```python
def application(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]

    start_response(status, headers)

    return [b"Hello, WSGI!"]
```

### Important Features

* Synchronous
* Handles one request at a time per worker
* Excellent for traditional web applications
* Commonly used with Django and Flask

---

# 2. ASGI

**ASGI** stands for:

> **Asynchronous Server Gateway Interface**

ASGI is the modern successor to WSGI.

It supports both:

* Synchronous programming
* Asynchronous programming

### Architecture

```text
Client
  ↓
Web Server
  ↓
ASGI Server
  ↓
ASGI Application
  ↓
Python Web Framework
```

### Example

```text
Browser
   ↓
Nginx
   ↓
Uvicorn
   ↓
FastAPI
```

---

## ASGI Example

```python
async def application(scope, receive, send):
    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [
            [b"content-type", b"text/plain"]
        ]
    })

    await send({
        "type": "http.response.body",
        "body": b"Hello, ASGI!"
    })
```

The `async` and `await` keywords allow the application to handle asynchronous operations efficiently.

---

# 3. WSGI vs ASGI

| Feature           | WSGI                         | ASGI                                  |
| ----------------- | ---------------------------- | ------------------------------------- |
| Full Form         | Web Server Gateway Interface | Asynchronous Server Gateway Interface |
| Programming Style | Synchronous                  | Synchronous + Asynchronous            |
| Performance       | Good                         | Excellent for concurrent operations   |
| HTTP Support      | Yes                          | Yes                                   |
| WebSockets        | Not natively supported       | Supported                             |
| Long Connections  | Limited                      | Excellent                             |
| Streaming         | Limited                      | Better support                        |
| Common Servers    | Gunicorn, uWSGI              | Uvicorn, Daphne, Hypercorn            |
| Common Frameworks | Flask, Django                | FastAPI, Django                       |

---

# 4. Synchronous vs Asynchronous

## WSGI: Synchronous

Suppose a server receives three requests:

```text
Request 1 ──► Processing
              ↓
Request 2 ──► Wait
              ↓
Request 3 ──► Wait
```

The application generally waits for one operation to complete before continuing.

---

## ASGI: Asynchronous

```text
Request 1 ──► Waiting for Database
                    │
Request 2 ──────────┼──► Process
                    │
Request 3 ──────────┼──► Process
```

While Request 1 is waiting for a database or network operation, the server can work on other requests.

---

# 5. WSGI Example: Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"
```

This application can run using a WSGI server such as:

```text
Flask Application
       ↓
    Gunicorn
       ↓
     Client
```

---

# 6. ASGI Example: FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello FastAPI"}
```

It can run using an ASGI server such as:

```text
FastAPI Application
        ↓
      Uvicorn
        ↓
      Client
```

---

# 7. WebSocket Support

WebSockets allow continuous two-way communication between the client and server.

### Example Applications

* Chat applications
* Online gaming
* Live notifications
* Real-time dashboards
* Stock price updates

### WSGI

```text
Client ──► Request ──► Response
```

### ASGI

```text
Client ◄────────────► Server
       Continuous
       Communication
```

ASGI is better suited for WebSocket-based applications.

---

# 8. Django and WSGI/ASGI

Django supports both:

```text
Django
  ├── WSGI
  └── ASGI
```

### WSGI

Used for traditional synchronous applications.

```text
Django
   ↓
WSGI
   ↓
Gunicorn
```

### ASGI

Used for asynchronous features and real-time applications.

```text
Django
   ↓
ASGI
   ↓
Uvicorn / Daphne
```

---

# 9. Simple Real-World Example

Imagine a restaurant application.

### WSGI

```text
Customer 1 places order
        ↓
Restaurant processes order
        ↓
Customer 1 receives response

Customer 2 waits
```

### ASGI

```text
Customer 1 ──► Order Processing
Customer 2 ──► Order Processing
Customer 3 ──► Order Processing
```

The server can handle multiple waiting operations efficiently.

---

# 10. Which One Should You Use?

### Use WSGI when:

* Building traditional web applications
* Using Flask or older Django applications
* Your application is mostly synchronous
* You do not need WebSockets

### Use ASGI when:

* Building FastAPI applications
* Developing real-time applications
* Using WebSockets
* Performing many network/database operations
* Building high-concurrency applications

---

## Easy Exam Definition

**WSGI** is a standard interface that allows Python web applications to communicate with web servers using a primarily synchronous model.

**ASGI** is a modern interface that supports both synchronous and asynchronous Python applications, including WebSockets and real-time communication.

### Remember:

```text
WSGI → Traditional + Synchronous
ASGI → Modern + Asynchronous + Real-time
```
