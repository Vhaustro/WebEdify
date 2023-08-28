# profiles/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2']
