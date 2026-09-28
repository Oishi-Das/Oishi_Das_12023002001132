from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open SauceDemo login page
driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# Enter username using By.ID
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

# Enter password using By.NAME
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

# Click Login button using By.XPATH
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()

# Validate that URL contains /inventory.html
assert "/inventory.html" in driver.current_url

print("Assignment 1 Passed!")
print("Current URL:", driver.current_url)

# Wait so you can see the result
time.sleep(3)

# Close browser
driver.quit()