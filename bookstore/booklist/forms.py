from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    covFormat = forms.CharField(label='Cover Format', max_length=100)
    noPages = forms.CharField(label='Number of Pages', max_length=100)
    authors = forms.CharField(label='Authors', max_length=100)
    publisher = forms.CharField(label='Publisher', max_length=100)
    yearPublish = forms.CharField(label='Year Published', max_length=100)
    edition = forms.CharField(label='Edition', max_length=100)
    isbn10 = forms.CharField(label='ISBN10', max_length=100)
    isbn13 = forms.CharField(label='ISBN13', max_length=100)

    class Meta:
        fields = ('title','covFormat','noPages','authors','publisher','yearPublish','edition','edition','isbn10','isbn13')