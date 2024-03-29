# import requests
import json
from twilio.rest import Client

# api_key = "8f7f2dab51e569f9ca115bec7d6745c0"

# response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?q=Detroit&appid=8f7f2dab51e569f9ca115bec7d6745c0")
# print(response.status_code)
# data = response.json()
data_dict = {}
with open("weather_data.json", "r") as data:
    data_dict = json.load(data)

hour_data = data_dict["list"]
weather_data = []
for value in hour_data:
    a = value["weather"][0]["id"]
    # b = value["weather"][0]["description"]
    weather_data.append(a)

# Twilio recovery code
# Twilio doesn't work now
# CZER1JKCLKN23S8ME8WWU3FH

# Twilio account SID
sid = "ACac73042a59d4cd333d43597b35b59ef1"
# Twilio Auth Token
auth_token = "5c0da295d7b86242d1642fd1adfd5214"
# Twilio Phone Number
phone_number = "+18337024356"

send_message = False
under_eight = [index for index,value in enumerate(weather_data) if value < 800]

for time in under_eight:
    if time < 4:
        send_message = True

account_sid = 'ACac73042a59d4cd333d43597b35b59ef1'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from='+18888080186',
  body='It's going to rain today. Bring an um-bah-rella',
  to='+17343205137'
)

print(message.sid)