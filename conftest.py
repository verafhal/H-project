import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

# ------------------- UI Fixtures -------------------

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # for CI/CD needs change it to (headless=True) mode
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('standard_user', 'secret_sauce')
    return login_page


# ------------------- API Fixtures -------------------

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api_request_context():
    with sync_playwright() as p:
        request_context = p.request.new_context(base_url=BASE_URL)
        yield request_context
        request_context.dispose()

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL