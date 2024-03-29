# Creating a Pixela Account to Track Your Habbits
# $ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
# {"message":"Success.","isSuccess":true}
from http.client import responses
import requests
import json

##### Start of Account Setup Information
pixela_endpoint = "https://pixe.la/v1/users"
user_name = "jumiduss"
token = "jumiduss@gmail.com_health_tracker"

user_params = {
    "token":token,
    "username":user_name,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

headers = {
    "X-USER-TOKEN":token
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
# information = ''

# try:#     
#     with open("information.txt", "a") as file:
#             json.dump(response.text, file)
        
# except (FileExistsError, FileNotFoundError):
#     with open("information.txt","w") as file:
#             json.dump(response.text, file)
##### End of Account Setup Information


# Creating a Graph Definition for our Username
#$ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'
#{"message":"Success.","isSuccess":true}

##### Start of Graph Creation
graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"
graph_id = "cycling01"
graph_name = "Cycling Tracker"

graph_params = {
    "id":graph_id,
    "name":graph_name,
    "unit":"Km",
    "type":"float",
    "color":"momiji",
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
# with open("information.txt","a") as file:
#     json.dump(f"\n\n{response.text}", file)
##### End of Graph Creation


# Viewing this Graph 
# Browse to graph within your account page


# Posting values to the graph
# $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
# {"message":"Success.","isSuccess":true}

##### Start of Posting Data
data_point_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph_id}"
# Date format yyyyMMdd
date = "20240125"
quantity = "2.1"
data_point_params = {
    "date":date,
    "quantity":quantity
}

# response = requests.post(url=data_point_endpoint, json=data_point_params, headers=headers)
# with open("information.txt","a") as file:
#     file.writelines("\n\n")
#     json.dump(response.text, file)
##### End of Posting Data 


# Viewing this Graph 
# Browse to graph within your account page

# Putting new values to existing dates
# curl -X PUT https://pixe.la/v1/users/a-know/graphs/test-graph/<yyyyMMdd> -H 'X-USER-TOKEN:thisissecret' -d '{"quantity":"5","optionalData":"7"}'
# {"message":"Success.","isSuccess":true}

##### Start of Putting Data
mod_date = "20240125"
data_point_mod_endpoint = f"{data_point_endpoint}/{mod_date}"

data_point_mod_endpoint_params = {
    "quantity":"7"
}

# response = requests.put(url=data_point_mod_endpoint, json=data_point_mod_endpoint_params, headers=headers)
# print(response.text)
# with open("information.txt","a") as file:
#     file.writelines("\n\n")
#     json.dump(response.text, file)
##### End of Putting Data


# Deleting existing values 
# curl -X PUT https://pixe.la/v1/users/a-know/graphs/test-graph/<yyyyMMdd> -H 'X-USER-TOKEN:thisissecret'
# {"message":"Success.","isSuccess":true}

# Start of Deleting Data

response = requests.delete(url=data_point_mod_endpoint, headers=headers)
print(response.text)
with open("information.txt","a") as file:
    file.writelines("\n\n")
    json.dump(response.text, file)