from requests import get as get_data
from arrow import now, get as get_time
from os import system
from time import sleep

city = input("City name: ")
KEY = 'd85b0e7dff1c47fdad452040212112'
response = get_data('https://api.worldweatheronline.com/premium/v1/tz.ashx'
                    f'?key={KEY}'
                    f'&q={city}'
                    '&format=json'
                    ).json()['data']

if 'error' not in response.keys():

    while True:

        try:

            system('clear')

            print(
                f"Local time in {response['request'][0]['query']}:",
                get_time(
                    response['time_zone'][0]['localtime'] + ":" + str(now().second).zfill(2),
                    'YYYY-MM-DD HH:mm:ss'
                ).format(
                    'HH:mm:ss A on DD MMM YYYY'
                ),
                "\n\nPress CTRL + C to stop."
            )

            sleep(0.5)

        except KeyboardInterrupt:

            break

else:

    print(
        "Not found"
    )
