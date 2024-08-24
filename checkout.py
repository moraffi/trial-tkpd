from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time


def shipping(driver, service, courier):
#choose service on checkout page
    ChooseService = "//*[@data-testid='btnShippingDurationDropDownCap'][@data-option-loading='false']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,ChooseService)))
    driver.find_element(By.XPATH,ChooseService).click()
    time.sleep(1)
    serviceopt = "//*[@aria-label='shipment dropdown item content']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,serviceopt)))
    arrayservice= driver.find_elements(By.XPATH,"(//*[@aria-label='shipment dropdown item content']/div/div/section/h5/b)")
    for a in range(len(arrayservice)):
        if service == arrayservice[a].text:
            driver.find_element(By.XPATH,"(//*[@aria-label='shipment dropdown item content']/div/div/section/h5/b)[" + str(a+1) + "]").click()
    if service == 'Instant 3 Jam' or service == 'Same Day 8 Jam':
        return False

#choose shipment on checkout page
    courierbtnship= "//*[@data-testid='shippingCourierDropDownCapValue']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,courierbtnship)))
    driver.find_element(By.XPATH,courierbtnship).click()
    time.sleep(1)
    courieropt = "//*[@aria-label='shipment title']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,courieropt)))
    arraycourier = driver.find_elements(By.XPATH,"(//*[@class = 'shipment-content__left-section css-1if1bl1']/section/h5/b)")
    for a in range(len(arraycourier)):
        if courier == arraycourier[a].text:
            driver.find_element(By.XPATH,"(//*[@class = 'shipment-content__left-section css-1if1bl1']/section/h5/b)[" + str(a+1) + "]").click()
    time.sleep(2)

def Checkout(driver):
    btnPembayaran = "//*[@data-testid='btnSafChoosePayment']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,btnPembayaran)))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element(By.XPATH,btnPembayaran).click()
    time.sleep(5)


def payment (driver, envr, paymethod):
    iframe = "scrooge-iframe"
    WebDriverWait (driver, 10).until(EC.presence_of_element_located((By.ID,iframe)))
    driver.switch_to.frame (driver.find_element(By.ID,iframe))
    time.sleep(3)
    if envr == 'staging':
        btnlihat = "//*[@class='css-nznt48']"
    elif envr == 'production':
        btnlihat = "//*[@class='css-fh74mg']"
    else: print ('environtment tidak ditemukan')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,btnlihat)))
    driver.find_element(By.XPATH,btnlihat).click()
    time.sleep(1)
    xpathpaymethod = ''
    if paymethod == "saldotokped": 
        xpathpaymethod = "//*[@id='tokopediawallet']"
    else:
        xpathpaymethod = "//*[@id='briepay']"
    driver.find_element (By.XPATH, xpathpaymethod).click()
    time.sleep(3)
    bayar = "btn-pay-confirm"
    driver.find_element(By.ID,bayar).click()
    time.sleep(1)

#swicth ke layar utama
    driver.switch_to.default_content()
    btnbayar = "(//*[@type='submit'])[1]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,btnbayar)))
    driver.find_element(By.XPATH,btnbayar).click()
    time.sleep(2)
    print ("PASSED!")