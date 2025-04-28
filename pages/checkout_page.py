from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.complete_header = page.locator('.complete-header')

    def start_checkout(self):
        self.checkout_button.click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def verify_order_completion(self):
        assert self.complete_header.is_visible(), "Order completion message should be visible"










