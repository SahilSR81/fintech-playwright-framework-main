import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(page):

    home = HomePage(page)

    home.navigate()

    home.login("john", "demo")

    heading = page.locator("h1.title").text_content()

    assert "Accounts Overview" in heading