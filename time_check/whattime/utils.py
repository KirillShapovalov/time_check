import requests


time_api_url = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'
url = 'http://127.0.0.1:8000/timecheck/'
delta = 500


def check_time(value):
    response = requests.get(time_api_url)
    if response.status_code == 200:
        time = int(response.json().get('unixtime'))
        valid = abs(int(time) - int(value)) < delta
        return bool(valid)
