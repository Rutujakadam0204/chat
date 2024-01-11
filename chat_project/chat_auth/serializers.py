from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

