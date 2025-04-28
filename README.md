# QA Automation Project – UI & API Testing

This project contains both UI and API automated tests developed using Playwright (Python) and Pytest.  
It demonstrates automation best practices such as Page Object Model (POM), fixtures, and clean assertions.

## 📚 Tools and Technologies

- Python 3.10+
- Playwright (Python bindings)
- Pytest
- Pytest markers for test organization
- POM (Page Object Model) for UI tests
- JSONPlaceholder mock API for API tests

## 🛠 Installation Instructions

1. Clone the repository or download the project.
2. (Optional) Create and activate a virtual environment.
3. Install the project dependencies:

```
pip install -r requirements.txt
playwright install
```

## 🛠 How to Run Tests

### Run All Tests (UI + API)
```
pytest
```
### Run Only UI Tests

All UI tests are located inside tests/ui_tests/.
```
pytest -m ui
```
Run a specific UI test file:
```
pytest tests/ui_tests/test_shopping.py
```
Run a specific UI test function:
```
pytest tests/ui_tests/test_shopping.py::test_successful_shopping_flow
```

### Run Only API Tests
All API tests are located inside tests/api_tests/.
```
pytest -m api
```
Run a specific API test file:
```
pytest tests/api_tests/test_posts_api.py
```
Run a specific API test function:
```
pytest tests/api_tests/test_posts_api.py::test_get_all_posts
```

## 📂 Folder Structure
```
project/
├── pages/                # Page Object Model files for UI
├── tests/                # Test cases for UI and API
│    ├── ui_tests/
│    └── api_tests/
├── utils/                # Helper utilities (e.g., safe JSON parsing)
│    └── json_helpers.py
├── conftest.py           # Fixtures for Playwright browser, login, API context
├── pytest.ini            # Pytest markers configuration
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

```
## 📢 Notes

UI tests interact with the SauceDemo web application.

API tests interact with the JSONPlaceholder public mock API.

JSONPlaceholder is a fake API, so POST operations succeed but do not persist new data.

API response JSON parsing is safely handled using a custom helper function (`safe_json_parse`)
to ensure error-resilient tests.

## �� Error Handling and Troubleshooting Questions

1. How you would handle intermittent or flaky tests in your automation suite?

  Handling Flaky Tests - Action Plan (by Priority DESC)

- Investigate and analyze failure patterns (logs, videos, retries) to identify the root causes.
- Stabilize locators,add smart waits (wait for conditions, not fixed timeouts), full test independence.
- Optimize environment stability (ensure network, backend, and browsers are reliable).
- Temporarily move unstable tests into a dedicated suite for monitoring, prioritize them based on business impact,
  and handle them systematically as part of the regular sprint planning process.

2. If an automated UI test fails due to a DOM element not being available, what steps would  you take to diagnose and resolve the issue? 

  Diagnosing and Resolving Missing DOM Element Failures:
  
- Review Logs,screenshots and video recording for the better understanding of the case.
- Analyze test timing.
- Validate the locator.
- Check for environmental issues.
- Collaborate with developers if the issue is due to a real application defect.
- Refactor the test.

3. How would you handle and report API failures within your automated test runs? 

- Explore full API request and response details for every filed request.
- Automatically capture API request and response whenever a test fails(include in reports for quick and easy research)
- Classify failures — distinguish between automation errors (e.g., wrong expectations) 
  and real backend issues (e.g., 500 server error, bad data).
- Prioritize based on business impact and collaborate with developers and backend teams
  if failures are due to system defects.

4. What strategies would you employ if your test automation suite encounters timeouts or  slow responses? 
 
- Analyze timeout logs and performance data to confirm if slowness is real or test-related.
- Use smart dynamic waits.
- Optimize application state and environment — clean test data, stable backend services, correct network conditions.
- Parallelize tests when possible to reduce overall suite execution time.
- Monitor test timings regularly to catch performance regressions early through CI dashboards.
- Collaborate with developers team if slow performance is found to be an application issue.

5. Provide an example of how you would use logging or debugging information effectively  when troubleshooting failed automation tests.

To use debugging information effectively, I can design my automation with clear, detailed logs, meaningful exception handling,descriptive assertion messages, etc.
When a failure occurs, this structured information immediately shows what action was taken, what was expected, and what actually happened, making root cause analysis fast and accurate without guessing or rerunning tests.

Examples of techniques:
- Attach artifacts (screenshots, HAR files, API request/response dumps)
- Use custom exception messages
- Capture browser console logs for UI tests
- Capture network logs during UI/API test failures
- Timestamp every log entry
- Tag logs by test step or module
- Integrate logs into test reports (like Allure, HTML reports)
- Store retry attempts and outcomes (if using retries)
