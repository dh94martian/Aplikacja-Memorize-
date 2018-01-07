from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """Wylogowanie uzytkownika"""
    logout(request)
    return HttpResponseRedirect(reverse('memorizeapp:index'))

def register(request):
    """Rejestracja nowego użytkownika"""
    if request.method != 'POST':
        #Wyświetlenie pustego formularza rejestracji
        form = UserCreationForm()
    else:
        #Przetworzenie wypełnionego formularza
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Zalogowanie i przekierowanie na stronę główną
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('memorizeapp:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
