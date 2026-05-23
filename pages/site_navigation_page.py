from playwright.sync_api import (
    Page,
    expect
)

import re


class SiteNavigationPage:

    def __init__(
        self,
        page: Page
    ):

        self.page = page

        # Footer locators
        self.footer_about_us_link = page.locator(
            "#footerPanel"
        ).get_by_role(
            "link",
            name="About Us"
        )

        self.footer_services_link = page.locator(
            "#footerPanel"
        ).get_by_role(
            "link",
            name="Services"
        ).last

        # Header locators
        self.home_icon_link = page.locator(
            "ul.button"
        ).get_by_role(
            "link",
            name="home"
        )

        self.contact_icon_link = page.locator(
            "ul.button"
        ).get_by_role(
            "link",
            name="contact"
        )

        self.about_icon_link = page.locator(
            "ul.button"
        ).get_by_role(
            "link",
            name="about"
        )

        # Left menu locators
        self.left_menu_about_us_link = page.locator(
            "ul.leftmenu"
        ).get_by_role(
            "link",
            name="About Us"
        )

        # Common locators
        self.page_title = page.locator(
            "h1.title"
        )

        self.services_heading = page.locator(
            "span.heading"
        ).first

        self.parabank_logo = page.locator(
            "img[title='ParaBank']"
        )

    def click_footer_about_us_link(self):

        self.footer_about_us_link.click()

    def verify_about_us_page(self):

        expect(
            self.page_title
        ).to_have_text(
            "ParaSoft Demo Website"
        )

    def click_footer_services_link(self):

        self.footer_services_link.click()

    def verify_services_page(self):

        expect(
            self.services_heading
        ).to_contain_text(
            "services"
        )

    def navigate_to_about_us_page(self):

        self.left_menu_about_us_link.click()

    def click_parabank_logo(self):

        self.parabank_logo.click()

    def verify_home_page_url(self):

        expect(
            self.page
        ).to_have_url(
            re.compile(r".*index\.htm.*")
        )

    def click_home_icon_link(self):

        self.home_icon_link.click()

    def click_contact_icon_link(self):

        self.contact_icon_link.click()

    def verify_customer_care_page(self):

        expect(
            self.page_title
        ).to_have_text(
            "Customer Care"
        )

    def click_about_icon_link(self):

        self.about_icon_link.click()