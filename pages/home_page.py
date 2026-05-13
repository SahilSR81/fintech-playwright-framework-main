from playwright.sync_api import Page # Importing the Page class from Playwright's sync API to interact with web pages


class HomePage:

    def __init__(self, page: Page):
        self.page = page   # Storing the Page object passed during initialization for later use in methods

        # Locators to be used in the methods
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")

        self.login_button = page.get_by_role("button", name="LOG IN")

        self.register_link = page.locator("text=Register")

        self.forgot_login_link = page.get_by_text("Forgot login info?")

        self.solutions_link = page.locator("text=Solutions")

    def navigate(self):  # Method to navigate to the home page of the application
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")

    def login(self, username, password):  # Method to perform login action using the provided username and password
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def go_to_register(self):  # Method to navigate to the registration page by clicking the register link
        self.register_link.click()

    def go_to_forgot_login(self):  # Method to navigate to the forgot login page by clicking the forgot login link
        self.forgot_login_link.click()
