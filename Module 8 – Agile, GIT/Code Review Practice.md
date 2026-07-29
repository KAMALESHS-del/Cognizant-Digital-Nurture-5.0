 

Code Review is the process of **examining another developer's code before it is merged into the main branch**. It helps improve code quality, identify bugs early, ensure coding standards, and facilitate knowledge sharing among team members.

---

# What is Code Review?

## Definition

A **Code Review** is a systematic examination of source code by one or more developers before it is merged into the main branch.

### Purpose

* Find bugs early
* Improve code quality
* Maintain coding standards
* Share knowledge among team members
* Ensure security and performance
* Reduce technical debt

---

## Example

Developer A creates a **Login Feature**.

Instead of merging directly into the **main** branch:

1. Push code to GitHub.
2. Create a Pull Request (PR).
3. Reviewer checks the code.
4. Developer fixes issues if needed.
5. Reviewer approves.
6. Code is merged.

---

# Code Review Workflow

```text
Developer Writes Code
          │
          ▼
     Create Pull Request
          │
          ▼
    Reviewer Checks Code
          │
   ┌──────┴──────┐
   │             │
Issues Found   No Issues
   │             │
Fix Changes    Approve PR
   │             │
   └──────┬──────┘
          ▼
   Merge into Main
```

---

# 1. What to Look for in Pull Requests (PRs)

A reviewer should examine multiple aspects of the code.

---

## A. Correctness

### Check

* Does the code solve the required problem?
* Does it work correctly?

### Example

Requirement:

User should log in with email and password.

Review:

* Does login succeed with valid credentials?
* Are invalid credentials handled correctly?

---

## B. Code Readability

Code should be easy to understand.

### Good Example

```python
total_price = price * quantity
```

### Bad Example

```python
x = a * b
```

Meaningful variable names improve readability.

---

## C. Coding Standards

Ensure the project follows consistent coding guidelines.

### Check

* Proper indentation
* Naming conventions
* Consistent formatting
* Appropriate comments

---

## Example

Good

```java
calculateTotalPrice()
```

Bad

```java
calc()
```

---

## D. Performance

Check whether the implementation is efficient.

### Bad Example

Nested loops over large datasets.

```python
for i in users:
    for j in users:
        ...
```

Time Complexity:

**O(n²)**

---

### Better Example

Use a dictionary or hash map.

Time Complexity:

**O(n)**

---

## E. Security

Ensure the code is secure.

### Check

* Input validation
* Password hashing
* SQL Injection prevention
* Authentication
* Authorization

---

### Bad Example

```sql
SELECT * FROM users
WHERE username='" + username + "'";
```

Risk:

SQL Injection

---

### Better Example

Use parameterized queries (prepared statements).

---

## F. Error Handling

Check whether exceptions are handled properly.

### Good Example

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
```

---

## G. Testing

Verify that the code has adequate tests.

### Check

* Unit tests
* Edge cases
* Test coverage
* Test results

---

## H. Documentation

Check whether the code is documented.

Example

```python
# Calculate total order amount
```

Useful comments explain **why**, not just **what**.

---

# PR Review Checklist

| Check            | Example               |
| ---------------- | --------------------- |
| Correctness      | Meets requirements    |
| Readability      | Clear variable names  |
| Coding Standards | Proper formatting     |
| Performance      | Efficient algorithms  |
| Security         | Prevent SQL Injection |
| Error Handling   | Exceptions handled    |
| Testing          | Unit tests available  |
| Documentation    | Helpful comments      |

---

# 2. Giving Constructive Feedback

## Definition

Constructive feedback helps improve code respectfully and professionally.

Focus on the **code**, not the **person**.

---

## Bad Feedback

❌

"This code is terrible."

---

## Better Feedback

✅

"Could we simplify this loop by using a dictionary? It may improve readability and performance."

---

## Another Example

Instead of

❌

"This is wrong."

Say

✅

"This function may not handle null values. Could we add a null check?"

---

## Tips

* Be respectful
* Explain the reason
* Suggest improvements
* Praise good work
* Ask questions instead of giving orders

---

# Good Feedback Examples

✅

"Nice implementation! Could you add error handling for invalid input?"

---

✅

"This logic works well. Consider extracting it into a helper method to improve reusability."

---

✅

"Would using a constant instead of a hardcoded value improve maintainability?"

---

# 3. Reviewer Etiquette

A reviewer should follow professional behavior.

---

## Responsibilities

* Review code promptly.
* Be respectful.
* Explain suggestions.
* Avoid personal criticism.
* Focus on code quality.
* Encourage discussion.

---

## Good Example

"I like the implementation. One suggestion is to rename this variable for better clarity."

---

## Avoid

"This code makes no sense."

---

# Reviewer Checklist

✔ Review functionality

✔ Check readability

✔ Verify coding standards

✔ Check security

✔ Review tests

✔ Suggest improvements politely

---

# 4. Author Etiquette

The author should also follow good practices.

---

## Responsibilities

* Keep Pull Requests small.
* Write meaningful commit messages.
* Respond politely to comments.
* Explain complex logic.
* Accept useful suggestions.
* Ask questions if feedback is unclear.

---

## Example

Reviewer

"Please add input validation."

Author

"Thanks! I've added validation and updated the tests."

---

## Good Commit Message

```text
Add password validation for login form
```

Bad

```text
Update
```

---

# 5. Review Checklists

A checklist ensures nothing important is missed during review.

---

## General Checklist

### Functionality

* Requirement implemented
* No bugs
* Edge cases handled

---

### Readability

* Meaningful variable names
* Clear function names
* Small methods

---

### Coding Standards

* Proper indentation
* Consistent formatting
* Naming conventions followed

---

### Performance

* Efficient algorithms
* No unnecessary loops
* No duplicate code

---

### Security

* Input validated
* Passwords encrypted/hashed
* SQL Injection prevented
* Sensitive data protected

---

### Testing

* Unit tests written
* Existing tests pass
* New features tested

---

### Documentation

* Comments where necessary
* README updated if required
* API documentation updated

---

## Example Review Checklist

| Item                        | Status |
| --------------------------- | ------ |
| Requirements met            | ✔      |
| Code readable               | ✔      |
| Naming conventions followed | ✔      |
| No duplicate code           | ✔      |
| Security verified           | ✔      |
| Tests passing               | ✔      |
| Documentation updated       | ✔      |

---

# Complete Example

Suppose a developer creates a **Registration Feature**.

### Pull Request

Reviewer checks:

* Registration works correctly ✔
* Password is hashed ✔
* Variable names are meaningful ✔
* Unit tests are included ✔
* Input validation exists ✔

Reviewer Comment:

> "Great work! Could you add validation for empty email addresses and update the related unit test?"

Developer updates the code, pushes the changes, and the reviewer approves the PR.

---

# Benefits of Code Reviews

* Improves code quality
* Detects bugs early
* Increases security
* Encourages collaboration
* Promotes knowledge sharing
* Maintains coding standards
* Reduces future maintenance costs
* Builds consistent and maintainable codebases

---

# Cognizant Technical Assessment – Important Questions

### 1. What is Code Review?

**Answer:** Code Review is the process of examining another developer's code before merging it into the main branch to improve quality, detect bugs, and ensure coding standards.

---

### 2. What should you look for in a Pull Request?

**Answer:**

* Correctness
* Readability
* Coding standards
* Performance
* Security
* Error handling
* Testing
* Documentation

---

### 3. What is constructive feedback?

**Answer:** Constructive feedback provides respectful, specific, and actionable suggestions that help improve the code without criticizing the developer personally.

---

### 4. What is reviewer etiquette?

**Answer:** Reviewers should be respectful, review promptly, explain suggestions clearly, focus on the code, and encourage productive discussion.

---

### 5. What is author etiquette?

**Answer:** Authors should create small PRs, write clear commit messages, respond politely to comments, explain complex code when needed, and address feedback professionally.

---

### 6. Why are review checklists important?

**Answer:** Review checklists ensure that important aspects such as functionality, readability, security, performance, testing, and documentation are consistently verified before code is merged.

---

### 7. Why are code reviews important?

**Answer:** They improve software quality, identify bugs early, enhance security, encourage collaboration, maintain coding standards, and help teams share knowledge.

---

# Quick Revision (1-Minute)

| Topic                 | Key Point                                                       |
| --------------------- | --------------------------------------------------------------- |
| Code Review           | Examine code before merging                                     |
| Pull Request (PR)     | Code submitted for review                                       |
| Review Focus          | Correctness, readability, performance, security, testing        |
| Constructive Feedback | Respectful, clear, and actionable suggestions                   |
| Reviewer Etiquette    | Be respectful, explain feedback, focus on the code              |
| Author Etiquette      | Keep PRs small, respond professionally, improve code            |
| Review Checklist      | Verify functionality, standards, security, tests, documentation |
| Main Goal             | Deliver high-quality, maintainable, and secure software         |

