from django.contrib.auth.models import AbstractUser
from django.db import models


class ToDoUser(AbstractUser):
    """Модель ToDoUser"""
    username = models.CharField(max_length=56, unique=True, null=True)
    email = models.EmailField(max_length=64, blank=True,
                              unique=True, verbose_name='email')
