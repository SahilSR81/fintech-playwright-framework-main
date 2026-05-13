import pytest
from pages.home_page import HomePage


@pytest.mark.smoke
def test_home_page_loaded(page): 

    home = HomePage(page)

    home.navigate()

    assert page.url == "https://parabank.parasoft.com/parabank/index.htm"

    assert page.locator(".caption").text_content() == "Experience the difference"