from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

COVER_FORMATS = (
    (1, "paperback"),
    (2, "hardcover"),
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    covFormat = forms.ChoiceField(label='Cover Format', choices=COVER_FORMATS)
    noPages = forms.IntegerField(label='Number of Pages', min_value=0)
    authors = forms.CharField(label='Authors', max_length=100)
    publisher = forms.CharField(label='Publisher', max_length=100)
    yearPublish = forms.IntegerField(label='Year Published')
    edition = forms.IntegerField(label='Edition', min_value=1)
    isbn10 = forms.IntegerField(label='ISBN10', min_value=1000000000, max_value=9999999999)
    isbn13 = forms.IntegerField(label='ISBN13', min_value=1000000000000, max_value=9999999999999)
    quantity = forms.IntegerField(label='Quantity', min_value=0)

    class Meta:
        fields = ('title','covFormat','noPages','authors','publisher','yearPublish','edition','edition','isbn10','isbn13','quantity')


class StockForm(forms.Form):
    isbn13 = forms.IntegerField(label='ISBN10', min_value=1000000000, max_value=9999999999)
    quantity = forms.IntegerField(label='Quantity', min_value=0)

    class Meta:
        fields = ('isbn13','quantity')