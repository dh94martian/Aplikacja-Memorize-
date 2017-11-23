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

def topic(request, topic_id):
    """Wyświetla pojedynczy temat i wszystkie powiązane z nim wpisy"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'memorizeapp/topic.html', context)
