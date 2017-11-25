from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from booklist.forms import RegistrationForm


def index(request):
    return render(request, 'booklist/index.html', {})

def work(request):
    return render(request, 'booklist/work.html', {})

def base(request):
    return render(request, 'booklist/base.html', {})

def browse(request):
    return render(request, 'booklist/browse.html', {})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #TODO: This should redirect to a success page
            return redirect('index')

    # If GET request
    else:
        form = RegistrationForm()
    return render(request, 'booklist/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'booklist/index.html', {})


