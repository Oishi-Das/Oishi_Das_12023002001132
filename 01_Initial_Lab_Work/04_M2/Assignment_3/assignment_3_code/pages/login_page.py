from selenium.webdriver.common.by import By
import time


class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SECURE_AREA = (By.TAG_NAME, "h2")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        time.sleep(1)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        time.sleep(1)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(3)

    def get_secure_area_text(self):
        return self.driver.find_element(*self.SECURE_AREA).text