class LoginPage:

    def __init__(self, page):
        self.page = page # Storing the Page object passed during initialization for later use in methods

        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_btn = page.locator("input.button")

    def login_user(self, username, password): # Method to perform login action using the provided username and password

        self.username.fill(username)
        self.password.fill(password)

        self.login_btn.click()