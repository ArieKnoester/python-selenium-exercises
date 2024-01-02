
# Scrape python.org for the dates and names of 'Upcoming Events' and add them to a dictionary

# https://www.selenium.dev/documentation/
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://www.python.org/")

# My solution using XPATH
event_times = driver.find_elements(By.XPATH, value="/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li/time")
event_names = driver.find_elements(By.XPATH, value="/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li/a")

# Instructor's solution using CSS_SELECTOR (Better than mine. More readable)
# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# for time in event_times:
#     print(time.text)
#
# for name in event_names:
#     print(name.text)

# My dictionary comprehension approach.
upcoming_events_dict = {
    i: {"time": event_times[i].text, "name": event_names[i].text} for i in range(0, len(event_times))
}

# Loop approach. Leaving this here to make the dictionary comprehension above a little easier to understand.
# upcoming_events_dict = {}
#
# for i in range(0, len(event_times)):
#     upcoming_events_dict[i] = {
#         "time": event_times[i].text,
#         "name": event_names[i].text
#     }
print(upcoming_events_dict)
driver.quit()
