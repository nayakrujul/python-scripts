from requests import get
from format_num import *


response = get('https://countriesnow.space/api/v0.1/countries/population/cities').json()


def get_data(city_name, country_name):

    for item in response['data']:

        if (
            (city_name in item['city'].lower() or item['city'].lower() in city_name)
            and (country_name in item['country'].lower() or item['country'].lower() in country_name)
        ):
            return item


if not response['error']:

    city = input("City (e.g. London): ")
    country = input("Country (e.g. United Kingdom): ")

    data = get_data(city.lower(), country.lower())
    if data is not None:

        print("\nPopulation counts for ", data["city"], ", ", data["country"], ":", sep="")
        counts = data["populationCounts"]
        for count in reversed(counts):
            print(count["year"], ": ", format_num(int(round(float(count["value"])))), " ",
                  estimate(int(round(float(count["value"])))), sep="")

    else:
        print("Not found.")

    print("\nAPI: https://countriesnow.space/api")

else:
    print("API cut connection.")
