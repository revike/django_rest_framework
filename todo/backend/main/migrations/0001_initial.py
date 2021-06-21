# Generated by Django 3.2.3 on 2021-06-16 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='название проекта')),
                ('link', models.CharField(max_length=128, verbose_name='ссылка на репоз-й')),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256, verbose_name='текст заметки')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='создан')),
                ('date_update', models.DateField(auto_now=True, verbose_name='обновлен')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='активен')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.project')),
            ],
        ),
    ]