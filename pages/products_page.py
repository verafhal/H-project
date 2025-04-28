from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown = page.locator('.product_sort_container')
        self.products_title =page.locator('.title')
        self.add_buttons = page.locator('button.btn_inventory')


    def verify_products_header_visible(self):
        assert self.products_title.is_visible(), "Products header should be visible"


    def sort_by_price_low_to_high(self):
        self.sort_dropdown.select_option('lohi')


    def _get_all_product_prices(self):
        """Helper method to return list of all product prices as floats."""
        prices_text = self.page.locator('.inventory_item_price').all_inner_texts()
        return [float(price.replace('$', '')) for price in prices_text]


    def verify_sorting_low_to_high(self):
        prices_float = self._get_all_product_prices()
        assert prices_float == sorted(prices_float), f"Products are not sorted correctly: {prices_float}"


    def add_cheapest_and_most_expensive_products(self):
        prices_float = self._get_all_product_prices()
        cheapest_index = prices_float.index (min(prices_float))
        most_expensive_index = prices_float.index(max(prices_float))

        self.add_buttons.nth(cheapest_index).click()
        self.add_buttons.nth(most_expensive_index).click()
