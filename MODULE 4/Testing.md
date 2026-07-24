MODULE 4 – UNIT TESTING

## Complete Cognizant Technical Assessment Preparation Notes

---

# 1. TESTING FUNDAMENTALS

## 1.1 What is Software Testing?

Software testing is the process of checking whether software works according to its requirements.

### Purpose of Testing

* Find bugs
* Verify requirements
* Improve software quality
* Prevent regression
* Reduce maintenance cost
* Ensure reliability

---

## 1.2 Testing Pyramid

```text
             /\
            /  \
           / E2E \
          /------\
         /        \
        /Integration\
       /------------\
      /              \
     /   Unit Tests   \
    /__________________\
```

### Unit Testing

Tests one function or module.

### Integration Testing

Tests multiple components working together.

### End-to-End Testing

Tests the complete application from the user's perspective.

### Comparison

| Feature | Unit  | Integration | E2E             |
| ------- | ----- | ----------- | --------------- |
| Scope   | Small | Medium      | Complete system |
| Speed   | Fast  | Medium      | Slow            |
| Cost    | Low   | Medium      | High            |
| Number  | Many  | Fewer       | Few             |

---

## 1.3 Arrange–Act–Assert (AAA)

Every test commonly follows:

```text
Arrange → Act → Assert
```

```python
def test_add():
    # Arrange
    a = 10
    b = 20

    # Act
    result = add(a, b)

    # Assert
    assert result == 30
```

---

## 1.4 Happy Path Testing

Tests normal, valid inputs.

Example:

```text
Input: 2, 3
Expected: 5
```

---

## 1.5 Edge Case Testing

Tests unusual or boundary inputs.

Examples:

```text
0
Negative values
Empty strings
Very large values
Null values
Duplicate values
```

---

# 2. PYTEST

## 2.1 Installation

```bash
pip install pytest
```

For coverage:

```bash
pip install pytest-cov
```

---

## 2.2 Test Discovery

PyTest automatically finds:

```text
test_*.py
*_test.py
```

Example:

```text
project/
│
├── calculator.py
└── test_calculator.py
```

---

## 2.3 Basic Test

### calculator.py

```python
def add(a, b):
    return a + b
```

### test_calculator.py

```python
from calculator import add


def test_add():
    assert add(2, 3) == 5
```

---

## 2.4 Running Tests

```bash
pytest
```

Verbose mode:

```bash
pytest -v
```

Specific file:

```bash
pytest test_calculator.py
```

Specific test:

```bash
pytest test_calculator.py::test_add
```

---

## 2.5 Assertions

```python
assert result == expected
```

Example:

```python
assert add(2, 3) == 5
```

---

## 2.6 Fixtures

Fixtures provide reusable data or setup.

```python
import pytest


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]


def test_sum(numbers):
    assert sum(numbers) == 15
```

### Fixture Advantages

* Reusable setup
* Avoids duplicate code
* Provides test data
* Can manage resources

---

## 2.7 Fixture Scope

```python
@pytest.fixture(scope="function")
```

```python
@pytest.fixture(scope="class")
```

```python
@pytest.fixture(scope="module")
```

```python
@pytest.fixture(scope="session")
```

### Scope Meaning

| Scope    | Runs                  |
| -------- | --------------------- |
| function | Every test            |
| class    | Once per class        |
| module   | Once per file         |
| session  | Once per test session |

---

## 2.8 Parameterization

Run the same test with multiple inputs.

```python
import pytest


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (5, False),
        (0, True),
        (-4, True)
    ]
)
def test_is_even(number, expected):
    assert number % 2 == 0
```

---

## 2.9 Markers

Markers categorize tests.

```python
@pytest.mark.smoke
def test_login():
    pass
```

Run marked tests:

```bash
pytest -m smoke
```

Common markers:

```text
smoke
slow
regression
integration
```

---

## 2.10 PyTest Exceptions

```python
import pytest


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

---

# 3. PYTHON UNITTEST

## 3.1 Basic Structure

```python
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(2 + 3, 5)


if __name__ == "__main__":
    unittest.main()
```

---

## 3.2 setUp and tearDown

### setUp()

Runs before each test.

Used for:

* Creating objects
* Opening files
* Creating test data

### tearDown()

Runs after each test.

Used for:

* Closing files
* Cleaning data
* Releasing resources

---

## 3.3 Common Assertions

```python
self.assertEqual(a, b)
```

```python
self.assertNotEqual(a, b)
```

```python
self.assertTrue(value)
```

```python
self.assertFalse(value)
```

```python
self.assertIsNone(value)
```

```python
self.assertIn(value, collection)
```

```python
self.assertRaises(Exception)
```

Example:

```python
with self.assertRaises(ValueError):
    divide(10, 0)
```

---

## 3.4 Test Suites

A test suite is a collection of test cases.

```python
suite = unittest.TestSuite()

suite.addTest(TestCalculator("test_add"))

runner = unittest.TextTestRunner()

runner.run(suite)
```

---

# 4. MOCKING AND TEST DOUBLES

## 4.1 Why Mock?

Suppose the code depends on:

```text
Application → Database
Application → API
Application → Payment Gateway
```

During unit testing, we replace real dependencies with mocks.

---

## 4.2 Types of Test Doubles

### Stub

Returns predefined data.

### Mock

Verifies interactions and calls.

### Spy

Records function calls.

### Fake

Simplified working implementation.

---

## 4.3 Python Mock

```python
from unittest.mock import Mock


mock_database = Mock()

mock_database.get_user.return_value = {
    "id": 1,
    "name": "John"
}

result = mock_database.get_user()

assert result["name"] == "John"
```

---

## 4.4 Verify Calls

```python
mock_database.get_user.assert_called_once()
```

```python
mock_database.get_user.assert_called_once_with()
```

Example:

```python
mock_api.get_user.assert_called_once_with(10)
```

---

## 4.5 side_effect

Used to simulate errors.

```python
mock_api.get_data.side_effect = Exception("Network Error")
```

---

# 5. MOCKING DATABASE CALL

```python
from unittest.mock import Mock


def get_user(database, user_id):
    return database.find_user(user_id)


def test_get_user():

    mock_database = Mock()

    mock_database.find_user.return_value = {
        "id": 1,
        "name": "Alice"
    }

    result = get_user(mock_database, 1)

    assert result["name"] == "Alice"

    mock_database.find_user.assert_called_once_with(1)
```

---

# 6. MOCKING HTTP REQUEST

```python
from unittest.mock import Mock


def get_data(api):
    return api.get("/users")


def test_get_data():

    mock_api = Mock()

    mock_api.get.return_value = {
        "status": 200,
        "data": ["Alice", "Bob"]
    }

    result = get_data(mock_api)

    assert result["status"] == 200

    mock_api.get.assert_called_once_with("/users")
```

---

# 7. JEST

## 7.1 Installation

```bash
npm init -y
```

```bash
npm install --save-dev jest
```

---

## 7.2 Basic JavaScript Function

### math.js

```javascript
function add(a, b) {
    return a + b;
}

module.exports = { add };
```

---

## 7.3 Jest Test

### math.test.js

```javascript
const { add } = require("./math");


test("adds two numbers", () => {
    expect(add(2, 3)).toBe(5);
});
```

Run:

```bash
npx jest
```

---

## 7.4 describe()

Groups related tests.

```javascript
describe("Calculator", () => {

    test("addition", () => {
        expect(2 + 3).toBe(5);
    });

    test("subtraction", () => {
        expect(10 - 5).toBe(5);
    });

});
```

---

## 7.5 Common Jest Matchers

```javascript
expect(value).toBe(5);
```

```javascript
expect(object).toEqual(expectedObject);
```

```javascript
expect(value).toBeTruthy();
```

```javascript
expect(value).toBeFalsy();
```

```javascript
expect(array).toContain(value);
```

```javascript
expect(() => functionCall()).toThrow();
```

---

# 8. JEST MOCKING

## Mock Function

```javascript
const mockFunction = jest.fn();

mockFunction("Hello");

expect(mockFunction).toHaveBeenCalled();
```

Verify arguments:

```javascript
expect(mockFunction).toHaveBeenCalledWith("Hello");
```

Return value:

```javascript
const mockFunction = jest.fn();

mockFunction.mockReturnValue(10);

expect(mockFunction()).toBe(10);
```

---

# 9. REACT COMPONENT TESTING

Common tools:

* Jest
* React Testing Library

Example:

```javascript
import { render, screen } from "@testing-library/react";
import App from "./App";


test("renders welcome message", () => {

    render(<App />);

    const text = screen.getByText("Welcome");

    expect(text).toBeInTheDocument();
});
```

Important concepts:

* Render component
* Find elements
* Simulate user interaction
* Check output
* Mock API calls

---

# 10. MOCHA

Mocha is a JavaScript test runner.

Installation:

```bash
npm install --save-dev mocha chai
```

---

## Mocha Test

```javascript
const { expect } = require("chai");


describe("Calculator", function () {

    it("should add two numbers", function () {

        const result = 2 + 3;

        expect(result).to.equal(5);
    });

});
```

Run:

```bash
npx mocha
```

---

## Mocha Hooks

```javascript
before(() => {
    console.log("Before all tests");
});
```

```javascript
after(() => {
    console.log("After all tests");
});
```

```javascript
beforeEach(() => {
    console.log("Before each test");
});
```

```javascript
afterEach(() => {
    console.log("After each test");
});
```

---

# 11. ASYNCHRONOUS TESTING

## Jest

```javascript
test("fetch data", async () => {

    const result = await fetchData();

    expect(result).toBe("Success");
});
```

---

## Mocha

```javascript
it("should fetch data", async function () {

    const result = await fetchData();

    expect(result).to.equal("Success");
});
```

---

# 12. TEST-DRIVEN DEVELOPMENT (TDD)

## Red–Green–Refactor

```text
RED
↓
Write failing test
↓
GREEN
↓
Write minimum code
↓
REFACTOR
↓
Improve code
```

---

## Example: TDD Calculator

### Step 1: RED

```python
def test_add():
    assert add(2, 3) == 5
```

The function does not exist.

Test fails.

---

### Step 2: GREEN

```python
def add(a, b):
    return a + b
```

Test passes.

---

### Step 3: REFACTOR

Improve code while keeping all tests passing.

---

# 13. CODE COVERAGE

## PyTest

Install:

```bash
pip install pytest-cov
```

Run:

```bash
pytest --cov=.
```

HTML report:

```bash
pytest --cov=. --cov-report=html
```

---

## Coverage Metrics

### Line Coverage

Percentage of executed lines.

### Branch Coverage

Percentage of executed decision paths.

Example:

```python
if age >= 18:
    return "Adult"
else:
    return "Minor"
```

Both branches should be tested.

---

## JavaScript Coverage

Jest:

```bash
npx jest --coverage
```

Istanbul/NYC:

```bash
npx nyc mocha
```

---

# 14. LINTING AND QUALITY

## Python

Pylint:

```bash
pip install pylint
```

Run:

```bash
pylint calculator.py
```

---

## JavaScript

ESLint:

```bash
npm install eslint --save-dev
```

Purpose:

* Find coding errors
* Enforce coding standards
* Improve code quality

---

# 15. COMPLETE PRACTICAL PROJECT

## Project: Calculator Testing

### Features

* Addition
* Subtraction
* Multiplication
* Division
* Division by zero handling

### Test Requirements

Write at least:

```text
1. Test addition
2. Test subtraction
3. Test multiplication
4. Test division
5. Test division by zero
6. Test negative values
7. Test zero
8. Test decimal values
9. Test large values
10. Test invalid input
```

---

# 16. COGNIZANT IMPORTANT QUESTIONS

### Testing

* What is Unit Testing?
* What is Integration Testing?
* What is E2E Testing?
* Explain Testing Pyramid.
* Explain AAA Pattern.
* What are happy paths and edge cases?

### PyTest

* How does PyTest discover tests?
* What are fixtures?
* What is parameterization?
* How do you test exceptions?
* How do you generate coverage reports?

### unittest

* What is `TestCase`?
* What is `setUp()`?
* What is `tearDown()`?
* What are assertions?

### Mocking

* What is mocking?
* Why mock database calls?
* What is a test double?
* Difference between mock and stub.
* How do you verify mock calls?

### Jest

* What is Jest?
* What is `describe()`?
* What is `test()`?
* What are matchers?
* How do you mock functions?

### Mocha

* What is Mocha?
* What is Chai?
* What are hooks?
* How do you test asynchronous code?

### TDD

* What is TDD?
* Explain Red-Green-Refactor.
* Why write tests first?

### Coverage

* What is code coverage?
* Difference between line and branch coverage.
* How do you generate coverage reports?

---

# 🔥 FINAL COGNIZANT PREPARATION PRIORITY

## Very High Priority ⭐⭐⭐

1. Unit Testing Fundamentals
2. AAA Pattern
3. PyTest
4. Fixtures
5. Parameterization
6. Mocking
7. `unittest.mock`
8. Jest
9. Jest Matchers
10. TDD
11. Code Coverage

## High Priority ⭐⭐

12. Python unittest
13. Mocha
14. Chai
15. Async Testing
16. React Component Testing

## Medium Priority ⭐

17. Snapshot Testing
18. Advanced Plugins
19. ESLint
20. Pylint

---

# ✅ FINAL SKILL CHECKLIST

By the end of Module 4, you should be able to:

* [ ] Explain the Testing Pyramid
* [ ] Write AAA-based tests
* [ ] Write PyTest tests
* [ ] Use PyTest fixtures
* [ ] Use parameterization
* [ ] Test exceptions
* [ ] Use Python unittest
* [ ] Use `setUp()` and `tearDown()`
* [ ] Mock database calls
* [ ] Mock HTTP requests
* [ ] Verify mock arguments
* [ ] Write Jest tests
* [ ] Use Jest matchers
* [ ] Mock JavaScript functions
* [ ] Test React components
* [ ] Write Mocha tests
* [ ] Use Chai assertions
* [ ] Test asynchronous functions
* [ ] Follow TDD
* [ ] Generate coverage reports
* [ ] Write at least 10 meaningful tests
