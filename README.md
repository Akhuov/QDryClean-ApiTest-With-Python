# QDryClean QA Automation Framework

A clean and structured Python-based QA automation framework for **QDryCleaning** service.  
Technologies used: **Pytest**, **Playwright**, **Requests**, **Allure**.

---

## Table of Contents
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Parallel Test Execution](#parallel-test-execution)
- [Repeating Tests](#repeating-tests)
- [Linting with Ruff](#linting-with-ruff)
- [Generating Reports](#generating-reports)
- [References](#references)
---

## Installation

1. Clone the repository and create a virtual environment:
```cmd
python -m venv venv
venv\Scripts\activate
```

2. Install all required packages using ***requirements.txt***:

```cmd
pip install -r requirements.txt
```
* requirements.txt includes all mandatory libraries:
  * playwright (for browser automation)
  * pytest (test runner)
  * pytest-playwright (Playwright plugin for pytest)
  * requests (API testing)
  * python-dateutil (date handling)
  * pytest-xdist (parallel test execution)
  * pytest-repeat (repeating tests)
  * ruff (code linting)
  * "allure-pytest (Allure reporting)"

3. Install Browsers:
```cmd
playwright install
```

---

# Running Tests
Run all tests:
```cmd
pytest
```

Run with verbose output and short traceback:
```cmd
pytest -v --tb=short
```
---

# Parallel Test Execution
Run tests in parallel (uses pytest-xdist from requirements.txt):
```cmd
pytest -n 4
```
-n 4 — runs tests on 4 parallel workers.

---

# Repeating Tests
Run a test multiple times (uses pytest-repeat from requirements.txt):
```cmd
pytest --count=5
```

# Linting with Ruff
Ruff helps keep your code clean and consistent (installed via requirements.txt):
```cmd
ruff check .          # check code
ruff check . --fix    # check and automatically fix issues
```
---

# Generating Reports
Run tests with an HTML report:
```cmd
pytest --template=html1/index.html --report=reports\file_name.html
```
---
# References
* [Playwright Python CLI Options](https://playwright.dev/python/docs/test-runners#cli-arguments)
* [Allure Pytest Documentation](https://docs.qameta.io/allure/#_pytest)

***Happy Testing! 🚀***
