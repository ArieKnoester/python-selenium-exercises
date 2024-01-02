# https://www.selenium.dev/documentation/
from selenium import webdriver
from selenium.webdriver.common.by import By


# If using Chrome, the window will immediately close.
# These options do not appear necessary for Firefox.
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# When using Chrome/Selenium to access an Amazon page you may get presented
# with a CAPTCHA and this code will fail. This doesn't appear to happen with Firefox.
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Instant-Pot-60-Programmable/dp/B01NBKTPTS/?th=1")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"{price_dollar.text}.{price_cents.text}")

driver = webdriver.Firefox()

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.size)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.text)
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

submit_website_bug_link = driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(submit_website_bug_link.text)
print(submit_website_bug_link.get_attribute("href"))

# Closes a single tab
# driver.close()
# Closes the whole browser
driver.quit()
