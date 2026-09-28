from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://tutorialsninja.com/demo/index.php?route=account/login"
    LOGOUT_URL = "https://tutorialsninja.com/demo/index.php?route=account/logout"

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
            EC.visibility_of_element_located(self.EMAIL)
        )

    def enter_email(self, email):
        field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        )
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_warning_message(self):
        warning = self.wait.until(
            EC.visibility_of_element_located(self.WARNING)
        )
        return warning.text.strip()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def logout(self):
        self.driver.get(self.LOGOUT_URL)