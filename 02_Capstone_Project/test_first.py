from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://tutorialsninja.com/demo/")

print(driver.title)

driver.quit()