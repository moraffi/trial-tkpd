from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def login(driver):
    LoginButton="//*[@data-testid='btnHeaderLogin']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LoginButton)))
    driver.find_element(By.XPATH,LoginButton).click()
    time.sleep(1)


def datalogin(driver,email,pas):
    #input email
    emailtext= driver.find_element(By.ID,"email-phone")
    emailtext.send_keys(email)
    time.sleep(1)
    emailbtn="email-phone-submit"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,emailbtn)))
    driver.find_element(By.ID, emailbtn).click()
    time.sleep(2)

    #input password
    psword = driver.find_element(By.ID, "password-input")
    psword.send_keys(pas)
    passbtn = "//span[@aria-label='login-button']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,passbtn)))
    driver.find_element(By.XPATH,passbtn).click()
    time.sleep(1)
    header_profile = "//*[@data-testid='btnHeaderMyProfile']"
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,header_profile)))


def closePop(driver):
    try:
        popup = "//*[@aria-label='Tutup tampilan modal']"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,popup)))
        driver.find_element(By.XPATH,popup).click()
    except:
        print("Elemen tidak ditemukan!")
    time.sleep(5)

#Cart
def cart(driver):
    btncart= "//*[@data-testid='btnHeaderCart']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,btncart)))
    closePop()
    driver.find_element(By.XPATH,btncart).click()
    time.sleep(2)

#HeaderProfil
def header(driver, action):
    header_profile = "//*[@data-testid='btnHeaderMyProfile']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,header_profile)))
    closePop()
    action.move_to_element(driver.find_element(By.XPATH,header_profile)).perform()
    time.sleep(5)

def setting(driver):
    setting = "(//*[@class='css-ifllvv'])[9]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,setting)))
    driver.find_element(By.XPATH,setting).click()
    time.sleep(1)

def detail_transaksi(driver):
    bom = "(//*[@class='css-ifllvv'])[6]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,bom)))
    driver.find_element(By.XPATH,bom).click()
    time.sleep(1)

def logout(driver):
    btnlogout= "css-15qug2e"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,btnlogout)))
    driver.find_element(By.CLASS_NAME,btnlogout).click()
    time.sleep(1)
