from playwright.sync_api import Page, expect


class BillPayPage:

    def __init__(self, page: Page):

        self.page = page

        # Navigation
        self.bill_pay_link = page.get_by_role(
            "link",
            name="Bill Pay"
        )

        # Payee Information
        self.payee_name_input = page.locator(
            'input[name="payee.name"]'
        )

        self.address_input = page.locator(
            'input[name="payee.address.street"]'
        )

        self.city_input = page.locator(
            'input[name="payee.address.city"]'
        )

        self.state_input = page.locator(
            'input[name="payee.address.state"]'
        )

        self.zipcode_input = page.locator(
            'input[name="payee.address.zipCode"]'
        )

        self.phone_input = page.locator(
            'input[name="payee.phoneNumber"]'
        )

        # Account Information
        self.account_number_input = page.locator(
            'input[name="payee.accountNumber"]'
        )

        self.verify_account_input = page.locator(
            'input[name="verifyAccount"]'
        )

        # Payment
        self.amount_input = page.locator(
            'input[name="amount"]'
        )

        self.from_account_dropdown = page.get_by_role(
            "combobox"
        )

        self.send_payment_button = page.get_by_role(
            "button",
            name="Send Payment"
        )

        # Success
        self.bill_payment_complete_heading = (
            page.get_by_role(
                "heading",
                name="Bill Payment Complete"
            )
        )

        self.success_message = page.get_by_text(
            "Bill Payment to"
        )

    def navigate_to_bill_pay(self):
        expect(self.bill_pay_link).to_be_visible(timeout=15000)
        self.bill_pay_link.click()

    def fill_payee_information(
        self,
        payee_name: str,
        address: str,
        city: str,
        state: str,
        zipcode: str,
        phone: str,
    ):

        self.payee_name_input.fill(
            payee_name
        )

        self.address_input.fill(
            address
        )

        self.city_input.fill(
            city
        )

        self.state_input.fill(
            state
        )

        self.zipcode_input.fill(
            zipcode
        )

        self.phone_input.fill(
            phone
        )

    def fill_account_information(
        self,
        account_number: str
    ):

        self.account_number_input.fill(
            account_number
        )

        self.verify_account_input.fill(
            account_number
        )

    def enter_payment_amount(
        self,
        amount: str
    ):

        self.amount_input.fill(
            amount
        )

    def select_from_account(
        self,
        index: int = 0
    ):

        expect(
            self.from_account_dropdown
        ).to_be_visible()

        self.from_account_dropdown.select_option(
            index=index
        )

    def click_send_payment(self):

        self.send_payment_button.click()

    def pay_bill(
        self,
        payee_name: str,
        address: str,
        city: str,
        state: str,
        zipcode: str,
        phone: str,
        account_number: str,
        amount: str,
        from_account_index: int = 0,
    ):

        self.fill_payee_information(
            payee_name,
            address,
            city,
            state,
            zipcode,
            phone,
        )

        self.fill_account_information(
            account_number
        )

        self.enter_payment_amount(
            amount
        )

        self.select_from_account(
            from_account_index
        )

        self.click_send_payment()

    def verify_bill_payment_successful(self):

        expect(
            self.bill_payment_complete_heading
        ).to_be_visible()

        expect(
            self.success_message
        ).to_be_visible()