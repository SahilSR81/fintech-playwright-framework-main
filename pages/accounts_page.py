from playwright.sync_api import Page
from playwright.sync_api import expect

class AccountsPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators

        self.accounts_overview_link = page.get_by_role(
            "link",
            name="Accounts Overview"
        )

        self.account_details_links = page.locator(
            "#accountTable a"
        )

        self.account_id = page.locator(
            "#accountId"
        )

        self.account_type = page.locator(
            "#accountType"
        )

        self.account_balance = page.locator(
            "#balance"
        )

        self.transfer_funds_link = page.get_by_role(
            "link",
            name="Transfer Funds"
        )

        self.account_table = page.locator(
            "#accountTable"
        )

    # Actions

    def click_accounts_overview_link(self):

        self.accounts_overview_link.click()

    def click_account_details(self, account_index=0):

        expect(self.account_table).to_be_visible()

        expect(self.account_details_links.first).to_be_visible(timeout=15000)

        self.account_details_links.nth(account_index).click()

    def click_transfer_funds_link(self):

        self.transfer_funds_link.click()

    # Data Helpers

    def get_account_id(self):

        account_id = self.account_id.text_content()

        return account_id.strip() if account_id else None

    def get_account_type(self):

        account_type = self.account_type.text_content()

        return account_type.strip() if account_type else None

    def get_account_balance(self):

        balance = self.account_balance.text_content()

        return balance.strip() if balance else None