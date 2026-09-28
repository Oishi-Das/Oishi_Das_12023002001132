import os

from pages.iframe_page import IFramePage
from pages.windows_page import WindowsPage


def test_iframe_and_window_handling(driver):

    screenshot_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "screenshots"
    )

    os.makedirs(screenshot_dir, exist_ok=True)

    iframe_page = IFramePage(driver)

    iframe_page.open()

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_7_02_iframe_page.png"
        )
    )

    iframe_page.switch_to_iframe()

    iframe_page.enter_text("Selenium POM iframe test")

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_7_03_inside_iframe.png"
        )
    )

    iframe_page.switch_to_main_content()

    windows_page = WindowsPage(driver)

    windows_page.open()

    original_window = windows_page.get_current_window()

    old_handles = set(windows_page.get_window_handles())

    windows_page.open_new_window()

    new_handles = set(windows_page.get_window_handles())

    new_window_handles = new_handles - old_handles

    assert len(new_window_handles) == 1

    new_window = new_window_handles.pop()

    windows_page.switch_to_window(new_window)

    title = windows_page.get_title()

    assert title == "New Window"

    print("\nAssignment 6 POM Test")
    print("Iframe interaction: PASSED")
    print("New window opened: PASSED")
    print("Window title:", title)
    print("Window title assertion: PASSED")

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_7_04_new_window.png"
        )
    )

    windows_page.close_current_window()

    windows_page.switch_to_window(original_window)

    assert driver.current_window_handle == original_window

    print("New window closed: PASSED")
    print("Returned to original window: PASSED")

    driver.save_screenshot(
        os.path.join(
            screenshot_dir,
            "assignment_7_05_final_result.png"
        )
    )