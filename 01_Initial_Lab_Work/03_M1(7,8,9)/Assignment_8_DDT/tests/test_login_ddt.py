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


def test_login_data_driven(driver):

    page = LoginPage(driver)

    screenshot_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "screenshots"
    )

    os.makedirs(screenshot_dir, exist_ok=True)

    test_data = load_test_data()

    for index, case in enumerate(test_data, start=1):

        page.open()

        page.login(
            case["username"],
            case["password"]
        )

        if case["expected_result"] == "success":

            assert "route=account/account" in driver.current_url

            driver.save_screenshot(
                os.path.join(
                    screenshot_dir,
                    f"assignment_8_{index:02d}_{case['case_name']}.png"
                )
            )

            print(f"\n{case['case_name']}: PASSED")

            page.logout()

        else:

            message = page.get_warning_message()

            assert case["expected_message"] in message

            driver.save_screenshot(
                os.path.join(
                    screenshot_dir,
                    f"assignment_8_{index:02d}_{case['case_name']}.png"
                )
            )

            print(f"\n{case['case_name']}: PASSED")