import requests
import datetime
import time

url = 'http://api.open-notify.org/iss-now.json'

while True:
    response = requests.get(url=url)
    data = response.json()
    result = f'{datetime.datetime.now()};{data["iss_position"]["latitude"]};{data["iss_position"]["longitude"]}\n'
    print(result, end='')

    with open(f'statistics/position.csv', 'a') as file:
        file.write(result)
