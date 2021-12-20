print("")
print("Air India confidential.")
print("In association with British Airways.")
print("An RN code.")
print("")


SeatNumber = []


import random
planeNumber = random.randint(100,999)
timeHrs = random.randint(00,23)
timeMins = random.randint(00,59)


if(planeNumber >= 500):
    import random
    flightTime = random.randint(5,10)
    print("International flight AI " + str(planeNumber) + " departing at " + str(timeHrs).zfill(2) + ":" + str(timeMins).zfill(2) + " IST. Flight time is " + str(flightTime) + " hours.")
else:
    import random
    flightTime = random.randint(1,4)
    print("Domestic flight AI " + str(planeNumber) + " departing at " + str(timeHrs).zfill(2) + ":" + str(timeMins).zfill(2) + " IST. Flight time is " + str(flightTime) + " hours.")


BA_Customers = open("BA_Customers.txt", "r")


for Customer_Detail in BA_Customers:
  split = Customer_Detail.split("|| ")
  counter = 0
  display = ""
  for ele in split:
    detail = ele.strip()
    if(counter == 0):
        display = display + "The passenger " + detail
    elif(counter == 1):
        display = display + " is of age " + detail
    elif(counter == 2):
        display = display + ", is " + detail + " gender"
    import random
    seatLetter = random.randint(1,6)
    if(seatLetter == 1):
        seatLetter2 = "A (left window)"
    elif(seatLetter == 2):
        seatLetter2 = "B (left middle)"
    elif(seatLetter == 3):
        seatLetter2 = "C (left aisle)"
    elif(seatLetter == 4):
        seatLetter2 = "D (right aisle)"
    elif(seatLetter == 5):
        seatLetter2 = "E (right middle)"
    elif(seatLetter == 6):
        seatLetter2 = "F (right window)"
    else:
        seatLetter2 = " - System Malfunction. Please try again later. "
  
    counter = counter + 1
  import random
  seatNumber2 = random.randint(1,25)
  display = display + " and has a seat number of " + str(seatNumber2) + seatLetter2
  print(display)
  Seat = [str(seatNumber2), str(seatLetter2)]
  SeatNumber = SeatNumber + Seat

print("")

exit = 0

Baggage_Drop = raw_input("Would you like to do Self Baggage Drop? ")
if(Baggage_Drop == "Yes" or Baggage_Drop == "yes" or Baggage_Drop == "Y" or Baggage_Drop == "y"):
    while(exit != 1):
        bags = raw_input("Please enter your bag. Type 'D' when you're done and press enter to exit. ")
        if(bags == ""):
            exit = exit + 1
        else:
            import random
            weight = random.randint(10,35)
            if(weight > 25):
                print("Your bag is too heavy. It is " + str(weight) + "kg. Please enter another one.")
            else:
                print("Your bag is " + str(weight) + "kg. Going through to your plane. ")

print("")