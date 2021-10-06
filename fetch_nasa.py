import requests
from load_image import load_image


def get_apod_pics(path, token):
  url = 'https://api.nasa.gov/planetary/apod'
  payload = {'count': '10', 'api_key': token}
  response = requests.get(url, params=payload)
  response.raise_for_status()
  response = response.json()
  for index, pic in enumerate(response, start=1):
    filename = f'nasa{index}.jpg'
    load_image(path, filename, pic['url'])


def get_epic_pics(path, token_nasa, date):
    payload = {'api_key': token_nasa}
    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{date}", params=payload)
    response.raise_for_status()
    response = response.json()
    year, month, day = date.split("-")
    for index, pic in enumerate(response, start=1):
        image = pic['image']
        filename = f'earth{index}.jpg'
        link = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png'
        load_image(path, filename, link, params=payload)



