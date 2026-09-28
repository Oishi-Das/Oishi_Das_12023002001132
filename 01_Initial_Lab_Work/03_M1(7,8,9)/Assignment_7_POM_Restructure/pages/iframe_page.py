from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IFramePage:

    URL = "https://the-internet.herokuapp.com/iframe"

    IFRAME = (By.ID, "mce_0_ifr")
    EDITOR = (By.ID, "tinymce")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get(self.URL)

    def switch_to_iframe(self):
        iframe = self.wait.until(
            EC.presence_of_element_located(self.IFRAME)
        )
        self.driver.switch_to.frame(iframe)

    def enter_text(self, text):
        editor = self.wait.until(
            EC.presence_of_element_located(self.EDITOR)
        )

        self.driver.execute_script(
            "arguments[0].innerHTML = arguments[1];",
            editor,
            text
        )

    def switch_to_main_content(self):
        self.driver.switch_to.default_content()