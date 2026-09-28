from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://tutorialsninja.com/demo/index.php?route=account/login"

    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    WARNING = (By.CSS_SELECTOR, ".alert.alert-danger")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(
            EC.presence_of_element_located(self.EMAIL)
        )

    def login(self, email, password):
        email_field = self.wait.until(
            EC.presence_of_element_located(self.EMAIL)
        )

        password_field = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD)
        )

        email_field.clear()
        email_field.send_keys(email)

        password_field.clear()
        password_field.send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_warning_message(self):
        warning = self.wait.until(
            EC.presence_of_element_located(self.WARNING)
        )
        return warning.get_attribute("textContent").replace("×", "").strip()