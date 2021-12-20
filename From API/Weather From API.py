import requests, time

codes_csv = open('weather_codes_csv.csv')
codes_raw = codes_csv.read().split("\n")
codes = []
for i in codes_raw:
  codes.append(i.split(","))
codes_csv.close()

def get_weather(city, country):

  country_correct = False
  for x in codes:
    for y in range(len(x)):
      x[y] = x[y].lower()
    if country.lower() in x:
      country_correct = True
      code = x[1]
  
  if not country_correct:
    return False

  weather = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=d7dd1ed940c4ec5af650c6cc3d43b6a4&q={city},{code}').json()

  if weather['cod'] != '200':
    return False

  return weather

def direction(deg):
  if deg <= 11:
    return "N"
  if deg <= 34:
    return "NNE"
  if deg <= 56:
    return "NE"
  if deg <= 79:
    return "ENE"
  if deg <= 101:
    return "E"
  if deg <= 124:
    return "ESE"
  if deg <= 146:
    return "SE"
  if deg <= 169:
    return "SSE"
  if deg <= 191:
    return "S"
  if deg <= 214:
    return "SSW"
  if deg <= 236:
    return "SW"
  if deg <= 259:
    return "WSW"
  if deg <= 281:
    return "W"
  if deg <= 304:
    return "WNW"
  if deg <= 326:
    return "NW"
  if deg <= 349:
    return "NNW"
  if deg <= 359:
    return "N"

def get_date(x,t=True):
  days = ["Mon ", "Tue ", "Wed ", "Thu ", "Fri ", "Sat ", "Sun "]
  y = time.gmtime(x)
  if t:
    return days[int(y.tm_wday)] + str(y.tm_mday) + "/" + str(y.tm_mon) + " " + str(y.tm_hour).zfill(2) + ":00 - "
  else:
    return days[int(y.tm_wday)] + str(y.tm_mday) + "/" + str(y.tm_mon) + " - "

def display(name, weather, later):

  print(f"Right now in {name[0].upper()}{name[1:]}, the temperature is {round(weather['main']['temp']-273.15,2)}C (feels like {round(weather['main']['feels_like']-273.15,2)}C).\nMainly {weather['weather'][0]['description']} with a windspeed of {weather['wind']['speed']}m/s, direction bearing {weather['wind']['deg']} degrees from North ({direction(weather['wind']['deg'])}).\n")

  print("Forecast (24 hours):")
  for times in range(0,9):
    print(f"{get_date(later[times]['dt'])}{round(later[times]['main']['temp']-273.15,2)}C - {later[times]['weather'][0]['description']}")

  print("(Times in GMT)\n")

  print("Forecast (5 days):")
  for times in range(0,5):
    print(f"{get_date(later[times*8]['dt'],False)}{round(later[times*8]['main']['temp']-273.15,2)}C - {later[times]['weather'][0]['description']}")

city = input("Town or City (e.g. London): ")
country = input("Country or ISO code (e.g. United Kingdom or GB): ")

weather = get_weather(city, country)
print("")

if weather != False:

  weather_now = weather['list'][0]
  later = weather['list']
  display(city, weather_now, later)

else:
  print("Location not found.")