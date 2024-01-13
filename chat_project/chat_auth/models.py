from django.db import models
from django.contrib.auth.models import User


class Interest(models.Model):
    title = models.CharField(blank=True, max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    is_online = models.BooleanField(default=False)
    phone = models.IntegerField(null=True, blank=True)
    gender = models.CharField(blank=True, max_length=100)
    country = models.TextField(blank=True, max_length=1000)
    interests = models.ManyToManyField(Interest)
