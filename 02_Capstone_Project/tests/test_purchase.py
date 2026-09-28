import json
import time

from utilities.alert_handler import handle_alert
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utilities.screenshot import take_screenshot


def load_test_data():
    with open("test_data/testdata.json", "r") as file:
        return json.load(file)


def pause():
    time.sleep(2)


def test_purchase_product(driver):

    data = load_test_data()

    driver.get(data["url"])
    pause()
    take_screenshot(driver, "homepage")

    driver.find_element(
        "xpath",
        "//span[contains(text(),'My Account')]"
    ).click()
    pause()

    driver.find_element(
        "link text",
        "Login"
    ).click()
    pause()

    login_page = LoginPage(driver)
    login_page.login(
        data["email"],
        data["password"]
    )
    pause()
    take_screenshot(driver, "login")

    home_page = HomePage(driver)
    home_page.search_product(data["product"])
    pause()
    take_screenshot(driver, "search")

    product_page = ProductPage(driver)
    product_page.open_product(data["product"])
    pause()
    take_screenshot(driver, "product")

    product_page.add_to_cart()
    pause()

    handle_alert(driver)
    pause()
    take_screenshot(driver, "added_to_cart")

    cart_page = CartPage(driver)
    cart_page.open_cart()
    pause()

    cart_page.update_quantity(data["quantity"])
    pause()
    take_screenshot(driver, "updated_cart")

    cart_details = cart_page.get_cart_details()

    assert data["product"] in cart_details

    print("Product successfully verified in cart.")

    pause()