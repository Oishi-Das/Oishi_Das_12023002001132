from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import shutil

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

base_dir = os.path.dirname(os.path.abspath(__file__))
screenshot_dir = os.path.join(base_dir, "screenshots")

if os.path.isdir(screenshot_dir):
    shutil.rmtree(screenshot_dir)
elif os.path.isfile(screenshot_dir):
    os.remove(screenshot_dir)

os.makedirs(screenshot_dir, exist_ok=True)

try:
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/iframe")

    print("iFrame page opened successfully.")

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_6_01_iframe_page.png"
        )
    )

    iframe = wait.until(
        EC.presence_of_element_located(
            (By.ID, "mce_0_ifr")
        )
    )

    driver.switch_to.frame(iframe)

    print("Switched to iframe successfully.")

    editor = wait.until(
        EC.presence_of_element_located(
            (By.ID, "tinymce")
        )
    )

    driver.execute_script(
        "arguments[0].innerHTML = 'Selenium iframe interaction successful';",
        editor
    )

    print("Interacted inside iframe successfully.")

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_6_02_inside_iframe.png"
        )
    )

    driver.switch_to.default_content()

    print("Switched back to main page successfully.")

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_6_03_iframe_completed.png"
        )
    )

    driver.get("https://the-internet.herokuapp.com/windows")

    print("Multiple Windows page opened successfully.")

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_6_04_windows_page.png"
        )
    )

    original_window = driver.current_window_handle

    old_window_count = len(driver.window_handles)

    click_here = wait.until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Click Here")
        )
    )

    click_here.click()

    print("New window link clicked.")

    wait.until(
        lambda d: len(d.window_handles) > old_window_count
    )

    window_handles = driver.window_handles

    print("\nWINDOW HANDLES")
    print("-" * 50)

    for handle in window_handles:
        print(handle)

    new_window = next(
        handle
        for handle in window_handles
        if handle != original_window
    )

    driver.switch_to.window(new_window)

    print("Switched to new window successfully.")

    new_window_title = driver.title

    print("New Window Title:", new_window_title)

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_6_05_new_window.png"
        )
    )

    driver.close()

    print("New window closed successfully.")

    driver.switch_to.window(original_window)

    print("Returned to original window successfully.")

    driver.execute_script(
        """
        var box = document.createElement('div');

        box.innerHTML =
            '<b style="font-size:24px;">ASSIGNMENT 6 RESULT</b><br><br>' +
            '<b>iFrame:</b> Successfully accessed<br><br>' +
            '<b>Frame Switch:</b> Successful<br><br>' +
            '<b>iFrame Interaction:</b> Successful<br><br>' +
            '<b>New Window:</b> Successfully opened<br><br>' +
            '<b>Window Handles:</b> Successfully retrieved<br><br>' +
            '<b>New Window Title:</b> ' + arguments[0] + '<br><br>' +
            '<b>New Window:</b> Successfully closed<br><br>' +
            '<b>Main Window:</b> Successfully restored';

        box.style.position = 'fixed';
        box.style.top = '20px';
        box.style.right = '20px';
        box.style.zIndex = '999999';
        box.style.background = 'white';
        box.style.color = 'black';
        box.style.padding = '25px';
        box.style.border = '4px solid red';
        box.style.borderRadius = '10px';
        box.style.fontFamily = 'Arial';
        box.style.minWidth = '400px';

        document.body.appendChild(box);
        """,
        new_window_title
    )

    time.sleep(3)

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_6_06_final_result.png"
        )
    )

    print("\n" + "=" * 60)
    print("ASSIGNMENT 6 COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print("iFrame interaction: SUCCESS")
    print("Frame switching: SUCCESS")
    print("New window opened: SUCCESS")
    print("Window handles: SUCCESS")
    print("New window title:", new_window_title)
    print("New window closed: SUCCESS")
    print("Returned to main window: SUCCESS")
    print("All screenshots saved successfully.")

    time.sleep(2)

except Exception as e:
    print("\nASSIGNMENT 6 ERROR")
    print("Error Type:", type(e).__name__)
    print("Error:", repr(e))

    try:
        driver.save_screenshot(
            os.path.join(
                screenshot_dir,
                "assignment_6_ERROR.png"
            )
        )
        print("Error screenshot saved.")
    except:
        pass

finally:
    driver.quit()