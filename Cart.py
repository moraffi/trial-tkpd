from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def checkproduct(driver):
    checkbox_xpath = "(//*[@type='checkbox'])[3]"
    checkbox_element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH,checkbox_xpath)))
    if checkbox_element.get_attribute('type') == 'checkbox':
        if not checkbox_element.is_selected():
            checkbox_element.click()
            print("Checkbox was not checked. Now checked.")
        else:
            print("Checkbox was already checked.")
    else:
        print("The found element is not a checkbox.")
    time.sleep(1)


#Click beli button on Cart
def beli(driver):
    belibtn = "//*[@data-testid='cartCheckoutBTNWrapper']"
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,belibtn)))
    driver.find_element(By.XPATH,belibtn).click()
    time.sleep(3)