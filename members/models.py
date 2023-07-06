from django.db import models

#class declared to crate a table called Member in our model.
class Member(models.Model):
    #first field of our model and it's attribute, other fields of our model as assigned in similar manner
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    # null= true implies that this field can be left blank
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    
    #function to format the value of some fields of our model to strings
    def __str__(self):  
        return f'{self.firstname} {self.lastname}' 
 
 #Creates a python class named Cryptols as model to store the cryptocurrency data of our csv file
 #taking Model as parameter
class Cryptols(models.Model):
    #Symbol field is defined using the field type CharField,it is similar to 
    # other fields with field type CharField
    symbol = models.CharField(max_length=13, null=True) #,unique = True
    #priceChange field is defined using the field type FloatField,it is similar to 
    # other fields with field type FloatField
    priceChange = models.FloatField(max_length=14, null=True) 
    priceChangePercent = models.FloatField(max_length=18, null=True) 
    weightedAvgPrice = models.FloatField(max_length=16, null=True) 
    prevClosePrice = models.FloatField(max_length=17, null=True) 
    lastPrice = models.FloatField(max_length=16, null=True)
    lastQty = models.FloatField(max_length=17, null=True) 
    bidPrice = models.FloatField(max_length=16, null=True) 
    bidQty = models.FloatField(max_length=18, null=True) 
    askPrice = models.FloatField(max_length=16, null=True) 
    askQty = models.FloatField(max_length=18, null=True) 
    openPrice = models.FloatField(max_length=16, null=True) 
    highPrice = models.FloatField(max_length=16, null=True) 
    lowPrice = models.FloatField(max_length=16, null=True) 
    volume = models.FloatField(max_length=21, null=True) 
    quoteVolume = models.FloatField(max_length=19, null=True) 
    openTime = models.IntegerField(max_length=13, null=True) 
    closeTime = models.IntegerField(max_length=13, null=True) 
    firstId = models.IntegerField(max_length=10, null=True) 
    lastId = models.IntegerField(max_length=10, null=True) 
    count = models.IntegerField(max_length=7, null=True)
    
    def __str__(self): #overides the variable type from it's default type to string 
        return f'{self.symbol} {self.priceChange}' 
