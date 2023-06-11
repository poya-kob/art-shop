from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, mobile_number, **extra_fields):
        if not mobile_number:
            raise ValueError(_("Please enter your mobile number."))
        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.save()
        return user
