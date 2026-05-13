import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage

@pytest.mark.smoke
@pytest.mark.register
def test_register_new_user(page):

    home = HomePage(page)
    register = RegisterPage(page)

    home.navigate()
    home.go_to_register()

    register.register_new_user(
        "Sahil",
        "Singh",
        "Patna Street",
        "Patna",
        "Bihar",
        "800001",
        "9999999999",
        "123456",
        "sahilraj123",
        "Password123"
    )

    success_message = page.locator("h1.title").text_content()

    assert "Welcome" in success_message