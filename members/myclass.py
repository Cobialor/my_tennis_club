import csv

class myclass:
    #contructor to initialize the class that was created.
    def __init__(self,cryptoList):
        self.symbol = cryptoList[0]
        self.priceChange = cryptoList[1]
        self.priceChangePercent = cryptoList[2]
        self.weightedAvgPrice = cryptoList[3]
        self.prevClosePrice = cryptoList[4]
        self.lastPrice = cryptoList[5]
        self.lastQty = cryptoList[6]
        self.bidPrice = cryptoList[7] 
        self.bidQty = cryptoList[8] 
        self.askPrice = cryptoList[9] 
        self.askQty = cryptoList[10] 
        self.openPrice = cryptoList[11] 
        self.highPrice = cryptoList[12] 
        self.lowPrice = cryptoList[13] 
        self.volume = cryptoList[14] 
        self.quoteVolume = cryptoList[15] 
        self.openTime = cryptoList[16] 
        self.closeTime = cryptoList[17] 
        self.firstId = cryptoList[18] 
        self.lastId = cryptoList[19] 
        self.count = cryptoList[20]
                
headers = ['symbol', 'priceChange', 'priceChangePercent', 'weightedAvgPrice', 'prevClosePrice', 'lastPrice','lastQty', 'bidPrice', 'bidQty', 'askPrice', 'askQty', 'openPrice', 'highPrice', 'lowPrice', 'volume', 'quoteVolume', 'openTime', 'closeTime', 'firstId', 'lastId', 'count']

def retunLength(oldLength,newLength):
    x = len(newLength)
    if oldLength > x:
        x = oldLength
    return x

cryptoElist = []
listLength = []
for items in headers:
    listLength.append(0)
with open ("crypto.csv","r") as cryptoData:
    crypto = csv.reader(cryptoData)
    for items in crypto:
        cryptoElist.append(myclass(items))
        for i,item in enumerate (items):
            listLength[i] = retunLength(listLength[i],items[i])
            
print(listLength)
xx = input("Please enter the crypto currency symbol")


for items in cryptoElist:
    if xx.lower()==items.symbol.lower():
        print(items.symbol, items.priceChange,items.priceChangePercent)