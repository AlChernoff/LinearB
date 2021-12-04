import collections
import decimal
import functools
import operator

import simplejson as json
from Exceptions.TooMuchCoinsException import TooMuchCoinsException

inventory = [
    {
        "type": "BILL", "value": "200", "amount": 7
    },
    {
        "type": "BILL", "value": "100", "amount": 4
    },
    {
        "type": "COIN", "value": "10", "amount": 6
    },
    {
        "type": "COIN", "value": "5", "amount": 1
    },
    {
        "type": "COIN", "value": "0.1", "amount": 12
    },
    {
        "type": "COIN", "value": "0.01", "amount": 21
    },
]

request = {
    "currency": "ILS",
    "amount": 820.7
}

result = collections.defaultdict(list)

for d in inventory:
    if "BILL" in d.values():
        if(d["amount"]) > 0:
            result["bills"].append(d)
    else:
        if(d["amount"]) > 0:
            result['coins'].append(d)

result["bills"] =  sorted(result["bills"], key=lambda d: d['value'], reverse=True)
result["coins"] =  sorted(result["coins"], key=lambda d: d['value'], reverse=True)

amount = request.get("amount")
result_amount = collections.defaultdict(list)


def updateValues(value, amount):
    d = next(item for item in inventory if item['value'] == value)
    d['amount'] -= amount


def getAmountOfCoins(value, amount):
    inventory_amount = 0
    if(amount > decimal.Decimal(value["value"]),2):
        inventory_amount = round(decimal.Decimal(amount),2) // round(decimal.Decimal(value['value']),2)

    if(decimal.Decimal(inventory_amount)) > value["amount"]:
            inventory_amount = value["amount"]
    if (inventory_amount > 0):
        amount = round(decimal.Decimal(amount),2) % round(decimal.Decimal(value["value"]),2)
        result_amount[value["type"].lower()+"s"].append({value['value']:inventory_amount})
        updateValues(value['value'],inventory_amount)




    return amount



if(result["bills"]):
    for dictionary in result["bills"]:
        if amount >0:
            amount = getAmountOfCoins(dictionary, amount)
if amount > 0:
    for dictionary in result["coins"]:
        if amount >0:
            amount = getAmountOfCoins(dictionary, amount)

# sum the values with same keys
coins_sum = dict(functools.reduce(operator.add,
                               map(collections.Counter, result_amount["coins"])))
coins_sum = sum(coins_sum.values())
coins_sum = 50
if coins_sum >=50:
    raise TooMuchCoinsException("Sorry, amount of coins is more or equal 50")
if(amount) > 0:
        raise ValueError("Sorry, not enough inventory in ATM!")
output = json.dumps({"result":result_amount},use_decimal=True)

print(output)

