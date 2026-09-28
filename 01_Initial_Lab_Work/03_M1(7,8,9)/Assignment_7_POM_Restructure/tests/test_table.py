import os

from pages.table_page import TablePage


def test_mango_price(driver):

    page = TablePage(driver)

    page.open()

    table_data = page.get_table_data()

    assert len(table_data) > 0

    price = page.get_value_for_name("Mango", "Price")

    assert price == "299"

    screenshot_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "screenshots"
    )

    os.makedirs(screenshot_dir, exist_ok=True)

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_7_01_table_test.png"
        )
    )

    print("\nAssignment 5 POM Test")
    print("Target Name: Mango")
    print("Retrieved Price:", price)
    print("Assertion: PASSED")