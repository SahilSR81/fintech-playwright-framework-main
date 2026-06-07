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

    def get_available_account_numbers(self):

        expect(self.from_account_dropdown).to_be_visible(
            timeout=15000
        )

        self.page.wait_for_function(
            "() => document.querySelectorAll('#fromAccountId option').length > 0",
            timeout=15000
        )

        options = self.from_account_dropdown.locator(
            "option"
        )

        count = options.count()

        accounts = []

        for index in range(count):

            option_value = options.nth(index).get_attribute(
                "value"
            )

            if option_value:

                cleaned_value = option_value.strip()

                if cleaned_value:

                    accounts.append(cleaned_value)

        return accounts

    def select_from_account(self, from_account: str):

        expect(self.from_account_dropdown).to_be_visible(
            timeout=15000
        )

        self.from_account_dropdown.select_option(
            value=from_account
        )

    def apply_for_loan(
        self,
        amount: str,
        down_payment: str,
        from_account: str | None = None
    ):

        self.amount_input.click()
        self.amount_input.fill(amount)

        self.down_payment_input.click()
        self.down_payment_input.fill(
            down_payment
        )

        if from_account is None:
            accounts = self.get_available_account_numbers()
            if not accounts:
                raise Exception(
                    "No accounts available for loan request"
                )
            from_account = accounts[0]

        self.select_from_account(
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