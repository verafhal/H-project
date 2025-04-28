from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#user-name')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#login-button')
        self.error_message = page.locator('[data-test="error"]')
        self.burger_menu_button =page.locator('#react-burger-meny-btn')
        self.logout_link = page.locator('#logout_sidebar_link')


    def navigate(self):
        self.page.goto('https://www.saucedemo.com/')


    def login(self,username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        if self.burger_menu_button.is_visible(timeout=2000):  # Try to detect if logged in
            self.burger_menu_button.click()
            self.logout_link.wait_for(state="visible", timeout=3000)
            self.logout_link.click()
            self.page.wait_for_selector('#login-button', timeout=3000)


    def assert_login_error(self):
        assert self.error_message.is_visible(), "Expected error message to be visible for invalid login"
        error_text = self.error_message.inner_text()
        assert "Epic sadface" in error_text, f"Unexpected error text: {error_text}"


