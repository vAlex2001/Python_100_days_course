import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  # Load from .env

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_token = os.getenv("SHEETY_TOKEN")
        self.sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
        self.headers = {
            "Authorization": f"Bearer {self.sheety_token}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(self.sheety_endpoint, headers=self.headers, verify=False)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.sheety_endpoint}/{city['id']}",
                json=new_data,
                headers=self.headers,
                verify=False
            )
            print(response.text)
            
    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.sheety_endpoint}/{city['id']}",
                json=new_data,
                headers=self.headers,
                verify=False
            )
            print(response.text)