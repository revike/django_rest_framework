# Generated by Django 3.2.3 on 2021-06-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=128, verbose_name='ссылка на репоз-й'),
        ),
    ]
