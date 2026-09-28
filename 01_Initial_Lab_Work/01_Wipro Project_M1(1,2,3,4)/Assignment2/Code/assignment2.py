from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome browser
driver = webdriver.Chrome()

# Open dynamic loading page
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# Maximize browser
driver.maximize_window()

# Click the Start button
start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
start_button.click()

# Create explicit wait
wait = WebDriverWait(driver, 10)

# Wait until the Hello World text is visible
text_element = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
)

# Extract the text
result_text = text_element.text

print("Extracted Text:", result_text)

# Validate the extracted text
assert result_text == "Hello World!"

print("Assignment 2 Passed!")

# Close browser
driver.quit()