# Generated by Django 5.0.2 on 2024-02-25 01:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="photos"),
        ),
    ]
