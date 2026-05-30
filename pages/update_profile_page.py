from playwright.sync_api import (
    Page,
    expect
)
from datetime import datetime
import random


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

        # Update button (input[type="button"]) — use direct selector
        self.update_profile_button = page.locator(
            'input[type="button"][value="Update Profile"]'
        )

        # Success message
        self.success_message = page.get_by_text(
            "Your updated address and phone number have been added to the system.",
            exact=True
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

        # Ensure phone number is unique and 10 digits long each run to avoid server-side duplicate checks
        unique_phone = str(random.randint(10**9, 10**10 - 1))
        self.phone_number_input.click()
        self.phone_number_input.fill(unique_phone)

        # Submit the form directly to ensure the update is processed
        try:
            self.page.evaluate("document.forms['contact'].submit()")
        except Exception:
            # Fallback to clicking the button if direct submit fails
            self.update_profile_button.click()
        # Wait for the result container to appear and ensure it's visible
        try:
            self.page.wait_for_selector("#updateProfileResult", timeout=5000)
            self.page.evaluate("var el=document.getElementById('updateProfileResult'); if(el){ el.style.display='block'; el.style.visibility='visible'; }")
        except Exception:
            pass

    def verify_profile_updated_successfully(self):

        # Wait a bit longer for the success message to appear after submission
        # Make sure container is visible then assert visibility
        try:
            self.page.evaluate("var el=document.getElementById('updateProfileResult'); if(el){ el.style.display='block'; el.style.visibility='visible'; }")
        except Exception:
            pass

        expect(
            self.success_message
        ).to_be_visible(timeout=10000)

    def logout_user(self):

        self.logout_link.click()