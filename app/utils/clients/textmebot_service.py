import os
import requests
from django.conf import settings

def send_verification_code(phone_number, message):
    
    api_key = os.getenv('TEXTMEBOT_API_KEY')
    #url = "https://api.textmebot.com/send.php"
    url = (f'https://api.textmebot.com/send.php?recipient={phone_number}&apikey={api_key}&text={message}')
    # payload = {
    #     'number': phone_number,
    #     'message': message,
    #     # 'message': f"Your verification code is {code}",
    #     'key': api_key
    # }
    print(url)
    response = requests.post(url)
    return response.status_code == 200
