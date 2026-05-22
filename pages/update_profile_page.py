from playwright.sync_api import (
    Page,
    expect
)


class UpdateProfilePage:

    def __init__(
        self,
        page: Page
    ):

        self.page = page

        # Navigation locator
        self.update_contact_info_link = page.get_by_role(
            "link",
            name="Update Contact Info"
        )

        # Form locators
        self.first_name_input = page.locator(
            '[id="customer.firstName"]'
        )

        self.last_name_input = page.locator(
            '[id="customer.lastName"]'
        )

        self.street_input = page.locator(
            '[id="customer.address.street"]'
        )

        self.city_input = page.locator(
            '[id="customer.address.city"]'
        )

        self.state_input = page.locator(
            '[id="customer.address.state"]'
        )

        self.zip_code_input = page.locator(
            '[id="customer.address.zipCode"]'
        )

        self.phone_number_input = page.locator(
            '[id="customer.phoneNumber"]'
        )

        # Update button
        self.update_profile_button = page.get_by_role(
            "button",
            name="Update Profile"
        )

        # Success message
        self.success_message = page.get_by_text(
            "Your updated address and phone number have been added to the system."
        )

        # Logout
        self.logout_link = page.get_by_role(
            "link",
            name="Log Out"
        )

    def navigate_to_update_contact_info_page(self):

        self.update_contact_info_link.click()

    def update_contact_information(
        self,
        first_name: str,
        last_name: str,
        street: str,
        city: str,
        state: str,
        zip_code: str,
        phone_number: str
    ):

        self.first_name_input.click()
        self.first_name_input.fill(first_name)

        self.last_name_input.click()
        self.last_name_input.fill(last_name)

        self.street_input.click()
        self.street_input.fill(street)

        self.city_input.click()
        self.city_input.fill(city)

        self.state_input.click()
        self.state_input.fill(state)

        self.zip_code_input.click()
        self.zip_code_input.fill(zip_code)

        self.phone_number_input.click()
        self.phone_number_input.fill(phone_number)

        self.update_profile_button.click()

    def verify_profile_updated_successfully(self):

        expect(
            self.success_message
        ).to_be_visible()

    def logout_user(self):

        self.logout_link.click()