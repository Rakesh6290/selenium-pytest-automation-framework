# E-Commerce Selenium Pytest Automation Framework

A scalable and maintainable UI automation framework built using Python, Selenium, Pytest, and Page Object Model (POM) architecture.

This project automates end-to-end test scenarios for the SauceDemo e-commerce application, including login, product validation, cart operations, sorting, checkout, logout, and negative test scenarios.

---
                 
# Project Highlights           

* Selenium WebDriver with Python
* Pytest Testing Framework
* Page Object Model (POM)
* JSON Data-Driven Testing
* Reusable Base Page Utilities
* Cross Browser Testing
* HTML Reporting
* Parallel Test Execution
* Allure Reporting
* Screenshot Capture on Failure
* Pytest Fixtures & Hooks
* Smoke / Regression / Negative Test Markers
* Dynamic XPath Handling
* Explicit Waits
* Jenkins CI/CD Ready
* GitHub Integration

---

# Tech Stack

| Technology        | Usage                    |
| ----------------- | ------------------------ |
| Python            | Programming Language     |
| Selenium          | Browser Automation       |
| Pytest            | Test Execution Framework |
| Pytest HTML       | HTML Reporting           |
| Allure Reports    | Advanced Reporting       |
| WebDriver Manager | Driver Management        |
| Jenkins           | CI/CD Integration        |
| JSON              | Test Data Management     |
| Git & GitHub      | Version Control          |

---

# Project Structure

```text
selenium-pytest-automation-framework/
│   
├── SauceDemo_Manual_Testing
│   ├── BugReport.xlsx
│   ├── TestCases.xlsx
│   └── TestPlan_documentation.docx
│
│
│
├── data/
│   └── login_test_data.json
│   └── product_test_data.json
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_01_login.py
│   ├── test_02_product.py
│   ├── test_03_sorting.py
│   ├── test_04_checkout.py
│   └── test_05_logout.py
│
├── screenshots/
├── allure-results/
├── reports/
├── utils/
│   ├── config.py
│   └── driver_factory.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Jenkinsfile
└── README.md
```

---

# Framework Features

## 1. Page Object Model (POM)

Each application page is separated into individual classes for better maintainability and reusability.

Example:

* LoginPage
* ProductPage
* CartPage
* CheckoutPage

Benefits:

* Clean code structure
* Reusable methods
* Easy maintenance
* Better scalability

---

## 2. Data-Driven Testing Using JSON

All test data is maintained in JSON files.

Example:

```json
{

    "valid_user": {
      "username": "standard_user",
      "password": "secret_sauce"
    }
  
}
```

Benefits:

* No hardcoded test data
* Easy updates
* Scalable framework design

---

## 3. Screenshot Capture on Failure

The framework automatically captures screenshots whenever a test fails.

Example:

```text
screenshots/test_valid_login.png
```

Benefits:

* Easy debugging
* Faster issue analysis
* Better reporting

---

## 4. Cross Browser Testing

Framework supports:

* Chrome
* Firefox
* Edge

Execution Example:

```bash
pytest -v --browser=chrome
pytest -v --browser=firefox
pytest -v --browser=edge
```

---

## 5. HTML Reporting

Pytest HTML reports are generated after execution.

Execution:

```bash
pytest --html=report.html
```

Benefits:

* Professional execution reports
* Easy result sharing
* Pass/Fail visibility

---


## 6. Allure Reporting
Integrated Allure Reporting for advanced execution reports.

Features:

Interactive reports
Pass/Fail statistics
Graphs and trends
Execution history
Screenshot integration

Generate Report:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---
## 7. Parallel Test Execution
Framework supports parallel execution using pytest-xdist.

Execution Example:

```bash
pytest -n 4
```
Benefits:

* Faster execution
* Reduced execution time
* Better CI/CD performance

---
## 8. Jenkins CI/CD Integration
Framework integrated with Jenkins Pipeline.

Features:

* Automated test execution
* GitHub integration
* HTML report publishing
* Jenkinsfile support
* CI/CD automation


# Automated Test Scenarios

## Login Module

* Valid Login
* Invalid Username
* Invalid Password
* Empty Username
* Empty Password
* Both Invalid Credentials
* Both Fields Empty
* Locked User Validation

---

## Product Module

* Add Product to Cart
* Remove Product from Cart
* Verify Product Visibility
* Verify Cart Count

---

## Sorting Module

* Sort Products A-Z
* Sort Products by Price Low-High

---

## Checkout Module

* Successful Checkout Flow
* Empty First Name Validation
* Empty Last Name Validation
* Empty Zipcode Validation
* Remove All Items from Cart
* Finish Order Validation

---

## Logout Module

* Successful Logout Validation

---

## Security / Session Validation

* Unauthorized Access Validation

---


# Installation Setup

## Clone Repository

```bash
git clone <repository_url>
cd Login_Automation_Project
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Test Execution

## Run All Tests

```bash
pytest -v
```

---

## Run Smoke Tests

```bash
pytest -m smoke
```

---

## Run Regression Tests

```bash
pytest -m regression
```

---

## Run Negative Tests

```bash
pytest -m negative
```

---

## Run Cross Browser Tests

### Chrome

```bash
pytest -v --browser=chrome
```

### Firefox

```bash
pytest -v --browser=firefox
```

### Edge

```bash
pytest -v --browser=edge
```

---

# Jenkins CI/CD Integration

The framework is CI/CD ready using Jenkins.

Features:

* Automated execution
* GitHub integration
* HTML report publishing
* Jenkins pipeline support

---

# Key Automation Concepts Used

* Explicit Waits
* Dynamic XPath
* Reusable Methods
* Fixtures
* Hooks
* Assertions
* Data-Driven Testing
* Browser Parameterization
* Parallel Execution
* CI/CD Integration
* End-to-End Testing

---

# Future Enhancements

* API Automation Integration
* Docker Integration
* Selenium Grid
* GitHub Actions
* Database Validation
* Cloud Execution
* Playwright Automation

---

# Execution Result

```text
===========================================
22 passed in 152.70s
===========================================
```

