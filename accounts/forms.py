from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Email address',
    }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Password',
    }))
    class Meta:
        model = User
        fields = ['username', 'password']