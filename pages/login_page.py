from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators

        self.username_input = page.locator(
            "input[name='username']"
        )

        self.password_input = page.locator(
            "input[name='password']"
        )

        self.login_button = page.get_by_role(
            "button",
            name="Log In"
        )

        self.logout_link = page.get_by_role(
            "link",
            name="Log Out"
        )

        self.account_overview_text = page.get_by_role(
            "link",
            name="Accounts Overview"
        )

        self.login_error_message = page.get_by_text("Error!", exact=True)

    # Actions

    def fill_username(self, username):
        expect(self.username_input).to_be_visible(timeout=15000)
        self.username_input.fill(username)

    def fill_password(self, password):
        expect(self.password_input).to_be_visible(timeout=15000)
        self.password_input.fill(password)

    def click_login_button(self):
        expect(self.login_button).to_be_visible(timeout=15000)
        self.login_button.click()

    def click_logout_link(self):

        self.logout_link.click()

    # Reusable helper

    def login_user(self, username, password):

        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()