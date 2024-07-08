import smtplib
import time

import requests
from datetime import datetime
from email.message import EmailMessage
from Config import email_config

MY_LAT = 34.857660  # Your latitude
MY_LONG = -92.423740  # Your longitude
MY_EMAIL = email_config.MY_EMAIL
PASSWORD = email_config.PASSWORD


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    is_in_lat = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
    is_in_lon = MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    if is_in_lat and is_in_lon:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = datetime.fromisoformat(data['results']['sunrise']).astimezone().hour
    sunset_hour = datetime.fromisoformat(data['results']['sunset']).astimezone().hour

    current_hour = datetime.now().hour
    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True
    else:
        return False


def send_email():

    message = EmailMessage()
    message.set_content("Look up to see the iss")
    message["Subject"] = 'International Space Station Overhead'
    message['From'] = MY_EMAIL
    message['To'] = 'zgjohnson94@gmail.com'

    with smtplib.SMTP("smtp.gmail.com", 587) as email:
        email.starttls()
        email.login(user=MY_EMAIL, password=PASSWORD)
        email.send_message(message)


while True:
    time.sleep(60)
    print('ran')
    if is_iss_overhead() and is_night():
        send_email()
