
class InventoryPage:
    def __init__(self, page):
        self.page = page
        # Using the unique data-test attribute (Best Practice!)
        self.burger_menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.backpack_add_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.onesie_add_button = page.locator("[data-test='add-to-cart-sauce-labs-onesie']")
        self.bike_light_add_button = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.fleece_jacket_add_button = page.locator("[data-test='add-to-cart-sauce-labs-fleece-jacket']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.product_sort = page.locator("[data-test='product-sort-container']")



    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def add_onesie_to_cart(self):
        self.onesie_add_button.click()

    def add_bike_light_to_cart(self):
        self.bike_light_add_button.click()

    def add_fleece_jacket_to_cart(self):
        self.fleece_jacket_add_button.click()

    def go_to_cart(self):
        self.cart_link.click()

    def logout(self):
        # 1. Open the sidebar
        self.burger_menu_button.click()
        # 2. Click the logout link (Playwright waits for it to be visible!)
        self.logout_link.click()

    def sort_by_price_low_to_high(self):
        # Instead of clicking twice, we tell Playwright to select by the 'value'
        # The values in SauceDemo are: 'az', 'za', 'lohi', 'hilo'
        self.product_sort.select_option("lohi")

    def sort_by_price_high_to_low(self):
        self.product_sort.select_option("hilo")