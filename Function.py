from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import Homepage
import PDP
import Cart
import checkout


driver = webdriver.Chrome()
driver.maximize_window()
action = ActionChains(driver)

envr = ''
url = '1'
mail = 'pbs-mochammad.raafie+regress@tokopedia.com'
password = 'buyereg1'
product = 'https://www.tokopedia.com/dijk-s/black-kaos'
service = 'Reguler'
courier = 'SiCepat'
paymethod = 'saldotokped'

print(envr)
def envcheck (env):
    global url
    url= "2"

    # envr = env
    # if (envr == "staging"):
    #     url = "https://staging.tokopedia.com"
    # elif (envr == "production"):
    #     url = "https://www.tokopedia.com"
    # else:
    #     print("environment tidak ada")
    #     False
    # driver.get(url)
    # print(envr)
    print(url)
envcheck("production")


print(url)
# Homepage.login(driver)
# Homepage.datalogin(driver, mail, password)
# PDP.GoToPDP(driver, product)
# PDP.closePop(driver)
# PDP.addtocart(driver)
# PDP.btnviewcart(driver)
# Cart.checkproduct(driver)
# Cart.beli(driver)
# checkout.shipping(driver,service,courier)
# checkout.Checkout(driver)
# checkout.payment(driver,envr,paymethod)