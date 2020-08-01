import json
from Utils.Tools import getProjectFolder


def checkPrice2BuyDIAMOND(price):
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    if price <= data['valueBuyDIAMOND']:
        return True
    else:
        return False


def getQuantMinDIAMOND():
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    return int(data['quantMinimunSellDIAMOND'])


def getPriceSellDIAMOND():
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    return int(data['valueSellDIAMOND'])
