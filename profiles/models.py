from django.db import models
from django.contrib.auth.models import AbstractUser


class AbstractUser(Registration):
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2']
