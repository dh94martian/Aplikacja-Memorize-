from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    """Dodaj nowy temat"""
    if request.method != 'POST':
        #Nie przekazano żadnych danych - tworzę pusty formularz
        form = TopicForm()
    else:
        #Przekazano dane za pomocą żądania POST - przetwarzam je
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('memorizeapp:topics'))

    context = {'form': form}
    return render(request, 'memorizeapp/new_topic.html', context)

def new_entry(request, topic_id):
    """Dodaj nowy wpis dla określonego tematu"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nie przekazano danych - pusty formularz
        form = EntryForm()
    else:
        #Przekazano dane - przetwarzam je
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('memorizeapp:topic', args=[topic_id]))

    context = { 'topic': topic, 'form': form }
    return render(request, 'memorizeapp/new_entry.html', context)
