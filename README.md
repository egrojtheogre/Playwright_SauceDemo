## Playwright SauceDemo Automation Framework
A little automation suite built with Python, Playwright, and Pytest targeting the SauceDemo (Swag Labs) platform.

## 🚀 Features
Page Object Model (POM): Clean separation of UI locators and test logic.

Data-Driven Testing: Parametrized tests to validate multiple user personas.

Automated Reporting: Self-contained HTML reports with failure screenshots.

Cross-Browser Support: Configured for Chromium, Firefox, and WebKit.

Categorization: Custom Pytest markers for smoke and negative suites.

## 🛠️ Setup & Installation
Clone the repo:

   ```bash
   
   git clone https://github.com/egrojtheogre/Playwright_SauceDemo.git
   cd Playwright_SauceDemo
   ```

Create a virtual environment:

   ```bash
   
   python -m venv .venv
   .venv\Scripts\activate
   ```
Install dependencies:

   ```bash
   
   pip install pytest-playwright pytest-html
   playwright install
   ```

## 🧪 Running Tests
Run all tests and generate a report:

   ```bash
   
   pytest --html=test_results/report.html --self-contained-html
   ```
Run only Smoke tests:

   ```bash
   
   pytest -m smoke --headed
   ```
Run in a specific browser:

   ```bash
   
   pytest --browser firefox --headed
   ```