from pages.accounts_overview_page import (
    AccountsOverviewPage
)

from pages.login_page import LoginPage


def test_account_overview_details(page):

    # Page objects
    login_page = LoginPage(page)

    accounts_overview_page = (
        AccountsOverviewPage(page)
    )

    # Login
    login_page.login_user(
        username="john",
        password="demo"
    )

    # Verify accounts overview page
    accounts_overview_page.verify_accounts_overview_page()

    # Get account details
    account_number = (
        accounts_overview_page.get_first_account_number()
    )

    balance = (
        accounts_overview_page.get_first_account_balance()
    )

    # Validate account details
    assert account_number.isdigit()

    assert "$" in balance


def test_navigate_to_account_details(page):

    # Page objects
    login_page = LoginPage(page)

    accounts_overview_page = (
        AccountsOverviewPage(page)
    )

    # Login
    login_page.login_user(
        username="john",
        password="demo"
    )

    # Get account number
    account_number = (
        accounts_overview_page.get_first_account_number()
    )

    # Navigate to account details
    accounts_overview_page.click_first_account()

    # Verify account details page
    accounts_overview_page.verify_account_details_page(
        account_number
    )


def test_account_activity_filtering(page):

    # Page objects
    login_page = LoginPage(page)

    accounts_overview_page = (
        AccountsOverviewPage(page)
    )

    # Login
    login_page.login_user(
        username="john",
        password="demo"
    )

    # Open account details
    accounts_overview_page.click_first_account()

    # Filter account activity
    accounts_overview_page.filter_account_activity()

    # Verify transaction results
    accounts_overview_page.verify_transaction_results()


def test_total_balance_presence(page):

    # Page objects
    login_page = LoginPage(page)

    accounts_overview_page = (
        AccountsOverviewPage(page)
    )

    # Login
    login_page.login_user(
        username="john",
        password="demo"
    )

    # Verify total balance label
    accounts_overview_page.verify_total_balance_present()