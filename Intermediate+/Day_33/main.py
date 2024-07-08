import requests
import datetime as dt

parameters = {
    'lat': 34.857660,
    'lng': -92.423740,
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = dt.datetime.fromisoformat(data['results']['sunrise']).astimezone()
sunset = dt.datetime.fromisoformat(data['results']['sunset']).astimezone()
print(sunrise)
print(sunset)
# print(dt.datetime.now(tz=dt.timezone.utc) )
# print(dt.datetime.now())
