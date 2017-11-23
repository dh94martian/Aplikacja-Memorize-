"""Wzorce adresów URL dla memorizeapp"""

from django.conf.urls import url

from . import views

urlpatterns = [
    #Strona główna
    url(r'^$', views.index, name='index'),
]
