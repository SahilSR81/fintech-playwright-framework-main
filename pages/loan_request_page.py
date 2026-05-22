from playwright.sync_api import (
    Page,
    expect
)


class LoanRequestPage:

    def __init__(
        self,
        page: Page
    ):

        self.page = page

        # Navigation locator
        self.request_loan_link = page.get_by_role(
            "link",
            name="Request Loan"
        )

        # Form locators
        self.amount_input = page.locator(
            "#amount"
        )

        self.down_payment_input = page.locator(
            "#downPayment"
        )

        self.from_account_dropdown = page.locator(
            "#fromAccountId"
        )

        # Action button
        self.apply_now_button = page.get_by_role(
            "button",
            name="Apply Now"
        )

        # Result locators
        self.loan_status = page.locator(
            "#loanStatus"
        )

        self.loan_approved_message = page.get_by_text(
            "Congratulations, your loan has been approved."
        )

        self.loan_denied_message = page.get_by_text(
            "We cannot grant a loan in that amount with your available funds.",
            exact=True
        )

    def navigate_to_request_loan_page(self):

        self.request_loan_link.click()

    def apply_for_loan(
        self,
        amount: str,
        down_payment: str,
        from_account: str
    ):

        self.amount_input.click()
        self.amount_input.fill(amount)

        self.down_payment_input.click()
        self.down_payment_input.fill(
            down_payment
        )

        self.from_account_dropdown.select_option(
            from_account
        )

        self.apply_now_button.click()

    def verify_loan_approved(self):

        expect(
            self.loan_approved_message
        ).to_be_visible()

    def verify_loan_denied(self):

        expect(
            self.loan_denied_message
        ).to_be_visible()

    def get_loan_status(self) -> str:

        expect(
            self.loan_status
        ).to_be_visible()

        return self.loan_status.inner_text()