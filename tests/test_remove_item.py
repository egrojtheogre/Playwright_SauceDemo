
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage  #
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage    #
from playwright.sync_api import expect

import pytest


def test_remove_item_cart(page):
    # Initialize all pages
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)
    cart = CartPage(page)

    # 1. Login
    login.navigate()
    login.login("standard_user", "secret_sauce")

    # 2. Add product & Go to cart
    inventory.add_bolt_tshirt_to_cart()
    inventory.add_onesie_to_cart()
    inventory.go_to_cart()

    #3. Remove one product
    cart.remove_first_item()
    cart.go_to_checkout()

    # 3. Complete Information
    checkout.fill_checkout_info("John", "Connor", "10121")

    # 4. Final Step & Verification
    checkout.finish_checkout()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
    # expect(checkout.complete_header).to_have_text("WRONG HEADER TEXT")
    pass