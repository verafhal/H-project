
def test_intentional_ui_failure(page):
    page.goto("https://www.saucedemo.com/")
    # This will fail — the selector doesn't exist
    assert page.is_visible("div.this_element_does_not_exist"), "This element should be visible"