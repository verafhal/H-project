import os
import pytest
import allure
import requests

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

# ------------------- Base Configuration -------------------

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")


# ------------------- Session-Level Playwright -------------------

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


# ------------------- UI Fixtures -------------------

@pytest.fixture
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


# ------------- Parameterized Login Fixture with Logout -------------

@pytest.fixture
def login(page):
    """
    Fixture that returns a login function.
    It performs login with credentials, and handles logout after the test.
    """
    login_page = LoginPage(page)

    def _login(username: str, password: str) -> LoginPage:
        login_page.navigate()
        login_page.login(username, password)
        return login_page

    yield _login

    # Teardown – logout after test if possible
    try:
        login_page.logout()
    except Exception:
        pass


# ------------------- API Fixtures -------------------

@pytest.fixture(scope="session")
def api_request_context(playwright_instance, base_url):
    request_context = playwright_instance.request.new_context(base_url=base_url)
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session")
def auth_headers():
    # Replace with real token generation
    token = "your-token-here"
    return {"Authorization": f"Bearer {token}"}


# -------------- Screenshots on Failure & Allure Integration ---------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)

def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\nScreenshot saved to: {screenshot_path}")
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
