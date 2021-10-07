import os
import pathlib
from os import listdir
from os.path import isfile
from os.path import join as joinpath
from time import sleep

import telegram
from dotenv import load_dotenv

from fetch_nasa import fetch_apod_pics, fetch_epic_pics
from fetch_spacex import fetch_spacex_launch


def send_pics_tg(tg_token, tg_channel, path):
    bot = telegram.Bot(token=tg_token)
    bot.send_message(chat_id=tg_channel, text='Hi')
    for files in listdir(path):
        filename = joinpath(path, files)
        if isfile(filename):
            with open(filename, 'rb') as file:
                bot.send_document(chat_id=tg_channel, document=file)
        sleep(86400)


def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    tg_token = os.getenv('TG_BOT_TOKEN')
    tg_channel = os.getenv('TG_CHANNEL')
    path = 'files'
    pathlib.Path(path).mkdir(exist_ok=True)
    fetch_spacex_launch(path, '67')
    fetch_apod_pics(path, nasa_token)
    fetch_epic_pics(path, nasa_token, '2021-10-03')

    while True:
        send_pics_tg(tg_token, tg_channel, path)



if __name__ == '__main__':
    main()


