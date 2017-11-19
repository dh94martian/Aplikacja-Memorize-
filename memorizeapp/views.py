from django.shortcuts import render

# Create your views here.
def index(request):
	# strona główna aplikacji Memorize!
	return render(request, 'memorizeapp/index.html')