from django.db import models


class User(models.Model):
    """Модель User"""
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'user: {self.user_name} --> email: {self.email}'
