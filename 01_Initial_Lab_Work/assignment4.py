from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome
driver = webdriver.Chrome()

# Open JavaScript Alerts page
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Maximize browser
driver.maximize_window()

# Create explicit wait
wait = WebDriverWait(driver, 10)


# ==========================================
# PART 1: JAVASCRIPT ALERT
# ==========================================

# Click "Click for JS Alert"
alert_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Alert']")
    )
)

alert_button.click()

# Switch to JavaScript alert
alert = wait.until(
    EC.alert_is_present()
)

print("Alert Text:", alert.text)

# Accept the alert
alert.accept()

print("JavaScript Alert: ACCEPTED")


# ==========================================
# PART 2: JAVASCRIPT CONFIRM
# ==========================================

# Click "Click for JS Confirm"
confirm_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Confirm']")
    )
)

confirm_button.click()

# Switch to confirm dialog
confirm = wait.until(
    EC.alert_is_present()
)

print("Confirm Text:", confirm.text)

# Dismiss the confirm box
confirm.dismiss()

print("JavaScript Confirm: DISMISSED")


# ==========================================
# PART 3: JAVASCRIPT PROMPT
# ==========================================

# Click "Click for JS Prompt"
prompt_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Prompt']")
    )
)

prompt_button.click()

# Switch to prompt
prompt = wait.until(
    EC.alert_is_present()
)

print("Prompt Text:", prompt.text)

# Enter text into the prompt
prompt.send_keys("Selenium Assignment 4")

# Accept/submit the prompt
prompt.accept()

print("Prompt Text Submitted: Selenium Assignment 4")


# ==========================================
# VALIDATION
# ==========================================

result = driver.find_element(By.ID, "result")

print("Result:", result.text)

# Verify prompt result
assert "Selenium Assignment 4" in result.text

print("Alert validation: PASSED")
print("Confirm validation: PASSED")
print("Prompt validation: PASSED")
print("Assignment 4 Passed!")

input("Press ENTER to close the browser...")
# Close browser
driver.quit()