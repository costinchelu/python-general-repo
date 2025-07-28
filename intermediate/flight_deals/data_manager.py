import requests
import os
from pprint import pprint


class DataManager:

    def __init__(self):
        self.sheety_project_id = os.getenv("SHEETY_ID")
        self.sheety_token = os.getenv("SHEETY_TOKEN")
        self.sheety_headers = {
            "Authorization": f"Bearer {self.sheety_token}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        sheety_endpoint_get = f"https://api.sheety.co/{self.sheety_project_id}/flightTrack/prices"

        sheety_get_response = requests.get(
            url=sheety_endpoint_get,
            headers=self.sheety_headers
        )
        sheety_get_response.raise_for_status()
        self.destination_data = sheety_get_response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            sheety_endpoint_put = f"https://api.sheety.co/{self.sheety_project_id}/flightTrack/prices/{city["id"]}"
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheety_put_response = requests.put(
                url=sheety_endpoint_put,
                headers=self.sheety_headers,
                json=new_data
            )
            sheety_put_response.raise_for_status()
            print(sheety_put_response.text)