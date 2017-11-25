from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from booklist.forms import RegistrationForm
from booklist.forms import BookForm

from booklist.query import insertBook

def index(request):
    return render(request, 'booklist/index.html', {})

def work(request):
    return render(request, 'booklist/work.html', {})

def base(request):
    return render(request, 'booklist/base.html', {})

def browse(request):
    return render(request, 'booklist/browse.html', {})

def stock(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get(title)
            covFormat = form.cleaned_data.get(covFormat)
            noPages = form.cleaned_data.get(noPages)
            authors = form.cleaned_data.get(authors)
            publisher = form.cleaned_data.get(publisher)
            yearPublish = form.cleaned_data.get(yearPublish)
            edition = form.cleaned_data.get(edition)
            isbn10 = form.cleaned_data.get(isbn10)
            isbn13 = form.cleaned_data.get(isbn13)
            #put update function here
            insertBook (title,covFormat,noPages,authors,publisher,yearPublish,edition,isbn10,isbn13)
            return redirect('index')
    else:
        form = BookForm
    return render(request, 'booklist/stock.html', {'form': form})

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


