from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import User

UserModel: User = get_user_model()


class RegisterUserSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=11)

    def create(self, validated_data):
        return UserModel.objects.create(is_active=False, **validated_data)

    def update(self, instance, validated_data):
        pass

    def validate_mobile_number(self, value: str):
        """
             Check that the mobile number is unique.
        """
        if User.objects.filter(mobile_number=value).exists():
            raise serializers.ValidationError(_('mobile number is not unique!!'))
        return value
