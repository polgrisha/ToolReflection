import geocoder


class GeocoderAPI:

    @staticmethod
    def geocode(location):
        """
        Geocodes a given location.

        Args:
            location (str): The location to be geocoded.

        Returns:
            dict: A dictionary containing geocoding information, including latitude, longitude, address, etc.
        """
        result = geocoder.osm(location)
        if result.ok:
            geocoding_info = {
                'latitude': result.lat,
                'longitude': result.lng,
                'address': result.address,
                # Add additional geocoding information as needed
            }
            return geocoding_info
        else:
            return None

    @staticmethod
    def reverse_geocode(latitude, longitude):
        """
        Reverse geocodes a given latitude and longitude.

        Args:
            latitude (float): The latitude coordinate.
            longitude (float): The longitude coordinate.

        Returns:
            dict: A dictionary containing reverse geocoding information, including address, city, state, etc.
        """
        result = geocoder.reverse((latitude, longitude), exactly_one=True, provider="osm")
        if result.ok:
            reverse_geocoding_info = {
                'address': result.address,
                'city': result.city,
                'state': result.state,
                # Add additional reverse geocoding information as needed
            }
            return reverse_geocoding_info
        else:
            return None


if __name__ == '__main__':
    print("What is the geolocation of Beijing, China?")
    print(GeocoderAPI.geocode("Beijing, China"))

    print("Can you provide the address, city, and state for the location at coordinates  22.542883, 114.062996")
    print(GeocoderAPI.reverse_geocode(22.542883, 114.062996))

    print("Can you provide the address, city, and state for the location at coordinates  31.224361, 121.469170")
    print(GeocoderAPI.reverse_geocode(31.224361, 121.469170))

"""
    Question: "What is the geolocation of Beijing, China?"
    API Call: GeocoderAPI.geocode("Beijing, China")
    Result: {'latitude': 39.9057136, 'longitude': 116.3912972, 'address': '北京市, 东城区, 首都功能核心区, 北京市, 100010, 中国'}
    Answer: The geolocation of Beijing, China is approximately latitude 39.9042 and longitude 116.4074.

    Question: "Can you provide the address, city, and state for the location at coordinates  22.542883, 114.062996"
    API Call: GeocoderAPI.reverse_geocode(37.7749, -122.4194)
    Result: {'address': '岗厦北站, 彩田路, 岗厦社区, 福田街道, 福田区, 深圳市, 广东省, 518000, 中国', 'city': '福田区', 'state': '广东省'}
    Answer: The location at coordinates 37.7749, -122.4194 corresponds to the address Shenzhen, Guangdong, China. The city is Shenzhen and the state is Guangdong.
    
    Question: "Can you provide the address for the location at coordinates 31.224361, 121.469170"
    API Call: GeocoderAPI.reverse_geocode(41.8819, -87.6278)
    Result: {'address': '瑞安广场, 马当路, 太平桥, 淮海中路街道, 上海市, 黄浦区, 上海市, 200021, 中国', 'city': '上海市', 'state': '上海市'}
    Answer: The location at coordinates 41.8819, -87.6278 corresponds to the address Shanghai, China.

    Question: "What is the geolocation of Paris, France?"
    API Call: GeocoderAPI.geocode("Paris, France")
    Result: The latitude is 48.8566, the longitude is 2.3522.
    Answer: The geolocation of Paris, France is approximately latitude 48.8566 and longitude 2.3522.

    Question: "Can you provide the address, city, and state for the location at coordinates 37.7749, -122.4194?"
    API Call: GeocoderAPI.reverse_geocode(37.7749, -122.4194)
    Result: The address is San Francisco, California, US. The city is San Francisco and the state is California.
    Answer: The location at coordinates 37.7749, -122.4194 corresponds to the address San Francisco, California, US.

    Question: "What are the coordinates and address for 5th Avenue in New York?"
    API Call: GeocoderAPI.geocode("5th Avenue, New York")
    Result: The latitude is 40.779668, the longitude is -73.963613, and the address is 5th Avenue, New York, NY, USA.
    Answer: The coordinates for 5th Avenue in New York are approximately latitude 40.779668 and longitude -73.963613. The address is 5th Avenue, New York, NY, USA.

    Question: "What is the address for the location at coordinates 48.8566, 2.3522?"
    API Call: GeocoderAPI.reverse_geocode(48.8566, 2.3522)
    Result: The address is Paris, France.
    Answer: The location at coordinates 48.8566, 2.3522 corresponds to the address Paris, France.

    Question: "What are the coordinates for the Statue of Liberty in New York?"
    API Call: GeocoderAPI.geocode("Statue of Liberty, New York")
    Result: The latitude is 40.6892534, the longitude is -74.044548, and the address is Statue of Liberty, New York, NY 10004, USA.
    Answer: The coordinates for the Statue of Liberty in New York are approximately latitude 40.6892534 and longitude -74.044548. The address is Statue of Liberty, New York, NY 10004, USA.

    Question: "Can you provide the address, city, and state for the location at coordinates 37.4219999, -122.0840575?"
    API Call: GeocoderAPI.reverse_geocode(37.4219999, -122.0840575)
    Result: The address is 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA. The city is Mountain View and the state is California.
    Answer: The location at coordinates 37.4219999, -122.0840575 corresponds to the address 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA. The city is Mountain View and the state is California.

    Question: "What are the coordinates for Sydney, Australia?"
    API Call: GeocoderAPI.geocode("Sydney, Australia")
    Result: The latitude is -33.8548157, the longitude is 151.2164539, and the address is Sydney NSW, Australia.
    Answer: The coordinates for Sydney, Australia are approximately latitude -33.8548157 and longitude 151.2164539. The address is Sydney NSW, Australia.

    Question: "What is the address for the location at coordinates 37.8651, -119.5383?"
    API Call: GeocoderAPI.reverse_geocode(37.8651, -119.5383)
    Result: The address is Yosemite Valley, CA 95389, USA.
    Answer: The location at coordinates 37.8651, -119.5383 corresponds to the address Yosemite Valley, CA 95389, USA.

    Question: "What are the latlon coords for Sedona, Arizona?"
    API Call: GeocoderAPI.geocode("Sedona, Arizona")
    Result: The latitude is 34.8697, the longitude is -111.7609, and the address is Sedona, AZ, USA.
    Answer: The coordinates for Sedona, Arizona are approximately latitude 34.8697 and longitude -111.7609. The address is Sedona, AZ, USA.

    Question: "Can you provide the address, city, and state for the location at coordinates 33.6405, -79.0058?"
    API Call: GeocoderAPI.reverse_geocode(33.6405, -79.0058)
    Result: The address is Myrtle Beach, South Carolina, US. The city is Myrtle Beach and the state is South Carolina.
    Answer: The location at coordinates 33.6405, -79.0058 corresponds to the address Myrtle Beach, South Carolina, US. The city is Myrtle Beach and the state is South Carolina.

    Question: "What are the location for 1600 Pennsylvania Avenue NW in Washington, D.C.?"
    API Call: GeocoderAPI.geocode("1600 Pennsylvania Avenue NW, Washington, D.C.")
    Result: The latitude is 38.8976757, the longitude is -77.0364821, and the address is 1600 Pennsylvania Ave NW, Washington, DC 20500, USA.
    Answer: The coordinates for the location 1600 Pennsylvania Avenue NW in Washington, D.C. are approximately latitude 38.8976757 and longitude -77.0364821. The address is 1600 Pennsylvania Ave NW, Washington, DC 20500, USA.

    Question: "What is the address for the location at coordinates -34.6037, -58.3816?"
    API Call: GeocoderAPI.reverse_geocode(-34.6037, -58.3816)
    Result: The address is Buenos Aires, Argentina.
    Answer: The location at coordinates -34.6037, -58.3816 corresponds to the address Buenos Aires, Argentina.

    Question: "What are the latitude, longitude, and address for Stanford University?"
    API Call: GeocoderAPI.geocode("Stanford University, California")
    Result: The latitude is 37.4274745, the longitude is -122.169719, and the address is Stanford, CA 94305, USA.
    Answer: The coordinates for Stanford University in California are approximately latitude 37.4274745 and longitude -122.169719. The address is Stanford, CA 94305, USA.

    Question: "Can you provide the address for the location at coordinates 52.5200, 13.4050?"
    API Call: GeocoderAPI.reverse_geocode(52.5200, 13.4050)
    Result: The address is Berlin, Germany.
    Answer: The location at coordinates 52.5200, 13.4050 corresponds to the address Berlin, Germany.

    Question: "What are the coordinates for the location 'Rue de l'Église' in Paris?"
    API Call: GeocoderAPI.geocode("Rue de l'Église, Paris")
    Result: The latitude is 48.8534934, the longitude is 2.3333346, and the address is Rue de l'Église, 75015 Paris, France.
    Answer: The coordinates for the location 'Rue de l'Église' in Paris are approximately latitude 48.8534934 and longitude 2.3333346. The address is Rue de l'Église, 75015 Paris, France.

    Question: "What is the address for the location at coordinates 39.5501, -105.7821?"
    API Call: GeocoderAPI.reverse_geocode(39.5501, -105.7821)
    Result: The address is Rocky Mountains, Colorado, USA.
    Answer: The location at coordinates 39.5501, -105.7821 corresponds to the address Rocky Mountains, Colorado, USA.

    Question: "What are the latitude and longitude for Central Park in New York?"
    API Call: GeocoderAPI.geocode("Central Park, New York")
    Result: The latitude is 40.7829, the longitude is -73.9654, and the address is Central Park, New York, NY, USA.
    Answer: The coordinates for Central Park in New York are approximately latitude 40.7829 and longitude -73.9654. The address is Central Park, New York, NY, USA.

    Question: "Can you provide the address for the location at coordinates 41.8819, -87.6278?"
    API Call: GeocoderAPI.reverse_geocode(41.8819, -87.6278)
    Result: The address is Chicago, Illinois, US.
    Answer: The location at coordinates 41.8819, -87.6278 corresponds to the address Chicago, Illinois, US.

    Question: "What are the geoposition for Springfield?"
    API Call: GeocoderAPI.geocode("Springfield")
    Result: The latitude is 37.2153, the longitude is -93.2982, and the address is Springfield, MO, USA.
    Answer: The coordinates for Springfield are approximately latitude 37.2153 and longitude -93.2982. The address is Springfield, MO, USA.

    Question: "What is the address for the location at coordinates 52.379189, 4.899431?"
    API Call: GeocoderAPI.reverse_geocode(52.379189, 4.899431)
    Result: The address is Prinsengracht 263, 1016 GV Amsterdam, Netherlands.
    Answer: The location at coordinates 52.379189, 4.899431 corresponds to the address Prinsengracht 263, 1016 GV Amsterdam, Netherlands.
    """
