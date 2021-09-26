import os
from os import listdir
from os.path import isfile
from os.path import join as joinpath
from time import sleep

import telegram
from dotenv import load_dotenv

from fetch_nasa import get_epic_pics
from fetch_spacex import fetch_spacex_last_launch


def main():
    load_dotenv()
    token_nasa = os.getenv('NASA_TOKEN')
    token_tg = os.getenv('TG_BOT_TOKEN')
    bot = telegram.Bot(token=token_tg)
    fetch_spacex_last_launch(url='https://api.spacexdata.com/v3/launches/67')
    get_epic_pics(token_nasa, url='https://api.nasa.gov/EPIC/api/natural')
    while True:
        sleep(10)
        bot.send_message(chat_id='@annfike_tg', text='Hi')
        mypath = 'files'
        for files in listdir(mypath):
            filename = joinpath(mypath, files)
            if isfile(joinpath(mypath, files)):
                bot.send_document(chat_id='@annfike_tg', document=open(filename, 'rb'))


if __name__ == '__main__':
    main()


