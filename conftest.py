import pytest
import allure

from playwright.sync_api import sync_playwright

from utils.config_reader import ConfigReader
from utils.logger import setup_logger
from utils.screenshot_helper import take_screenshot


logger = setup_logger()


@pytest.fixture(scope="function")
def page():

    logger.info("Starting browser session")

    with sync_playwright() as p:

        browser_name = ConfigReader.get_browser()

        logger.info(f"Selected browser: {browser_name}")

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

        context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
        )

        page = context.new_page()

        logger.info(
            f"Navigating to: {ConfigReader.get_base_url()}"
        )

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

        logger.info("Closing browser session")

        context.close()

        browser.close()


# Screenshot + Allure attachment on failure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            logger.error(
                f"Test Failed: {item.name}"
            )

            screenshot_path = take_screenshot(
                page,
                item.name
            )

            logger.info(
                f"Screenshot saved at: {screenshot_path}"
            )

            allure.attach.file(
                screenshot_path,
                name=item.name,
                attachment_type=allure.attachment_type.PNG
            )