# Module: Selenium – Page Object Model (POM)

## Overview

The **Page Object Model (POM)** is a design pattern used in Selenium automation testing to improve the organization, maintainability, and reusability of test scripts. In POM, each web page of an application is represented by a separate class containing the page's elements (locators) and methods (actions). Test scripts interact with these page classes instead of directly accessing UI elements.

---

# 1. What is Page Object Model (POM)?

Page Object Model (POM) is a design pattern where:

* Each web page has its own class.
* UI elements (locators) are stored inside the page class.
* Page actions are implemented as methods.
* Test scripts call these methods instead of interacting with elements directly.

---

## Objectives

* Reduce code duplication.
* Improve maintainability.
* Increase code reusability.
* Separate UI logic from test logic.
* Simplify test script maintenance.

---

## Without POM

The test script contains:

* Locators
* Selenium commands
* Test logic

Everything is mixed together, making maintenance difficult.

Example:

```python
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "login").click()
```

If the page changes, every test script using these locators must be updated.

---

## With POM

The page class stores the locators and actions.

Test script:

```python
login_page.login("admin", "password")
```

If the login button ID changes, only the page class needs to be updated.

---

# 2. POM Architecture

```text
                Test Script
                     │
                     ▼
             Page Object Classes
        (LoginPage, HomePage, CartPage)
                     │
                     ▼
           Selenium WebDriver API
                     │
                     ▼
                Web Browser
```

---

# 3. Creating Page Classes

Each page of the application has its own Python class.

Example Project Structure:

```text
Project/
│
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   └── cart_page.py
│
├── tests/
│   └── test_login.py
│
├── utils/
│   └── driver.py
│
└── requirements.txt
```

---

## Example: Login Page Class

```python
from selenium.webdriver.common.by import By

class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
```

---

## Test Script

```python
from pages.login_page import LoginPage

login = LoginPage(driver)

login.login("admin", "password123")
```

The test is clean and easy to read because it calls page methods rather than Selenium commands directly.

---

# 4. Locator Management

## What is Locator Management?

Locator management means storing all page locators in one place (inside the page class) rather than scattering them across test scripts.

Example:

```python
USERNAME = (By.ID, "username")
PASSWORD = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login")
```

---

## Advantages

* Easy maintenance.
* Avoids duplicate locators.
* Improves readability.
* Simplifies updates when the UI changes.

---

## Good Practice

Store locators as class variables.

```python
SEARCH_BOX = (By.NAME, "search")
SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-btn")
```

---

# 5. Separation of Test Logic from UI Logic

One of the biggest benefits of POM is separating business logic from UI interactions.

---

## UI Logic (Page Class)

```python
def login(self, username, password):
    self.enter_username(username)
    self.enter_password(password)
    self.click_login()
```

---

## Test Logic

```python
def test_valid_login():
    login.login("admin", "admin123")

    assert "Dashboard" in driver.title
```

The page class handles **how** the interaction happens, while the test focuses on **what** should be verified.

---

# 6. Reusability

The same page class can be used in many tests.

Example:

```python
login.login("admin", "password")
```

Used in:

* Login test
* Checkout test
* Profile update test
* Order history test

Only one login implementation is maintained.

---

# 7. Maintainability

Suppose the Login button changes from:

```html
<button id="login">
```

to

```html
<button id="signin">
```

Without POM:

Every test script must be updated.

With POM:

Only this line changes:

```python
LOGIN_BUTTON = (By.ID, "signin")
```

All tests continue to work without modification.

---

# 8. Advantages of POM

* Better code organization.
* Reduced duplication.
* Easier maintenance.
* Improved readability.
* Higher reusability.
* Easier collaboration among team members.
* Scales well for large projects.

---

# 9. Limitations of POM

* Initial setup takes more time.
* More files to manage.
* Small projects may not benefit significantly.
* Requires understanding of object-oriented programming.

---

# 10. Best Practices

* Create one page class per web page.
* Store locators inside page classes.
* Use meaningful method names (e.g., `login()`, `search_product()`).
* Keep assertions in test files, not in page classes.
* Reuse common functionality through base page classes.
* Avoid duplicate locators across pages.

---

# POM Workflow

```text
Open Browser
      │
      ▼
Create Page Object
      │
      ▼
Call Page Methods
      │
      ▼
Perform Assertions
      │
      ▼
Close Browser
```

---

# Real-Time Example

**Project:** Online Banking System

### Page Classes

* `LoginPage`
* `DashboardPage`
* `TransferPage`
* `TransactionHistoryPage`

### Test Flow

1. Open browser.
2. Create `LoginPage` object.
3. Log in using `login()`.
4. Create `TransferPage` object.
5. Transfer funds.
6. Verify the success message.
7. Close the browser.

If the login page changes, only `LoginPage` is updated while all related tests continue to use the same interface.

---

# Interview Questions

1. What is the Page Object Model (POM)?
2. Why is POM used in Selenium?
3. What are the advantages of POM?
4. How does POM improve maintainability?
5. What is locator management?
6. Why should test logic be separated from UI logic?
7. How does POM improve code reusability?
8. How do you create a page class?
9. Where should assertions be written—in page classes or test classes?
10. What are the limitations of POM?
11. How would you organize a Selenium project using POM?
12. What happens if a page locator changes in a POM-based framework?
13. What is the role of the `__init__()` method in a page class?
14. Why are page methods preferred over direct Selenium commands in test scripts?
15. How does POM help large automation projects?

---

# Key Points to Remember

* **Page Object Model (POM)** is a design pattern that represents each web page as a separate class.
* Page classes contain **locators** and **methods** that perform actions on the page.
* Test scripts should call **page methods** instead of directly interacting with Selenium elements.
* Centralized **locator management** makes updates easier when the application's UI changes.
* POM separates **UI interaction logic** from **test validation logic**, improving readability and maintainability.
* **Assertions** should generally remain in the test classes, while page classes should focus on page interactions.
* POM promotes **code reusability**, reduces duplication, and is well-suited for medium and large Selenium automation projects.
* Following POM best practices results in cleaner, more scalable, and easier-to-maintain test automation frameworks.
