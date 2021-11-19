from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    user_id = models.CharField(max_length=20, unique=True, primary_key=True)
    nickname = models.CharField(max_length=8, null=True, blank=True, unique=True)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nickname
