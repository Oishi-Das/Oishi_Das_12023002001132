from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WindowsPage:

    URL = "https://the-internet.herokuapp.com/windows"

    OPEN_WINDOW = (By.LINK_TEXT, "Click Here")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get(self.URL)

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_window_handles(self):
        return self.driver.window_handles

    def open_new_window(self):
        link = self.wait.until(
            EC.element_to_be_clickable(self.OPEN_WINDOW)
        )
        link.click()

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def get_title(self):
        return self.driver.title

    def close_current_window(self):
        self.driver.close()