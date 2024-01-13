from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class RoomNames(models.Model):
    my_user = models.ForeignKey(User,related_name='my_user', on_delete = models.CASCADE)
    other_user = models.ForeignKey(User, on_delete = models.CASCADE)
    group_name = models.CharField(max_length=1000, blank=True)


class MessageHistory(models.Model):
    room = models.ForeignKey(RoomNames, on_delete = models.CASCADE, blank=True)
    sender = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    text = models.TextField(max_length=10000, blank=True)
    sent_date = models.DateTimeField(default=timezone.now)
