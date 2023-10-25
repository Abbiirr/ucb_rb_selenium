import os
import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

os.environ['PATH'] += r"C:\chromedriver_win32"
driver = webdriver.Chrome()
def fund_transfer(driver, file_path, user_id, password):
    fundtransferButton = driver.find_element(By.CSS_SELECTOR, "#navbarSupportedContent > ul > li:nth-child(2) > a")
    fundtransferButton.click()

    bulkFundTransferButton = driver.find_element(By.CSS_SELECTOR,
                                                 "#navbarSupportedContent > ul > li.nav-item.dropdown.root.inactive.show > ul > li:nth-child(4) > a")
    bulkFundTransferButton.click()

    bulkFundTransferLabel = driver.find_element(By.CSS_SELECTOR,
                                                "#navbarSupportedContent > ul > li:nth-child(2) > ul > li:nth-child(4) > ul > li:nth-child(1) > a")

    bulkFundTransferLabel.click()
    current_timestamp = str(time.time())
    fileUploadBtn = driver.find_element(By.CSS_SELECTOR, "#file")
    old_file_path = r"C:/Users/BS-1126/OneDrive - Brain Station 23 Ltd/Project-related-files/UCB-RB/Bulk file new/20/bulk mixed 20 - .xlsx"
    new_file_name = f"bulk mixed 20 - {current_timestamp}.xlsx"

    # Specify the directory where you want to create the new file
    directory_path = "C:/Users/BS-1126/OneDrive - Brain Station 23 Ltd/Project-related-files/UCB-RB/Bulk file new/20/"

    # Create the full file path
    new_file_path = os.path.join(directory_path, new_file_name)

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

    nextbtn = driver.find_element(By.CSS_SELECTOR,
                                  "#app > div > div > div > div:nth-child(2) > div.text-center > button")
    nextbtn.click()

fund_transfer(driver, "shovon33", "nion33", "12345@Ss")

