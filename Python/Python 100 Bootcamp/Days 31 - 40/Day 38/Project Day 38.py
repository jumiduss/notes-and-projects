import requests
import json
from datetime import date,datetime

## Start of Nutritionix
nutritionix_base_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
application_id = "090de8b4"
nutritionix_api_key = "379bdfa515f2cc727c75049ca1d42a3f"

header = {
    "x-app-id":application_id,
    "x-app-key":nutritionix_api_key,
}

def age(birth_date):    
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < ((birth_date).month, birth_date.day))

birth_date = date(1995,4,17)
query = 'Ran 2 Km and walked for 3 Km'
weight = "200"
height = "90.7"

## Start of Setting up first workout
# user_params = {
#     "query":query,
#     "weight_kg":weight,
#     "height_cm":height,
#     "age":age(birth_date)
# }

# request = requests.post(url=nutritionix_base_url,headers=header,json=user_params)
# print(request.text)
## End of Setting up first workout

## End of Nutritionix


## Start of Editing Request Data
with open("information.json","r") as file:
    workout_information = json.load(file)

workout_sets = workout_information["exercises"]
workout_table_data = [{
    "Exercise":(exercise["user_input"]).title(),
    "Duration":exercise["duration_min"],
    "Calories":exercise["nf_calories"],    
    } for exercise in workout_sets]
## End of Editing Request Data


## Start of Sheety
sheety_username = 'd6898de5627f71dd0234e3c95b0585dc'
sheety_projectName = 'myWorkouts'
sheety_sheetName = 'workouts'
sheety_base_url = f"https://api.sheety.co/{sheety_username}/{sheety_projectName}/{sheety_sheetName}"


id = 2

def workout_details(exercise):
    global id
    id += 1
    today = datetime.now()
    today_date = today.strftime("%Y/%m/%d")
    today_time = today.strftime("%H:%M:%S")
    print(today_date)
    print(today_time)
    return {
        "date":today_date,
        "time":today_time,
        "exercise":exercise["Exercise"],
        "duration":exercise["Duration"],
        "calories":exercise["Calories"],
        "id":id
    }


# sheet_get_request = requests.get(url=sheety_base_url)
# print(sheet_get_request.text)

# for i,exercise in enumerate(workout_table_data):
#     workout_table_data[i] = workout_details(exercise)
    
for i,exercise in enumerate(workout_table_data):
    workout_dict = {"workout":workout_details(exercise)}
    sheet_request = requests.post(url=sheety_base_url, json=workout_dict)
    print(sheet_request.text)

# workout_dict = {"workout":workout_table_data}
# print(workout_dict)
# sheet_request = requests.post(url=sheety_base_url, json=workout_dict)
# print(sheet_request.text)    

## End of Sheety