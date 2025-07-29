import requests
import os
import datetime
import time


class FlightSearch:

    def __init__(self):
        self.token_file_cache = "../../resources/output/.token_temp"
        self.client_id = os.getenv("AMADEUS_ID")
        self.client_secret = os.getenv("AMADEUS_SECRET")
        self._bearer_token = self.get_new_token()

    def get_new_token(self):
        """
        Generates the authentication token used for accessing the Amadeus API and returns it.
        This function makes a POST request to the Amadeus token endpoint with the required
        credentials (API key and API secret) to obtain a new client credentials token.
        Upon receiving a response, the function updates the FlightSearch instance's token.
        Returns:
            str: The new access token obtained from the API response.
        """
        token_from_cache = self.read_token_cache()
        if not token_from_cache:
            token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"

            req_body = {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret
            }

            req_headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }

            response = requests.post(url=token_url, data=req_body, headers=req_headers)
            response.raise_for_status()
            self.write_token_cache(response.json())
            return response.json()["access_token"]
        else:
            print("Token used from cache")
            return token_from_cache

    def get_destination_code(self, city_name):
        cities_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        req_params = {
            "keyword": city_name,
            "max": 2,
            "include": "AIRPORTS",
        }

        req_headers = {
            "Authorization": f"Bearer {self._bearer_token}"
        }

        response = requests.post(url=cities_url, params=req_params, headers=req_headers)
        response.raise_for_status()
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def read_token_cache(self):
        try:
            with open(self.token_file_cache) as file:
                file_content = file.read().split("|")
                if len(file_content) == 2:
                    expiry_time = file_content[0]
                    if int(expiry_time) < int(time.time()):
                        return None
                    else:
                        return file_content[1]
        except FileNotFoundError:
            return None

    def write_token_cache(self, content):
        expiry_time = int((datetime.datetime.now() + datetime.timedelta(seconds=content["expires_in"]-100)).timestamp())
        token = content["access_token"]
        to_write = f"{expiry_time}|{token}"
        with open(self.token_file_cache, "w") as file:
            file.write(to_write)

    def check_flights(self, origin_city_code, destination_city_code, from_time: datetime, to_time: datetime, is_direct=True):
        """
        Searches for flight options between two cities on specified departure and return dates
        using the Amadeus API.
        Parameters:
            origin_city_code (str): The IATA code of the departure city.
            destination_city_code (str): The IATA code of the destination city.
            from_time (datetime): The departure date.
            to_time (datetime): The return date.
            is_direct (Boolean): True if the flight is direct
        Returns:
            dict or None:
            A dictionary containing flight offer data if the query is successful;
            None if there is an error.
        The function constructs a query with the flight search parameters and sends a GET request to
        the API. It handles the response, checking the status code and parsing the JSON data if the
        request is successful. If the response status code is not 200, it logs an error message and
        provides a link to the API documentation for status code details.
        """

        flight_offers_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        # print(f"Using this token to check_flights() {self._token}")
        headers = {"Authorization": f"Bearer {self._bearer_token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "EUR",
            "max": "10",
        }

        response = requests.get(
            url=flight_offers_endpoint,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()


# https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335
# https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference