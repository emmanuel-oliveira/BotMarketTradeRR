import json
from Utils.Tools import getProjectFolder


def checkPrice2BuyURANIUM(price):
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    if price <= data['valueBuyURANIUM']:
        return True
    else:
        return False


def getQuantMinURANIUM():
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    return int(data['quantMinimunSellURANIUM'])


def getPriceSellURANIUM():
    with open(getProjectFolder() + "/values.json") as file:
        data = json.load(file)
    return int(data['valueSellURANIUM'])
