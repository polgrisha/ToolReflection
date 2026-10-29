import datetime
import pytz
from dateutil import parser
from whenareyou import whenareyou


class TimeConverterAPI:

    @staticmethod
    def now():
        return datetime.datetime.now().strftime("%H:%M")

    @staticmethod
    def convert_to_timezone(time_str, source_tz, target_tz):
        """
        Converts the given time from source timezone to target timezone.

        Args:
            time_str (str): The time string to convert (e.g., "12:30", "12:30:45").
            source_tz (str): The source timezone or city (e.g., "Russia/Moscow", "Moscow").
            target_tz (str): The target timezone (e.g., "Asia/Shanghai", "Shanghai").

        Returns:
            str: The converted time string in the target timezone.
        """
        source_time = parser.parse(time_str)
        source_tz = pytz.timezone(whenareyou(source_tz))
        target_tz = pytz.timezone(whenareyou(target_tz))

        source_time = source_tz.localize(source_time)
        target_time = source_time.astimezone(tz=target_tz)
        return target_time.strftime("%H:%M")

    @staticmethod
    def convert_to_12h_format(time_str):
        """
        Converts the given time string to 12-hour format.

        Args:
            time_str (str): The time string to convert (e.g., "15:30", "15:30:45").

        Returns:
            str: The time string in 12-hour format.
        """

        source_time = parser.parse(time_str)
        return source_time.strftime("%I:%M %p")

    @staticmethod
    def convert_to_24h_format(time_str):
        """
        Converts the given time string to 24-hour format.

        Args:
            time_str (str): The time string to convert (e.g., "3:30 PM", "03:30:45 PM").

        Returns:
            str: The time string in 24-hour format.
        """
        
        source_time = parser.parse(time_str)
        return source_time.strftime("%H:%M")


if __name__ == '__main__':
    print("What is the current time in Tokyo if I'm in Sydney?")
    print(TimeConverterAPI.convert_to_timezone(TimeConverterAPI.now(), "Australia/Sydney", "Asia/Tokyo"))

    print("How do I convert 15:30 in 24-hour format to 12-hour format?")
    print(TimeConverterAPI.convert_to_12h_format("15:30"))

    print("How do I convert 5:30 PM in 24-hour format?")
    print(TimeConverterAPI.convert_to_24h_format("5:30 PM"))

    print("If it's 13:20 in London, what time in 12-hour format is it in Beijing?")
    print(TimeConverterAPI.convert_to_12h_format(
        TimeConverterAPI.convert_to_timezone("13:20", "Europe/London", "Asia/Shanghai")))

"""
    Question: What is the current time in Tokyo if I'm in Sydney?
    API Call: TimeConverterAPI.convert_to_timezone(TimeConverterAPI.now(), "Australia/Sydney", "Asia/Tokyo")
    Result: "10:00 PM"
    Answer: The current time in Tokyo is 10:00 PM.

    Question: How do I convert 15:30 in 24-hour format to 12-hour format?
    API Call: TimeConverterAPI.convert_to_12h_format("05:30")
    Result: "03:30 AM"
    Answer: To convert 15:30 in 24-hour format to 12-hour format, it remains as 3:30 AM.

    Question: What time will it be in London if it's 12:00 PM in Sydney?
    API Call: TimeConverterAPI.convert_to_timezone("12:00 PM", "Australia/Sydney", "Europe/London")
    Result: "03:00 AM"
    Answer: If it's 12:00 PM in Sydney, it will be 3:00 AM in London.

    Question: I have a meeting at 3:30 PM CST. Can you convert it to Eastern Standard Time (EST)?
    API Call: TimeConverterAPI.convert_to_timezone("3:30 PM", "America/Chicago", "America/New_York")
    Result: "4:30 PM"
    Answer: If the meeting is at 3:30 PM CST, it will be at 4:30 PM EST.

    Question: What time is it in Moscow if it's 10:30 AM in New York?
    API Call: TimeConverterAPI.convert_to_timezone("10:30 AM", "America/New_York", "Europe/Moscow")
    Result: "05:30 PM"
    Answer: If it's 10:30 AM in New York, it will be 5:30 PM in Moscow.

    Question: Can you convert 15:45 in 24-hour format to 12-hour format?
    API Call: TimeConverterAPI.convert_to_12h_format("15:45")
    Result: "03:45 PM"
    Answer: To convert 15:45 in 24-hour format to 12-hour format, it would be 3:45 PM.

    Question: If it's 6:00 AM in Sydney, what time is it in Los Angeles?
    API Call: TimeConverterAPI.convert_to_timezone("6:00 AM", "Australia/Sydney", "America/Los_Angeles")
    Result: "01:00 PM"
    Answer: If it's 6:00 AM in Sydney, it will be 1:00 PM the previous day in Los Angeles due to the time zone difference.

    Question: I want to convert 9:30 AM in 12-hour format to 24-hour format. How can I do that?
    API Call: TimeConverterAPI.convert_to_24h_format("9:30 AM")
    Result: "09:30"
    Answer: To convert 9:30 AM in 12-hour format to 24-hour format, it remains as 09:30.

    Question: What time will it be in Tokyo if it's 8:00 PM in London?
    API Call: TimeConverterAPI.convert_to_timezone("8:00 PM", "Europe/London", "Asia/Tokyo")
    Result: "04:00 AM"
    Answer: If it's 8:00 PM in London, it will be 4:00 AM the next day in Tokyo.

    Question: How do I convert 14:00 in 24-hour format to 12-hour format?
    API Call: TimeConverterAPI.convert_to_12h_format("14:00")
    Result: "02:00 PM"
    Answer: To convert 14:00 in 24-hour format to 12-hour format, it would be 2:00 PM.

    Question: If it's 10:30 AM in New Delhi, what time is it in Dubai?
    API Call: TimeConverterAPI.convert_to_timezone("10:30 AM", "Asia/Kolkata", "Asia/Dubai")
    Result: "09:00 AM"
    Answer: If it's 10:30 AM in New Delhi, it will be 9:00 AM in Dubai.

    Question: I have a flight at 20:15. Can you convert it to 12-hour format?
    API Call: TimeConverterAPI.convert_to_12h_format("20:15")
    Result: "08:15 PM"
    Answer: 20:15 in 12-hour format is 08:15 PM.

    Question: If it's 3:00 PM on Friday in Tokyo, what time is it in Sydney?
    API Call: TimeConverterAPI.convert_to_timezone("3:00 PM", "Asia/Tokyo", "Australia/Sydney")
    Result: "2:00 PM"
    Answer: If it's 3:00 PM on Friday in Tokyo, it will be 2:00 PM on Friday in Sydney.

    Question: Can you convert 11:30 PM in 12-hour format to 24-hour format?
    API Call: TimeConverterAPI.convert_to_24h_format("11:30 PM")
    Result: "23:30"
    Answer: 11:30 PM in 24-hour format is 23:30.

    Question: What time will it be in Rome if it's 9:30 AM in New York?
    API Call: TimeConverterAPI.convert_to_timezone("9:30 AM", "America/New_York", "Europe/Rome")
    Result: "03:30 PM"
    Answer: If it's 9:30 AM in New York, it will be 3:30 PM in Rome.

    Question: I need to convert 17:45 to 12-hour format. How can I do that?
    API Call: TimeConverterAPI.convert_to_12h_format("17:45")
    Result: "05:45 PM"
    Answer: To convert 17:45 to 12-hour format, it would be 5:45 PM.

    Question: What time is it in Honolulu if it's 12:00 PM in Tokyo?
    API Call: TimeConverterAPI.convert_to_timezone("12:00 PM", "Asia/Tokyo", "Pacific/Honolulu")
    Result: "07:00 PM"
    Answer: If it's 12:00 PM in Tokyo, it will be 7:00 PM the previous day in Honolulu due to the time zone difference.

    Question: Can you convert 08:30 to 12-hour format?
    API Call: TimeConverterAPI.convert_to_12h_format("08:30")
    Result: "08:30 AM"
    Answer: 08:30 in 12-hour format remains as 08:30 AM.

    Question: If it's 6:45 PM in Sydney, what time is it in Mumbai?
    API Call: TimeConverterAPI.convert_to_timezone("6:45 PM", "Australia/Sydney", "Asia/Kolkata")
    Result: "02:15 PM"
    Answer: If it's 6:45 PM in Sydney, it will be 2:15 PM in Mumbai.

    Question: I have a meeting at 14:30. Can you convert it to 12-hour format?
    API Call: TimeConverterAPI.convert_to_12h_format("14:30")
    Result: "02:30 PM"
    Answer: 14:30 in 12-hour format is 02:30 PM.

    Question: What time will it be in Vancouver if it's 10:00 AM in Toronto?
    API Call: TimeConverterAPI.convert_to_timezone("10:00 AM", "America/Toronto", "America/Vancouver")
    Result: "07:00 AM"
    Answer: If it's 10:00 AM in Toronto, it will be 7:00 AM in Vancouver.

    Question: How do I convert 21:45 in 24-hour format to 12-hour format?
    API Call: TimeConverterAPI.convert_to_12h_format("21:45")
    Result: "09:45 PM"
    Answer: To convert 21:45 in 24-hour format to 12-hour format, it would be 9:45 PM.

    Question: What is the time difference between Berlin and Madrid?
    Answer: Berlin and Madrid are in the same time zone, so there is no time difference between them.

    Question: If it's 9:30 AM in Mumbai, what time is it in Dubai?
    API Call: TimeConverterAPI.convert_to_timezone("9:30 AM", "Asia/Kolkata", "Asia/Dubai")
    Result: "8:00 AM"
    Answer: If it's 9:30 AM in Mumbai, it will be 8:00 AM in Dubai.

    Question: Can you convert 18:30 to 12-hour format?
    API Call: TimeConverterAPI.convert_to_12h_format("18:30")
    Result: "06:30 PM"
    Answer: 18:30 in 12-hour format is 06:30 PM.
	
    Question: What time is it in New York right now? I'm currently in London.
    API Call: TimeConverterAPI.convert_to_timezone("now", "Europe/London", "America/New_York")
    Result: "14:30"
    Answer: The current time in New York is 2:30 PM.

    Question: How do I convert 2:30 PM in 12-hour format to 24-hour format?
    API Call: TimeConverterAPI.convert_to_24h_format("2:30 PM")
    Result: "14:30"
    Answer: To convert 2:30 PM to 24-hour format, it would be 14:30.

    Question: Can you tell me the time difference between Tokyo and Sydney?
    Answer: The time difference between Tokyo and Sydney is not constant due to daylight saving time changes. It can vary from 0 to 3 hours.

    Question: I want to convert 10:45 PM in 12-hour format to 24-hour format. Can you help?
    API Call: TimeConverterAPI.convert_to_24h_format("10:45 PM")
    Result: "22:45"
    Answer: 10:45 PM in 24-hour format is 22:45.

    Question: What time will it be in Paris if it's 8:00 AM in Los Angeles?
    API Call: TimeConverterAPI.convert_to_timezone("8:00 AM", "America/Los_Angeles", "Europe/Paris")
    Result: "17:00"
    Answer: If it's 8:00 AM in Los Angeles, it will be 5:00 PM in Paris.

    Question: I need to convert 4:15 PM to 24-hour format. How can I do that?
    API Call: TimeConverterAPI.convert_to_24h_format("4:15 PM")
    Result: "16:15"
    Answer: To convert 4:15 PM to 24-hour format, it would be 16:15.

    Question: If it's 2:00 PM in London, what time is it in Beijing?
    API Call: TimeConverterAPI.convert_to_timezone("2:00 PM", "Europe/London", "Asia/Shanghai")
    Result: "21:00"
    Answer: If it's 2:00 PM in London, it will be 9:00 PM in Beijing.

    Question: Can you convert 5:30 AM in 12-hour format to 24-hour format?
    API Call: TimeConverterAPI.convert_to_24h_format("5:30 AM")
    Result: "05:30"
    Answer: 5:30 AM in 24-hour format is 05:30.

    Question: How many hours ahead is Moscow from New York?
    Answer: Moscow is usually 8 hours ahead of New York. However, please note that this time difference may change during daylight saving time transitions.

    Question: What is the current time in Chicago if it's 11:45 PM in Sydney?
    API Call: TimeConverterAPI.convert_to_timezone("now", "Australia/Sydney", "America/Chicago")
    Result: "08:45"
    Answer: The current time in Chicago is 8:45 AM.

    Question: I have a meeting at 9:30 AM PST. Can you convert it to Central Standard Time (CST)?
    API Call: TimeConverterAPI.convert_to_timezone("9:30 AM", "America/Los_Angeles", "America/Chicago")
    Result: "11:30 AM"
    Answer: If your meeting is at 9:30 AM PST, it will be at 11:30 AM CST.

    Question: If it's 7:30 PM on Thursday in Los Angeles, what time is it in London?
    API Call: TimeConverterAPI.convert_to_timezone("7:30 PM", "America/Los_Angeles", "Europe/London")
    Result: "03:30 AM"
    Answer: If it's 7:30 PM on Thursday in Los Angeles, it will be 3:30 AM on Friday in London.

    Question: How do I convert 16:45 in 24-hour format to 12-hour format?
    API Call: TimeConverterAPI.convert_to_12h_format("16:45")
    Result: "04:45 PM"
    Answer: To convert 16:45 in 24-hour format to 12-hour format, it would be 4:45 PM.

    Question: What is the time difference between Dubai and Mumbai?
    Answer: Dubai and Mumbai have a time difference of 1 hour, with Dubai being 1 hour ahead of Mumbai.

    Question: If it's 10:00 AM on Monday in Tokyo, what time is it in Berlin?
    API Call: TimeConverterAPI.convert_to_timezone("10:00 AM", "Asia/Tokyo", "Europe/Berlin")
    Result: "03:00 AM"
    Answer: If it's 10:00 AM on Monday in Tokyo, it will be 3:00 AM on Monday in Berlin.

    Question: Can you convert 8:20 PM in 12-hour format to 24-hour format?
    API Call: TimeConverterAPI.convert_to_24h_format("8:20 PM")
    Result: "20:20"
    Answer: 8:20 PM in 24-hour format is 20:20.

    Question: What time will it be in Buenos Aires if it's 3:30 PM in New York?
    API Call: TimeConverterAPI.convert_to_timezone("3:30 PM", "America/New_York", "America/Argentina/Buenos_Aires")
    Result: "4:30 PM"
    Answer: If it's 3:30 PM in New York, it will be 4:30 PM in Buenos Aires.

    Question: I have a flight at 6:45 AM. Can you convert it to 24-hour format?
    API Call: TimeConverterAPI.convert_to_24h_format("6:45 AM")
    Result: "06:45"
    Answer: 6:45 AM in 24-hour format is 06:45.

    Question: How many hours behind is Los Angeles from Sydney?
    Answer: Los Angeles is usually 17 hours behind Sydney. However, please note that this time difference may change during daylight saving time transitions.

    Question: If it's 1:15 AM on Tuesday in London, what time is it in New York?
    API Call: TimeConverterAPI.convert_to_timezone("1:15 AM", "Europe/London", "America/New_York")
    Result: "08:15 PM"
    Answer: If it's 1:15 AM on Tuesday in London, it will be 8:15 PM on Monday in New York.
    
    Question: Convert "12:30" from UTC to "America/New_York" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("12:30", "UTC", "America/New_York")
    Result: "08:30 AM"
    Answer: "12:30" in UTC is equivalent to "08:30 AM" in the America/New_York timezone.

    Question: Convert "15:45:30" from "Europe/London" to "Asia/Tokyo" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("15:45:30", "Europe/London", "Asia/Tokyo")
    Result: "00:45:30"
    Answer: "15:45:30" in the Europe/London timezone is equivalent to "00:45:30" the next day in the Asia/Tokyo timezone.

    Question: Convert "9:00 AM" to 24-hour format.
    API Call: TimeConverterAPI.convert_to_24h_format("9:00 AM")
    Result: "09:00"
    Answer: "9:00 AM" in 24-hour format remains as "09:00".

    Question: Convert "17:30:15" to 12-hour format in "Australia/Sydney" timezone.
    API Call: TimeConverterAPI.convert_to_12h_format(TimeConverterAPI.convert_to_timezone("17:30:15", "UTC", "Australia/Sydney"))
    Result: "05:30:15 PM"
    Answer: "17:30:15" in the UTC timezone is equivalent to "05:30:15 PM" in the Australia/Sydney timezone.

    Question: Convert "10:30 AM" from "America/Los_Angeles" to "Europe/Paris" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("10:30 AM", "America/Los_Angeles", "Europe/Paris")
    Result: "07:30 PM"
    Answer: "10:30 AM" in the America/Los_Angeles timezone is equivalent to "07:30 PM" in the Europe/Paris timezone.

    Question: Convert "21:15" to 12-hour format in "Asia/Dubai" timezone.
    API Call: TimeConverterAPI.convert_to_12h_format(TimeConverterAPI.convert_to_timezone("21:15", "UTC", "Asia/Dubai"))
    Result: "09:15 PM"
    Answer: "21:15" in the UTC timezone is equivalent to "09:15 PM" in the Asia/Dubai timezone.

    Question: Convert "4:45 PM" from "Asia/Kolkata" to "America/Chicago" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("4:45 PM", "Asia/Kolkata", "America/Chicago")
    Result: "6:15 AM"
    Answer: "4:45 PM" in the Asia/Kolkata timezone is equivalent to "6:15 AM" the next day in the America/Chicago timezone.

    Question: Convert "13:20" to 12-hour format in "America/Denver" timezone.
    API Call: TimeConverterAPI.convert_to_12h_format(TimeConverterAPI.convert_to_timezone("13:20", "UTC", "America/Denver"))
    Result: "07:20 AM"
    Answer: "13:20" in the UTC timezone is equivalent to "07:20 AM" in the America/Denver timezone.

    Question: Convert "8:30 AM" from "America/Toronto" to "Australia/Melbourne" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("8:30 AM", "America/Toronto", "Australia/Melbourne")
    Result: "10:30 PM"
    Answer: "8:30 AM" in the America/Toronto timezone is equivalent to "10:30 PM" the previous day in the Australia/Melbourne timezone.

    Question: Convert "16:55:30" to 12-hour format in "Europe/Madrid" timezone.
    API Call: TimeConverterAPI.convert_to_12h_format(TimeConverterAPI.convert_to_timezone("16:55:30", "UTC", "Europe/Madrid"))
    Result: "06:55:30 PM"
    Answer: "16:55:30" in the UTC timezone is equivalent to "06:55:30 PM" in the Europe/Madrid timezone.

    Question: Convert "11:30 AM" to 24-hour format.
    API Call: TimeConverterAPI.convert_to_24h_format("11:30 AM")
    Result: "11:30"
    Answer: "11:30 AM" in 24-hour format remains as "11:30".

    Question: Convert "18:45:20" from "Europe/Paris" to "America/New_York" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("18:45:20", "Europe/Paris", "America/New_York")
    Result: "12:45:20 PM"
    Answer: "18:45:20" in the Europe/Paris timezone is equivalent to "12:45:20 PM" in the America/New_York timezone.

    Question: Convert "5:15 PM" from "Australia/Sydney" to "Asia/Singapore" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("5:15 PM", "Australia/Sydney", "Asia/Singapore")
    Result: "3:15 PM"
    Answer: "5:15 PM" in the Australia/Sydney timezone is equivalent to "3:15 PM" in the Asia/Singapore timezone.

    Question: Convert "22:30" to 12-hour format in "Asia/Shanghai" timezone.
    API Call: TimeConverterAPI.convert_to_12h_format(TimeConverterAPI.convert_to_timezone("22:30", "UTC", "Asia/Shanghai"))
    Result: "10:30 PM"
    Answer: "22:30" in the UTC timezone is equivalent to "10:30 PM" in the Asia/Shanghai timezone.

    Question: Convert "9:45 AM" from "America/Denver" to "Europe/London" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("9:45 AM", "America/Denver", "Europe/London")
    Result: "4:45 PM"
    Answer: "9:45 AM" in the America/Denver timezone is equivalent to "4:45 PM" in the Europe/London timezone.

    Question: Convert "12:00" from UTC to "America/Los_Angeles" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("12:00", "UTC", "America/Los_Angeles")
    Result: "05:00 AM"
    Answer: "12:00" in the UTC timezone is equivalent to "05:00 AM" in the America/Los_Angeles timezone.

    Question: Convert "19:30:10" from "Asia/Tokyo" to "Europe/Paris" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("19:30:10", "Asia/Tokyo", "Europe/Paris")
    Result: "12:30:10 PM"
    Answer: "19:30:10" in the Asia/Tokyo timezone is equivalent to "12:30:10 PM" in the Europe/Paris timezone.

    Question: Convert "6:15 PM" to 12-hour format in "America/Chicago" timezone.
    API Call: TimeConverterAPI.convert_to_12h_format(TimeConverterAPI.convert_to_timezone("6:15 PM", "UTC", "America/Chicago"))
    Result: "1:15 PM"
    Answer: "6:15 PM" in the UTC timezone is equivalent to "1:15 PM" in the America/Chicago timezone.

    Question: Convert "10:30 AM" from "Asia/Kolkata" to "America/New_York" timezone.
    API Call: TimeConverterAPI.convert_to_timezone("10:30 AM", "Asia/Kolkata", "America/New_York")
    Result: "12:00 AM"
    Answer: "10:30 AM" in the Asia/Kolkata timezone is equivalent to "12:00 AM" the next day in the America/New_York timezone.

    Question: Convert "16:20" to 12-hour format in "Australia/Sydney" timezone.
    API Call: TimeConverterAPI.convert_to_12h_format(TimeConverterAPI.convert_to_timezone("16:20", "UTC", "Australia/Sydney"))
    Result: "02:20 PM"
    Answer: "16:20" in the UTC timezone is equivalent to "02:20 PM" in the Australia/Sydney timezone.
"""
