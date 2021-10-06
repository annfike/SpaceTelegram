import os
from os import listdir
from os.path import isfile
from os.path import join as joinpath
from time import sleep
import pathlib

import telegram
from dotenv import load_dotenv

from fetch_nasa import get_epic_pics, get_apod_pics
from fetch_spacex import fetch_spacex_launch


def main():
    load_dotenv()
    token_nasa = os.getenv('NASA_TOKEN')
    token_tg = os.getenv('TG_BOT_TOKEN')
    channel = os.getenv('TG_CHANNEL')
    bot = telegram.Bot(token=token_tg)
    path = 'files'
    pathlib.Path(path).mkdir(exist_ok=True)
    fetch_spacex_launch(path, '67')
    get_apod_pics(path, token_nasa)
    get_epic_pics(path, token_nasa, '2021-10-03')


    while True:
        bot.send_message(chat_id=channel, text='Hi')
        for files in listdir(path):
            filename = joinpath(path, files)
            if isfile(filename):
                with open(filename, "rb") as file:
                    f = file.read()
                bot.send_document(chat_id=channel, document=f)
        sleep(86400)


if __name__ == '__main__':
    main()


