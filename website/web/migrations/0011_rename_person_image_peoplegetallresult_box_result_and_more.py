# Generated by Django 5.0.2 on 2024-02-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0010_peoplegetallresult"),
    ]

    operations = [
        migrations.RenameField(
            model_name="peoplegetallresult",
            old_name="person_image",
            new_name="box_result",
        ),
        migrations.AddField(
            model_name="peoplegetallresult",
            name="cropped_result",
            field=models.CharField(default="", max_length=500),
            preserve_default=False,
        ),
    ]
