from twilio.rest import Client
import requests

lat = 47.158455

lon = 27.601442

api_key = "your_api_key"

api_url = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {"lat": lat, "lon": lon, "appid": api_key, "cnt": 4}

will_rain = False

account_sid = "you_twilio_sid"
auth_token = "you_twilio_sid_token"

response = requests.get(api_url, params=weather_params, verify=False)
response.raise_for_status()
weather_data_response = response.json()
weather_data = weather_data_response["list"]

for item in weather_data:
    condition_code = (item["weather"][0]["id"])
    if condition_code < 1000:
        will_rain = True
        
if will_rain:
    client  = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella",
        from_='your_phone_number',
        to='recipient_phone_number'
    )
    print("Bring an umbrella")