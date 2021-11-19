from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, user_id, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
            )
        return self.create_user(user_id, password, **other_fields)

    def create_user(self, user_id,  password, **other_fields):

        if not user_id:
            raise ValueError(_('You must provide an email address'))

        user = self.model(user_id = user_id, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser):

    user_id = models.CharField(max_length=20, unique=True, primary_key=True)
    nickname = models.CharField(max_length=15, null=True, blank=True, unique=True)
    password = models.CharField('비밀번호', max_length=200)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user_id
