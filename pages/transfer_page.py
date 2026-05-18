from playwright.sync_api import Page


class TransferPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators

        self.transfer_funds_heading = page.get_by_role(
            "heading",
            name="Transfer Funds"
        )

        self.transfer_amount_input = page.locator(
            "#amount"
        )

        self.from_account_dropdown = page.locator(
            "#fromAccountId"
        )

        self.to_account_dropdown = page.locator(
            "#toAccountId"
        )

        self.transfer_button = page.locator(
            "input[value='Transfer']"
        )

        self.transfer_complete_heading = page.get_by_role(
            "heading",
            name="Transfer Complete!"
        )

        self.transfer_complete_message = page.get_by_text(
            "Your transfer is complete"
        )

        self.confirmation_amount = page.locator(
            "#amountResult"
        )

        self.confirmation_from_account = page.locator(
            "#fromAccountIdResult"
        )

        self.confirmation_to_account = page.locator(
            "#toAccountIdResult"
        )

    # Actions

def get_available_account_numbers(self):

    self.page.wait_for_timeout(3000)

    options = self.from_account_dropdown.locator(
        "option"
    )

    count = options.count()

    print(f"\nDropdown Option Count: {count}")

    accounts = []

    for index in range(count):

        option_value = options.nth(index).get_attribute(
            "value"
        )

        print(f"Option {index}: {option_value}")

        if option_value:

            cleaned_value = option_value.strip()

            if cleaned_value:

                accounts.append(cleaned_value)

    print(f"\nAvailable Accounts: {accounts}")

    return accounts

    def fill_transfer_amount(self, amount):

        self.transfer_amount_input.fill(
            str(amount)
        )

    def select_from_account(self, accounts):

        self.from_account_dropdown.select_option(
            value=accounts[0]
        )

    def select_to_account(self, accounts):

        self.to_account_dropdown.select_option(
            value=accounts[1]   
        )

    def click_transfer_button(self):

        self.transfer_button.click()

    # Reusable Helper

    def transfer_funds(self, amount):

        accounts = self.get_available_account_numbers()

        if len(accounts) < 2:

            raise Exception(
                f"Not enough accounts found: {accounts}"
            )

        from_account = accounts[0]

        to_account = accounts[1]

        print(
            f"\nTransferring from "
            f"{from_account} to {to_account}"
        )

        self.fill_transfer_amount(amount)

        self.select_from_account(from_account)

        self.select_to_account(to_account)

        self.click_transfer_button()

    # Data Helpers

    def get_confirmation_amount(self):

        amount = self.confirmation_amount.text_content()

        return amount.strip() if amount else None