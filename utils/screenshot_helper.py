import os
from datetime import datetime


def take_screenshot(page, test_name):

    screenshot_dir = "reports/screenshots"

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    screenshot_path = os.path.join(
        screenshot_dir,
        f"{test_name}_{timestamp}.png"
    )

    page.screenshot(path=screenshot_path)

    return screenshot_path