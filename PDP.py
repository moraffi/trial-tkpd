from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def GoToPDP (driver, link_product):
    driver.get(link_product)
    time.sleep(5)

def closePop(driver):
    try:
        popup = "//*[@aria-label='Tutup tampilan modal']"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,popup)))
        driver.find_element(By.XPATH,popup).click()
    except:
        print("Elemen tidak ditemukan!")
    time.sleep(2)

#click button keranjang PDP
def addtocart(driver):
    pdp = "//*[@data-testid='pdpBtnNormalPrimary']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,pdp)))
    driver.find_element(By.XPATH,pdp).click()
    time.sleep(2)


#popup on PDP for click Lihat Keranjang
def btnviewcart(driver):
    pdp_cart ="//*[@data-testid='btnDetailViewCart']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,pdp_cart)))
    driver.find_element(By.XPATH,pdp_cart).click()
    time.sleep(1)

#click icon Cart
def btncart (driver):
    cart = "//*[@data-testid='btnHeaderCart']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,cart)))
    driver.find_element(By.XPATH,cart).click()
    time.sleep(2)
