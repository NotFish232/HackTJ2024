# Generated by Django 5.0.2 on 2024-02-25 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0007_alter_alert_contact_alter_alert_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alert",
            name="person",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="web.person",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="person",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="web.person",
            ),
        ),
    ]
