from pages.login_page import LoginPage
from pages.bill_pay_page import BillPayPage


def login_and_navigate(
    page
) -> BillPayPage:

    # Login
    login_page = LoginPage(page)

    login_page.login_user(
        username="john",
        password="demo"
    )

    # Navigate
    bill_pay_page = BillPayPage(page)

    bill_pay_page.navigate_to_bill_pay()

    return bill_pay_page


def test_user_can_pay_bill(page):

    bill_pay_page = (
        login_and_navigate(page)
    )

    # Pay Bill
    bill_pay_page.pay_bill(
        payee_name="Sahil Singh",
        address="Janak Nagar, Ranchi",
        city="Ranchi",
        state="Jharkhand",
        zipcode="834005",
        phone="1234567890",
        account_number="1234567890",
        amount="200",
        from_account_index=0,
    )

    # Validation
    bill_pay_page.verify_bill_payment_successful()