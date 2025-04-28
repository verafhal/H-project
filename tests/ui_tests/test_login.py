import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
def test_login_with_valid_credentials(page):
    # Open the login page
    login_page =LoginPage(page)
    login_page.navigate()

    # Try to logout first, just in case
    login_page.logout()

    #  Try to login with valid credentials
    login_page.login('standard_user','secret_sauce')

    # Verify that the user is navigated to the Products page
    assert page.locator('.title').inner_text() == "Products", "User should be navigated to the Products page"

