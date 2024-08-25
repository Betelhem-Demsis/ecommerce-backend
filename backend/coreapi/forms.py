from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'typeusername'
    }))

    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'email'
    }))

    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'password'
    }))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'confirm password'
    }))

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'typeusername'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'password'
    }))
