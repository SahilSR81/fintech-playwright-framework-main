from pages.login_page import LoginPage
from pages.find_transactions_page import (
    FindTransactionsPage
)


def login_and_navigate(
    page
) -> FindTransactionsPage:

    # Login
    login_page = LoginPage(page)

    login_page.login_user(
        username="john",
        password="demo"
    )

    # Navigate
    find_transactions_page = (
        FindTransactionsPage(page)
    )

    find_transactions_page.navigate_to_find_transactions()

    return find_transactions_page


def test_search_transaction_by_invalid_id(page):

    find_transactions_page = (
        login_and_navigate(page)
    )

    # Select account
    find_transactions_page.select_account(
        index=0
    )

    # Search invalid transaction ID
    find_transactions_page.search_by_transaction_id(
        "123456"
    )

    # Validation
    find_transactions_page.verify_no_results()


def test_search_transaction_by_date(page):

    find_transactions_page = (
        login_and_navigate(page)
    )

    # Search
    find_transactions_page.search_by_date(
        "06-20-2026"
    )

    # Validation
    find_transactions_page.verify_results_visible()


def test_search_transaction_by_date_range(page):

    find_transactions_page = (
        login_and_navigate(page)
    )

    # Select account
    find_transactions_page.select_account(
        index=0
    )

    # Search
    find_transactions_page.search_by_date_range(
        from_date="04-01-2026",
        to_date="05-20-2026"
    )

    # Validation
    find_transactions_page.verify_results_visible()


def test_search_transaction_by_amount(page):

    find_transactions_page = (
        login_and_navigate(page)
    )

    # Select account
    find_transactions_page.select_account(
        index=0
    )

    # Search
    find_transactions_page.search_by_amount(
        "10"
    )

    # Validation
    find_transactions_page.verify_results_visible()