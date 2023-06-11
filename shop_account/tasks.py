from art_shop.celery import app


@app.task
def send_otp(otp, phone_number):
    # todo: send opt to number
    print(f'otp is => {otp}')
