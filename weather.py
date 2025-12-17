from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# we wanna load the API_KEY from our .env file, which this function does
load_dotenv()

def get_current_weather( city="San Francisco" ):

    request_url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial"
    
    weather_data = requests.get(request_url).json()

    return weather_data

# let's make this a module:
if __name__ == "__main__":

    print("\n*** Get Current Weather Conditions ***")

    city = input("\nPlease enter the city name: ")

    # how to check for empty strings or string with only spaces
    # and we will return SF if when we strip the city name of it's spaces. if it is empty, then we will return the default city of SF.
    if not bool(city.strip()):
        city = "San Francisco"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)