# Generated by Django 4.1 on 2022-09-29 14:09

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0006_user_role"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.AlterField(
            model_name="user", name="birth_date", field=models.DateField(null=True),
        ),
    ]
