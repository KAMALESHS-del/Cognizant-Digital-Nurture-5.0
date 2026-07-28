# Django: Project Setup, Models & ORM, Views & Templates, URL Routing, Forms, Admin Interface, Authentication

---

# 1. Django Project Setup

A Django project is the main container that holds the entire web application.

## Step 1: Install Django

```bash
pip install django
```

Check the installed version:

```bash
django-admin --version
```

---

## Step 2: Create a Django Project

```bash
django-admin startproject myproject
```

Project structure:

```text
myproject/
│
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
```

---

## Step 3: Create an App

```bash
python manage.py startapp student
```

App structure:

```text
student/
│
├── admin.py
├── apps.py
├── models.py
├── views.py
├── tests.py
├── migrations/
```

---

## Step 4: Register the App

In `settings.py`:

```python
INSTALLED_APPS = [
    'student',
]
```

---

## Step 5: Run the Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 2. Models & ORM

## Model

A **Model** defines the structure of a database table.

### Example

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
```

Each object becomes a row in the database.

---

## ORM (Object Relational Mapper)

ORM lets you interact with the database using Python instead of SQL.

### Create

```python
student = Student(name="John", age=20, email="john@example.com")
student.save()
```

### Read

```python
Student.objects.all()
```

### Get One Record

```python
Student.objects.get(id=1)
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

## Migrations

Create migration files:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

---

# 3. Views & Templates

## View

A **View** handles requests and returns responses.

### Example

```python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```

---

## Template

A **Template** is an HTML file used to display data.

Example (`home.html`):

```html
<!DOCTYPE html>
<html>
<body>
<h1>Welcome {{ name }}</h1>
</body>
</html>
```

View passing data:

```python
def home(request):
    return render(request, "home.html", {"name": "King"})
```

Output:

```text
Welcome King
```

---

# 4. URL Routing

URL routing maps URLs to views.

### App `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
```

### Project `urls.py`

```python
from django.urls import include, path

urlpatterns = [
    path('', include('student.urls')),
]
```

When a user visits:

```text
http://localhost:8000/
```

the `home()` view is executed.

---

# 5. Django Forms

Forms collect user input.

## Example Form

```python
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
```

---

## Using the Form in a View

```python
from django.shortcuts import render
from .forms import StudentForm

def register(request):
    form = StudentForm()
    return render(request, "form.html", {"form": form})
```

---

## Template

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

### Advantages of Django Forms

* Input validation
* CSRF protection
* Easy HTML generation
* Cleaner code

---

# 6. Admin Interface

Django provides a built-in **Admin Panel** to manage data.

## Create Admin User

```bash
python manage.py createsuperuser
```

Enter:

* Username
* Email
* Password

---

## Register a Model

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

---

## Access the Admin Panel

```text
http://127.0.0.1:8000/admin/
```

### Admin Features

* Add records
* Edit records
* Delete records
* Search data
* Manage users
* Filter records

---

# 7. Authentication

Authentication verifies a user's identity.

## Login Flow

```text
User
  │
  ▼
Login Page
  │
  ▼
Username & Password
  │
  ▼
Authentication
  │
  ▼
Database
  │
  ▼
Login Success / Failure
```

---

## Create a User

```python
from django.contrib.auth.models import User

User.objects.create_user(
    username="john",
    password="12345"
)
```

---

## Login View

```python
from django.contrib.auth import authenticate, login

user = authenticate(username="john", password="12345")

if user is not None:
    login(request, user)
```

---

## Logout

```python
from django.contrib.auth import logout

logout(request)
```

---

## Check Login Status

```python
if request.user.is_authenticated:
    print("User Logged In")
```

---

## Features of Django Authentication

* User registration
* Login
* Logout
* Password hashing
* Permission management
* User groups
* Session management

---

# Django Request–Response Flow

```text
Browser
   │
   ▼
URL Request
   │
   ▼
urls.py
   │
   ▼
View
   │
   ├──► Model (Database)
   │
   └──► Template (HTML)
   │
   ▼
HTTP Response
```

---

# Common Django Commands

| Command                               | Purpose                  |
| ------------------------------------- | ------------------------ |
| `pip install django`                  | Install Django           |
| `django-admin startproject myproject` | Create a project         |
| `python manage.py startapp appname`   | Create an app            |
| `python manage.py runserver`          | Start development server |
| `python manage.py makemigrations`     | Create migration files   |
| `python manage.py migrate`            | Apply migrations         |
| `python manage.py createsuperuser`    | Create an admin user     |

---

# Interview / Exam Questions

### 1. What is a Django Model?

A model defines the structure of a database table and stores application data.

### 2. What is Django ORM?

ORM (Object Relational Mapper) allows developers to perform database operations using Python code instead of SQL.

### 3. What is the purpose of Views?

Views process HTTP requests, execute business logic, and return HTTP responses.

### 4. What is URL Routing?

URL routing maps incoming URLs to the appropriate view functions.

### 5. What is the Django Admin Interface?

It is a built-in web interface for managing application data, users, and models.

### 6. What is Authentication?

Authentication is the process of verifying a user's identity before granting access to protected resources.

---

# Key Points to Remember

* **Project** → Main Django application container.
* **App** → A module that provides specific functionality.
* **Model** → Defines database tables.
* **ORM** → Performs database operations using Python.
* **View** → Processes requests and returns responses.
* **Template** → Generates dynamic HTML pages.
* **URL Routing** → Connects URLs to views.
* **Forms** → Collect and validate user input.
* **Admin Interface** → Built-in panel to manage data.
* **Authentication** → Handles login, logout, user registration, permissions, and session management.
