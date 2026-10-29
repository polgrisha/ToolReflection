import pint


class PintAPI:
    ureg = pint.UnitRegistry()

    @staticmethod
    def convert_units(from_value, from_unit, to_unit):
        """Convert from one unit to another."""
        from_quantity = from_value * PintAPI.ureg(from_unit)
        to_quantity = from_quantity.to(to_unit)
        return to_quantity.magnitude


if __name__ == '__main__':
    print("Hey, how many kilometers are there in 25 miles?")
    print("There are approximately", PintAPI.convert_units(25, 'miles', 'kilometers'), "kilometers in 25 miles.")

"""
    Question: "Hey, how many kilometers are there in 25 miles?"
    API Call: PintAPI.convert_units(25, 'miles', 'kilometers')
    Result:  40.2336
    Answer: There are approximately 40.2336 kilometers in 25 miles.

    Question: "I've got 50 pounds of luggage, how many kilograms is that?"
    API Call: PintAPI.convert_units(50, 'pounds', 'kilograms')
    Result:  22.6796
    Answer: 50 pounds is approximately equal to 22.6796 kilograms.

    Question: "Can you convert 10 acres into square meters for me?"
    API Call: PintAPI.convert_units(10, 'acres', 'square_meters')
    Result:  40468.5642
    Answer: 10 acres is approximately equal to 40468.5642 square meters.

    Question: "My recipe calls for 100 grams of sugar, but I only have cups. How many cups is that?"
    API Call: PintAPI.convert_units(100, 'grams', 'cups')
    Result:  0.4238
    Answer: 100 grams of sugar is approximately equal to 0.4238 cups.

    Question: "How many liters are in 3 gallons of milk?"
    API Call: PintAPI.convert_units(3, 'gallons', 'liters')
    Result:  11.3562
    Answer: 3 gallons of milk is approximately equal to 11.3562 liters.

    Question: "If I run a 10K, how many miles is that?"
    API Call: PintAPI.convert_units(10, 'kilometers', 'miles')
    Result:  6.2137
    Answer: A 10K run is approximately equal to 6.2137 miles.

    Question: "I'm looking at a property that's 500 square feet, can you tell me what that is in square meters?"
    API Call: PintAPI.convert_units(500, 'square_feet', 'square_meters')
    Result:  46.4515
    Answer: A property measuring 500 square feet is approximately equal to 46.4515 square meters.

    Question: "I need to bake a cake, but the recipe is in Celsius and my oven uses Fahrenheit. How hot should I set it for 180 degrees Celsius?"
    API Call: PintAPI.convert_units(180, 'degC', 'degF')
    Result:  356
    Answer: To set the oven to 180 degrees Celsius, you should set it to approximately 356 degrees Fahrenheit.

    Question: "How many ounces are in 1.5 pounds?"
    API Call: PintAPI.convert_units(1.5, 'pounds', 'ounces')
    Result:  24
    Answer: 1.5 pounds is approximately equal to 24 ounces.

    Question: "Can you help me convert 20 inches into centimeters?"
    API Call: PintAPI.convert_units(20, 'inches', 'centimeters')
    Result:  50.8
    Answer: 20 inches is approximately equal to 50.8 centimeters.

    Question: "My garden is 2000 square feet. How large is it in square meters?"
    API Call: PintAPI.convert_units(2000, 'square_feet', 'square_meters')
    Result:  185.806
    Answer: A garden measuring 2000 square feet is approximately equal to 185.806 square meters.

    Question: "I'm driving 55 miles per hour, what's that in kilometers per hour?"
    API Call: PintAPI.convert_units(55, 'miles/hour', 'kilometers/hour')
    Result:  88.5139
    Answer: Driving at 55 miles per hour is approximately equal to 88.5139 kilometers per hour.

    Question: "I need 2 liters of water for a recipe, but I only have quart containers. How many quarts should I use?"
    API Call: PintAPI.convert_units(2, 'liters', 'quarts')
    Result:  2.11338
    Answer: 2 liters of water is approximately equal to 2.11338 quarts.

    Question: "I'm 6 feet tall. How many meters is that?"
    API Call: PintAPI.convert_units(6, 'feet', 'meters')
    Result:  1.8288
    Answer: A height of 6 feet is approximately equal to 1.8288 meters.

    Question: "The room I'm painting is 12 by 15 feet, how many square meters is that?"
    API Call: PintAPI.convert_units(12*15, 'square_feet', 'square_meters')
    Result:  20.9032
    Answer: A room measuring 12 by 15 feet is approximately equal to 20.9032 square meters.

    Question: "I'm traveling to a country that uses kilometers. If the speed limit is 90 km/h, how fast is that in mph?"
    API Call: PintAPI.convert_units(90, 'kilometers/hour', 'miles/hour')
    Result:  55.9234
    Answer: A speed limit of 90 km/h is approximately equal to 55.9234 mph.

    Question: "My car's fuel efficiency is 35 miles per gallon. What is that in kilometers per liter?"
    API Call: PintAPI.convert_units(35, 'miles/gallon', 'kilometers/liter')
    Result:  14.7859
    Answer: A fuel efficiency of 35 miles per gallon is approximately equal to 14.7859 kilometers per liter.

    Question: "I'm trying to convert a recipe from the UK. It says I need 500 milliliters of milk. How many cups is that?"
    API Call: PintAPI.convert_units(500, 'milliliters', 'cups')
    Result:  2.11338
    Answer: 500 milliliters of milk is approximately equal to 2.11338 cups.

    Question: "I just ran a 5K. How many miles did I run?"
    API Call: PintAPI.convert_units(5, 'kilometers', 'miles')
    Result:  3.10686
    Answer: Completing a 5K run is approximately equal to running 3.10686 miles.

    Question: "I weigh 200 pounds. How much would that be in kilograms?"
    API Call: PintAPI.convert_units(200, 'pounds', 'kilograms')
    Result:  90.7185
    Answer: A weight of 200 pounds is approximately equal to 90.7185 kilograms.

    Question: Convert 5 miles to kilometers.
    API Call: PintAPI.convert_units(5, 'miles', 'kilometers')
    Result:  8.04672
    Answer: 5 miles is approximately equal to 8.04672 kilometers.

    Question: Convert 72 degrees Fahrenheit to Celsius.
    API Call: PintAPI.convert_units(72, 'degF', 'degC')
    Result:  22.2222
    Answer: 72 degrees Fahrenheit is approximately equal to 22.2222 degrees Celsius.

    Question: Convert 150 pounds to kilograms.
    API Call: PintAPI.convert_units(150, 'pounds', 'kilograms')
    Result:  68.0389
    Answer: 150 pounds is approximately equal to 68.0389 kilograms.

    Question: Convert 60 miles per hour to kilometers per hour.
    API Call: PintAPI.convert_units(60, 'miles/hour', 'kilometers/hour')
    Result:  96.5606
    Answer: 60 miles per hour is approximately equal to 96.5606 kilometers per hour.

    Question: Convert 10 gallons to liters.
    API Call: PintAPI.convert_units(10, 'gallons', 'liters')
    Result:  37.8541
    Answer: 10 gallons is approximately equal to 37.8541 liters.

    Question: Convert 1 atmosphere to Pascals.
    API Call: PintAPI.convert_units(1, 'atm', 'Pa')
    Result:  101325
    Answer: 1 atmosphere is approximately equal to 101325 Pascals.

    Question: Convert 500 Joules to calories.
    API Call: PintAPI.convert_units(500, 'J', 'cal')
    Result:  119.591
    Answer: 500 Joules is approximately equal to 119.591 calories.

    Question: Convert 1 Hertz to RPM (revolutions per minute).
    API Call: PintAPI.convert_units(1, 'Hz', 'rpm')
    Result: 60
    Answer: 1 Hertz is equal to 60 RPM (revolutions per minute).

    Question: Convert 1 day to seconds.
    API Call: PintAPI.convert_units(1, 'day', 'second')
    Result: 86400
    Answer: 1 day is equal to 86400 seconds.

    Question: Convert 1 gigabyte to bytes.
    API Call: PintAPI.convert_units(1, 'GB', 'byte')
    Result: 1073741824
    Answer: 1 gigabyte is equal to 1073741824 bytes.

    Question: Convert 1 acre to square meters.
    API Call: PintAPI.convert_units(1, 'acre', 'm^2')
    Result:  4046.86
    Answer: 1 acre is approximately equal to 4046.86 square meters.

    Question: Convert 300 Kelvin to Fahrenheit.
    API Call: PintAPI.convert_units(300, 'kelvin', 'degF')
    Result:  80.33
    Answer: 300 Kelvin is approximately equal to 80.33 degrees Fahrenheit.

    Question: Convert 1 Newton to pound-force.
    API Call: PintAPI.convert_units(1, 'N', 'lbf')
    Result:  0.2248
    Answer: 1 Newton is approximately equal to 0.2248 pound-force.

    Question: Convert 745.7 Watts to horsepower.
    API Call: PintAPI.convert_units(745.7, 'W', 'hp')
    Result: 1
    Answer: 745.7 Watts is equal to 1 horsepower.

    Question: Convert 1 foot per second to meters per second.
    API Call: PintAPI.convert_units(1, 'feet/second', 'meters/second')
    Result:  0.3048
    Answer: 1 foot per second is approximately equal to 0.3048 meters per second.

    Question: Convert 1 British thermal unit to Joules.
    API Call: PintAPI.convert_units(1, 'BTU', 'J')
    Result:  1055.06
    Answer: 1 British thermal unit is approximately equal to 1055.06 Joules.

    Question: Convert 1 bar to PSI (Pound-force per square inch).
    API Call: PintAPI.convert_units(1, 'bar', 'psi')
    Result:  14.5038
    Answer: 1 bar is approximately equal to 14.5038 PSI.

    Question: Convert 1 cubic inch to cubic centimeters.
    API Call: PintAPI.convert_units(1, 'inch^3', 'cm^3')
    Result:  16.387
    Answer: 1 cubic inch is approximately equal to 16.387 cubic centimeters.

    Question: Convert 1 Megabit per second to Kilobytes per second.
    API Call: PintAPI.convert_units(1, 'Mbps', 'KB/s')
    Result: 125
    Answer: 1 Megabit per second is equal to 125 Kilobytes per second.

    Question: Convert 1 ounce to grams.
    API Call: PintAPI.convert_units(1, 'oz', 'g')
    Result:  28.3495
    Answer: 1 ounce is approximately equal to 28.3495 grams.

    Question: Convert 1 week to hours.
    API Call: PintAPI.convert_units(1, 'week', 'hour')
    Result: 168
    Answer: 1 week is equal to 168 hours.

    Question: Convert 1 BTU per hour to Watts.
    API Call: PintAPI.convert_units(1, 'BTU/hour', 'W')
    Result:  0.293071
    Answer: 1 BTU per hour is approximately equal to 0.293071 Watts.

    Question: Convert 1 gram per cubic centimeter to pounds per cubic foot.
    API Call: PintAPI.convert_units(1, 'g/cm^3', 'lb/ft^3')
    Result:  62.427961
    Answer: 1 gram per cubic centimeter is approximately equal to 62.427961 pounds per cubic foot.

    Question: Convert 1 nautical mile to kilometers.
    API Call: PintAPI.convert_units(1, 'nautical_mile', 'km')
    Result:  1.852
    Answer: 1 nautical mile is approximately equal to 1.852 kilometers.

    Question: Convert 1 meter per second squared to feet per second squared.
    API Call: PintAPI.convert_units(1, 'm/s^2', 'ft/s^2')
    Result:  3.28084
    Answer: 1 meter per second squared is approximately equal to 3.28084 feet per second squared.

    Question: Convert 5 miles to kilometers.
    API Call: PintAPI.convert_units(5, 'miles', 'kilometers')
    Result:  8.04672
    Answer: 5 miles is approximately equal to 8.04672 kilometers.

    Question: Convert 72 degrees Fahrenheit to Celsius.
    API Call: PintAPI.convert_units(72, 'degF', 'degC')
    Result:  22.2222
    Answer: 72 degrees Fahrenheit is approximately equal to 22.2222 degrees Celsius.

    Question: Convert 150 pounds to kilograms.
    API Call: PintAPI.convert_units(150, 'pounds', 'kilograms')
    Result:  68.0389
    Answer: 150 pounds is approximately equal to 68.0389 kilograms.

    Question: Convert 60 miles per hour to kilometers per hour.
    API Call: PintAPI.convert_units(60, 'miles/hour', 'kilometers/hour')
    Result:  96.5606
    Answer: 60 miles per hour is approximately equal to 96.5606 kilometers per hour.

    Question: Convert 10 gallons to liters.
    API Call: PintAPI.convert_units(10, 'gallons', 'liters')
    Result:  37.8541
    Answer: 10 gallons is approximately equal to 37.8541 liters.
"""
