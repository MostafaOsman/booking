# Generated by Django 4.1 on 2022-09-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0005_remove_user_is_customer_remove_user_is_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("H", "Host"), ("G", "Guest"), ("A", "Admin")],
                default="G",
                max_length=255,
            ),
        ),
    ]
