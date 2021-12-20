# RN09 Studios
# November 2021
# Python 3.8

# This program lets the user enter a month and a year,
# then displays the calendar of that specified month.

# This program uses the module 'arrow'.
# This will only work on Python 3.6+


import sys

try:
  import arrow, os
except ModuleNotFoundError:
  print("\033[1;31;40mYou are not on Python 3.6+, meaning you cannot run this program.\033[1;40;0m")
  sys.exit(0)


class Calendar:


  def __init__(self):

    x = arrow.now()
    self.date = arrow.get(f"{str(x.day).zfill(2)}/{str(x.month).zfill(2)}/{x.year}", "DD/MM/YYYY")


  def change_day(self, m, y):

    if not (m.isdigit() and y.isdigit()):
      return False

    m = str(int(m))

    y = int(y)

    if len(str(y)) == 1:
      y = "200" + str(y)
    if len(str(y)) == 2:
      if y < 50:
        y = "20" + str(y)
      else:
        y = "19" + str(y)
    if len(str(y)) == 3:
      y = "1" + str(y)
    
    y = str(y)

    try:
      self.date = arrow.get(f"01/{str(m).zfill(2)}/{str(y).zfill(4)}", "DD/MM/YYYY")
      return True
    
    except:
      return False


  def get_start_day(self):

    current_weekday = self.date.weekday()
    current_day = self.date.day - 1

    day_of_first = current_weekday - current_day
    while day_of_first < 0:
      day_of_first += 7
    
    return day_of_first
  

  def leap_year(self):

    if self.date.year % 4 == 0:
      return 29
    else:
      return 28


  def draw(self):

    os.system('clear')

    print(str(self.date.month).zfill(2), "/", str(self.date.year).zfill(4), "\n", sep="")

    print("| MO | TU | WE | TH | FR | SA | SU |")

    first = self.get_start_day()
    for x in range(0, first):
      print("|    ", end="")

    for y in range(first+1, 8):
      print(f"| {str(y-first).zfill(2)} ", end="")
    print("|")
    y += 1

    for z in range(y, y+7):
      print(f"| {str(z-first).zfill(2)} ", end="")
    print("|")
    z += 1

    for a in range(z, z+7):
      print(f"| {str(a-first).zfill(2)} ", end="")
    print("|")
    a += 1

    for b in range(a, a+7):
      print(f"| {str(b-first).zfill(2)} ", end="")
    print("|")
    b += 1

    days = [31,self.leap_year(),31,30,31,30,31,31,30,31,30,31]

    if b-first <= days[self.date.month-1]:
      for c in range(b, b+7):
        if c-first <= days[self.date.month-1]:
          print(f"| {str(c-first).zfill(2)} ", end="")
        else:
          print("|    ", end="")
      print("|")

    else:
      c = b

    if c-first <= days[self.date.month-1]:
      for d in range(c, c+7):
        if d-first <= days[self.date.month-1]:
          print(f"| {str(d-first).zfill(2)} ", end="")
        else:
          print("|    ", end="")
      print("|")

    print("")


  def get_input(self):

    print("Leave blank to exit.")
    month = input("Month (e.g. 5): ")
    year = input("Year: ")

    if month == "" or year == "":
      return False

    if self.change_day(month, year):
      self.draw()
    else:
      print("Wrong format.\n")
  
    return True
  

  def loop(self):

    looping = True
    while looping:
      looping = self.get_input()


cal = Calendar()
cal.draw()
cal.loop()