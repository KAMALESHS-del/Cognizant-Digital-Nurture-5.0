
Before using **GitHub Copilot**, you need to install the extension, sign in with your GitHub account, and enable Copilot in your code editor. Once configured, Copilot can suggest code, functions, comments, and documentation as you type.

> **Note:** A GitHub account is required to use GitHub Copilot. Some plans include Copilot features, while full access may require an eligible subscription or license.

---

# What is GitHub Copilot Setup?

## Definition

GitHub Copilot setup is the process of:

* Installing the GitHub Copilot extension
* Signing in with a GitHub account
* Enabling Copilot
* Using it inside Visual Studio Code (VS Code)

---

# Requirements

Before installing GitHub Copilot, ensure you have:

* Visual Studio Code (VS Code)
* GitHub account
* Internet connection
* GitHub Copilot access

---

# Setup Workflow

```text
Install VS Code
        │
        ▼
Install GitHub Copilot Extension
        │
        ▼
Sign in to GitHub
        │
        ▼
Authorize GitHub Copilot
        │
        ▼
Start Coding
        │
        ▼
AI Suggestions Appear
```

---

# 1. Installing GitHub Copilot Extension in VS Code

## Step 1

Open **Visual Studio Code**.

---

## Step 2

Click the **Extensions** icon on the left sidebar.

Shortcut:

```text
Ctrl + Shift + X
```

---

## Step 3

Search for:

```text
GitHub Copilot
```

---

## Step 4

Select the official **GitHub Copilot** extension.

---

## Step 5

Click:

```text
Install
```

VS Code installs the extension automatically.

---

# Installation Process

```text
VS Code
     │
     ▼
Extensions
     │
     ▼
Search "GitHub Copilot"
     │
     ▼
Install
```

---

# 2. Connecting to a GitHub Account

After installation,

VS Code asks you to sign in.

---

## Step 1

Click

```text
Sign in to GitHub
```

---

## Step 2

Browser opens automatically.

---

## Step 3

Login using your GitHub account.

Example

```text
Username

Password
```

---

## Step 4

Authorize Visual Studio Code.

---

## Step 5

Return to VS Code.

GitHub Copilot is now connected.

---

# Login Flow

```text
VS Code
     │
     ▼
Sign in
     │
     ▼
GitHub Website
     │
     ▼
Login
     │
     ▼
Authorize
     │
     ▼
VS Code Connected
```

---

# Verify GitHub Copilot

Open any supported programming file.

Example

```text
hello.py
```

or

```text
Program.java
```

Start typing.

If Copilot is active,

AI suggestions appear automatically.

---

# 3. Beginner-Friendly First Coding Task

Let's write a simple Python program.

---

## Step 1

Create

```text
hello.py
```

---

## Step 2

Type the comment

```python
# Print Hello World
```

---

## Step 3

GitHub Copilot may suggest:

```python
print("Hello World")
```

Press:

```text
Tab
```

to accept the suggestion (the exact accept key can vary if you've customized shortcuts).

---

# Example 2

Type

```python
# Create a function that adds two numbers
```

Copilot may suggest

```python
def add(a, b):
    return a + b
```

---

# Example 3

Java

Type

```java
// Find the largest number in an array
```

Copilot may generate

```java
public static int findLargest(int[] arr) {
    int max = arr[0];

    for (int num : arr) {
        if (num > max)
            max = num;
    }

    return max;
}
```

---

# Example 4

JavaScript

Type

```javascript
// Reverse a string
```

Copilot may suggest

```javascript
function reverseString(str) {
    return str.split("").reverse().join("");
}
```

---

# Example 5

HTML

Type

```html
<!-- Create a login form -->
```

Copilot may generate

```html
<form>
    <input type="text" placeholder="Username">
    <input type="password" placeholder="Password">
    <button>Login</button>
</form>
```

---

# Copilot Coding Workflow

```text
Developer Types Comment
          │
          ▼
GitHub Copilot
          │
Reads Context
          │
          ▼
Suggests Code
          │
          ▼
Developer Reviews
          │
     Accept or Edit
```

---

# Tips for Beginners

### Write descriptive comments

Instead of

```text
Function
```

Write

```text
Create a function that checks whether a number is prime.
```

---

### Use meaningful variable names

Example

```python
studentMarks
```

Instead of

```python
x
```

---

### Review every suggestion

Never accept AI-generated code without reading it.

---

### Test generated code

Run the program and verify the output.

---

### Modify if needed

Copilot suggestions are a starting point, not always the final solution.

---

# Example Session

Developer writes

```python
# Read numbers from a file and calculate the average
```

↓

GitHub Copilot suggests

Python code

↓

Developer reviews

↓

Runs the program

↓

Makes improvements if necessary

↓

Commits the verified code to Git.

---

# Advantages of GitHub Copilot Setup

* Quick installation
* Easy GitHub integration
* Supports many programming languages
* Works directly in VS Code
* Improves coding speed
* Reduces repetitive typing
* Helps beginners learn coding patterns
* Enhances productivity

---

# Best Practices

* Keep VS Code and the Copilot extension updated.
* Review and test all AI-generated code.
* Avoid including passwords, API keys, or confidential information in prompts or source files.
* Use comments to describe your intent for better suggestions.
* Follow your team's coding standards.

---

# Complete Example

Suppose a developer starts a **Student Management System**.

### Step 1

Install the GitHub Copilot extension in VS Code.

### Step 2

Sign in with a GitHub account.

### Step 3

Open:

```text
student.py
```

### Step 4

Write:

```python
# Create a Student class with name and age
```

### Step 5

Copilot suggests the class.

### Step 6

The developer reviews, tests, and modifies the code if required.

### Step 7

The verified code is saved and committed to Git.

---

# Setup Summary

| Step | Action                              |
| ---- | ----------------------------------- |
| 1    | Install Visual Studio Code          |
| 2    | Install GitHub Copilot extension    |
| 3    | Sign in with a GitHub account       |
| 4    | Authorize GitHub Copilot            |
| 5    | Open a programming file             |
| 6    | Start typing comments or code       |
| 7    | Review, accept, or edit suggestions |

---

# Cognizant Technical Assessment – Important Questions

### 1. How do you install GitHub Copilot in VS Code?

**Answer:** Open VS Code → Extensions (`Ctrl + Shift + X`) → Search for **GitHub Copilot** → Install the official extension.

---

### 2. How do you connect GitHub Copilot to your account?

**Answer:** After installing the extension, click **Sign in to GitHub**, log in through the browser, authorize Visual Studio Code, and return to VS Code.

---

### 3. How do you verify that GitHub Copilot is working?

**Answer:** Open a supported programming file, type a descriptive comment or begin writing code, and check whether Copilot displays code suggestions.

---

### 4. Give a beginner-friendly GitHub Copilot task.

**Answer:**

```python
# Create a function that adds two numbers
```

Copilot may suggest:

```python
def add(a, b):
    return a + b
```

---

### 5. What are the benefits of GitHub Copilot?

**Answer:**

* Faster coding
* Reduced repetitive typing
* AI-assisted code completion
* Documentation assistance
* Test generation
* Support for many programming languages

---

### 6. What are some best practices when using GitHub Copilot?

**Answer:**

* Review every suggestion.
* Test generated code.
* Avoid sharing sensitive information.
* Use clear comments for better suggestions.
* Follow coding standards.

---

# Quick Revision (1-Minute)

| Topic           | Key Point                                                   |
| --------------- | ----------------------------------------------------------- |
| Install Copilot | Install the GitHub Copilot extension in VS Code             |
| Sign In         | Connect using a GitHub account                              |
| Verify          | Start typing to receive AI suggestions                      |
| First Task      | Write a descriptive comment and review the generated code   |
| Best Practice   | Review, test, and modify AI-generated code before using it  |
| Benefits        | Faster coding, better productivity, AI-assisted development |
