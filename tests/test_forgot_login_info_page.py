import re
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.forgot_login_info_page import ForgotLoginInfoPage

class TestForgotLoginInfoPage:

    def test_forgot_login_info_page_navigation(self, page):

        home_page = HomePage(page)

        home_page.click_forgot_login_info_link()

        forgot_login_info_page = ForgotLoginInfoPage(page)

        expect(
            forgot_login_info_page.customer_lookup_heading
        ).to_be_visible()

    def test_find_login_info_with_blank_fields(self, page):

        home_page = HomePage(page)

        home_page.click_forgot_login_info_link()

        forgot_login_info_page = ForgotLoginInfoPage(page)

        forgot_login_info_page.click_find_login_info_button()

        expect(
            forgot_login_info_page.page.get_by_text(
                "First name is required."
            )
        ).to_be_visible()

    def test_find_login_info_with_valid_details_known_bug(
        self,
        page
    ):

        """
        Known Application Behavior:
        Even with valid customer details,
        ParaBank fails to retrieve login info.
        Current application displays customer not found error.
        """

        home_page = HomePage(page)

        home_page.click_forgot_login_info_link()

        forgot_login_info_page = ForgotLoginInfoPage(page)

        forgot_login_info_page.fill_customer_lookup_form(
            first_name="Sahil",
            last_name="Singh",
            address="103b",
            city="Ranchi",
            state="Jharkhand",
            zip_code="834001",
            ssn="1234"
        )

        forgot_login_info_page.click_find_login_info_button()

        expect(page).to_have_url(re.compile(r".*lookup\.htm.*"))