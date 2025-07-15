import requests
from datetime import datetime
from pprint import pprint

import requests


class FlightScheduleService:
    BASE_STACK_URL = 'https://api.stackaviation.com/flights'
    BASE_SKY_URL = 'https://partners.api.skyscanner.net/flights'

    def get_flights(self, from_city: str, to_city: str, date: datetime):
        # Make a GET request to the StackAviation API
        stack_response = requests.get(
            f'https://api.stackaviation.com/flights?from_city={from_city}&to_city={to_city}&date={date.isoformat()}')
        stack_flights = stack_response.json()

        # Make a GET request to the Skyscanner API
        sky_response = requests.get(
            f'https://partners.api.skyscanner.net/flights?from_city={from_city}&to_city={to_city}&date={date.isoformat()}')
        sky_flights = sky_response.json()

        # Combine the flights from both APIs
        combined_flights = stack_flights + sky_flights

        return combined_flights

    def get_cheapest_flight(self, from_city: str, to_city: str, date: datetime):
        flights = self.get_flights(from_city, to_city, date)

        # Assuming each flight in the list is a dict with a 'price' field
        cheapest_flight = min(flights, key=lambda flight: flight['price'])

        return cheapest_flight

    def get_non_stop_flights(self, from_city: str, to_city: str, date: datetime):
        flights = self.get_flights(from_city, to_city, date)
        non_stop_flights = [flight for flight in flights if flight['stops'] == 0]
        return non_stop_flights

    def get_earliest_flight(self, from_city: str, to_city: str, date: datetime):
        flights = self.get_flights(from_city, to_city, date)
        earliest_flight = min(flights, key=lambda flight: flight['departure_time'])
        return earliest_flight

    def get_flights_after_time(self, from_city: str, to_city: str, date: datetime, time: datetime.time):
        flights = self.get_flights(from_city, to_city, date)
        flights_after_time = [flight for flight in flights if flight['departure_time'] > time]
        return flights_after_time

    def get_flights_arriving_before(self, from_city: str, to_city: str, date: datetime, time: datetime.time):
        flights = self.get_flights(from_city, to_city, date)
        flights_arriving_before = [flight for flight in flights if flight['arrival_time'] < time]
        return flights_arriving_before

    def get_direct_flights(self, from_city: str, to_city: str, date: datetime):
        return self.get_non_stop_flights(from_city, to_city, date)

    def get_latest_flight(self, from_city: str, to_city: str, date: datetime):
        flights = self.get_flights(from_city, to_city, date)
        latest_flight = max(flights, key=lambda flight: flight['departure_time'])
        return latest_flight

    def get_business_class_flight(self, from_city: str, to_city: str, date: datetime):
        flights = self.get_flights(from_city, to_city, date)
        business_flights = [flight for flight in flights if flight['class'] == 'business']
        return business_flights

    def get_red_eye_flights(self, from_city: str, to_city: str, date: datetime):
        flights = self.get_flights(from_city, to_city, date)
        red_eye_flights = [flight for flight in flights if
                           flight['departure_time'] >= datetime.time(21, 0) and flight['arrival_time'] <= datetime.time(
                               5, 0)]
        return red_eye_flights

    def get_flights_with_layover_less_than(self, from_city: str, to_city: str, date: datetime, duration: int):
        flights = self.get_flights(from_city, to_city, date)
        flights_with_short_layovers = [flight for flight in flights if flight['layover'] < duration]
        return flights_with_short_layovers

    def get_duration_of_direct_flight(self, from_city: str, to_city: str, date: datetime):
        direct_flights = self.get_direct_flights(from_city, to_city, date)
        if direct_flights:
            return direct_flights[0]['duration']
        else:
            return None

    def get_operating_airlines(self, from_city: str, to_city: str, date: datetime):
        flights = self.get_flights(from_city, to_city, date)
        airlines = {flight['airline'] for flight in flights}
        return airlines

    def get_flight_stopovers(self, from_city: str, to_city: str, date: datetime):
        flights = self.get_flights(from_city, to_city, date)
        stopovers = [flight['stops'] for flight in flights]
        return stopovers

    def get_flights_departing_in_time_range(self, from_city: str, to_city: str, date: datetime,
                                            start_time: datetime.time, end_time: datetime.time):
        flights = self.get_flights(from_city, to_city, date)
        flights_in_time_range = [flight for flight in flights if start_time <= flight['departure_time'] <= end_time]
        return flights_in_time_range


if __name__ == '__main__':

    # For use case 4) - Earliest flight from Tianjin to Nanjing next Wednesday
    next_wednesday = (datetime.now() + timedelta((2 - datetime.now().weekday() + 7) % 7)).strftime('%Y-%m-%d')
    flights = get_flight_schedules('TSN', 'NKG')
    if flights and 'data' in flights:
        flights = filter_flights(flights['data'],
                                 lambda flight: flight['departure']['estimated'] and flight['departure'][
                                     'estimated'].startswith(next_wednesday))
        earliest_flight = min(flights, key=lambda flight: flight['departure']['estimated'])
        print('Earliest flight:', earliest_flight)

    # For use case 5) - Flights from Chongqing to Xi'an leaving after 8 PM this Friday
    next_friday = (datetime.now() + timedelta((4 - datetime.now().weekday() + 7) % 7)).strftime('%Y-%m-%d')
    flights = get_flight_schedules('CKG', 'XIY')
    if flights and 'data' in flights:
        flights = filter_flights(flights['data'],
                                 lambda flight: flight['departure']['estimated'] and flight['departure'][
                                     'estimated'].startswith(next_friday) and int(
                                     flight['departure']['estimated'][11:13]) >= 20)
        print('Flights leaving after 8 PM:', flights)

"""
    User Request: "What are the flights from New York to London on June 15, 2023?"
    API Call: get_flights('New York', 'London', datetime(2023, 6, 15))
    Result: List of flights from both StackAviation and Skyscanner APIs
    Full Answer: Here are the flights from New York to London on June 15, 2023: [flight1, flight2, ...]
    
    User Request: "Find the cheapest flight from Los Angeles to Paris on July 1, 2023."
    API Call: get_cheapest_flight('Los Angeles', 'Paris', datetime(2023, 7, 1))
    Result: Cheapest flight from both StackAviation and Skyscanner APIs
    Full Answer: The cheapest flight from Los Angeles to Paris on July 1, 2023 is flightX.
    
    User Request: "Are there any non-stop flights from Chicago to Miami on August 10, 2023?"
    API Call: get_non_stop_flights('Chicago', 'Miami', datetime(2023, 8, 10))
    Result: List of non-stop flights from both StackAviation and Skyscanner APIs
    Full Answer: Yes, there are non-stop flights from Chicago to Miami on August 10, 2023. Here are the flight options: [flight1, flight2, ...]
    
    User Request: "What is the earliest flight from San Francisco to Denver on September 20, 2023?"
    API Call: get_earliest_flight('San Francisco', 'Denver', datetime(2023, 9, 20))
    Result: Earliest flight from both StackAviation and Skyscanner APIs
    Full Answer: The earliest flight from San Francisco to Denver on September 20, 2023 is flightY.
    
    User Request: "Show me flights from London to Barcelona on October 5, 2023 after 2:00 PM."
    API Call: get_flights_after_time('London', 'Barcelona', datetime(2023, 10, 5), time(14, 0))
    Result: List of flights from both StackAviation and Skyscanner APIs departing after 2:00 PM
    Full Answer: Here are the flights from London to Barcelona on October 5, 2023 departing after 2:00 PM: [flight1, flight2, ...]
    
    User Request: "Find flights from New York to Los Angeles on November 10, 2023 arriving before 6:00 PM."
    API Call: get_flights_arriving_before('New York', 'Los Angeles', datetime(2023, 11, 10), time(18, 0))
    Result: List of flights from both StackAviation and Skyscanner APIs arriving before 6:00 PM
    Full Answer: Here are the flights from New York to Los Angeles on November 10, 2023 arriving before 6:00 PM: [flight1, flight2, ...]
    
    User Request: "Are there any direct flights from Seattle to San Francisco on December 15, 2023?"
    API Call: get_direct_flights('Seattle', 'San Francisco', datetime(2023, 12, 15))
    Result: List of direct flights from both StackAviation and Skyscanner APIs
    Full Answer: Yes, there are direct flights from Seattle to San Francisco on December 15, 2023. Here are the flight options: [flight1, flight2, ...]
    
    User Request: "What is the latest flight from Boston to Chicago on January 1, 2024?"
    API Call: get_latest_flight('Boston', 'Chicago', datetime(2024, 1, 1))
    Result: Latest flight from both StackAviation and Skyscanner APIs
    Full Answer: The latest flight from Boston to Chicago on January 1, 2024 is flightZ.
    
    User Request: "Find business class flights from San Diego to Las Vegas on February 5, 2024."
    API Call: get_business_class_flight('San Diego', 'Las Vegas', datetime(2024, 2, 5))
    Result: List of business class flights from both StackAviation and Skyscanner APIs
    Full Answer: Here are the business class flights from San Diego to Las Vegas on February 5, 2024: [flight1, flight2, ...]
    
    User Request: "Are there any red-eye flights from Houston to Orlando on March 10, 2024?"
    API Call: get_red_eye_flights('Houston', 'Orlando', datetime(2024, 3, 10))
    Result: List of red-eye flights from both StackAviation and Skyscanner APIs
    Full Answer: Yes, there are red-eye flights from Houston to Orlando on March 10, 2024. Here are the flight options: [flight1, flight2, ...]
    
    User Request: "Find flights from Atlanta to New York on April 15, 2024 with layovers less than 2 hours."
    API Call: get_flights_with_layover_less_than('Atlanta', 'New York', datetime(2024, 4, 15), 120)
    Result: List of flights from both StackAviation and Skyscanner APIs with layovers less than 2 hours
    Full Answer: Here are the flights from Atlanta to New York on April 15, 2024 with layovers less than 2 hours: [flight1, flight2, ...]
    
    User Request: "What is the duration of a direct flight from Miami to Houston on May 20, 2024?"
    API Call: get_duration_of_direct_flight('Miami', 'Houston', datetime(2024, 5, 20))
    Result: Duration of the direct flight from both StackAviation and Skyscanner APIs (if available)
    Full Answer: The duration of a direct flight from Miami to Houston on May 20, 2024 is 3 hours and 30 minutes.
    
    User Request: "Which airlines operate flights from Dallas to Phoenix on June 25, 2024?"
    API Call: get_operating_airlines('Dallas', 'Phoenix', datetime(2024, 6, 25))
    Result: List of airlines operating flights from both StackAviation and Skyscanner APIs
    Full Answer: The flights from Dallas to Phoenix on June 25, 2024 are operated by the following airlines: [airline1, airline2, ...]
    
    User Request: "How many stopovers are there on flights from Denver to Seattle on July 30, 2024?"
    API Call: get_flight_stopovers('Denver', 'Seattle', datetime(2024, 7, 30))
    Result: List of the number of stopovers for flights from both StackAviation and Skyscanner APIs
    Full Answer: The flights from Denver to Seattle on July 30, 2024 have the following number of stopovers: [0, 1, 2, ...]
    
    User Request: "Find flights from London to Paris on August 5, 2024 departing between 9:00 AM and 12:00 PM."
    API Call: get_flights_departing_in_time_range('London', 'Paris', datetime(2024, 8, 5), time(9, 0), time(12, 0))
    Result: List of flights from both StackAviation and Skyscanner APIs departing in the specified time range
    Full Answer: Here are the flights from London to Paris on August 5, 2024 departing between 9:00 AM and 12:00 PM: [flight1, flight2, ...]
    
    User Request: "What are the flights from New York to London on September 15, 2024?"
    API Call: get_flights('New York', 'London', datetime(2024, 9, 15))
    Result: List of flights from both StackAviation and Skyscanner APIs
    Full Answer: Here are the flights from New York to London on September 15, 2024: [flight1, flight2, ...]
    
    User Request: "Find the cheapest flight from Los Angeles to Paris on October 1, 2024."
    API Call: get_cheapest_flight('Los Angeles', 'Paris', datetime(2024, 10, 1))
    Result: Cheapest flight from both StackAviation and Skyscanner APIs
    Full Answer: The cheapest flight from Los Angeles to Paris on October 1, 2024 is flightX.
    
    User Request: "Are there any non-stop flights from Chicago to Miami on November 10, 2024?"
    API Call: get_non_stop_flights('Chicago', 'Miami', datetime(2024, 11, 10))
    Result: List of non-stop flights from both StackAviation and Skyscanner APIs
    Full Answer: Yes, there are non-stop flights from Chicago to Miami on November 10, 2024. Here are the flight options: [flight1, flight2, ...]
    
    User Request: "What is the earliest flight from San Francisco to Denver on December 20, 2024?"
    API Call: get_earliest_flight('San Francisco', 'Denver', datetime(2024, 12, 20))
    Result: Earliest flight from both StackAviation and Skyscanner APIs
    Full Answer: The earliest flight from San Francisco to Denver on December 20, 2024 is flightY.
    
    User Request: "Show me flights from London to Barcelona on January 5, 2025 after 2:00 PM."
    API Call: get_flights_after_time('London', 'Barcelona', datetime(2025, 1, 5), time(14, 0))
    Result: List of flights from both StackAviation and Skyscanner APIs departing after 2:00 PM
    Full Answer: Here are the flights from London to Barcelona on January 5, 2025 departing after 2:00 PM: [flight1, flight2, ...]
"""