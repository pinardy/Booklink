from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')