from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

screenshot_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "screenshots"
)

try:
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/upload-download-test/")

    print("Opening Rahul Shetty Academy...")
    print("Waiting for table data...")

    mango_cell = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[normalize-space(text())='Mango']")
        )
    )

    print("Table data loaded successfully.")

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_5_01_table_page.png"
        )
    )

    rows = driver.find_elements(
        By.XPATH,
        "//*[@role='row']"
    )

    print("\nTABLE DATA")
    print("-" * 60)

    target_name = "Mango"
    target_price = None
    target_row = None

    for row in rows:
        cells = row.find_elements(
            By.XPATH,
            "./*[@role='cell']"
        )

        row_data = [
            cell.text.strip()
            for cell in cells
        ]

        if row_data:
            print(row_data)

        if target_name in row_data:
            target_row = row

            name_index = row_data.index(target_name)

            if len(row_data) > 3:
                target_price = row_data[3]

            break

    if target_row is None:
        raise AssertionError("Mango row was not found.")

    if target_price is None:
        raise AssertionError("Mango price was not found.")

    print("\nTARGET ROW FOUND")
    print("-" * 60)
    print("Fruit Name:", target_name)
    print("Price:", target_price)

    driver.execute_script(
        """
        arguments[0].scrollIntoView({block: 'center'});
        arguments[0].style.backgroundColor = 'yellow';
        arguments[0].style.outline = '3px solid red';
        """,
        target_row
    )

    driver.execute_script(
        """
        var resultBox = document.createElement('div');

        resultBox.innerHTML =
            '<div style="font-size:24px;font-weight:bold;margin-bottom:15px;">' +
            'SELENIUM TABLE RESULT' +
            '</div>' +
            '<div style="font-size:20px;margin:8px 0;">' +
            '<b>Target Name:</b> ' + arguments[0] +
            '</div>' +
            '<div style="font-size:20px;margin:8px 0;">' +
            '<b>Price:</b> ' + arguments[1] +
            '</div>' +
            '<div style="font-size:20px;margin:8px 0;">' +
            '<b>Status:</b> Row Found Successfully' +
            '</div>';

        resultBox.style.position = 'fixed';
        resultBox.style.top = '20px';
        resultBox.style.right = '20px';
        resultBox.style.zIndex = '999999';
        resultBox.style.backgroundColor = 'white';
        resultBox.style.color = 'black';
        resultBox.style.padding = '25px';
        resultBox.style.border = '4px solid red';
        resultBox.style.borderRadius = '10px';
        resultBox.style.boxShadow = '0 4px 15px rgba(0,0,0,0.4)';
        resultBox.style.fontFamily = 'Arial, sans-serif';
        resultBox.style.minWidth = '330px';

        document.body.appendChild(resultBox);
        """,
        target_name,
        target_price
    )

    time.sleep(3)

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_5_02_target_row_found.png"
        )
    )

    print("\nSUCCESS: Target row highlighted.")
    print("Result displayed on webpage.")
    print("Screenshot saved successfully.")

    time.sleep(2)

except Exception as e:
    print("\nERROR TYPE:", type(e).__name__)
    print("ERROR:", repr(e))

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_5_ERROR.png"
        )
    )

finally:
    driver.quit()