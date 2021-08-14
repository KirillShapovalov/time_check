import requests
import os


def check_time(value):
    response = requests.get(os.environ.get('time_api_url'))
    if response.status_code == 200:
        time = int(response.json().get('unixtime'))
        valid = abs(int(time) - int(value)) < int(os.environ.get('delta'))
        return bool(valid)
