from django.shortcuts import render

# Create your views here.

def index(request):
    """Strona główna dla aplikacji Memorize!"""
    return render(request, 'memorizeapp/index.html')
