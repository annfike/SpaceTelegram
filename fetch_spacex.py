from pathlib import Path
import requests


def load_image(path, filename, url, params = None):
    path = Path(path)
    filepath = path / filename
    response = requests.get(url, params=params)
    response.raise_for_status()
    with filepath.open('wb') as file:
        file.write(response.content)


def fetch_spacex_launch(path, launch):
    url = f'https://api.spacexdata.com/v3/launches/{launch}'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    response = response['links']['flickr_images']
    for index, link in enumerate(response, start=1):
        filename = f'spacex{index}.jpg'
        load_image(path, filename, link)
