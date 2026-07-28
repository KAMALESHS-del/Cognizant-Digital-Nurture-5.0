# Django Framework

## Definition

**Django** is a **high-level, open-source Python web framework** used to develop secure, scalable, and maintainable web applications quickly. It follows the **MVT (Model–View–Template)** architecture and includes many built-in features such as authentication, an admin panel, and database management.

> **Exam Definition:**
> Django is a high-level Python web framework that enables rapid development of secure and maintainable web applications using the MVT architecture.

---

# Features of Django

* Open-source and free
* Written in Python
* Follows MVT architecture
* Built-in Admin Panel
* Built-in Authentication
* Uses Django ORM (Object Relational Mapper)
* Highly Secure
* Scalable for large applications
* URL Routing
* Template Engine
* Supports SQLite, MySQL, PostgreSQL, Oracle

---

# Advantages of Django

* Rapid application development
* Less coding due to built-in features
* Strong security against common web attacks
* Easy database management with ORM
* Reusable components
* Large community support
* Easy integration with APIs

---

# Disadvantages of Django

* Steeper learning curve for beginners
* Can be heavyweight for very small projects
* Less flexible than micro-frameworks like Flask

---

# Django Architecture (MVT)

Django follows the **Model–View–Template (MVT)** architecture.

```text
        User
          │
          ▼
       URL Request
          │
          ▼
         View
          │
   ┌──────┴──────┐
   ▼             ▼
Model         Template
   │             │
   ▼             │
Database ◄───────┘
          │
          ▼
      HTTP Response
```

---

# Components of MVT

## 1. Model

The **Model** represents the database structure.

### Responsibilities

* Defines database tables
* Stores data
* Performs database operations
* Uses Django ORM

### Example

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

---

## 2. View

A **View** contains the business logic. It receives requests, processes them, and returns responses.

### Example

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django")
```

---

## 3. Template

A **Template** is an HTML file used to display dynamic data.

### Example

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Welcome {{ name }}</h1>
</body>
</html>
```

If:

```text
name = "King"
```

Output:

```text
Welcome King
```

---

# Django Project Structure

```
myproject/
│
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
│
└── myapp/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── tests.py
    ├── urls.py
    └── migrations/
```

---

# Important Files

## manage.py

* Command-line utility
* Runs the development server
* Creates migrations
* Creates apps

Example:

```bash
python manage.py runserver
```

---

## settings.py

Stores project configuration:

* Installed apps
* Database settings
* Middleware
* Templates
* Static files
* Security settings

---

## urls.py

Maps URLs to views.

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
```

---

## models.py

Defines database tables.

Example:

```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
```

---

## views.py

Contains application logic.

Example:

```python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```

---

## admin.py

Registers models to appear in the Django Admin Panel.

Example:

```python
from django.contrib import admin
from .models import Employee

admin.site.register(Employee)
```

---

# Django Request–Response Cycle

```text
Browser
   │
   ▼
HTTP Request
   │
   ▼
urls.py
   │
   ▼
views.py
   │
   ▼
models.py (if database needed)
   │
   ▼
Database
   │
   ▼
Template
   │
   ▼
HTTP Response
```

---

# Django ORM (Object Relational Mapper)

Django ORM allows developers to work with database records using Python code instead of writing SQL.

### Create

```python
student = Student(name="John", age=20)
student.save()
```

### Read

```python
Student.objects.all()
```

### Update

```python
student = Student.objects.get(id=1)
student.age = 21
student.save()
```

### Delete

```python
student.delete()
```

---

# Django Commands

Create a project:

```bash
django-admin startproject myproject
```

Create an app:

```bash
python manage.py startapp myapp
```

Run the server:

```bash
python manage.py runserver
```

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

---

# Django Admin Panel

The Django Admin Panel is a built-in interface for managing application data.

### Features

* Add records
* Edit records
* Delete records
* Search
* Filter
* User management

Access:

```text
http://127.0.0.1:8000/admin/
```

---

# Django Middleware

Middleware processes requests before they reach the view and responses before they are sent back to the client.

### Common Middleware

* Authentication
* Session Management
* Security
* CSRF Protection
* Logging

Flow:

```text
Request
   │
Middleware
   │
View
   │
Middleware
   │
Response
```

---

# Django Templates

Templates generate dynamic HTML pages.

Example:

```html
<h2>Hello {{ username }}</h2>
```

Output:

```text
Hello King
```

---

# Django URL Routing

```python
from django.urls import path
from .views import about

urlpatterns = [
    path('about/', about),
]
```

Visiting:

```text
http://localhost:8000/about/
```

calls the `about()` view.

---

# Real-World Applications of Django

* E-commerce websites
* Social networking platforms
* Content Management Systems (CMS)
* Online learning platforms
* Banking and finance applications
* Healthcare systems
* News portals

---

# Django vs Flask vs FastAPI

| Feature        | Django                 | Flask           | FastAPI               |
| -------------- | ---------------------- | --------------- | --------------------- |
| Type           | Full-stack Framework   | Micro Framework | API Framework         |
| Architecture   | MVT                    | Flexible        | API-first             |
| Performance    | Good                   | Good            | Excellent             |
| Built-in Admin | Yes                    | No              | No                    |
| ORM            | Built-in               | External        | External              |
| Authentication | Built-in               | Extensions      | External              |
| Best For       | Large web applications | Small projects  | High-performance APIs |

---

# Advantages of Django ORM

* No need to write SQL
* Database-independent
* Easy CRUD operations
* Secure against SQL injection
* Easy migrations

---

# Interview / Exam Questions

### 1. What is Django?

A high-level Python web framework for developing secure, scalable, and maintainable web applications.

### 2. What architecture does Django follow?

**MVT (Model–View–Template).**

### 3. What is Django ORM?

A feature that allows interaction with databases using Python objects instead of SQL queries.

### 4. What is the purpose of `manage.py`?

It is a command-line utility used to run the server, create apps, manage migrations, and perform administrative tasks.

### 5. What is the difference between a Project and an App?

| Project                      | App                                    |
| ---------------------------- | -------------------------------------- |
| Complete website/application | A module with a specific functionality |
| Contains project settings    | Contains business logic                |
| Can include multiple apps    | Belongs to a project                   |

---

# Key Points to Remember

* **Django = High-level Python Web Framework**
* **Architecture = MVT (Model–View–Template)**
* **Database = ORM**
* **Admin Panel = Built-in**
* **Security = Strong**
* **Best for = Large, secure web applications**
* **Commands = `startproject`, `startapp`, `runserver`, `makemigrations`, `migrate`, `createsuperuser`**
