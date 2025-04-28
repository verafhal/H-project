import pytest
from pages.login_page import LoginPage

@pytest.mark.neg
def test_negative_login_with_invalid_credentials(page):
    # Open the login page
    login_page = LoginPage(page)
    login_page.navigate()

    # Try to logout first, just in case
    login_page.logout()

    # Try to login with valid credentials
    login_page.login('wrong_user', 'wrong_password')

    # Verify that an error message appears
    login_page.assert_login_error()