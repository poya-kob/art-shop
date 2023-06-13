from django.conf import settings
from sms_ir import SmsIr


def send_sms(otp: int, mobile_number: str) -> None:
    print('saaaaaaaaaalam',otp)
    sms_ir = SmsIr(settings.SMS_API, settings.SMS_NUMBER)
    message = f"""کد ورود( به هیچ عنوان این کد را در اختیار فرد دیگر قرار ندهید.)
    Code:{otp}"""
    sms_ir.send_sms(mobile_number, message, settings.SMS_NUMBER)
