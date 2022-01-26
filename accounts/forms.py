from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    password2 = None

    class Meta:
        model = User
        fields = ("username", "password1", "email")
