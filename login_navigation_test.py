from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
print("TEST STARTED")
options=Options()
options.binary_location="/usr/bin/firefox-esr"
service=Service("/usr/local/bin/geckodriver")
driver=webdriver.Firefox(service=service, options=options)
print("Browser launched successfully")
driver.get("https://the-internet.herokuapp.com/login")
print("Login page opened")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()
print("Login submitted")
time.sleep(2)
if "Secure Area" in driver.page_source:
        print("LOGIN TEST PASSED")
else:
        print("LOGIN TEST FAILED")
driver.save_screenshot("login_success.png")
print("Screenshot saved as login_success.png")
driver.quit()
print("Browser closed")
print("TEST COMPLETED SUCCESSFULLY")
