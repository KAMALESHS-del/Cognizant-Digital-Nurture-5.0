# Flask Framework (With Examples)

## What is Flask?

**Flask** is a lightweight, open-source Python web framework used to build web applications and REST APIs. It is called a **micro-framework** because it provides only the essential features, allowing developers to add extra functionality using extensions.

**Exam Definition:**

> Flask is a lightweight Python web framework that helps developers build web applications and APIs quickly and easily.

---

# Features of Flask

* Lightweight and simple
* Easy to learn
* Built-in development server
* URL routing
* Supports Jinja2 template engine
* REST API development
* Extensible using plugins
* Compatible with databases like SQLite, MySQL, and PostgreSQL

---

# Advantages of Flask

* Simple and easy for beginners
* Fast development
* Flexible project structure
* Large community support
* Easy integration with databases and APIs

---

# Disadvantages of Flask

* No built-in admin panel
* No built-in ORM (uses extensions like SQLAlchemy)
* Developers must add many features manually

---

# Flask Architecture

```text
Client (Browser)
       │
       ▼
HTTP Request
       │
       ▼
Flask Application
       │
       ▼
View Function
       │
       ▼
Database (Optional)
       │
       ▼
HTTP Response
```

---

# Installing Flask

Install Flask using pip:

```bash
pip install flask
```

Check the version:

```bash
python -c "import flask; print(flask.__version__)"
```

---

# First Flask Program

```python
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return "Welcome to Flask!"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

### Output

Open the browser:

```
http://127.0.0.1:5000/
```

Output:

```
Welcome to Flask!
```

### Explanation

* `Flask(__name__)` creates the Flask application.
* `@app.route("/")` maps the URL `/` to the `home()` function.
* `app.run(debug=True)` starts the development server.

---

# URL Routing

Routing connects a URL to a Python function.

### Example

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
    return "Contact Page"

app.run(debug=True)
```

### URLs

```
http://127.0.0.1:5000/
```

Output:

```
Home Page
```

```
http://127.0.0.1:5000/about
```

Output:

```
About Us
```

```
http://127.0.0.1:5000/contact
```

Output:

```
Contact Page
```

---

# Dynamic Routing

Flask can accept values from the URL.

### Example

```python
from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")
def user(name):
    return f"Welcome {name}"

app.run(debug=True)
```

### URL

```
http://127.0.0.1:5000/user/King
```

Output

```
Welcome King
```

---

# Rendering HTML Templates

Flask uses the **Jinja2 Template Engine**.

### Folder Structure

```
project/
│
├── app.py
└── templates/
      └── home.html
```

### app.py

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", name="King")

app.run(debug=True)
```

### templates/home.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome {{ name }}</h1>
</body>
</html>
```

### Output

```
Welcome King
```

---

# Handling Forms

### HTML Form

```html
<form method="POST">
    Name:
    <input type="text" name="username">
    <input type="submit">
</form>
```

### Flask Code

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["username"]
        return "Hello " + name

    return '''
    <form method="POST">
        <input type="text" name="username">
        <input type="submit">
    </form>
    '''

app.run(debug=True)
```

### Output

Input:

```
King
```

Output:

```
Hello King
```

---

# Flask with Database (SQLite)

```python
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY,
name TEXT
)
""")

cursor.execute("INSERT INTO student(name) VALUES(?)", ("King",))

conn.commit()
conn.close()
```

This creates a database and inserts a student record.

---

# Returning JSON (REST API)

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/student")
def student():
    return jsonify({
        "id": 1,
        "name": "King",
        "course": "Python"
    })

app.run(debug=True)
```

### Output

```json
{
    "id": 1,
    "name": "King",
    "course": "Python"
}
```

---

# HTTP Methods in Flask

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Login Successful"

    return "Login Page"

app.run(debug=True)
```

---

# Project Structure

```
project/
│
├── app.py
├── static/
│      ├── style.css
│      └── script.js
│
├── templates/
│      ├── home.html
│      └── login.html
│
└── database.db
```

---

# Flask Request–Response Cycle

```
Browser
   │
   ▼
HTTP Request
   │
   ▼
Flask Application
   │
   ▼
Route
   │
   ▼
View Function
   │
   ▼
Database (Optional)
   │
   ▼
HTML / JSON Response
   │
   ▼
Browser
```

---

# Flask vs Django

| Feature        | Flask            | Django                 |
| -------------- | ---------------- | ---------------------- |
| Type           | Micro Framework  | Full-Stack Framework   |
| Learning Curve | Easy             | Moderate               |
| Admin Panel    | No               | Yes                    |
| Built-in ORM   | No               | Yes                    |
| Performance    | Fast             | Good                   |
| Flexibility    | High             | Moderate               |
| Best For       | Small apps, APIs | Large web applications |

---

# Real-World Applications of Flask

* REST APIs
* Machine Learning model deployment
* Portfolio websites
* IoT applications
* Dashboards
* Small business websites
* Microservices

---

# Frequently Asked Exam Questions

### 1. What is Flask?

Flask is a lightweight Python web framework used to develop web applications and REST APIs.

### 2. Why is Flask called a micro-framework?

Because it provides only the essential web development features and relies on extensions for additional functionality.

### 3. What is URL routing in Flask?

URL routing maps a URL to a Python function using the `@app.route()` decorator.

### 4. What template engine does Flask use?

**Jinja2**.

### 5. Can Flask be used to build REST APIs?

Yes. Flask is widely used for developing RESTful APIs using `jsonify()` and route handlers.

---

# Key Points to Remember

* **Flask** is a lightweight Python web framework.
* It is called a **micro-framework** because it includes only essential features.
* Use `Flask(__name__)` to create an application.
* Use `@app.route()` to define URL routes.
* Use `render_template()` to display HTML pages.
* Use `request` to read form data.
* Use `jsonify()` to return JSON responses.
* Flask is ideal for **small web applications, REST APIs, and microservices**.

