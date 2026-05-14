from playwright.sync_api import Page


class ForgotLoginInfoPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators

        self.first_name_input = page.locator(
            "#firstName"
        )

        self.last_name_input = page.locator(
            "#lastName"
        )

        self.address_input = page.locator(
            "#address\\.street"
        )

        self.city_input = page.locator(
            "#address\\.city"
        )

        self.state_input = page.locator(
            "#address\\.state"
        )

        self.zip_code_input = page.locator(
            "#address\\.zipCode"
        )

        self.ssn_input = page.locator(
            "#ssn"
        )

        self.find_login_info_button = self.find_login_info_button = page.locator("input[value='Find My Login Info']")

        self.customer_lookup_heading = page.get_by_role(
            "heading",
            name="Customer Lookup"
        )

        # Known Application Behavior / Existing Bug

        self.customer_not_found_error_message = page.get_by_text(
            "Error! The customer"
        )

    # Actions

    def fill_first_name(self, first_name):

        self.first_name_input.fill(first_name)

    def fill_last_name(self, last_name):

        self.last_name_input.fill(last_name)

    def fill_address(self, address):

        self.address_input.fill(address)

    def fill_city(self, city):

        self.city_input.fill(city)

    def fill_state(self, state):

        self.state_input.fill(state)

    def fill_zip_code(self, zip_code):

        self.zip_code_input.fill(zip_code)

    def fill_ssn(self, ssn):

        self.ssn_input.fill(ssn)

    def click_find_login_info_button(self):

        self.find_login_info_button.click()

    # Reusable helper

    def fill_customer_lookup_form(
        self,
        first_name,
        last_name,
        address,
        city,
        state,
        zip_code,
        ssn
    ):

        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_address(address)
        self.fill_city(city)
        self.fill_state(state)
        self.fill_zip_code(zip_code)
        self.fill_ssn(ssn)
        