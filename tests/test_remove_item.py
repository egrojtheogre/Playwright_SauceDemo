
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
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

    # 3. Remove one product and go checkout
    cart.remove_first_item()
    cart.go_to_checkout()

    # 4. Complete Information
    checkout.fill_checkout_info("John", "Connor", "10121")

    # 4. Final Step & Verification
    checkout.finish_checkout()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
    # expect(checkout.complete_header).to_have_text("WRONG HEADER TEXT")
    pass


def test_remove_shop_checkout(page):
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
    inventory.add_fleece_jacket_to_cart()
    inventory.go_to_cart()

    # 3. Remove one product and back to inventory
    cart.remove_first_item()
    cart.continue_shopping()

    # 4 Add another item and go to cart
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    # 5. Checkout and Complete Information
    cart.go_to_checkout()
    checkout.fill_checkout_info("John", "Connor", "10121")

    # 6. Final Step & Verification
    checkout.finish_checkout()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
    # expect(checkout.complete_header).to_have_text("WRONG HEADER TEXT")
    pass