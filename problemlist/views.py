from django.shortcuts import render
from django.http import HttpResponse

from .leet_test import leetclass as leet
from .webscrapper_test import webscrapper

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#urlpatterns = ...

#urlpatterns += staticfiles_urlpatterns()

def hello(request):

    data = leet.get_data()

    final_data = []

    scrapped_data = webscrapper.get_scrapped_data()

    context ={
        "data":"List of problems solved",
        "list": []
    }

    return render(request, 'problemlist/testhtml.html')