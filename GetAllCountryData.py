from requests import get


location = get('https://countriesnow.space/api/v0.1/countries/positions').json()
population = get('https://countriesnow.space/api/v0.1/countries/population').json()
currency = get('https://countriesnow.space/api/v0.1/countries/currency').json()
codes = get('https://countriesnow.space/api/v0.1/countries/iso').json()
cities = get('https://countriesnow.space/api/v0.1/countries').json()


def get_data(country_name):

    lst = []

    best_match = "", 0
    for item in location['data']:
        if country_name.lower() == item['name'].lower():
            best_match = item, 2
        if (country_name.lower() in item['name'].lower()
                or item['name'].lower() in country_name.lower()):
            if best_match[1] < 1:
                best_match = item, 1
    if best_match[0] == "":
        return False
    lst.append(best_match[0])

    best_match = "", 0
    for item in population['data']:
        if country_name.lower() == item['country'].lower():
            best_match = item, 2
        if (country_name.lower() in item['country'].lower()
                or item['country'].lower() in country_name.lower()):
            if best_match[1] < 1:
                best_match = item, 1
    if best_match[0] == "":
        return False
    lst.append(best_match[0])

    best_match = "", 0
    for item in currency['data']:
        if country_name.lower() == item['name'].lower():
            best_match = item, 2
        if (country_name.lower() in item['name'].lower()
                or item['name'].lower() in country_name.lower()):
            if best_match[1] < 1:
                best_match = item, 1
    if best_match[0] == "":
        return False
    lst.append(best_match[0])

    best_match = "", 0
    for item in codes['data']:
        if country_name.lower() == item['name'].lower():
            best_match = item, 2
        if (country_name.lower() in item['name'].lower()
                or item['name'].lower() in country_name.lower()):
            if best_match[1] < 1:
                best_match = item, 1
    if best_match[0] == "":
        return False
    lst.append(best_match[0])

    best_match = "", 0
    for item in cities['data']:
        if country_name.lower() == item['country'].lower():
            best_match = item, 2
        if (country_name.lower() in item['country'].lower()
                or item['country'].lower() in country_name.lower()):
            if best_match[1] < 1:
                best_match = item, 1
    if best_match[0] == "":
        return False
    lst.append(best_match[0])

    lst.append(lst[0]['name'])
    return lst


if not (location['error'] and population['error'] and currency['error'] and cities['error'] and codes['error']):

    country = input("Country (e.g. United Kingdom): ")
    print("")

    data = get_data(country)

    if data is not False:

        print(f"Country {data[5]}:\n")

        print(
            f"Location: {data[0]['lat']} N/S, {data[0]['long']} E/W"
        )

        print(
            f"Population as of {data[1]['populationCounts'][-1]['year']}: {data[1]['populationCounts'][-1]['value']}"
        )

        print(
            f"Currency: {data[2]['currency']}"
        )

        print(
            f"ISO codes: {data[3]['Iso2']} / {data[3]['Iso3']}"
        )

        city = input(f"\nIs this city in {data[5]}: ")

        if city.lower() in [x.lower() for x in data[4]['cities']]:
            print("Yes.")
        else:
            print("No.")

    else:
        print("Country not found.")

    print("\nAPI: https://countriesnow.space/api")

else:
    print("API cut connection.")
