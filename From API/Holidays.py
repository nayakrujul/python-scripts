import datetime
import requests
import sys


def format_date(date, split='-'):

    if len(date.split(split)) == 3:

        y, m, d = date.split(split)

        if d.isdigit() and m.isdigit() and y.isdigit():

            d, m, y = int(d), int(m), int(y)

            if 1 <= d <= 31 and 1 <= m <= 12:

                _date = {
                    1: '1st',
                    2: '2nd',
                    3: '3rd',
                    21: '21st',
                    22: '22nd',
                    23: '23rd',
                    31: '31st'
                }
                month = [
                    'January',
                    'February',
                    'March',
                    'April',
                    'May',
                    'June',
                    'July',
                    'August',
                    'September',
                    'October',
                    'November',
                    'December'
                ]

                if d in _date.keys():
                    day = _date[d]
                else:
                    day = str(d) + 'th'

                return datetime.datetime(y, m, d).strftime('%A') + ' ' + day + ' ' + month[m - 1] + ', ' + str(y)

    return date


print('Enter the year and the country to get the public holidays.')

year = input('Year: ')

if not year.isdigit():
    year = datetime.datetime.now().year

country = input('Country code (e.g. GB): ')


print('\n')


try:
    data = requests.get(f'https://date.nager.at/api/v3/PublicHolidays/{year}/{country}').json()
except requests.exceptions.JSONDecodeError:
    print('An error occurred.')
    sys.exit()


if isinstance(data, list):

    for event in data:

        print(format_date(event['date']))
        print(event['name'])
        print(['Local', 'Full country'][int(event['global'])], 'event')
        if event['counties'] is not None:
            print('Regions:', ', '.join(event['counties']))
        print('\n- - - - - - - - - -\n')

else:

    print('An error occurred.')
