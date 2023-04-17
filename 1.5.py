import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")

driver.find_element(By.LINK_TEXT, "File Upload").click()
#driver.find_element(By.ID, "file-upload").send_keys("C:\\Users\\GIGA\\Desktop\\New folder\\download.jfif")
driver.find_element(By.ID, "file-submit").click()

# success_upload = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/h3").text
# if "File Uploaded!" == success_upload:
#     print("successfull upload")

error_upload = driver.find_element(By.XPATH,"/html/body/h1").text
if "Internal Server Error" == error_upload:
    print("error upload")
time.sleep(5)


