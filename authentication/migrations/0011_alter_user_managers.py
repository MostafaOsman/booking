# Generated by Django 4.1 on 2022-10-21 14:14

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0010_delete_usermanager"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
    ]