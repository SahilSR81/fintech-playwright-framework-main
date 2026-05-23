from pages.site_navigation_page import (
    SiteNavigationPage
)


def test_footer_about_us_navigation(page):

    # Page object
    site_navigation_page = (
        SiteNavigationPage(page)
    )

    # Navigate to About Us page
    site_navigation_page.click_footer_about_us_link()

    # Verify About Us page
    site_navigation_page.verify_about_us_page()


def test_footer_services_navigation(page):

    # Page object
    site_navigation_page = (
        SiteNavigationPage(page)
    )

    # Navigate to Services page
    site_navigation_page.click_footer_services_link()

    # Verify Services page
    site_navigation_page.verify_services_page()


def test_home_page_logo_navigation(page):

    # Page object
    site_navigation_page = (
        SiteNavigationPage(page)
    )

    # Navigate to About Us page
    site_navigation_page.navigate_to_about_us_page()

    # Click ParaBank logo
    site_navigation_page.click_parabank_logo()

    # Verify home page URL
    site_navigation_page.verify_home_page_url()


def test_header_home_link(page):

    # Page object
    site_navigation_page = (
        SiteNavigationPage(page)
    )

    # Click home icon
    site_navigation_page.click_home_icon_link()

    # Verify home page URL
    site_navigation_page.verify_home_page_url()


def test_header_contact_link(page):

    # Page object
    site_navigation_page = (
        SiteNavigationPage(page)
    )

    # Click contact icon
    site_navigation_page.click_contact_icon_link()

    # Verify Customer Care page
    site_navigation_page.verify_customer_care_page()


def test_header_about_link(page):

    # Page object
    site_navigation_page = (
        SiteNavigationPage(page)
    )

    # Click about icon
    site_navigation_page.click_about_icon_link()

    # Verify About Us page
    site_navigation_page.verify_about_us_page()