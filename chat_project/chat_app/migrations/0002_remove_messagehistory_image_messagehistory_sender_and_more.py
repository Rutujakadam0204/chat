# Generated by Django 4.2.9 on 2024-01-13 18:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagehistory',
            name='image',
        ),
        migrations.AddField(
            model_name='messagehistory',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messagehistory',
            name='room',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chat_app.roomnames'),
        ),
        migrations.AlterField(
            model_name='messagehistory',
            name='sent_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 14, 0, 0, 22, 927624)),
        ),
    ]
