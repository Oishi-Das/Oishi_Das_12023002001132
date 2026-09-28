from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
import time


@given("I open the login page")
def open_login_page(context):

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    context.driver.maximize_window()

    time.sleep(2)

    context.driver.get(
        "https://the-internet.herokuapp.com/login"
    )

    time.sleep(3)

    context.login_page = LoginPage(context.driver)


@when("I enter valid username and password")
def enter_credentials(context):

    context.login_page.enter_username("tomsmith")

    context.login_page.enter_password(
        "SuperSecretPassword!"
    )

    time.sleep(2)


@when("I click the login button")
def click_login_button(context):

    context.login_page.click_login()

    time.sleep(2)


@then("I should see the secure area")
def verify_secure_area(context):

    heading = context.login_page.get_secure_area_text()

    assert heading == "Secure Area"

    time.sleep(3)

    context.driver.quit()