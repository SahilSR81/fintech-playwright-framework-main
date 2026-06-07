# 🚀 Fintech Playwright Framework

<div align="center">

### End-to-End QA Automation Framework using Playwright + Pytest

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Automation-2EAD33?style=flat-square&logo=playwright)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?style=flat-square&logo=pytest)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Reports-FF6B6B?style=flat-square)](https://docs.qameta.io/allure/)

</div>

---

# 📌 Overview

This project is a modern End-to-End QA automation framework built using **Playwright**, **Pytest**, and **Python** for testing fintech-style web applications.

The framework follows the **Page Object Model (POM)** design pattern and focuses on:
- Scalable automation architecture
- Reusable components
- Maintainable test structure
- Real-world workflow validation
- Robust test execution practices

### 🔗 Application Under Test

https://parabank.parasoft.com

---

# 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Running Tests](#️-running-tests)
- [Allure Reports](#-allure-reports)
- [Reporting & Debugging](#-reporting--debugging)
- [Learning Resources](#-learning-resources)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)

---

# ✨ Features

- ✅ Playwright with Python
- ✅ Pytest-based execution
- ✅ Page Object Model (POM)
- ✅ End-to-End workflow testing
- ✅ Allure reporting
- ✅ Cross-browser execution
- ✅ Reusable utilities & helpers
- ✅ Logging support
- ✅ Screenshot capture support
- ✅ Config-driven execution

---

# 🛠️ Tech Stack

| Tool | Purpose | Version |
|------|---------|---------|
| Python | Programming Language | 3.10+ |
| Playwright | Browser Automation | 1.40+ |
| Pytest | Test Framework | 7.4+ |
| Allure | Reporting | 2.29+ |
| ConfigParser | Configuration Management | Built-in |

---

# 📁 Project Structure

```bash
fintech-playwright-framework-main/
│
├── .github/
│   └── workflows/
│       └── e2e-test.yml
│
├── config/
│   └── config.ini
│
├── pages/
│   ├── accounts_overview_page.py
│   ├── accounts_page.py
│   ├── bill_pay_page.py
│   ├── find_transactions_page.py
│   ├── forgot_login_info_page.py
│   ├── home_page.py
│   ├── loan_request_page.py
│   ├── login_page.py
│   ├── open_account_page.py
│   ├── register_page.py
│   ├── site_navigation_page.py
│   ├── transfer_funds_page.py
│   ├── update_profile_page.py
│   └── __init__.py
│
├── reports/
│   ├── allure-results/
│   ├── logs/
│   ├── screenshots/
│   └── report.html
│
├── tests/
│   ├── test_accounts_overview_page.py
│   ├── test_accounts_page.py
│   ├── test_bill_pay_page.py
│   ├── test_end2end_happy_path.py
│   ├── test_find_transactions_page.py
│   ├── test_forgot_login_info_page.py
│   ├── test_home_page.py
│   ├── test_loan_request_page.py
│   ├── test_login_page.py
│   ├── test_open_account_page.py
│   ├── test_register_page.py
│   ├── test_site_navigation_page.py
│   ├── test_transfer_page.py
│   ├── test_update_profile_page.py
│   └── conftest.py
│
├── utils/
│   ├── config_reader.py
│   ├── logger.py
│   ├── screenshot_helper.py
│   ├── test_data_generator.py
│   ├── waits.py
|   ├── session_manager.py
│   └── __init__.py
│
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

---

# ⚡ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/SahilSR81/fintech-playwright-framework-main.git
cd fintech-playwright-framework-main
```

### 2️⃣ Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Playwright Browsers

```bash
playwright install
```

---

# ▶️ Running Tests

### Run Complete Test Suite

```bash
python -m pytest -v
```

### Run Specific Test File

```bash
python -m pytest tests/test_login_page.py -v
```

### Run Tests with Browser UI

```bash
python -m pytest -v --headed
```

### Run Tests with Allure Reports

```bash
python -m pytest -v --alluredir=reports/allure-results
```

### Generate Allure Report

```bash
allure serve reports/allure-results
```

### View Allure Report Locally

1. Run tests and generate Allure results:

```bash
python -m pytest -v --alluredir=reports/allure-results
```

2. Start the Allure server and open the report in your browser:

```bash
allure serve reports/allure-results
```

3. For a static report, generate to `reports/allure-report`:

```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

> The framework now also writes Allure environment details and report categories automatically, so the generated report includes environment info, grouped failure categories, and attached screenshots for failed tests.

---

# 📊 Allure Reports

The framework supports detailed reporting with:

- ✅ Execution status
- ✅ Logs and details
- ✅ Screenshot capture on failures
- ✅ Failure tracking
- ✅ Execution timeline
- ✅ Test statistics

---

# 📸 Reporting & Debugging

Current framework utilities include:

- ✅ Reusable waits and conditions
- ✅ Screenshot helpers for debugging
- ✅ Centralized configuration management
- ✅ Comprehensive logging support
- ✅ Test data generation utilities
- ✅ Dynamic test data handling

---

# 📚 Learning Resources

- 📖 [Playwright Python Documentation](https://playwright.dev/python/)
- 🧪 [Pytest Documentation](https://docs.pytest.org/)
- 🏗️ [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- 🔄 [GitHub Actions Workflows](https://docs.github.com/en/actions)
- 📊 [Allure Report Documentation](https://docs.qameta.io/allure/)
- 🎓 [Best Practices in Test Automation](https://www.guru99.com/test-automation-best-practices.html)

---

# 🚧 Future Enhancements

- [ ] Better exception handling
- [ ] More robust retry mechanisms
- [ ] Advanced logging improvements
- [ ] Parallel test execution
- [ ] Data-driven testing
- [ ] Environment-based execution
- [ ] Enhanced reporting
- [ ] API testing integration
- [✅] GitHub Actions CI/CD pipeline optimization

---

# 🤝 Contributing

Contributions, improvements, criticism and suggestions are welcome.

Fork the repository and create a pull request.

---

<div align="center">

## "Make it work. Make it clean. Make it scalable." 🚀

</div>
