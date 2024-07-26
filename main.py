import os
from dotenv import load_dotenv
from twilio.rest import Client
import random
import requests 

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
YOUR_PHONE_NUMBER = os.getenv('YOUR_PHONE_NUMBER')

def get_random_quote():
    quotes = [
        "the people who are crazy enough to think that they can change the world are the ones who do",
        "the scrolling is endless, life isnt"

    ]
    return random.choice(quotes)

def send_sms(message_body):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message_body,
        number_from=TWILIO_PHONE_NUMBER,
        number_to=YOUR_PHONE_NUMBER
    )
    print(f"Quote of the Day Sent")

if __name__ == "__main__":
    message_body = get_random_quote()
    send_sms(message_body)