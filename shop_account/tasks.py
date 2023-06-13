from art_shop.celery import app
from utils.sms import send_sms


@app.task
def send_otp(otp, phone_number):
    send_sms(otp, phone_number)
