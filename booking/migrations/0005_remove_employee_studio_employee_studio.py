# Generated by Django 4.1 on 2022-10-23 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0004_remove_employee_studio_employee_studio"),
    ]

    operations = [
        migrations.RemoveField(model_name="employee", name="studio",),
        migrations.AddField(
            model_name="employee",
            name="studio",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="booking.studio",
            ),
            preserve_default=False,
        ),
    ]
