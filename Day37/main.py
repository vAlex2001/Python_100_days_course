import requests
from datetime import datetime

# This is the linkf format to access the graph
# https://pixe.la/v1/users/alextest01/graphs/graph1.html

USERNAME = "alextest01"
TOKEN = "abcdefghijkl"

########## Creating an account on pixela. ##########
pixela_endpoint_for_creating_user = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint_for_creating_user, json=user_parameters, verify=False)

try:
    #response.raise_for_status()
    print("User created successfully!")
except requests.exceptions.HTTPError as err:
    if response.status_code == 409:
        print("User already exists.")
    else:
        print(f"Something went wrong: {err}")

#print(response.text)

########## Creating a graph on pixela. ##########

graph_endpoint = f"{pixela_endpoint_for_creating_user}/{USERNAME}/graphs"

graph_configuration = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes/day",
    "type": "float",
    "color": "kuro",
}

authentication_header = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_configuration, headers=authentication_header, verify=False)
#print(response.text)

########## Creating a pixel in pixela. ##########

today_date = datetime.today().strftime('%Y%m%d')
#print(today_date)

existing_graph = f"{graph_endpoint}/graph1"

pixel_configuration = {
    "date": today_date,
    "quantity": "1",
}

response = requests.post(url=existing_graph, json=pixel_configuration, headers=authentication_header, verify=False)
#print(response.text)

########## Modifying a pixel in pixela. ##########

existing_pixel = f"{existing_graph}/{today_date}"
#print(existing_pixel)

update_pixel_configuration = {
    "quantity": "5",
}

response = requests.put(url=existing_pixel, json=update_pixel_configuration, headers=authentication_header, verify=False)
response.raise_for_status()

########## Delete an existing pixel. ##########

response = requests.delete(url=existing_pixel, headers=authentication_header, verify=False)


