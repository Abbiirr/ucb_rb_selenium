import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\Users\abirh\Downloads\Compressed\chromedriver_win32"
driver = webdriver.Chrome()
driver.get("http://localhost:7082/login.html#!")
driver.implicitly_wait(30)
userNameBox = driver.find_element("id", "fldLoginUserId")
userNameBox.send_keys("Abir")
passwordBox = driver.find_element("id", "SKBPassword")
passwordBox.send_keys("123456")
time.sleep(2)
signInButton = driver.find_element(By.CLASS_NAME, "btn-danger")
signInButton.click()
time.sleep(3)

closeButton = driver.find_element(By.CSS_SELECTOR, "#lastLogin > div > div > div.modal-footer > button")
closeButton.click()
time.sleep(2)