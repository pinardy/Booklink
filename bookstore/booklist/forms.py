from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class BookForm(forms.Form):
    title = forms.EmailField(label='Title', max_length=100)
    covFormat = forms.EmailField(label='Cover Format', max_length=100)
    noPages = forms.EmailField(label='Number of Pages', max_length=100)
    authors = forms.EmailField(label='Authors', max_length=100)
    publisher = forms.EmailField(label='Publisher', max_length=100)
    yearPublish = forms.EmailField(label='Year Published', max_length=100)
    edition = forms.EmailField(label='Edition', max_length=100)
    isbn10 = forms.EmailField(label='ISBN10', max_length=100)
    isbn13 = forms.EmailField(label='ISBN13', max_length=100)

    class Meta:
        fields = ('title','covFormat','noPages','authors','publisher','yearPublish','edition','edition','isbn10','isbn13')