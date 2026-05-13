class ForgotLoginPage:

    def __init__(self, page): # Initializing the ForgotLoginPage class with a Page object to interact with the forgot login page of the application
        self.page = page

        self.first_name = page.locator("input[name='firstName']")
        self.last_name = page.locator("input[name='lastName']")
        self.address = page.locator("input[name='address.street']")
        self.city = page.locator("input[name='address.city']")
        self.state = page.locator("input[name='address.state']")
        self.zip_code = page.locator("input[name='address.zipCode']")
        self.ssn = page.locator("input[name='ssn']")

        self.find_login_button = page.get_by_role(
            "button",
            name="Find My Login Info"
        )# Locator for the button to submit the forgot login info form and retrieve the login information based on the provided user details

    def recover_info(
        self,
        first,
        last,
        address,
        city,
        state,
        zip_code,
        ssn
    ):# Method to fill in the forgot login info form with the provided user details and submit the form to recover the login information for the user

        self.first_name.fill(first)
        self.last_name.fill(last)
        self.address.fill(address)
        self.city.fill(city)
        self.state.fill(state)
        self.zip_code.fill(zip_code)
        self.ssn.fill(ssn)

        self.find_login_button.click()