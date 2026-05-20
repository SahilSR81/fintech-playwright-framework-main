from playwright.sync_api import Page, expect


class OpenAccountPage:

    def __init__(self, page: Page):

        self.page = page

        self.open_new_account_link = page.get_by_role(
            "link",
            name="Open New Account"
        )

        self.account_type_dropdown = page.locator(
            "select#type"
        )

        self.from_account_dropdown = page.locator(
            "select#fromAccountId"
        )

        self.open_account_button = page.locator(
            "input[value='Open New Account']"
        )

        self.account_opened_heading = page.get_by_role(
            "heading",
            name="Account Opened!"
        )

        self.success_message = page.get_by_text(
            "Congratulations, your account is now open."
        )

        self.new_account_id = page.locator(
            "#newAccountId"
        )

    def navigate_to_open_account(self):

        self.open_new_account_link.click()

    def open_account(
        self,
        account_type: str,
        from_account_index: int = 0
    ):

        # Wait for account dropdown options
        expect(
            self.from_account_dropdown.locator(
                "option"
            ).first
        ).to_be_attached()

        # Select account type
        self.account_type_dropdown.select_option(
            account_type
        )

        # Select first available account
        self.from_account_dropdown.select_option(
            index=from_account_index
        )

        # Submit
        self.open_account_button.click()

    def verify_account_opened(self):

        expect(
            self.account_opened_heading
        ).to_be_visible()

        expect(
            self.success_message
        ).to_be_visible()
        
        expect(
            self.new_account_id
        ).to_be_visible()

    def get_new_account_id(self):

        return self.new_account_id.text_content()