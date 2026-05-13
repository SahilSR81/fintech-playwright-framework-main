from pages.home_page import HomePage
from pages.forgot_login_info_page import ForgotLoginPage

def test_forgot_login(page):

    home = HomePage(page)
    forgot = ForgotLoginPage(page)

    home.navigate()
    home.go_to_forgot_login()

    forgot.recover_info(
        "John",
        "Doe",
        "Main Street",
        "New York",
        "NY",
        "10001",
        "12345"
    )

    title = page.locator(".title").text_content()

    assert "Customer Lookup" in title