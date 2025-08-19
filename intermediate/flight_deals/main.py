import time
from datetime import datetime, timedelta
from intermediate.flight_deals.flight_search import FlightSearch
from intermediate.flight_deals.data_manager import DataManager
from intermediate.flight_deals.flight_data import find_cheapest_flight
from intermediate.flight_deals.notification_service import NotificationService


def main():
    flight_search_service = FlightSearch()
    data_manager_service = DataManager()
    notification_service = NotificationService()

    origin_city_iata = "OTP"

    sheet_data = data_manager_service.get_destination_data()
    print(f"sheet_data:\n {sheet_data}")

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in sheet_data:
        print(f"Getting flights for {destination['city']}...")
        flights = flight_search_service.check_flights(
            origin_city_iata,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        cheapest_flight = find_cheapest_flight(flights)
        print(f"{destination['city']}: EUR {cheapest_flight.price}")
        time.sleep(2)

        if cheapest_flight.price == "N/A":
            print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
            stopover_flights = flight_search_service.check_flights(
                origin_city_iata,
                destination["iataCode"],
                from_time=tomorrow,
                to_time=six_month_from_today,
                is_direct=False
            )
            cheapest_flight = find_cheapest_flight(stopover_flights)
            print(f"Cheapest indirect flight price is: EUR {cheapest_flight.price}")
        data_manager_service.write_in_price_journal(cheapest_flight)

    # stub for user mail notifier
    customer_data = data_manager_service.get_customer_emails()
    customer_email_list = [row["whatIsYourEmailAddress?"] for row in customer_data]
    notification_service.send_email(customer_email_list, f"<Message>")


if __name__ == "__main__":
    main()