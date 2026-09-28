from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome
driver = webdriver.Chrome()

# Open Selenium Web Form
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Maximize browser
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 10)


# ==========================================
# PART 1: CHECKBOXES
# ==========================================

# Locate the default checkbox
default_checkbox = wait.until(
    EC.presence_of_element_located(
        (By.ID, "my-check-2")
    )
)

# Select it if it is not already selected
if not default_checkbox.is_selected():
    default_checkbox.click()

# Verify checkbox state
assert default_checkbox.is_selected()

print("Default checkbox selected:",
      default_checkbox.is_selected())


# Locate the already checked checkbox
checked_checkbox = driver.find_element(
    By.ID, "my-check-1"
)

# Verify its state
assert checked_checkbox.is_selected()

print("Checked checkbox selected:",
      checked_checkbox.is_selected())


# ==========================================
# PART 2: AUTOCOMPLETE / DATALIST
# ==========================================

# The ID 'my-options' belongs to the datalist.
# The input is connected to it through the list attribute.

autocomplete = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[list='my-options']")
    )
)

# Type into the autocomplete field
autocomplete.send_keys("S")


# ==========================================
# PART 3: LOOP THROUGH SUGGESTIONS
# ==========================================

# Get all options from the datalist
suggestions = driver.find_elements(
    By.CSS_SELECTOR,
    "#my-options option"
)

selected_option = None

for suggestion in suggestions:

    option_value = suggestion.get_attribute("value")

    print("Suggestion:", option_value)

    # Find the required matching option
    if option_value.lower() == "san francisco":

        selected_option = option_value

        # Enter the matching value
        autocomplete.clear()
        autocomplete.send_keys(option_value)

        print("Matching option selected:", option_value)

        break


# ==========================================
# PART 4: VALIDATION
# ==========================================

# Make sure a matching option was found
assert selected_option == "San Francisco"

# Verify checkbox states
assert default_checkbox.is_selected()
assert checked_checkbox.is_selected()

# Verify autocomplete value
assert autocomplete.get_attribute("value") == "San Francisco"

print("Checkbox validation: PASSED")
print("Autocomplete validation: PASSED")
print("Assignment 3 Passed!")


# Close browser
driver.quit()