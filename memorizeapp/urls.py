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

    #Strona przeznaczona do dodawania nowego tematu
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #Strona przeznaczona do dodawania nowego wpisu
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #Strona przeznaczona do edycji wpisu
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
