import datetime
import requests
from fetch_spacex import load_image


def get_epic_pics(token_nasa, url):
    date = datetime.datetime(year=2021, month=9, day=21)
    # объясняю строчку с датой - я не могу вытащить фотки от 'сегодня',
    # последние фотки там почему-то от 21.09
    # https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY
    payload = {'date': date.date(), 'api_key': token_nasa}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    response = response.json()
    for i, pic in enumerate(response, start=1):
        image = pic['image']
        formatted_date = date.strftime('%Y/%m/%d')
        filename = f'earth{i}.jpg'
        link = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{image}.png?api_key={token_nasa}'
        load_image('files', filename, link)



