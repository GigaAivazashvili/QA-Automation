import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")

driver.find_element(By.LINK_TEXT, "Dropdown").click()
Select(driver.find_element(By.TAG_NAME, "select")).select_by_visible_text("Option 2")
selected_option = Select(driver.find_element(By.TAG_NAME, "select")).first_selected_option.text
assert "Option 2" in selected_option
driver.back()
driver.find_element(By.LINK_TEXT, "Redirect Link").click()

time.sleep(30)
