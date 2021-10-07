from pathlib import Path

import requests


def load_image(path, filename, url, params=None):
    filepath = Path(path) / filename
    response = requests.get(url, params=params)
    response.raise_for_status()
    with filepath.open('wb') as file:
        file.write(response.content)
