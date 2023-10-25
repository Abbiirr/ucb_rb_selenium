import os
import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# os.environ['PATH'] += r"C:\chromedriver_win32"
# driver = webdriver.Chrome()
def sign_in(url, driver, org_code, user_id, password):
    driver.get(url)
    driver.maximize_window()
    advancedButton = driver.find_element(By.ID, "details-button")
    advancedButton.click()
    proceedButton = driver.find_element(By.ID, "proceed-link")
    proceedButton.click()
    driver.implicitly_wait(30)
    enterpriseButton = driver.find_element(By.ID, "fldLoginOrgCode")
    enterpriseButton.send_keys(org_code)
    userNameBox = driver.find_element("id", "fldLoginUserId")
    userNameBox.send_keys(user_id)
    passwordBox = driver.find_element("id", "SKBPassword")
    passwordBox.send_keys(password)
    signInButton = driver.find_element(By.CSS_SELECTOR, "#section > div.signin_button_div > div > div:nth-child(2) > input.btn.btn-danger.password-button")
    signInButton.click()

# sign_in(driver, "shovon33", "nion33", "12345@Ss")
# time.sleep(300)

# driver.get("https://172.25.47.87:9081/eb")
# driver.maximize_window()
# advancedButton = driver.find_element(By.ID, "details-button")
# advancedButton.click()
# proceedButton = driver.find_element(By.ID, "proceed-link")
# proceedButton.click()
# driver.implicitly_wait(30)
# enterpriseButton = driver.find_element(By.ID, "fldLoginOrgCode")
# enterpriseButton.send_keys("shovon33")
# userNameBox = driver.find_element("id", "fldLoginUserId")
# userNameBox.send_keys("nion33")
# passwordBox = driver.find_element("id", "SKBPassword")
# passwordBox.send_keys("12345@Ss")
# # time.sleep(2)
# signInButton = driver.find_element(By.CSS_SELECTOR,
#                                    "#section > div.signin_button_div > div > div:nth-child(2) > input.btn.btn-danger.password-button")
# signInButton.click()
# time.sleep(300000)
