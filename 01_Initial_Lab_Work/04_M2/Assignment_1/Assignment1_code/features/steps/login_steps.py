from behave import given, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


@given("I open the login page")
def open_login_page(context):

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    context.driver.maximize_window()

    time.sleep(5)

    context.driver.get("https://the-internet.herokuapp.com/login")

    time.sleep(5)


@then("I should see the login page")
def verify_login_page(context):

    login_heading = context.driver.find_element(
        By.TAG_NAME, "h2"
    ).text

    time.sleep(5)

    assert login_heading == "Login Page"

    time.sleep(5)

    context.driver.quit()