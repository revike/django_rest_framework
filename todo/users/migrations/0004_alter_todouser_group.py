# Generated by Django 3.2.3 on 2021-05-29 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0003_alter_todouser_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todouser',
            name='group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
