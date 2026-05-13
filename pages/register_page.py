class RegisterPage:

    def __init__(self, page): # Initializing the RegisterPage class with a Page object to interact with the registration page of the application
        self.page = page

        self.first_name = page.locator("#customer\\.firstName")
        
        self.last_name = page.locator("input[id='customer.lastName']")

        self.address = page.locator("[id='customer.address.street']")

        self.city = page.get_by_label("City:")

        self.state = page.locator("input[id='customer.address.state']")

        self.zip_code = page.locator("input[id='customer.address.zipCode']")

        self.phone = page.locator("input[id='customer.phoneNumber']")

        self.ssn = page.locator("input[id='customer.ssn']")

        self.username = page.locator("input[id='customer.username']")

        self.password = page.locator("input[id='customer.password']")

        self.confirm_password = page.locator("#repeatedPassword")

        self.register_button = page.locator("input[value='Register']")

    def register_new_user(
        self,
        first,
        last,
        address,
        city,
        state,
        zip_code,
        phone,
        ssn,
        username,
        password
    ): # Method to fill in the registration form with the provided user details and submit the form to register a new user

        self.first_name.fill(first)
        self.last_name.fill(last)
        self.address.fill(address)
        self.city.fill(city)
        self.state.fill(state)
        self.zip_code.fill(zip_code)
        self.phone.fill(phone)
        self.ssn.fill(ssn)
        self.username.fill(username)
        self.password.fill(password)
        self.confirm_password.fill(password)

        self.register_button.click()