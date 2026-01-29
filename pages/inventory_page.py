
class InventoryPage:
    def __init__(self, page):
        self.page = page
        # Using the unique data-test attribute (Best Practice!)
        self.burger_menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.backpack_add_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("[data-test='checkout']")

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def go_to_cart(self):
        self.cart_link.click()

    def logout(self):
        # 1. Open the sidebar
        self.burger_menu_button.click()
        # 2. Click the logout link (Playwright waits for it to be visible!)
        self.logout_link.click()

