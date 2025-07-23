import requests

from asyncgram.api.methods import ApiMethods
from asyncgram.bot.bot import Bot
from asyncgram.constants.urls import base_url
from rich import print_json

class Dispatcher:
    def __init__(self):
        self.token = None
        self.url = None

    # def __call__(self, *args, **kwargs):



    def set_token(self, token: str):
        self.token = token
        self.url = base_url + token + '/'


    def start_polling(self, bot: Bot):
        self.set_token(bot.token)
        url = self.url + ApiMethods.GET_UPDATES
        offset = None
        while True:
            data = {
                'offset': offset,
                'timeout': 10000
            }
            try:
                r = requests.post(url, data=data)
            except Exception as e:
                print(e)
                print('////ABORTED/////')
                continue

            result = r.json()['result']
            offset = result[-1].get('update_id', None) if result else None
            offset = offset + 1 if offset else offset
            print(f'//////////////////////////////////////////////////////: {offset}')
            print_json(data=r.json())