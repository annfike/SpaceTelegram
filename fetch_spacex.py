from pathlib import Path
import requests


def load_image(path, filename, url):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    filepath = path / filename
    response = requests.get(url)
    response.raise_for_status()
    with filepath.open('wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    response = response['links']['flickr_images']
    for i, link in enumerate(response, start=1):
        filename = f'spacex{i}.jpg'
        load_image('files', filename, link)
