import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TablePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "test_data",
            "table.html"
        )

        self.URL = "file:///" + file_path.replace("\\", "/")

    TABLE = (By.TAG_NAME, "table")
    ROWS = (By.CSS_SELECTOR, "table tbody tr")

    def open(self):
        self.driver.get(self.URL)

        self.wait.until(
            EC.presence_of_element_located(self.TABLE)
        )

    def get_table_data(self):
        rows = self.driver.find_elements(*self.ROWS)

        table_data = []

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")

            if cells:
                table_data.append(
                    [cell.text.strip() for cell in cells]
                )

        return table_data

    def get_value_for_name(self, name, column_name):
        headers = self.driver.find_elements(
            By.CSS_SELECTOR,
            "table thead tr th"
        )

        header_names = [
            header.text.strip()
            for header in headers
        ]

        if column_name not in header_names:
            raise ValueError(
                f"Column '{column_name}' not found."
            )

        column_index = header_names.index(column_name)

        rows = self.driver.find_elements(*self.ROWS)

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")

            if cells:
                values = [
                    cell.text.strip()
                    for cell in cells
                ]

                name_index = header_names.index("Fruit Name")

                if values[name_index] == name:
                    return values[column_index]

        raise ValueError(
            f"Name '{name}' was not found."
        )