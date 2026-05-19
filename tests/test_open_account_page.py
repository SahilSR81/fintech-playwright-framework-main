from pages.login_page import LoginPage
from pages.open_account_page import OpenAccountPage


def test_user_can_open_savings_account(page):

    # Page objects
    login_page = LoginPage(page)
    open_account_page = OpenAccountPage(page)

    # Login
    login_page.login_user(
        username="john",
        password="demo"
    )

    # Navigate to Open Account page
    open_account_page.navigate_to_open_account()

    # Open account
    open_account_page.open_account(
        account_type="1",
        from_account_index=0
    )

    # Validate success
    open_account_page.verify_account_opened()