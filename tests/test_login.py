import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

@pytest.mark.parametrize("username, should_pass", [
    ("standard_user", True),
    ("problem_user", True),
    ("performance_glitch_user", True),
    ("error_user", True),
    ("visual_user", True),
    ("locked_out_user", False)  # This one we expect to fail login
])
@pytest.mark.smoke
def test_multiple_user_logins(page, username, should_pass):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login(username, "secret_sauce")

    if should_pass:
        # Happy Path: Verify we reach inventory and then logout
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        inventory_page.logout()
        expect(page).to_have_url("https://www.saucedemo.com/")
    else:
        # Negative Path: Verify error message appears
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text("Sorry, this user has been locked out.")

    pass
