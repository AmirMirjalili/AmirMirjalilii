from kavenegar import KavenegarAPI
import random
from .models import OTP

def send_otp(phone):
    otp_code = random.randint(100000, 999999)
    OTP.objects.create(phone=phone, code=str(otp_code))

    api = KavenegarAPI('4B55782B487A6461685534707A75366C4A5658536F4D555433794B4C34545531417270392F76526E5A74383D')
    params = {
        'receptor': phone,
        'message': f"Your OTP code is: {otp_code}",
        'sender': '',
    }
    try:
        response = api.sms_send(params)
        print(f"OTP {otp_code} sent to {phone}")
    except Exception as e:
        print(f"Error sending OTP: {str(e)}")

    return otp_code
