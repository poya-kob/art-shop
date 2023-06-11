from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache

mobile_number_validator = RegexValidator(
    regex=r'^09\d{9}$',
    message=_("Mobile number format is incorrect"),
)


def otp_validator(otp: int, phone_number: str):
    value = cache.get(phone_number)
    if otp != value:
        return False
    cache.delete(phone_number)
    return True