from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members2/', views.members2, name='members2'),
    path('members2/details2/<int:id>', views.details2, name='details2'),
    path('members/firstnames', views.firstnames, name='firstnames'),
    path('members/search-member', views.filterByFirstname, name='searchMember'),
    path('members/import-data', views.importFromCSV, name='importData'),
    path('members/cryptom', views.getCoins, name='cryptol'),
    path('members/displayimage', views.displayimage, name='displayimage'),
    path('members/getcoinsdetails/<int:id>', views.getCoinsDetails, name='getcoinsdetails'),
    #path('members/update-name-success', views.updateNameSuccess, name='updateNameSuccess'),

]
 