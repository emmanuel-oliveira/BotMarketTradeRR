import json
from Utils.Tools import getProjectFolder


def checkPrice2BuyBBL(price):
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    if price <= data['valueBuyBBL']:
        return True
    else:
        return False


def getQuantMinBBL():
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    return int(data['quantMinimunSellBBL'])


def getPriceSellBBL():
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    return int(data['valueSellBBL'])
