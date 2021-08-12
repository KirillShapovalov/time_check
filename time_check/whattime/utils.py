import requests
from decouple import config


def check_time(value):
    response = requests.get(config('time_api_url'))
    if response.status_code == 200:
        time = int(response.json().get('unixtime'))
        valid = abs(int(time) - int(value)) < int(config('delta'))
        return bool(valid)
