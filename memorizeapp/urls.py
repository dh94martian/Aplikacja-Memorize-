"""Wzorce adresów URL dla memorizeapp"""

from django.conf.urls import url

from . import views

urlpatterns = [
    #Strona główna
    url(r'^$', views.index, name='index'),

    #Wyświetlenie wszystkich tematów
    url(r'^topics/$', views.topics, name='topics'),

    #Strona szczegółowa dotycząca pojedynczego tematu
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
