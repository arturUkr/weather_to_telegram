import requests
from datetime import datetime
from api_config import DARKSKY_TOKEN, WEATHER_URL, CITY_COORD
from pprint import pprint


def get_weather(city_name):
    city_coord = CITY_COORD.get(city_name.lower())
    url = WEATHER_URL + DARKSKY_TOKEN + '/' + city_coord + '?exclude=minutely,hourly,daily,alerts,flags?lang=uk'
    response = requests.get(url).json()  # , verify=False
    current_data = response['currently']

    temperature = current_data['temperature']
    temperature_celsius = round((temperature - 32) * (5 / 9), 1)
    summary = current_data['summary']
    date = datetime.fromtimestamp(float(current_data['time']))

    result_str = f"Temperature in {city_name.capitalize()} is " \
        f"{temperature_celsius}{chr(176)}C on {date}, " \
        f"summary - {summary}"

    return result_str


if __name__ == "__main__":
    pprint(get_weather('lviv'))
