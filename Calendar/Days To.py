from datetime import datetime as dt

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

class Calendar:

  def add(self, days, month):

    for i in range(1, days+1):

      self.calendar.append(f"{i} {month}")

  def check_leap_year():

    # In a leap year, e.g. 2016
    if dt.now().year % 4 == 0:

      # Before or in February (29th Feb still to come)
      if dt.now().month <= 2:

        return True
      
      # After February (29th Feb has passed)
      else:

        return False
    
    # The year before a leap year, e.g. 2015
    elif dt.now().year % 4 == 3:

      # After February (29th Feb coming within a year)
      if dt.now().month > 2:

        return True
      
      # Before or in February (29th Feb over 1 year away)
      else:

        return False

    # Any other year
    else:

      return False

  def __init__(self):

    self.calendar = []

    self.add(31, "January")
    if Calendar.check_leap_year():
      self.add(29, "February")
    else:
      self.add(28, "February")
    self.add(31, "March")
    self.add(30, "April")
    self.add(31, "May")
    self.add(30, "June")
    self.add(31, "July")
    self.add(31, "August")
    self.add(30, "September")
    self.add(31, "October")
    self.add(30, "November")
    self.add(31, "December")

  def sort(self):

    year = dt.now().year
    month = months[(dt.now().month)-1]
    day = dt.now().day

    print(f"Today is {day} {month} {year}.")

    today = f"{day} {month}"

    index = 0

    while self.calendar[0] != today:

      moving = self.calendar[0]

      self.calendar.remove(moving)
      self.calendar.append(moving)

  def days_entered(self, i):
    
    i = int(i)

    if i >= len(self.calendar):

      print("Sorry, we couldn't calculate that...")
      return -1
    
    print(f"{i} days in the future is {self.calendar[i]}.")

  def date_entered(self, s):

    if s.count('/') != 1:

      print("Sorry, we couldn't calculate that...")
      return -1
    
    day = s.split('/')[0]
    month = s.split('/')[1]

    if (not month.isdigit()) or (not day.isdigit()):

      print("Sorry, we couldn't calculate that...")
      return -1
    
    day = int(day)
    month = int(month)

    if month > 12:

      print("Sorry, we couldn't calculate that...")
      return -1
    
    month_str = months[month-1]

    if f"{day} {month_str}" not in self.calendar:

      print("Sorry, we couldn't calculate that...")
      return -1
    
    print(f"{day} {month_str} is {self.calendar.index(str(day) + ' ' + month_str)} days in the future.")

  def check(self, d):

    if d.isdigit():

      self.days_entered(d)
    
    elif "/" in d:

      self.date_entered(d)
    
    else:
      
      print("Sorry, we couldn't calculate that...")
      return -1

calendar = Calendar()

calendar.sort()

print("\n-------------------------------------------")

print("\nDays to:")
print(f"\nChristmas")
calendar.check('25/12')
print(f"\nNew Year")
calendar.check('1/1')
print(f"\nStart of Summer (21st June)")
calendar.check('21/6')

print("\n-------------------------------------------")

days = input("\nEnter a number of days in the future (up to 1 year, e.g. 35),\nor a date in the format DD/MM (no year, e.g. 25/12): ")
print("")

calendar.check(days)