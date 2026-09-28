import os
import pytest
from selenium import webdriver
import pytest_html


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            screenshot_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "screenshots"
            )

            os.makedirs(screenshot_dir, exist_ok=True)

            screenshot_path = os.path.join(
                screenshot_dir,
                f"{item.name}_failed.png"
            )

            driver.save_screenshot(screenshot_path)

            if hasattr(report, "extras"):
                report.extras.append(
                    pytest_html.extras.image(screenshot_path)
                )