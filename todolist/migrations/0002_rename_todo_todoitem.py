# Generated by Django 5.0.7 on 2024-07-29 02:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='TodoItem',
        ),
    ]
