from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://www.python.org")

inputValue = driver.find_element(By.ID, "id-search-field")

inputValue.send_keys("3.10")

button = driver.find_element(By.ID, "submit")

button.click()