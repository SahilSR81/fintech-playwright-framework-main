from playwright.sync_api import Page


class RegisterPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators

        self.first_name_input = page.locator(
            "#customer\\.firstName"
        )

        self.last_name_input = page.locator(
            "#customer\\.lastName"
        )

        self.address_input = page.locator(
            "#customer\\.address\\.street"
        )

        self.city_input = page.locator(
            "#customer\\.address\\.city"
        )

        self.state_input = page.locator(
            "#customer\\.address\\.state"
        )

        self.zip_code_input = page.locator(
            "#customer\\.address\\.zipCode"
        )

        self.phone_number_input = page.locator(
            "#customer\\.phoneNumber"
        )

        self.ssn_input = page.locator(
            "#customer\\.ssn"
        )

        self.username_input = page.locator(
            "#customer\\.username"
        )

        self.password_input = page.locator(
            "#customer\\.password"
        )

        self.confirm_password_input = page.locator(
            "#repeatedPassword"
        )

        self.register_button = page.locator(
            "//input[@value='Register']"
        )

        # Validation Messages

        self.success_message = page.get_by_text(
            "Your account was created"
        )

        self.password_required_message = page.get_by_text(
            "Password confirmation is required."
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

    def fill_phone_number(self, phone_number):

        self.phone_number_input.fill(phone_number)

    def fill_ssn(self, ssn):

        self.ssn_input.fill(ssn)

    def fill_username(self, username):

        self.username_input.fill(username)

    def fill_password(self, password):

        self.password_input.fill(password)

    def fill_confirm_password(self, password):

        self.confirm_password_input.fill(password)

    def click_register_button(self):

        self.register_button.click()

    # Reusable Form Helper

    def fill_registration_form(
        self,
        first_name,
        last_name,
        address,
        city,
        state,
        zip_code,
        phone_number,
        ssn,
        username,
        password
    ):

        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_address(address)
        self.fill_city(city)
        self.fill_state(state)
        self.fill_zip_code(zip_code)
        self.fill_phone_number(phone_number)
        self.fill_ssn(ssn)
        self.fill_username(username)
        self.fill_password(password)
        self.fill_confirm_password(password)