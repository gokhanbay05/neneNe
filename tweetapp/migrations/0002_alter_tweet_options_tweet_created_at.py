# Generated by Django 5.0.6 on 2024-11-30 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tweetapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tweet",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="tweet",
            name="created_at",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
