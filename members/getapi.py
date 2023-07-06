import requests
import json
import csv

try:
    api_get = requests.get('https://data.binance.com/api/v3/ticker/24hr')
    api_data = api_get.json()
except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)
    api_data = []

cryptoList = ['symbol', 'priceChange', 'priceChangePercent', 'weightedAvgPrice', 'prevClosePrice', 'lastPrice',
              'lastQty', 'bidPrice', 'bidQty', 'askPrice', 'askQty', 'openPrice', 'highPrice', 'lowPrice', 'volume',
              'quoteVolume', 'openTime', 'closeTime', 'firstId', 'lastId', 'count']

with open("crypto.csv", "w", newline="") as cryptoFile:
    decoy = csv.DictWriter(cryptoFile, cryptoList)
    decoy.writeheader()
    
    for items in api_data:
        decoy.writerow(items)
        print(items)
