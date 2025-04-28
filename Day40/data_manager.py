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
        
        # Save your Sheety endpoints an environment variables
        # self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        # self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        
        self.headers = {
            "Authorization": f"Bearer {self.sheety_token}"
        }
        self.destination_data = {}
        self.customer_data = {}

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
            
    # To be implemented after the google form is created and linked to the users sheet.
    # def get_customer_emails(self):
    #     response = requests.get(url=self.users_endpoint)
    #     data = response.json()
    #     # See how Sheet data is formatted so that you use the correct column name!
    #     # pprint(data)
    #     # Name of spreadsheet 'tab' with the customer emails should be "users".
    #     self.customer_data = data["users"]
    #     return self.customer_data