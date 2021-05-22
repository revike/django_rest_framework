from django.db import models

from users.models import ToDoUser


class Project(models.Model):
    """Модель Project"""
    name = models.CharField(max_length=32, verbose_name='название проекта')
    link = models.CharField(max_length=128, verbose_name='ссылка на репоз-й')
    users = models.ManyToManyField(ToDoUser, verbose_name='пользователи')


class ToDo(models.Model):
    """Модель заметка"""
    project = models.ForeignKey(Project, models.PROTECT)
    text = models.CharField(max_length=256, verbose_name='текст заметки')
    date_creation = models.DateField(auto_now_add=True, verbose_name='создан')
    date_update = models.DateField(auto_now=True, verbose_name='обновлен')
    user = models.OneToOneField(ToDoUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='активен')
