from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
    """Strona główna dla aplikacji Memorize!"""
    return render(request, 'memorizeapp/index.html')

def topics(request):
    """Wyświetlenie wszystkich tematów"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'memorizeapp/topics.html', context)
