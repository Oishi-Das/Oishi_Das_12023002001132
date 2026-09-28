from selenium.webdriver.common.by import By
import time


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    CART_LINK = (By.ID, "cart-total")
    QUANTITY_BOX = (By.NAME, "quantity")

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        time.sleep(2)

    def update_quantity(self, quantity):
        quantity_box = self.driver.find_element(*self.QUANTITY_BOX)
        quantity_box.clear()
        quantity_box.send_keys(str(quantity))

        buttons = self.driver.find_elements(By.TAG_NAME, "button")

        for button in buttons:
            try:
                title = button.get_attribute("title")
                original_title = button.get_attribute("data-original-title")

                if title == "Update" or original_title == "Update":
                    self.driver.execute_script(
                        "arguments[0].click();",
                        button
                    )
                    break
            except:
                continue

        time.sleep(3)

    def get_cart_details(self):
        return self.driver.execute_script(
            "return document.body.innerText;"
        )