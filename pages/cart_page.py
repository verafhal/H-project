from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator('.shopping_cart_link')
        self.cart_items = page.locator('.cart_item')


    def go_to_cart(self):
        self.cart_icon.click()


    def verify_cart_items_count(self,expected_count):
        items = self.cart_items.count()
        assert items == expected_count, f"Expected {expected_count} items in cart, but found {items}"