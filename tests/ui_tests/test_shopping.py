import pytest
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.ui
def test_successful_shopping_flow(page, login):
    login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    #Product Page
    products_page.verify_products_header_visible()
    products_page.sort_by_price_low_to_high()
    products_page.verify_sorting_low_to_high()
    products_page.add_cheapest_and_most_expensive_products()

    # Cart Page
    cart_page.go_to_cart()
    cart_page.verify_cart_items_count(2)

    # Checkout Process
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('John', 'Doe', '12345')
    checkout_page.finish_checkout()

    # Verify Checkout Completion
    checkout_page.verify_order_completion()



