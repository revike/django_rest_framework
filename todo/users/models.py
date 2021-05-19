from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class ToDoUser(AbstractBaseUser):
    """Модель ToDoUser"""
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.user_name} - {self.email}'
