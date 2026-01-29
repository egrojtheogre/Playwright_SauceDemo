
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage  # Add this!
from pages.checkout_page import CheckoutPage    # Add this!
from playwright.sync_api import expect

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login(page):
    login_page = LoginPage(page)

    # Action
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Assertion: Playwright assertions have built-in retry logic!
    from playwright.sync_api import expect
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    pass

@pytest.mark.negative
def test_locked_out_user(page):
    login = LoginPage(page)
    login.navigate()
    login.login("locked_out_user", "secret_sauce")

    # Assert that the error message is visible and contains the right text
    expect(login.error_message).to_be_visible()
    expect(login.error_message).to_contain_text("Sorry, this user has been locked out.")
    pass

@pytest.mark.regression
def test_full_purchase_flow(page):
    # Initialize all pages
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)

    # 1. Login
    login.navigate()
    login.login("standard_user", "secret_sauce")

    # 2. Add product & Go to cart
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()
    page.locator("#checkout").click()  # Quick click on checkout button

    # 3. Complete Information
    checkout.fill_checkout_info("Jorge", "Tester", "12345")

    # 4. Final Step & Verification
    checkout.finish_checkout()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
    # expect(checkout.complete_header).to_have_text("WRONG HEADER TEXT")
    pass