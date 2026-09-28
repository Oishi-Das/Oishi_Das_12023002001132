import csv
import os

from pages.login_page import LoginPage


def load_test_data():

    data_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "test_data",
        "login_data.csv"
    )

    with open(data_file, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def test_login(driver):

    page = LoginPage(driver)

    screenshot_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "screenshots"
    )

    os.makedirs(screenshot_dir, exist_ok=True)

    case = load_test_data()[0]

    page.open()

    page.login(
        case["email"],
        case["password"]
    )

    assert "route=account/account" in driver.current_url

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_9_01_valid_login.png"
        )
    )

    print("\nvalid_login: PASSED")