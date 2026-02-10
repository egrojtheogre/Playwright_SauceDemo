# This file contains elements to interact on the checkout page, as well as the actions that can be performed on the page, defined as functions.
# this is the best practice according to POM (Page Object Model)


class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.zip_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.complete_header = page.locator(".complete-header")

    def fill_checkout_info(self, first, last, zip):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.zip_code.fill(zip)
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()
