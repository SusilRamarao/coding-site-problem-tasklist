#from django.conf.urls.defaults import *

from problemtasklist.settings import MEDIA_ROOT

from django.urls import path

#from .views import hello

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('hello/')
]

