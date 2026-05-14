import pytest
from playwright.sync_api import sync_playwright

from utils.config_reader import ConfigReader


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser_name = ConfigReader.get_browser()

        if browser_name == "chromium":

            browser = p.chromium.launch(
                headless=ConfigReader.get_headless()
            )

        elif browser_name == "firefox":

            browser = p.firefox.launch(
                headless=ConfigReader.get_headless()
            )

        else:

            browser = p.webkit.launch(
                headless=ConfigReader.get_headless()
            )

        context = browser.new_context()

        page = context.new_page()

        # Better page loading strategy

        page.goto(
            ConfigReader.get_base_url(),
            wait_until="domcontentloaded",
            timeout=60000
        )

        # Default element/action timeout

        page.set_default_timeout(
            ConfigReader.get_timeout()
        )

        yield page

        context.close()

        browser.close()