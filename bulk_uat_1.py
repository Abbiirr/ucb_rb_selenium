import os
import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bulk_uat_sign_in import sign_in

os.environ['PATH'] += r"C:\chromedriver_win32"
driver = webdriver.Chrome()

# url = "https://172.25.47.87:9081/eb"
url = "http://localhost:9233/eb"


enterpriseUser = "shovon33"
enterpriseUser = "avliash"



username = "nion33"
username = "avilash4"


password = "12345@Ss"
password = "123456@As"


base_file_path = "C:/Users/BS-1126/OneDrive - Brain Station 23 Ltd/Project-related-files/UCB-RB/Bulk file new/"

old_file_path = base_file_path + "20/bulk mixed 20 - .xlsx"



current_timestamp = str(time.time())
new_file_name = f"20/bulk mixed 20 - {current_timestamp}.xlsx"
new_file_path = os.path.join(base_file_path, new_file_name)


# sign_in(url, driver, enterpriseUser, username, password)


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


fundtransferButton = driver.find_element(By.CSS_SELECTOR, "#navbarSupportedContent > ul > li:nth-child(2) > a")
fundtransferButton.click()

bulkFundTransferButton = driver.find_element(By.CSS_SELECTOR,
                                             "#navbarSupportedContent > ul > li.nav-item.dropdown.root.inactive.show > ul > li:nth-child(4) > a")
bulkFundTransferButton.click()

bulkFundTransferLabel = driver.find_element(By.CSS_SELECTOR,
                                            "#navbarSupportedContent > ul > li:nth-child(2) > ul > li:nth-child(4) > ul > li:nth-child(1) > a")

bulkFundTransferLabel.click()

fileUploadBtn = driver.find_element(By.CSS_SELECTOR, "#file")
# old_file_path = "C:/Users/BS-1126/OneDrive - Brain Station 23 Ltd/Project-related-files/UCB-RB/Bulk file new/20/bulk mixed 20 - .xlsx"
# new_file_name = f"bulk mixed 20 - {current_timestamp}.xlsx"

# Specify the directory where you want to create the new file
directory_path = "C:/Users/BS-1126/OneDrive - Brain Station 23 Ltd/Project-related-files/UCB-RB/Bulk file new/20/"

# Create the full file path


# Create and write content to the new file
shutil.copyfile(old_file_path, new_file_path)
fileUploadBtn.send_keys(new_file_path)
time.sleep(2)

fromAccountBtn = Select(driver.find_element(By.ID, "fromAccountNumber"))

total_options = len(fromAccountBtn.options)
fromAccountBtn.select_by_index(total_options - 1)

narrationBtn = driver.find_element(By.ID, "debitRemarks")
narrationBtn.send_keys("test")
bulkTransferTypeBtn = driver.find_element(By.ID, "paymentType")
bulkTransferTypeBtn.send_keys("test")

nextbtn = driver.find_element(By.CSS_SELECTOR, "#app > div > div > div > div:nth-child(2) > div.text-center > button")
nextbtn.click()
time.sleep(2)

