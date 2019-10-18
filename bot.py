import requests
from api_config import *
from weather_data import get_weather
from pprint import pprint


def get_updates():
    """
    gets text and chat_id from last message
    """
    url = TELEGRAM_URL + TELEGRAM_TOKEN + '/getUpdates'
    response = requests.get(url).json()
    last_object = response['result'][-1]  # -1 = last update

    chat_id = last_object['message']['chat']['id']
    message_text = last_object['message']['text']
    message = {
        'chat_id': chat_id,
        'text': message_text
    }
    return message


def send_message(chat_id, text='bla-bla'):
    url = TELEGRAM_URL + TELEGRAM_TOKEN + '/sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, json=answer).json()
    return response


if __name__ == "__main__":
    message = get_updates()
    pprint(message)
    if CITY_COORD.get(message['text'], False):
        send_message(message['chat_id'], get_weather(message['text']))
