# Flask: App Structure, Routing, Templates with Jinja2, Blueprints, Extensions, SQLAlchemy ORM (with Real Examples)

..................................................................

# 1. App Structure

## Definition

**App Structure** refers to the organization of files and folders in a Flask project. A good structure makes the application easier to develop, maintain, and scale.

### Basic Flask Project Structure

```text
my_flask_app/
│
├── app.py
├── templates/
│   ├── index.html
│   └── login.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│
├── models.py
├── routes.py
├── config.py
└── requirements.txt
```

### Purpose of Each File

| File/Folder      | Purpose                 |
| ---------------- | ----------------------- |
| app.py           | Main application file   |
| templates/       | Stores HTML pages       |
| static/          | CSS, JavaScript, Images |
| models.py        | Database models         |
| routes.py        | URL routes              |
| config.py        | Configuration settings  |
| requirements.txt | Project dependencies    |

### Real-Life Example

Imagine an **Online Shopping Website**.

```text
Shopping Website
│
├── app.py
├── templates/
│      ├── Home Page
│      ├── Products
│      └── Checkout
│
├── static/
│      ├── CSS
│      └── Product Images
│
└── models.py
       └── Product Database
```

Each file has a specific responsibility, making the project organized.

..................................................................

# 2. Routing

## Definition

**Routing** maps a URL to a Python function (called a view function). When a user visits a URL, Flask executes the corresponding function.

### Syntax

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask"

app.run(debug=True)
```

### Multiple Routes Example

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Us"

@app.route("/contact")
def contact():
    return "Contact Us"

app.run(debug=True)
```

### Output

```
http://localhost:5000/
→ Home Page

http://localhost:5000/about
→ About Us

http://localhost:5000/contact
→ Contact Us
```

### Dynamic Routing Example

```python
from flask import Flask

app = Flask(__name__)

@app.route("/student/<name>")
def student(name):
    return f"Welcome {name}"

app.run(debug=True)
```

Visiting:

```
http://localhost:5000/student/Rahul
```

Output:

```
Welcome Rahul
```

### Real-Life Example

A college website:

```
/students
/students/101
/students/102
```

Each student ID displays a different student's details.

..................................................................

# 3. Templates with Jinja2

## Definition

**Jinja2** is Flask's template engine. It allows developers to create dynamic HTML pages by inserting Python variables and logic into HTML.

### Folder Structure

```text
project/
│
├── app.py
└── templates/
      └── home.html
```

### Flask Code

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", name="King")

app.run(debug=True)
```

### HTML Template

```html
<!DOCTYPE html>
<html>
<body>

<h1>Welcome {{ name }}</h1>

</body>
</html>
```

### Output

```
Welcome King
```

### Jinja2 Loop Example

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    fruits = ["Apple", "Orange", "Banana"]
    return render_template("home.html", fruits=fruits)

app.run(debug=True)
```

```html
<ul>
{% for fruit in fruits %}
    <li>{{ fruit }}</li>
{% endfor %}
</ul>
```

### Output

```
Apple
Orange
Banana
```

### Real-Life Example

An e-commerce website displays products dynamically:

```html
<h2>{{ product.name }}</h2>
<p>Price: ${{ product.price }}</p>
```

Instead of creating a separate HTML page for every product, one template displays all products.

..................................................................

# 4. Blueprints

## Definition

A **Blueprint** is a way to organize a Flask application into separate modules. It helps divide large applications into smaller, reusable parts.

### Without Blueprints

Everything is written inside one file.

```
app.py
├── Login
├── Products
├── Orders
├── Admin
├── Users
```

The file becomes very large and difficult to manage.

### With Blueprints

```
project/

app.py

users/
    routes.py

products/
    routes.py

orders/
    routes.py

admin/
    routes.py
```

Each module manages its own routes.

### Blueprint Example

#### users/routes.py

```python
from flask import Blueprint

user_bp = Blueprint("users", __name__)

@user_bp.route("/users")
def users():
    return "User Page"
```

#### app.py

```python
from flask import Flask
from users.routes import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp)

app.run(debug=True)
```

### Output

```
http://localhost:5000/users

User Page
```

### Real-Life Example

A hospital management system:

```
Patient Module
Doctor Module
Pharmacy Module
Billing Module
```

Each module is developed independently using Blueprints.

..................................................................

# 5. Flask Extensions

## Definition

Flask extensions are additional libraries that provide extra features not included in the core Flask framework.

### Popular Extensions

| Extension        | Purpose               |
| ---------------- | --------------------- |
| Flask-SQLAlchemy | Database ORM          |
| Flask-Login      | User login management |
| Flask-WTF        | Form handling         |
| Flask-Mail       | Sending emails        |
| Flask-Migrate    | Database migrations   |

### Example: Flask-Login

```python
from flask_login import LoginManager

login_manager = LoginManager(app)
```

### Example: Flask-Mail

```python
from flask_mail import Mail

mail = Mail(app)
```

### Real-Life Example

An online banking application:

* Flask-Login → Secure customer login
* Flask-Mail → Email transaction alerts
* Flask-SQLAlchemy → Store account details
* Flask-Migrate → Update database structure safely

..................................................................

# 6. SQLAlchemy ORM

## Definition

**SQLAlchemy** is an **Object Relational Mapper (ORM)** that allows developers to interact with databases using Python objects instead of writing SQL queries.

### Installation

```bash
pip install flask-sqlalchemy
```

### Configure Database

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"

db = SQLAlchemy(app)
```

### Create Model

```python
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
```

### Create Database

```python
with app.app_context():
    db.create_all()
```

### Insert Data

```python
student = Student(name="King", age=21)

db.session.add(student)
db.session.commit()
```

### Read Data

```python
students = Student.query.all()

for s in students:
    print(s.name)
```

### Update Data

```python
student = Student.query.first()
student.age = 22

db.session.commit()
```

### Delete Data

```python
student = Student.query.first()

db.session.delete(student)
db.session.commit()
```

### Equivalent SQL

| SQLAlchemy                   | SQL                       |
| ---------------------------- | ------------------------- |
| `Student.query.all()`        | `SELECT * FROM student;`  |
| `db.session.add(student)`    | `INSERT INTO student ...` |
| `db.session.delete(student)` | `DELETE FROM student ...` |
| `db.session.commit()`        | `COMMIT;`                 |

### Real-Life Example

A **Library Management System** stores books.

```text
Book ID : 101
Title   : Python Programming
Author  : John Smith
Price   : $35
```

Using SQLAlchemy:

```python
book = Book(
    title="Python Programming",
    author="John Smith",
    price=35
)

db.session.add(book)
db.session.commit()
```

The record is automatically stored in the database without writing SQL queries.

..................................................................

# Summary Table

| Concept                | Purpose                                           | Real-Life Example                                                   |
| ---------------------- | ------------------------------------------------- | ------------------------------------------------------------------- |
| **App Structure**      | Organizes project files                           | Online shopping website folders                                     |
| **Routing**            | Maps URLs to Python functions                     | `/products`, `/about`, `/contact`                                   |
| **Templates (Jinja2)** | Creates dynamic HTML pages                        | Displaying product names and prices                                 |
| **Blueprints**         | Divides a large app into modules                  | Hospital system with patient, doctor, and billing modules           |
| **Extensions**         | Adds extra functionality                          | Login, email, forms, database support                               |
| **SQLAlchemy ORM**     | Performs database operations using Python objects | Library or student management system storing and retrieving records |

..................................................................

# Interview / Exam Questions

**1. What is Flask App Structure?**
It is the organized arrangement of files and folders in a Flask project to improve maintainability and scalability.

**2. What is Routing in Flask?**
Routing maps a URL to a Python view function using the `@app.route()` decorator.

**3. What is Jinja2?**
Jinja2 is Flask's template engine used to generate dynamic HTML pages by embedding Python variables and logic.

**4. What are Blueprints?**
Blueprints organize a large Flask application into reusable modules, making the code easier to manage.

**5. What are Flask Extensions?**
Extensions are additional libraries that provide features such as database support, authentication, forms, and email services.

**6. What is SQLAlchemy ORM?**
SQLAlchemy is an Object Relational Mapper that allows developers to interact with databases using Python objects instead of writing SQL queries directly.

