from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def open_product(self, product):
        self.driver.find_element(
            By.LINK_TEXT,
            product
        ).click()

    ADD_TO_CART = (By.ID, "button-cart")

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART).click()
        