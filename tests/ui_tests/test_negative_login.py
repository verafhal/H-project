import pytest
from pages.login_page import LoginPage
@pytest.mark.neg
@pytest.mark.parametrize("username, password, expected_error", [
    ("wrong_user", "wrong_pass", "Epic sadface"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
])
def test_negative_login(login, username, password, expected_error):
    login_page = login(username, password)
    login_page.assert_login_error(expected_error)
