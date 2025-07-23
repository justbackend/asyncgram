import requests

from asyncgram.constants.urls import base_url


class Bot:
    def __init__(self, token: str):
        self.token = token
        self.url = base_url + token + '/'

    def send_message(self, chat_id: int, text: str):
        url = self.url + 'sendMessage'
        data = {
            'chat_id': chat_id,
            'text': text
        }

        r = requests.post(url, data=data)

        return r.json()