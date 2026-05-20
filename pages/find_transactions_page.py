from playwright.sync_api import Page, expect


class FindTransactionsPage:

    def __init__(self, page: Page):

        self.page = page

        # Navigation
        self.find_transactions_link = (
            page.get_by_role(
                "link",
                name="Find Transactions"
            )
        )

        # Account dropdown
        self.account_dropdown = page.locator(
            "#accountId"
        )

        # Search by Transaction ID
        self.transaction_id_input = page.locator(
            "#transactionId"
        )

        self.find_by_id_button = page.locator(
            "#findById"
        )

        # Search by Date
        self.transaction_date_input = page.locator(
            "#transactionDate"
        )

        self.find_by_date_button = page.locator(
            "#findByDate"
        )

        # Search by Date Range
        self.from_date_input = page.locator(
            "#fromDate"
        )

        self.to_date_input = page.locator(
            "#toDate"
        )

        self.find_by_date_range_button = page.locator(
            "#findByDateRange"
        )

        # Search by Amount
        self.amount_input = page.locator(
            "#amount"
        )

        self.find_by_amount_button = page.locator(
            "#findByAmount"
        )

        # Results
        self.transaction_table = page.locator(
            "#transactionTable"
        )

        # Error messages
        self.id_error = page.locator(
            "#transactionIdError"
        )

        self.date_error = page.locator(
            "#transactionDateError"
        )

    def navigate_to_find_transactions(self):

        self.find_transactions_link.click()

    def select_account(
        self,
        index: int = 0
    ):

        expect(
            self.account_dropdown.locator(
                "option"
            ).first
        ).to_be_attached()

        self.account_dropdown.select_option(
            index=index
        )

    def search_by_transaction_id(
        self,
        transaction_id: str
    ):

        self.transaction_id_input.fill(
            transaction_id
        )

        self.find_by_id_button.click()

    def search_by_date(
        self,
        date: str
    ):

        self.transaction_date_input.fill(
            date
        )

        self.find_by_date_button.click()

        self.wait_for_results()

    def search_by_date_range(
        self,
        from_date: str,
        to_date: str
    ):

        self.from_date_input.fill(
            from_date
        )

        self.to_date_input.fill(
            to_date
        )

        self.find_by_date_range_button.click()

        self.wait_for_results()

    def search_by_amount(
        self,
        amount: str
    ):

        self.amount_input.fill(
            amount
        )

        self.find_by_amount_button.click()

        self.wait_for_results()

    def wait_for_results(self):

        expect(
            self.transaction_table
        ).to_be_visible(
            timeout=10000
        )

    def verify_results_visible(self):

        expect(
            self.transaction_table
        ).to_be_visible()

    def verify_no_results(self):

        expect(
            self.transaction_table
        ).not_to_be_visible()