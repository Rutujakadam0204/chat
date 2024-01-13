from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from . models import Profile


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user', 'is_online']