from pages.loan_request_page import (
    LoanRequestPage
)

from pages.login_page import LoginPage


def test_apply_for_loan_successfully(page):

    # Page objects
    login_page = LoginPage(page)

    loan_request_page = (
        LoanRequestPage(page)
    )

    # Login
    login_page.login_user(
        username="john",
        password="demo"
    )

    # Navigate to request loan page
    loan_request_page.navigate_to_request_loan_page()

    # Apply for valid loan using the first available account
    loan_request_page.apply_for_loan(
        amount="2.73",
        down_payment="1.03"
    )

    # Verify loan approval
    loan_request_page.verify_loan_approved()


def test_apply_for_loan_with_insufficient_funds(page):

    # Page objects
    login_page = LoginPage(page)

    loan_request_page = (
        LoanRequestPage(page)
    )

    # Login
    login_page.login_user(
        username="john",
        password="demo"
    )

    # Navigate to request loan page
    loan_request_page.navigate_to_request_loan_page()

    # Apply for invalid loan using the first available account
    loan_request_page.apply_for_loan(
        amount="123456789",
        down_payment="0"
    )

    # Verify loan denial
    loan_request_page.verify_loan_denied()