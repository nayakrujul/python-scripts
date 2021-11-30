import arrow, datetime

def has_friday_13th(year, month) -> True or False :

  year = str(year)
  month = str(month)

  year = year.replace(" ", "")
  year = year.replace("'", "")
  month = month.replace(" ", "")
  month = month.replace("'", "")

  if not (year.isdigit() and month.isdigit()):
    return None

  if int(month) > 12 or int(month) < 0:
    return None

  if len(year) == 2:
    if int(year) < 50:
      year = "20" + year
    else:
      year = "19" + year

  if len(year) != 4:
    return None

  if int(year) < 1950 or int(year) >= 2050:
    return None
  
  arrow_date = arrow.get(f'13/{str(month).zfill(2)}/{year}', 'DD/MM/YYYY')
  day = arrow_date.weekday()

  if day == 4:
    return True
  else:
    return False

def get_friday_13ths(months) -> [ True or False, True or False, ..., True or False ] :

  months = list(months)
  lst = []

  for month in months:

    if "/" in month:

      lengths = ((2,4),(1,4),(2,2),(1,2))
      split = month.split("/")

      if (len(split[0]), len(split[1])) in lengths:

        m = split[0]
        y = split[1]

        if has_friday_13th(y,m) == True:

          lst.append(f'{m.zfill(2)}/{y}')

  return lst

def next_friday_13th() -> "MM/YYYY":

  current_date = [int(datetime.datetime.now().month), int(datetime.datetime.now().year)]

  if int(datetime.datetime.now().day) > 13:
    current_date[0] += 1

    if current_date[0] > 12:

      current_date[0] -= 12
      current_date[1] += 1

  counter = 0

  while counter <= 24:

    counter += 1

    if has_friday_13th(current_date[1], current_date[0]):

      break
    
    current_date[0] += 1

    if current_date[0] > 12:

      current_date[0] -= 12
      current_date[1] += 1
  
  if counter < 24:
    return f'{str(current_date[0]).zfill(2)}/{current_date[1]}'

  else:
    return "Error"

print("11/2021 ->", has_friday_13th(2021, 11))
print("08/2021 ->", has_friday_13th("'21", 8))
print("08/1999 ->", has_friday_13th(99, " 8 "))
print("13/2020 ->", has_friday_13th(2020, 13))
print("01/abcd ->", has_friday_13th("abcd", 1))

print("\n- - - - - - - - - - - -\n")

print("*/2026 ->", get_friday_13ths(["1/26","2/26","3/26","4/26","5/26","6/26","7/26","8/26","9/26","10/26","11/26","12/26"]))
print("[abc, 02/2015, 05/2016, 03/2020] ->", get_friday_13ths(["abc", "2/2015", "05/16", "3/20"]))
print("abc ->", get_friday_13ths(["abc"]))

print("\n- - - - - - - - - - - -\n")

print("Next Friday 13th:", next_friday_13th())

print("\n- - - - - - - - - - - -\n")

print(has_friday_13th(input("Enter a year: "), input("Enter a month: ")))