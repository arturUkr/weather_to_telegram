from flask import Flask
from flask import request
from flask import jsonify
import requests
from api_config import *
from weather_data import get_weather


app = Flask(__name__)


# def get_updates():
#     """
#     gets text and chat_id from last message
#     """
#     url = TELEGRAM_URL + TELEGRAM_TOKEN + '/getUpdates'
#     response = requests.get(url).json()
#     last_object = response['result'][-1]  # -1 = last update
#
#     chat_id = last_object['message']['chat']['id']
#     message_text = last_object['message']['text']
#     message = {
#         'chat_id': chat_id,
#         'text': message_text
#     }
#     return message


def send_message(chat_id, text='bla-bla'):
    url = TELEGRAM_URL + TELEGRAM_TOKEN + '/sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, json=answer).json()
    return response


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        response = request.get_json()
        chat_id = response['message']['chat']['id']
        message = response['message']['text']

        if CITY_COORD.get(message, False):
            send_message(chat_id, get_weather(message))

        return jsonify(response)
    return '<h1>Hello bot</h1>'


if __name__ == "__main__":
    app.run()
