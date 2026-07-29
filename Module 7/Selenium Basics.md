# Module: Selenium Basics

## Overview

**Selenium** is one of the most widely used open-source automation testing tools for web applications. It allows testers and developers to automate browser actions, perform functional and regression testing, and execute tests across different browsers and operating systems.

Selenium supports multiple programming languages, including **Python, Java, C#, JavaScript, Ruby, and Kotlin**.

---

# 1. What is Selenium?

Selenium is an open-source framework used to automate web browsers for testing web applications.

### Objectives

* Automate repetitive testing tasks.
* Support cross-browser testing.
* Reduce manual testing effort.
* Integrate with CI/CD pipelines.
* Improve testing efficiency.

---

## Advantages of Selenium

* Free and open source.
* Supports multiple browsers.
* Supports multiple programming languages.
* Cross-platform (Windows, Linux, macOS).
* Large community support.
* Easy integration with TestNG, PyTest, Jenkins, GitHub Actions, etc.

---

## Limitations

* Automates only web applications.
* No built-in reporting.
* No built-in test management.
* Requires programming knowledge.

---

# 2. Selenium Architecture & Components

Selenium consists of several components that work together.

## A. Selenium WebDriver

WebDriver is the core component that directly communicates with browsers.

### Features

* Controls browser actions.
* Supports Chrome, Firefox, Edge, Safari.
* Faster than Selenium RC.
* Uses browser-specific drivers.

### Architecture

```text
Python Script
      │
      ▼
Selenium WebDriver
      │
      ▼
Browser Driver
(ChromeDriver / GeckoDriver / EdgeDriver)
      │
      ▼
Web Browser
```

---

## B. Selenium Grid

Selenium Grid allows multiple tests to run simultaneously on different browsers and operating systems.

### Advantages

* Parallel execution
* Faster testing
* Cross-browser testing
* Cross-platform testing

### Example

One test can run on:

* Chrome (Windows)
* Firefox (Linux)
* Edge (Windows)
* Safari (macOS)

at the same time.

---

## C. Selenium IDE

Selenium IDE is a browser extension used for recording and playback of test cases.

### Features

* No programming required.
* Record user actions.
* Replay tests.
* Export scripts.

### Advantages

* Easy for beginners.
* Quick test creation.

### Disadvantages

* Limited flexibility.
* Not suitable for complex automation.

---

# Selenium Components Summary

| Component     | Purpose                            |
| ------------- | ---------------------------------- |
| Selenium IDE  | Record and playback                |
| WebDriver     | Browser automation                 |
| Selenium Grid | Parallel and distributed execution |

---

# 3. Browser Drivers Setup

A browser driver acts as a bridge between Selenium and the browser.

Common browser drivers:

| Browser         | Driver       |
| --------------- | ------------ |
| Google Chrome   | ChromeDriver |
| Mozilla Firefox | GeckoDriver  |
| Microsoft Edge  | EdgeDriver   |
| Safari          | SafariDriver |

---

## Installation

### Step 1

Install Selenium:

```bash
pip install selenium
```

---

### Step 2

Install WebDriver Manager (recommended):

```bash
pip install webdriver-manager
```

---

### Step 3

Example (Chrome)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.google.com")
```

Using **webdriver-manager** automatically downloads the correct driver version.

---

# 4. Selenium Locators

Locators identify web elements.

---

## A. ID Locator

Most preferred because IDs are usually unique.

HTML

```html
<input id="username">
```

Python

```python
driver.find_element("id", "username")
```

---

## B. Name Locator

HTML

```html
<input name="email">
```

Python

```python
driver.find_element("name", "email")
```

---

## C. XPath Locator

Used when ID or Name is unavailable.

HTML

```html
<input id="password">
```

Python

```python
driver.find_element("xpath", "//input[@id='password']")
```

---

## D. CSS Selector

Usually faster than XPath.

HTML

```html
<input class="login">
```

Python

```python
driver.find_element("css selector", ".login")
```

---

## Other Common Locators

| Locator           | Example               |
| ----------------- | --------------------- |
| Class Name        | `"class name"`        |
| Tag Name          | `"tag name"`          |
| Link Text         | `"link text"`         |
| Partial Link Text | `"partial link text"` |

---

# Locator Comparison

| Locator      | Speed     | Reliability |
| ------------ | --------- | ----------- |
| ID           | Very Fast | Very High   |
| Name         | Fast      | High        |
| CSS Selector | Very Fast | High        |
| XPath        | Medium    | High        |
| Class Name   | Fast      | Medium      |

---

# 5. WebDriver Commands

---

## Opening Browser

```python
driver = webdriver.Chrome()
```

---

## Open Website

```python
driver.get("https://example.com")
```

---

## Get Current URL

```python
print(driver.current_url)
```

---

## Get Page Title

```python
print(driver.title)
```

---

## Maximize Window

```python
driver.maximize_window()
```

---

## Refresh Page

```python
driver.refresh()
```

---

## Navigate Back

```python
driver.back()
```

---

## Navigate Forward

```python
driver.forward()
```

---

## Close Current Window

```python
driver.close()
```

---

## Quit Browser

```python
driver.quit()
```

---

# Common Element Commands

Click Button

```python
driver.find_element("id", "login").click()
```

---

Enter Text

```python
driver.find_element("id", "username").send_keys("admin")
```

---

Clear Text

```python
driver.find_element("id", "username").clear()
```

---

Read Element Text

```python
text = driver.find_element("id", "message").text
```

---

Check Visibility

```python
driver.find_element("id", "login").is_displayed()
```

---

Check Enabled

```python
driver.find_element("id", "submit").is_enabled()
```

---

# 6. Handling Waits

Web pages often load elements asynchronously. Selenium provides waits to avoid failures caused by timing issues.

---

## A. Implicit Wait

Applies globally for locating elements.

```python
driver.implicitly_wait(10)
```

Meaning:

* Selenium waits up to **10 seconds** before throwing a `NoSuchElementException`.

### Advantages

* Easy to configure.
* Applies to all element searches.

### Disadvantages

* Less flexible.
* Can slow down test execution.

---

## B. Explicit Wait

Waits for a specific condition before continuing.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

login = wait.until(
    EC.element_to_be_clickable((By.ID, "login"))
)

login.click()
```

### Common Expected Conditions

| Condition                       | Purpose                  |
| ------------------------------- | ------------------------ |
| `presence_of_element_located`   | Element exists in DOM    |
| `visibility_of_element_located` | Element is visible       |
| `element_to_be_clickable`       | Element can be clicked   |
| `title_contains`                | Page title contains text |
| `alert_is_present`              | Alert is displayed       |

---

# Implicit vs Explicit Wait

| Feature     | Implicit Wait         | Explicit Wait               |
| ----------- | --------------------- | --------------------------- |
| Scope       | Entire driver session | Specific element/condition  |
| Flexibility | Low                   | High                        |
| Recommended | Limited use           | Preferred for dynamic pages |

---

# 7. Running Tests with Python

## Install Required Packages

```bash
pip install selenium
pip install webdriver-manager
pip install pytest
```

---

## Example Selenium Test

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://example.com")

assert "Example Domain" in driver.title

driver.quit()
```

---

## Running with PyTest

Save the file as:

```text
test_example.py
```

Run:

```bash
pytest test_example.py
```

PyTest automatically discovers test files whose names begin with `test_`.

---

# Complete Login Automation Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()
driver.get("https://example.com/login")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "login").click()

print(driver.title)

driver.quit()
```

---

# Real-Time Example

**Project:** Online Shopping Website

### Automated Test Flow

1. Open Chrome.
2. Navigate to the shopping website.
3. Enter username and password.
4. Click **Login**.
5. Search for a product.
6. Add the product to the cart.
7. Verify the cart count.
8. Log out.
9. Close the browser.

**Selenium Features Used**

* WebDriver
* ChromeDriver
* ID and CSS locators
* Explicit waits
* `send_keys()`
* `click()`
* Assertions

---

# Interview Questions

1. What is Selenium?
2. What are the components of Selenium?
3. What is Selenium WebDriver?
4. What is Selenium Grid used for?
5. What is Selenium IDE?
6. Why are browser drivers required?
7. What are the different Selenium locators?
8. Which locator is generally preferred and why?
9. What is the difference between XPath and CSS Selector?
10. Explain `click()`, `send_keys()`, and `clear()`.
11. What is the difference between `close()` and `quit()`?
12. What is an implicit wait?
13. What is an explicit wait?
14. Which wait is generally recommended for dynamic web applications?
15. How do you run Selenium tests with Python and PyTest?

---

# Key Points to Remember

* **Selenium** is an open-source framework for automating **web browser** testing.
* Its main components are **WebDriver**, **Grid**, and **IDE**.
* **Browser drivers** (ChromeDriver, GeckoDriver, EdgeDriver, SafariDriver) enable communication between Selenium and the browser.
* Common locators include **ID**, **Name**, **XPath**, and **CSS Selector**; **ID** is generally the most reliable and fastest when available.
* Frequently used WebDriver commands include `get()`, `click()`, `send_keys()`, `refresh()`, `back()`, `forward()`, `close()`, and `quit()`.
* **Explicit waits** are generally preferred over implicit waits for handling dynamic web elements because they wait only for specific conditions.
* Python Selenium projects commonly use **webdriver-manager** for automatic driver management and **PyTest** for test execution and reporting.
* Selenium is ideal for **functional, regression, and cross-browser testing** of web applications.

