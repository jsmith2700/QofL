from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput,TextInput

##Register User (Model Form)##
class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        }

##Autheticate a user (Model Form)##
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())