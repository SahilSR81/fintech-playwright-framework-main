import re
from playwright.sync_api import expect
from pages.home_page import HomePage


class TestHomePage:

    def test_home_page_elements_visibility(self, page):

        home_page = HomePage(page)

        expect(
            home_page.parabank_logo
        ).to_be_visible()

        expect(
            home_page.register_link
        ).to_be_visible()

        expect(
            home_page.forgot_login_info_link
        ).to_be_visible()

        expect(
            home_page.customer_login_heading
        ).to_be_visible()

    def test_register_link_navigation(self, page):

        home_page = HomePage(page)

        home_page.click_register_link()

        expect(page).to_have_url(re.compile(r".*register\.htm.*"))

    def test_forgot_login_info_navigation(self, page):

        home_page = HomePage(page)

        home_page.click_forgot_login_info_link()

        expect(page).to_have_url(re.compile(r".*lookup\.htm.*"))