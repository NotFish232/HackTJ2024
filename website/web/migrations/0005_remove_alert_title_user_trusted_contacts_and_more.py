# Generated by Django 5.0.2 on 2024-02-25 07:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0004_user_phone_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="alert",
            name="title",
        ),
        migrations.AddField(
            model_name="user",
            name="trusted_contacts",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name="Report",
        ),
    ]
