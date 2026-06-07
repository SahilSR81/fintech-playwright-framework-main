import json
import platform
from pathlib import Path

import pytest
import allure

from playwright.sync_api import sync_playwright

from utils.config_reader import ConfigReader
from utils.logger import setup_logger
from utils.screenshot_helper import take_screenshot


logger = setup_logger()


def _write_allure_environment():
    results_dir = Path("reports") / "allure-results"
    results_dir.mkdir(parents=True, exist_ok=True)

    env_path = results_dir / "environment.properties"
    env_properties = {
        "Base URL": ConfigReader.get_base_url(),
        "Browser": ConfigReader.get_browser(),
        "Headless": ConfigReader.get_headless(),
        "Timeout (ms)": ConfigReader.get_timeout(),
        "Page Load Timeout (ms)": ConfigReader.get_page_load_timeout(),
        "Platform": platform.platform(),
        "Python Version": platform.python_version(),
    }

    with env_path.open("w", encoding="utf-8") as env_file:
        for key, value in env_properties.items():
            env_file.write(f"{key}={value}\n")

    categories_path = results_dir / "categories.json"
    categories = [
        {
            "name": "Assertion Failures",
            "matchedStatuses": ["FAILED"],
            "messageRegex": "AssertionError"
        },
        {
            "name": "Timeout Issues",
            "matchedStatuses": ["FAILED"],
            "messageRegex": "TimeoutError"
        },
        {
            "name": "Broken Tests",
            "matchedStatuses": ["BROKEN"]
        },
        {
            "name": "Skipped Tests",
            "matchedStatuses": ["SKIPPED"]
        }
    ]

    with categories_path.open("w", encoding="utf-8") as categories_file:
        json.dump(categories, categories_file, indent=2)


def pytest_sessionstart(session):
    _write_allure_environment()


@pytest.fixture(autouse=True)
def allure_test_metadata(request):
    feature_name = request.node.fspath.basename.replace("test_", "").replace("_", " ").replace(".py", "").title()
    story_name = request.node.name.replace("_", " ").title()

    allure.dynamic.feature(feature_name)
    allure.dynamic.story(story_name)
    allure.dynamic.severity("normal")

    test_doc = request.node.function.__doc__
    if test_doc:
        allure.dynamic.description(test_doc)


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

        # Wait until network is mostly idle to ensure dynamic elements load
        page.wait_for_load_state(
            "networkidle",
            timeout=ConfigReader.get_page_load_timeout()
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