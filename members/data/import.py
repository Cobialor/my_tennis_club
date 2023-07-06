import pandas as pd
from my_tennis_club.members.models import Cryptols

dataframe = pd.read_csv('C:\\Users\\Acer\\Desktop\\Web Design Course\\L3 Diploma\\Django-tutorial\\myworld\\my_tennis_club\\members\\data\\crypto.csv',encoding='latin1')
dataframe = dataframe.tail(-1)
print(dataframe.to_string())

cryptGal = Cryptols()

cryptGal.symbol = dataframe.iloc[0]['symbol']
cryptGal.priceChange = dataframe.iloc[0]['priceChange']
cryptGal.priceChangePercent = dataframe.iloc[0]['priceChangePercent']
cryptGal.weightedAvgPrice = dataframe.iloc[0]['weightedAvgPrice']
cryptGal.prevClosePrice = dataframe.iloc[0]['prevClosePrice']
cryptGal.lastPrice = dataframe.iloc[0]['lastPrice']
cryptGal.lastQty = dataframe.iloc[0]['lastQty']
cryptGal.bidPrice = dataframe.iloc[0]['bidPrice']
cryptGal.bidQty = dataframe.iloc[0]['bidQty']
cryptGal.askPrice = dataframe.iloc[0]['askPrice']
cryptGal.askQty = dataframe.iloc[0]['askQty']
cryptGal.openPrice = dataframe.iloc[0]['openPrice']
cryptGal.highPrice = dataframe.iloc[0]['highPrice']
cryptGal.lowPrice = dataframe.iloc[0]['lowPrice']
cryptGal.volume = dataframe.iloc[0]['volume']
cryptGal.quoteVolume = dataframe.iloc[0]['quoteVolume']
cryptGal.openTime = dataframe.iloc[0]['openTime']
cryptGal.closeTime = dataframe.iloc[0]['closeTime']
cryptGal.firstId = dataframe.iloc[0]['firstId']
cryptGal.lastId = dataframe.iloc[0]['lastId']
cryptGal.count = dataframe.iloc[0]['count']

print(cryptGal)