import re
from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):

        self.page = page

        # Locators
        self.register_link = page.get_by_role("link", name="Register")
        self.forgot_login_info_link = page.get_by_role("link", name="Forgot login info?")

        self.customer_login_heading = page.get_by_role("heading", name="Customer Login")

        self.parabank_logo = page.get_by_role("img", name="ParaBank")

    # Actions

    def click_register_link(self):

        self.register_link.click()

    def click_forgot_login_info_link(self):

        self.forgot_login_info_link.click()