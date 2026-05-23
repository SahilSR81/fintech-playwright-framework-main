from playwright.sync_api import (
    Page,
    expect
)


class AccountsOverviewPage:

    def __init__(
        self,
        page: Page
    ):

        self.page = page

        # Page locators
        self.accounts_overview_title = page.locator(
            "#rightPanel h1.title"
        ).first

        self.account_table = page.locator(
            "#accountTable"
        )

        self.first_account_link = page.locator(
            "#accountTable tbody tr:first-child td a"
        )

        self.first_account_balance = page.locator(
            "#accountTable tbody tr:first-child td:nth-child(2)"
        )

        self.total_balance_label = page.locator(
            "td:has-text('Total')"
        )

        # Account details locators
        self.account_details_title = page.locator(
            "#rightPanel h1.title"
        ).first

        self.account_id = page.locator(
            "#accountId"
        )

        # Transaction filtering locators
        self.month_dropdown = page.locator(
            "#month"
        )

        self.transaction_type_dropdown = page.locator(
            "#transactionType"
        )

        self.go_button = page.locator(
            "input[value='Go']"
        )

        self.transaction_table = page.locator(
            "#transactionTable"
        )

        self.no_transactions_message = page.get_by_text(
            "No transactions found."
        )

    def wait_for_accounts_data(self):

        expect(
            self.account_table
        ).to_be_visible()

        expect(
            self.first_account_link
        ).to_be_visible()

    def verify_accounts_overview_page(self):

        expect(
            self.accounts_overview_title
        ).to_have_text(
            "Accounts Overview"
        )

    def get_first_account_number(self) -> str:

        self.wait_for_accounts_data()

        return self.first_account_link.inner_text()

    def get_first_account_balance(self) -> str:

        self.wait_for_accounts_data()

        return self.first_account_balance.inner_text()

    def click_first_account(self):

        self.wait_for_accounts_data()

        self.first_account_link.click()

    def verify_account_details_page(
        self,
        account_number: str
    ):

        expect(
            self.account_details_title
        ).to_have_text(
            "Account Details"
        )

        expect(
            self.account_id
        ).to_have_text(
            account_number
        )

    def filter_account_activity(self):

        self.month_dropdown.select_option(
            "All"
        )

        self.transaction_type_dropdown.select_option(
            "All"
        )

        self.go_button.click()

    def verify_transaction_results(self):

        self.page.wait_for_timeout(500)

        assert (
            self.transaction_table.is_visible()
            or
            self.no_transactions_message.is_visible()
        )

    def verify_total_balance_present(self):

        expect(
            self.total_balance_label
        ).to_be_visible()