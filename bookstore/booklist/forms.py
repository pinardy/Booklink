from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from booklist.query.book import getAllBookIsbnTitle, getBook

COVER_FORMATS = (
    ('paperback', "paperback"),
    ('hardcover', "hardcover"),
)
STATISTICS = (
    ('book', "Book"),
    ('authors', "Authors"),
    ('publisher', "Publishers"),
)

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    authors = forms.CharField(label='Authors', max_length=100)
    publisher = forms.CharField(label='Publisher', max_length=100)
    yearPublish = forms.IntegerField(label='Year Published')
    cost = forms.IntegerField(label='Cost')
    isbn10 = forms.IntegerField(label='ISBN10', min_value=1000000000, max_value=9999999999)
    isbn13 = forms.IntegerField(label='ISBN13', min_value=1000000000000, max_value=9999999999999)
    quantity = forms.IntegerField(label='Quantity', min_value=0)

    def clean(self):
        isbn13 = self.cleaned_data['isbn13']
        book = getBook(isbn13)
        if book:
            raise forms.ValidationError("ISBN13 EXISTS!! PLS MERCY ON THE DATABASE PROF")
    class Meta:
        fields = ('title','authors','publisher','yearPublish','cost','isbn10','isbn13','quantity')


class StockForm(forms.Form):
    title = forms.ChoiceField(choices=getAllBookIsbnTitle())
    quantity = forms.IntegerField(label='quantity', min_value=1)

    class Meta:
        fields = ('title','quantity')

class StatisticsForm(forms.Form):
    choices = forms.ChoiceField(choices=STATISTICS)
    m = forms.IntegerField(label='m', min_value=1)

    class Meta:
        fields = ('choices','m')