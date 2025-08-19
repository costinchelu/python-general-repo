import requests
import os


class DataManager:

    def __init__(self):
        self._sheety_project_id = os.getenv("SHEETY_ID")
        self._sheety_token = os.getenv("SHEETY_TOKEN")
        self._sheety_headers = {
            "Authorization": f"Bearer {self._sheety_token}"
        }
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        sheety_endpoint_get = f"https://api.sheety.co/{self._sheety_project_id}/flightTrack/prices"

        sheety_get_response = requests.get(
            url=sheety_endpoint_get,
            headers=self._sheety_headers
        )
        sheety_get_response.raise_for_status()
        self.destination_data = sheety_get_response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            sheety_endpoint_put = f"https://api.sheety.co/{self._sheety_project_id}/flightTrack/prices/{city["id"]}"
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheety_put_response = requests.put(
                url=sheety_endpoint_put,
                headers=self._sheety_headers,
                json=new_data
            )
            sheety_put_response.raise_for_status()
            print(sheety_put_response.text)

    def write_in_price_journal(self, data):
        sheety_endpoint_post_journal = f"https://api.sheety.co/{self._sheety_project_id}/flightTrack/journal"
        new_data = {
            "journal": {
                "from": data.origin_airport,
                "to": data.destination_airport,
                "price": data.price,
                "out": data.out_date,
                "return": data.return_date
            }
        }
        sheety_post_journal_response = requests.post(
            url=sheety_endpoint_post_journal,
            headers=self._sheety_headers,
            json=new_data
        )
        sheety_post_journal_response.raise_for_status()

    def get_customer_emails(self):
        sheety_endpoint_get_user_email = f"https://api.sheety.co/{self._sheety_project_id}/flightTrack/users"
        sheety_get_user_email_response = requests.get(url=sheety_endpoint_get_user_email, headers=self._sheety_headers)
        sheety_get_user_email_response.raise_for_status()
        self.customer_data = sheety_get_user_email_response.json()["users"]
        return self.customer_data