from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import User

UserModel: User = get_user_model()


class RegisterUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)

    def create(self, validated_data):
        return UserModel.objects.get_or_create(**validated_data)

    def update(self, instance, validated_data):
        pass
