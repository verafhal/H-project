import pytest
@pytest.mark.ui

def test_login_with_valid_credentials(login):
    login_page = login('standard_user', 'secret_sauce')
    assert login_page.get_title() == "Products", "User should be navigated to the Products page"