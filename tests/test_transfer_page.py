from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.accounts_page import AccountsPage
from pages.transfer_funds_page import TransferFundsPage

class TestTransferFundsPage:

    def test_transfer_funds_successfully(self, page):

        login_page = LoginPage(page)

        login_page.login_user(
            username="john",
            password="demo"
        )

        accounts_page = AccountsPage(page)

        accounts_page.click_transfer_funds_link()

        transfer_page = TransferFundsPage(page)

        expect(
            transfer_page.transfer_funds_heading
        ).to_be_visible()

        transfer_page.transfer_funds(amount=100)

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

    def test_transfer_funds_with_empty_amount(self, page):

        login_page = LoginPage(page)

        login_page.login_user(
            username="john",
            password="demo"
        )

        accounts_page = AccountsPage(page)

        accounts_page.click_transfer_funds_link()

        transfer_page = TransferFundsPage(page)

        expect(
            transfer_page.transfer_funds_heading
        ).to_be_visible()

        transfer_page.click_transfer_button()

        expect(
            transfer_page.transfer_funds_heading
        ).to_be_visible()

    def test_transfer_page_fields_visibility(self, page):

        login_page = LoginPage(page)

        login_page.login_user(
            username="john",
            password="demo"
        )

        accounts_page = AccountsPage(page)

        accounts_page.click_transfer_funds_link()

        transfer_page = TransferFundsPage(page)

        expect(
            transfer_page.amount_input
        ).to_be_visible()

        expect(
            transfer_page.from_account_dropdown
        ).to_be_visible()

        expect(
            transfer_page.to_account_dropdown
        ).to_be_visible()

        expect(
            transfer_page.transfer_button
        ).to_be_visible()