"""Wzorce adresów URL dla aplikacji Memorize!"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #Strona logowania
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
]