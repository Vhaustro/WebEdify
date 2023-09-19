from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    class Meta:
        model = AbstractUser
        fields = ['username', 'email', 'password1', 'password2']

        def __str__(self):
            return self.username
        