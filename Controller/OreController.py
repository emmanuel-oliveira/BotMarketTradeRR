import json
from Utils.Tools import getProjectFolder


def checkPrice2BuyORE(price):
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)

    if price <= data['valueBuyORE']:
        return True
    else:
        return False


def getQuantMinORE():
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    return int(data['quantMinimunSellORE'])


def getPriceSellORE():
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    return int(data['valueSellORE'])
