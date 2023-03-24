from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import EmailNews


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Enter your first name'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Enter your last name'}))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Enter your username'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': 'Enter your email'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Enter your password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Confirm your password'}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")


class UserLogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input", "placeholder": "Enter your username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input", "placeholder": "Password"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class EmailNewsForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your email'}))

    class Meta:
        model = EmailNews
        fields = ['email']
