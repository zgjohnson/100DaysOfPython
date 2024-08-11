import requests
from twilio.rest import Client

from Config import open_weather_config, twillio_config

open_weather_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
account_sid = twillio_config.ACCOUNT_SID
auth_token = twillio_config.AUTH_TOKEN

parameters = {
    'lat': 35.335,
    'lon': -94.790,
    'appid': open_weather_config.API_KEY,
    'units': 'imperial',
    'cnt': 4
}

response = requests.get(url=open_weather_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]
will_rain = False
for hour_data in weather_data:
    condition_codes = hour_data["weather"][0]["id"]
    if int(condition_codes) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+18884489645',
        body='It\'s going to rain today. Don\'t forget to bring an ☔',
        to='+15016505352'
    )
    print(message.status)