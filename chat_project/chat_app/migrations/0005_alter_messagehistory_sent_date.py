# Generated by Django 4.2.9 on 2024-01-13 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0004_alter_messagehistory_sent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagehistory',
            name='sent_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 13, 19, 53, 28, 485569, tzinfo=datetime.timezone.utc)),
        ),
    ]
