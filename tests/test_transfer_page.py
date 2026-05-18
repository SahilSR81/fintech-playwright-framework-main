from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.accounts_page import AccountsPage
from pages.transfer_page import TransferPage


class TestTransferPage:

    def test_transfer_funds_between_accounts(self, page):

        login_page = LoginPage(page)

        login_page.login_user(
            username="john",
            password="demo"
        )

        accounts_page = AccountsPage(page)

        accounts_page.click_transfer_funds_link()

        transfer_page = TransferPage(page)

        expect(
            transfer_page.transfer_funds_heading
        ).to_be_visible()

        transfer_page.transfer_funds(amount=500)

        expect(
            transfer_page.transfer_complete_heading
        ).to_be_visible()

        expect(
            transfer_page.transfer_complete_message
        ).to_be_visible()

        expect(
            transfer_page.confirmation_amount
        ).to_be_visible()

        expect(
            transfer_page.confirmation_from_account
        ).to_be_visible()

        expect(
            transfer_page.confirmation_to_account
        ).to_be_visible()

    def test_transfer_with_decimal_amount(self, page):

        login_page = LoginPage(page)

        login_page.login_user(
            username="john",
            password="demo"
        )

        accounts_page = AccountsPage(page)

        accounts_page.click_transfer_funds_link()

        transfer_page = TransferPage(page)

        expect(
            transfer_page.transfer_funds_heading
        ).to_be_visible()

        transfer_page.transfer_funds(amount=250.50)

        expect(
            transfer_page.transfer_complete_heading
        ).to_be_visible()

        amount = transfer_page.get_confirmation_amount()

        assert amount is not None

        print(f"\nTransferred Amount: {amount}")