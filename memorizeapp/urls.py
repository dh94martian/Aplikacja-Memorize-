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
    
    #Testowanie przekierowania z utworzonego wpisu do listy tematów
    url(r'^topics/test_topic/', views.test_topic, name='test_topic'),
]
