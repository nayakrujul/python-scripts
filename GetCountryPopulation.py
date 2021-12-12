from requests import get
from format_num import *


response = get('https://countriesnow.space/api/v0.1/countries/population/').json()


def get_data(country_name):

    for item in response['data']:

        if (country_name.lower() in item['country'].lower()
                or item['country'].lower() in country_name.lower()
                or country_name.upper() == item['code'].upper()):

            return item


if not response['error']:

    country = input("Country (e.g. United Kingdom) or code (e.g. GBR): ")

    data = get_data(country)
    if data is not None:

        print(f"\nPopulation counts for {data['country']} ({data['code']}):")
        counts = data["populationCounts"]
        for count in reversed(counts):
            print(count["year"], ": ", format_num(int(round(float(count["value"])))), " ",
                  estimate(int(round(float(count["value"])))), sep="")

    else:
        print("Not found.")

    print("\nAPI: https://countriesnow.space/api")

else:
    print("API cut connection.")