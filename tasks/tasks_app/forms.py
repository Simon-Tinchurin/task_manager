from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import User, Task


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = 'title', 'content'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
