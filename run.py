# Program to get money total in selected currency

import json
import requests
import sys

url = "https://api.coingate.com/api/v2/rates/merchant/"
headers = {"accept": "text/plain"}

for arg in sys.argv:
    baseCur = arg

print(baseCur)

portfolio = open('portfolio.json')
data=json.load(portfolio)

for i in data['details']:
    print(i)
    response = requests.get(url+baseCur+"/"+i['currency']+"/", headers = headers)
    print(response.text)

portfolio.close()
