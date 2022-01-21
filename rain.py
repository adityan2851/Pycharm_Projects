import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api = "API_KEY"
account_sid = "ACC_SID"
auth_token = "AUTH_TOKEN"

weather_params = {
    "lat": 11.652120,
    "lon": 78.157982,
    "appid": api,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()

# print(response.status_code)

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
# print(weather_data["hourly"][0]["weather"][0]["id"])

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if not will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
                .create(
                     body="Its going to rain today!! Get an Umberella ☂️",
                     from_='+15075754505',
                     to='+919965264005'
                 )
    print(message.status)
# else:
#     print("Not Needed")