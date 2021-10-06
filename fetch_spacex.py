import requests
from load_image import load_image


def fetch_spacex_launch(path, launch):
    url = f'https://api.spacexdata.com/v3/launches/{launch}'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    response = response['links']['flickr_images']
    for index, link in enumerate(response, start=1):
        filename = f'spacex{index}.jpg'
        load_image(path, filename, link)
