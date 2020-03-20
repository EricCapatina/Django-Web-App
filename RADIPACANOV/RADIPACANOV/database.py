from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        help_texts = {
            'username': None,
            'email': None,
        }

class CreateNote(forms.ModelForm):
    class Meta:
        model = models.Notes
        fields = ['title', 'body']