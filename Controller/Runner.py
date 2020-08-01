import json
import time
from selenium import webdriver
from Controller.DiamondController import checkPrice2BuyDIAMOND, getQuantMinDIAMOND, getPriceSellDIAMOND
from Controller.OreController import checkPrice2BuyORE, getQuantMinORE, getPriceSellORE
from Controller.UraniumController import checkPrice2BuyURANIUM, getQuantMinURANIUM, getPriceSellURANIUM
from Utils.Tools import getProjectFolder
from Controller.PetroleumController import checkPrice2BuyBBL, getPriceSellBBL, getQuantMinBBL
import chromedriver_autoinstaller

browserDriver = None
priceResource = 0
quantResource = 0

itens = {
    'urlLogin': "https://rivalregions.com/",
    'buttonLoginGoogle': "/html/body/div[4]/div[2]/a[2]/div",  # xpath
    'inputGoogleEmail': "//*[@id='identifierId']",  # xpath
    'nextForPassword': "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]",
    # xpath
    'inputGooglePassword': "//*[@id='password']/div[1]/div/div[1]/input",  # xpath
    'formButtonLogin': "//*[@id='passwordNext']/span/span",  # xpath
    'homePage': "https://rivalregions.com/#overview",  # xpath
    'linkAcademy': "https://rivalregions.com/#slide/academy",
    'buttonBuildAcademy': "//*[@id='header_slide_inner']/div[3]/div[2]",
    'buttonForce': '/html/body/div[6]/div[1]/div[9]/div[2]/div[4]/div[1]',
    'buttonEducation': "/html/body/div[6]/div[1]/div[9]/div[2]/div[5]/div[1]",
    'buttonPerkCash': "/html/body/div[6]/div[1]/div[9]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div",
    'buttonPerkGold': "/html/body/div[6]/div[1]/div[9]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div",
    'linkMarket': "https://rivalregions.com/#storage",
    'divBBLClick': "//*[@id='content']/div[3]/div[1]",
    'divOREClick': "//*[@id='content']/div[4]/div[1]",
    'divURANIUMClick': "//*[@id='content']/div[5]/div[1]",
    'divDIAMONDClick': "//*[@id='content']/div[6]/div[2]",
    'valueResource': "//*[@id='storage_market']/div[2]/div[1]/div[3]/span/span",
    'quantResource': "//*[@id='storage_market']/div[2]/div[1]/div[4]/span",
    'inputValueOffer': "// *[ @ id = 'storage_market'] / div[2] / div[1] / div[5] / input",
    'buttonBuyOffer': "//*[@id='storage_market']/div[2]/div[1]/div[6]/div[1]",
    'spanLinkSell': "//*[@id='storage_market']/div[1]/div/span",
    'inputStock': "//*[@id='storage_market']/div[2]/div[2]/input",
    'inputSell': "//*[@id='storage_market']/div[2]/div[3]/input",
    'buttonSellOffer': "//*[@id='storage_sell_button_id']"
}


def printLin():
    print("-------------------------")


def startSession():
    print("PROGRAMA INICIADO")

    pathProject = getProjectFolder()
    browser = "chromedriver"
    fullRoute = getProjectFolder() + "/" + browser

    chromedriver_autoinstaller.install()
    webBrowser = webdriver.Chrome()
    global browserDriver
    browserDriver = webBrowser


def getSessionId():
    global browserDriver
    return browserDriver.session_id


def navigateToLogin(driver, link):
    driver.get(link)


def loginButton(driver, button):
    driver.find_element_by_xpath(button).click()
    time.sleep(5)


def formLoginGoogle(driver, emailForm, email, nextForPassword, passwordForm, password, buttonLogin):
    driver.find_element_by_xpath(emailForm).send_keys(email)
    driver.find_element_by_xpath(emailForm).send_keys(u'\ue007')

    # driver.find_element_by_xpath(nextForPassword).click()
    time.sleep(5)
    driver.find_element_by_xpath(passwordForm).send_keys(password)
    driver.find_element_by_xpath(passwordForm).send_keys(u'\ue007')
    # driver.find_element_by_xpath(buttonLogin).click()
    time.sleep(3)


def enterPage(driver, linkHome):
    printLin()
    driver.get(linkHome)
    driver.refresh()
    time.sleep(5)


def constructAcademy(driver, linkAcademy, buttonAcademy):
    print("Verificando academia militar")
    printLin()
    enterPage(driver, linkAcademy)
    time.sleep(3)
    try:
        driver.find_element_by_xpath(buttonAcademy).click()
    except:
        pass
    time.sleep(3)


def upPerk(driver, linkHome, buttonPerk, typePayment):
    print("Upando Perk")
    printLin()
    enterPage(driver, linkHome)
    time.sleep(3)
    try:
        driver.find_element_by_xpath(buttonPerk).click()
        driver.find_element_by_xpath(typePayment).click()
    except:
        pass
    time.sleep(3)


def openStorage(driver, linkMarket):
    driver.refresh()
    time.sleep(3)
    driver.get(linkMarket)
    time.sleep(3)
    driver.refresh()
    current_link = driver.current_url
    if current_link != linkMarket:
        print("TÁ FORA DO MERCADO")
    else:
        printLin()
        printLin()
        print("Dentro do mercado")
        printLin()
    time.sleep(3)


def getPriceResource(driver, boxResource, spanValue):
    driver.find_element_by_xpath(boxResource).click()
    time.sleep(2)
    for price in driver.find_elements_by_xpath(spanValue):
        price = price.text[:-2]
        price = price.replace(".", "")
        global priceResource
        priceResource = int(price)


def getQuantResource(driver, spanResource):
    for quant in driver.find_elements_by_xpath(spanResource):
        quan = quant.text
        quan = quan.replace(".", "")
        global quantResource
        quantResource = int(quan)


def buyResource(driver, price, amount, nameResource, inputQuant, buttonBuy):
    print(price)
    if nameResource == "BBL":
        if checkPrice2BuyBBL(price):
            driver.find_element_by_xpath(inputQuant).clear()
            driver.find_element_by_xpath(inputQuant).send_keys(amount)
            time.sleep(0.2)
            driver.find_element_by_xpath(buttonBuy).click()
            time.sleep(3)
        else:
            pass
    elif nameResource == "ORE":
        if checkPrice2BuyORE(price):
            driver.find_element_by_xpath(inputQuant).clear()
            driver.find_element_by_xpath(inputQuant).send_keys(amount)
            time.sleep(0.2)
            driver.find_element_by_xpath(buttonBuy).click()
            time.sleep(3)
        else:
            pass
    elif nameResource == "URANIUM":
        if checkPrice2BuyURANIUM(price):
            driver.find_element_by_xpath(inputQuant).clear()
            driver.find_element_by_xpath(inputQuant).send_keys(amount)
            time.sleep(0.2)
            driver.find_element_by_xpath(buttonBuy).click()
            time.sleep(3)
        else:
            pass
    elif nameResource == "DIAMOND":
        if checkPrice2BuyDIAMOND(price):
            driver.find_element_by_xpath(inputQuant).clear()
            driver.find_element_by_xpath(inputQuant).send_keys(amount)
            time.sleep(0.2)
            driver.find_element_by_xpath(buttonBuy).click()
            time.sleep(3)
        else:
            pass
    else:
        print("Não encontrado")


def sellResource(driver, spanLinkSell, inputStock, nameResource, inputSell, buttonSellOffer):
    for state in driver.find_elements_by_xpath(spanLinkSell):
        statestatus = state.text
    if statestatus == "coloque uma oferta":
        driver.find_element_by_xpath(spanLinkSell).click()
        time.sleep(2)
        stateStock = driver.find_element_by_xpath(inputStock).get_attribute("value")
        if nameResource == "BBL":
            if int(stateStock) >= getQuantMinBBL():
                driver.find_element_by_xpath(inputSell).send_keys(getPriceSellBBL())
                driver.find_element_by_xpath(buttonSellOffer).click()
                print("Oferta enviada com sucesso")
                time.sleep(2)
            else:
                print("Nao ha quantidade suficiente")
        elif nameResource == "ORE":
            if int(stateStock) >= getQuantMinORE():
                driver.find_element_by_xpath(inputSell).send_keys(getPriceSellORE())
                driver.find_element_by_xpath(buttonSellOffer).click()
                print("Oferta enviada com sucesso")
                time.sleep(2)
            else:
                print("Nao ha quantidade suficiente")
        elif nameResource == "URANIUM":
            if int(stateStock) >= getQuantMinURANIUM():
                driver.find_element_by_xpath(inputSell).send_keys(getPriceSellURANIUM())
                driver.find_element_by_xpath(buttonSellOffer).click()
                print("Oferta enviada com sucesso")
                time.sleep(2)
            else:
                print("Nao ha quantidade suficiente")
        elif nameResource == "DIAMOND":
            if int(stateStock) >= getQuantMinDIAMOND():
                driver.find_element_by_xpath(inputSell).send_keys(getPriceSellDIAMOND())
                driver.find_element_by_xpath(buttonSellOffer).click()
                print("Oferta enviada com sucesso")
                time.sleep(2)
            else:
                print("Nao ha quantidade suficiente")
    else:
        print("Ja existe uma oferta")
        pass


def Start():
    start = True
    while start:
        with open(getProjectFolder() + "/" + "values.json") as file:
            data = json.load(file)
            email = data['email']
            password = data['password']
        startSession()
        navigateToLogin(browserDriver, itens['urlLogin'])
        loginButton(browserDriver, itens['buttonLoginGoogle'])
        formLoginGoogle(browserDriver, itens['inputGoogleEmail'], email, itens['nextForPassword'],
                        itens['inputGooglePassword'], password, itens['formButtonLogin'])
        print("Logado")
        loop = True
        while loop:
            try:
                enterPage(browserDriver, itens['homePage'])
                constructAcademy(browserDriver, itens['linkAcademy'], itens['buttonBuildAcademy'])
                upPerk(browserDriver, itens['homePage'], itens['buttonEducation'], itens['buttonPerkCash'])
                i = 1
                while i <= 20:
                    openStorage(browserDriver, itens['linkMarket'])
                    printLin()
                    print("Petróleo")
                    resource = "BBL"
                    getPriceResource(browserDriver, itens['divBBLClick'], itens['valueResource'])
                    # newLine(priceResource, resource)
                    getQuantResource(browserDriver, itens['quantResource'])
                    buyResource(browserDriver, priceResource, quantResource, resource, itens['inputValueOffer'],
                                itens['buttonBuyOffer'])
                    sellResource(browserDriver, itens['spanLinkSell'], itens['inputStock'], resource,
                                 itens['inputSell'], itens['buttonSellOffer'])
                    time.sleep(3)
                    printLin()
                    print("Minério")
                    resource = "ORE"
                    getPriceResource(browserDriver, itens['divOREClick'], itens['valueResource'])
                    # newLine(priceResource, resource)
                    getQuantResource(browserDriver, itens['quantResource'])
                    buyResource(browserDriver, priceResource, quantResource, resource, itens['inputValueOffer'],
                                itens['buttonBuyOffer'])
                    sellResource(browserDriver, itens['spanLinkSell'], itens['inputStock'], resource,
                                 itens['inputSell'],
                                 itens['buttonSellOffer'])
                    time.sleep(3)

                    printLin()
                    print("Urânio")
                    resource = "URANIUM"
                    getPriceResource(browserDriver, itens['divURANIUMClick'], itens['valueResource'])
                    # newLine(priceResource, resource)
                    getQuantResource(browserDriver, itens['quantResource'])
                    buyResource(browserDriver, priceResource, quantResource, resource, itens['inputValueOffer'],
                                itens['buttonBuyOffer'])
                    sellResource(browserDriver, itens['spanLinkSell'], itens['inputStock'], resource,
                                 itens['inputSell'],
                                 itens['buttonSellOffer'])
                    time.sleep(3)
                    printLin()
                    print("Diamantes")
                    resource = "DIAMOND"
                    getPriceResource(browserDriver, itens['divDIAMONDClick'], itens['valueResource'])
                    # newLine(priceResource, resource)
                    getQuantResource(browserDriver, itens['quantResource'])
                    buyResource(browserDriver, priceResource, quantResource, resource, itens['inputValueOffer'],
                                itens['buttonBuyOffer'])
                    sellResource(browserDriver, itens['spanLinkSell'], itens['inputStock'], resource,
                                 itens['inputSell'],
                                 itens['buttonSellOffer'])
                    i = i + 1
            except:
                browserDriver.quit()
                printLin()
                print("SAINDO")
                loop = False
