import pytest
from playwright.sync_api import expect

from pages.accounts_page import AccountsPage
from pages.login_page import LoginPage


class TestAccountsPage:

    def test_accounts_overview_is_visible_after_login(self, page):

        login_page = LoginPage(page)

        login_page.login_user(
            username="john",
            password="demo"
        )

        accounts_page = AccountsPage(page)

        accounts_page.click_accounts_overview_link()

        expect(
            accounts_page.account_table
        ).to_be_visible()

    def test_account_details_open_successfully(self, page):

        login_page = LoginPage(page)

        login_page.login_user(
            username="john",
            password="demo"
        )

        accounts_page = AccountsPage(page)

        accounts_page.click_accounts_overview_link()

        accounts_page.click_account_details(0)

        expect(
            accounts_page.account_id
        ).to_be_visible()

        expect(
            accounts_page.account_balance
        ).to_be_visible()