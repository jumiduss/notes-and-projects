import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# #print(response) # Returns: <Response [200]>
# #print(response.status_code) # Returns: 200
# #response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["longitude"]
# iss_position = (longitude,latitude)
# print(iss_position)

parameters = {
    "lat": 0,
    "lng":0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)