from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.register_page import RegisterPage

from utils.test_data_generator import TestDataGenerator


class TestRegisterPage:

    def test_register_with_blank_fields(self, page):

        home_page = HomePage(page)

        home_page.click_register_link()

        register_page = RegisterPage(page)

        register_page.click_register_button()

        expect(
            register_page.password_required_message
        ).to_be_visible()

    def test_register_with_valid_details(self, page):

        home_page = HomePage(page)

        home_page.click_register_link()

        register_page = RegisterPage(page)

        username = TestDataGenerator.generate_username()

        password = TestDataGenerator.generate_password()

        register_page.fill_registration_form(
            first_name="Sahil",
            last_name="Singh",
            address="103b",
            city="Ranchi",
            state="Jharkhand",
            zip_code="834001",
            phone_number="9876543210",
            ssn="1234",
            username=username,
            password=password
        )

        register_page.click_register_button()

        expect(
            register_page.success_message
        ).to_be_visible()

        print(f"\nGenerated Username: {username}")
        print(f"Generated Password: {password}")

        return username, password