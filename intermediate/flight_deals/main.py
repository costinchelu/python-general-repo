import time
from datetime import datetime, timedelta
from intermediate.flight_deals.flight_data import FlightData
from intermediate.flight_deals.data_manager import DataManager
from intermediate.flight_deals.flight_search import find_cheapest_flight


def main():
    flight_data = FlightData()
    sheety = DataManager()
    # flight_search = FlightSearch()

    origin_city_iata = "IST"

    sheet_data = sheety.get_destination_data()
    # for row in sheet_data:
    #     if row["iataCode"] == "":
    #         row["iataCode"] = flight_data.get_destination_code(row["city"])
    #     # slowing down requests to avoid rate limit
    #     time.sleep(2)
    print(f"sheet_data:\n {sheet_data}")

    # sheety.destination_data = sheet_data
    # sheety.update_destination_codes()

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in sheet_data:
        print(f"Getting flights for {destination['city']}...")
        flights = flight_data.check_flights(
            origin_city_iata,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        cheapest_flight = find_cheapest_flight(flights)
        print(f"{destination['city']}: EUR {cheapest_flight.price}")
        # Slowing down requests to avoid rate limit
        time.sleep(2)


if __name__ == "__main__":
    main()




# https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335
# https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference