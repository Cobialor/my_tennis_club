from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Member, Cryptols
import pandas as pd
import datetime
from .forms import NameForm
from django.urls import reverse


def displayimage(request):
  template = loader.get_template('displayimage.html')
  return HttpResponse(template.render({},request))


def getCoins(request):
  querySet = Cryptols.objects.all().values()
  template = loader.get_template('cryptom.html')
  context = {
    'cryptoGal': querySet
  }
  return HttpResponse(template.render(context, request))

def getCoinsDetails(request,id):
  querySet = Cryptols.objects.get(id=id)
  template = loader.get_template('cryptodetails.html')
  context = {
    'cryptoGal': querySet
  }
  return HttpResponse(template.render(context, request))

# ###################################
# def details(request, id): #Gets request and id as argument.
#     mymember= Member.objects.get(id=id) #Uses the id to locate the correct record in the Member table
#     template = loader.get_template('details.html')#loads the details.html template.
#     context = {
#       'mymember': mymember #Creates an object containing the member.
      
#     }
# ####################################



def importFromCSV(request):
    dataframe = pd.read_csv('C:\\Users\\Acer\\Desktop\\Web Design Course\\L3 Diploma\\Django-tutorial\\myworld\\my_tennis_club\\members\\data\\crypto.csv',encoding='latin1')
    #dataframe = dataframe.tail(-1)
    




    for d in range(len(dataframe)):
      cryptGal = Cryptols()
      cryptGal.symbol = dataframe.iloc[d]['symbol']
      cryptGal.priceChange = dataframe.iloc[d]['priceChange']
      cryptGal.priceChangePercent = dataframe.iloc[d]['priceChangePercent']
      cryptGal.weightedAvgPrice = dataframe.iloc[d]['weightedAvgPrice']
      cryptGal.prevClosePrice = dataframe.iloc[d]['prevClosePrice']
      cryptGal.lastPrice = dataframe.iloc[d]['lastPrice']
      cryptGal.lastQty = dataframe.iloc[d]['lastQty']
      cryptGal.bidPrice = dataframe.iloc[d]['bidPrice']
      cryptGal.bidQty = dataframe.iloc[d]['bidQty']
      cryptGal.askPrice = dataframe.iloc[d]['askPrice']
      cryptGal.askQty = dataframe.iloc[d]['askQty']
      cryptGal.openPrice = dataframe.iloc[d]['openPrice']
      cryptGal.highPrice = dataframe.iloc[d]['highPrice']
      cryptGal.lowPrice = dataframe.iloc[d]['lowPrice']
      cryptGal.volume = dataframe.iloc[d]['volume']
      cryptGal.quoteVolume = dataframe.iloc[d]['quoteVolume']
      cryptGal.openTime = dataframe.iloc[d]['openTime']
      cryptGal.closeTime = dataframe.iloc[d]['closeTime']
      cryptGal.firstId = dataframe.iloc[d]['firstId']
      cryptGal.lastId = dataframe.iloc[d]['lastId']
      cryptGal.count = dataframe.iloc[d]['count']
      
      #cryptGal.save()  
    return HttpResponse("Data imported successfully")

def filterByFirstname(request):
  querySet =Member.objects.filter(firstname=request.GET['firstname']).values()
  template = loader.get_template('details.html')
  context ={
      'mymember' : querySet[0]
  }
  return HttpResponse(template.render(context,request))




def firstnames(request):
    firstnames= Member.objects.values_list ('firstname')
    template = loader.get_template('firstnames.html')
    context ={
        'firstnames': firstnames
    }
    return HttpResponse(template.render(context,request))





def members(request):
    mymembers= Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context ={
      'mymembers' : mymembers
    }
    return HttpResponse(template.render(context,request))
  
def details(request, id): #Gets request and id as argument.
    mymember= Member.objects.get(id=id) #Uses the id to locate the correct record in the Member table
    template = loader.get_template('details.html')#loads the details.html template.
    context = {
      'mymember': mymember #Creates an object containing the member.
      
    }
    return HttpResponse(template.render(context,request))#Sends the object to the template.Outputs the HTML that is rendered by the template.
def members2(request):
    mymembers= Member.objects.all().values()
    template = loader.get_template('all_members2.html')
    context ={
      'mymembers' : mymembers
    }
    return HttpResponse(template.render(context,request))
  
def details2(request, id): #Gets the id as an argument.
    mymember= Member.objects.get(id=id) #Uses the id to locate the correct record in the Member table
    template = loader.get_template('details2.html')#loads the details.html template.
    context = {
      'mymember': mymember #Creates an object containing the member.
      
    }
    return HttpResponse(template.render(context,request))#Sends the object to the template.Outputs the HTML that is rendered by the template.
  
  