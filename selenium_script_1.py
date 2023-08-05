import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\Users\abirh\Downloads\Compressed\chromedriver_win32"
driver = webdriver.Chrome()
driver.get("http://localhost:7082/login.html#!")
driver.maximize_window()
driver.implicitly_wait(30)
userNameBox = driver.find_element("id", "fldLoginUserId")
userNameBox.send_keys("Abir")
passwordBox = driver.find_element("id", "SKBPassword")
passwordBox.send_keys("123456")
# time.sleep(2)
signInButton = driver.find_element(By.CLASS_NAME, "btn-danger")
signInButton.click()
time.sleep(3)

closeButton = driver.find_element(By.CSS_SELECTOR, "#lastLogin > div > div > div.modal-footer > button")
closeButton.click()
time.sleep(2)

fundTransferButton = driver.find_element(By.CSS_SELECTOR, "#navbarSupportedContent > ul > li:nth-child(2) > a")
fundTransferButton.click()
time.sleep(2)

swadhinFundTransfer = driver.find_element(By.ID, "fundtransfer341106")
swadhinFundTransfer.click()
time.sleep(2)

ownSwadhinFundTransferToggle = driver.find_element(By.CSS_SELECTOR, "#fund-transfer > div > div.row.justify-content-center > div.col-md-10.currency-center > div > div > div > label:nth-child(2)")

# ownSwadhinFundTransferToggle.value_of_css_property("background-color")
print(ownSwadhinFundTransferToggle.value_of_css_property("background-color"))

otherSwadhinFundTransferToggle = driver.find_element(By.CSS_SELECTOR, "#fund-transfer > div > div.row.justify-content-center > div.col-md-10.currency-center > div > div > div > label:nth-child(4)")
print(otherSwadhinFundTransferToggle.value_of_css_property("background-color"))