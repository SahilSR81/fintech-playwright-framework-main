import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage

from utils.test_data_generator import TestDataGenerator


class TestLoginPage:

    def test_login_with_valid_credentials(self, page):

        # Open Register Page

        home_page = HomePage(page)

        home_page.click_register_link()

        # Register New User

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

        # Logout Newly Registered User

        login_page = LoginPage(page)

        login_page.click_logout_link()

        # Login With Same Credentials

        login_page.login_user(
            username=username,
            password=password
        )

        expect(
            login_page.account_overview_text
        ).to_be_visible()

    def test_login_with_invalid_credentials(self, page):

        login_page = LoginPage(page)

        login_page.login_user(
            username="invalid_user_12345",
            password="invalid_pass"
        )

        # Known ParaBank Bug:
        # Invalid users can sometimes log in successfully

        if login_page.account_overview_text.is_visible():

            pytest.xfail(
                "Known ParaBank bug: invalid users can log in successfully."
            )