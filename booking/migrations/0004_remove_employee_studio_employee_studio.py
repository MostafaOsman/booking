# Generated by Django 4.1 on 2022-10-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0003_employee"),
    ]

    operations = [
        migrations.RemoveField(model_name="employee", name="studio",),
        migrations.AddField(
            model_name="employee",
            name="studio",
            field=models.ManyToManyField(to="booking.studio"),
        ),
    ]
