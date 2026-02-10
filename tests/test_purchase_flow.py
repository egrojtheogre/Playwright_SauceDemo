# This file contains tests related to purchase flow, defined as functions, which perform several calls to different files inside pages folder.
# some modules are imported from playwright api

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage  #
from pages.checkout_page import CheckoutPage    #
from playwright.sync_api import expect

import pytest

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
    checkout.fill_checkout_info("John", "Connor", "10121")

    # 4. Final Step & Verification
    checkout.finish_checkout()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
    # expect(checkout.complete_header).to_have_text("WRONG HEADER TEXT")
    pass


def test_full_purchase_cheap(page):
    # Initialize all pages
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)

    # 1. Login
    login.navigate()
    login.login("standard_user", "secret_sauce")

    # 2. Sort price low to high
    inventory.sort_by_price_low_to_high()

    # 3. Add to cart
    inventory.add_onesie_to_cart()
    inventory.add_bike_light_to_cart()

    # 4. go to cart
    inventory.go_to_cart()
    page.locator("#checkout").click()  # Quick click on checkout button

    # 5. Complete Information
    checkout.fill_checkout_info("John", "Connor", "10121")

    # 6. Final Step & Verification
    checkout.finish_checkout()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
    pass

def test_full_purchase_expensive(page):
    # Initialize all pages
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)

    # 1. Login
    login.navigate()
    login.login("standard_user", "secret_sauce")

    # 2. Sort price low to high
    inventory.sort_by_price_high_to_low()

    # 3. Add to cart
    inventory.add_fleece_jacket_to_cart()
    inventory.add_backpack_to_cart()

    # 4. go to cart
    inventory.go_to_cart()
    page.locator("#checkout").click()  # Quick click on checkout button

    # 5. Complete Information
    checkout.fill_checkout_info("John", "Connor", "10121")

    # 6. Final Step & Verification
    checkout.finish_checkout()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
    pass