from selenium.common.exceptions import NoAlertPresentException


def handle_alert(driver):
    try:
        alert = driver.switch_to.alert
        print("Alert:", alert.text)
        alert.accept()
        return True
    except NoAlertPresentException:
        return False