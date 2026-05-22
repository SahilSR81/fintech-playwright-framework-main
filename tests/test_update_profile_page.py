from pages.login_page import LoginPage
from pages.update_profile_page import (
    UpdateProfilePage
)


def test_update_profile_information(page):

    # Page objects
    login_page = LoginPage(page)

    update_profile_page = (
        UpdateProfilePage(page)
    )

    # Login
    login_page.login_user(
        username="john",
        password="demo"
    )

    # Navigate to update profile page
    update_profile_page.navigate_to_update_contact_info_page()

    # Update profile information
    update_profile_page.update_contact_information(
        first_name="Sahil",
        last_name="Singh",
        street="Lowadih",
        city="Ranchi",
        state="JH",
        zip_code="834005",
        phone_number="9876543210"
    )

    # Verify success message
    update_profile_page.verify_profile_updated_successfully()

    # Logout
    update_profile_page.logout_user()