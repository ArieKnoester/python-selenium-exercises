# https://www.selenium.dev/documentation/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

# Automate clicking on a link
driver.find_element(By.LINK_TEXT, value="Content portals").click()

# Automate using the search bar on a page. Searches Wikipedia for the term, "Python".
search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

# Alternate way: clicking the search button.
# search_button = driver.find_element(By.CSS_SELECTOR, value=".cdx-search-input__end-button")
# search_button.click()

driver.quit()
