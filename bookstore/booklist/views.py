from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from booklist.query import insertBook, retrieveProfile
from booklist.forms import BookForm, RegistrationForm

from booklist.helperFunctions import input_formatting

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
            title = form.cleaned_data.get('title')
            title = input_formatting(title)
            covFormat = form.cleaned_data.get('covFormat')
            noPages = form.cleaned_data.get('noPages')
            authors = form.cleaned_data.get('authors')
            publisher = form.cleaned_data.get('publisher')
            yearPublish = form.cleaned_data.get('yearPublish')
            edition = form.cleaned_data.get('edition')
            isbn10 = form.cleaned_data.get('isbn10')
            isbn13 = form.cleaned_data.get('isbn13')
            quantity = form.cleaned_data.get('quantity')
            #put update function here
            insertBook (title,covFormat,noPages,authors,publisher,yearPublish,edition,isbn10,isbn13)
            return redirect('index')
    else:
        form = BookForm
    return render(request, 'booklist/stock.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
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
                # TODO: This should redirect to a success page
                return redirect('index')

        # If GET request
        else:
            form = RegistrationForm()
        return render(request, 'booklist/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'booklist/index.html', {})

def login_view(request):
    """
    Displays the login form and handles the login action.
    """
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():

                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user)

                return redirect('index')
        else:
            form = AuthenticationForm()

        return render(request, 'booklist/login.html', {'form': form})

def profile(request):
    """
    Profile Query
    """
    if not (request.user.is_authenticated):
        return redirect('index')
    else:
        user_profile = retrieveProfile(request.user.username)
        return render(request, 'booklist/profile.html', {'user_profile': user_profile})