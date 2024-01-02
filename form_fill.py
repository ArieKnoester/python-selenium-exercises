# https://www.selenium.dev/documentation/
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
# Dummy site. Does not collect submitted info.
driver.get("http://secure-retreat-92358.herokuapp.com/")

# Get required elements.
fName_input = driver.find_element(By.NAME, value="fName")
lName_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value="email")
sign_up_button = driver.find_element(By.CLASS_NAME, value="btn")

# Fill out the form and submit.
fName_input.send_keys("Python")
lName_input.send_keys("Student")
email_input.send_keys("stuff@things.com")
sign_up_button.click()

driver.quit()
