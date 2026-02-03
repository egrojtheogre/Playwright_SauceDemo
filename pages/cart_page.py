
class CartPage:
    def __init__(self, page):
        self.page = page
        # Using the unique data-test attribute (Best Practice!)
        self.burger_menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        self.first_remove_button = page.locator("button[id^='remove-']").first
        self.checkout_button = page.locator("[data-test='checkout']")

    def remove_first_item(self):
        self.first_remove_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def go_to_checkout(self):
        self.checkout_button.click()