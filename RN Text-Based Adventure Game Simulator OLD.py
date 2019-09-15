print("Welcome to the RN text-based adventure simulator.")

inst = input("Here are the intructions (Press enter to skip). To move forward, type 'F' and press 'Enter'. To turn left, type 'L' and press 'Enter'. To turn right, type 'R' and press 'Enter'. To shoot, type 'S' and press 'Enter'.")

while (inst != ""):
  inst = input("Press enter to start")


print("You can start in 3...")
print("2...")
print("1...")
start = input("Go... Press 'F' to start. ")


while (start != ""):    
  if(start == "F"):
    start = input("Enter another key. ")
    if(start == "R"):
      print("You are in shooting range.")
      start = input("Enter another key. ")
      if(start == "S"):
        print("Victory!")
        start = ""
      else:
        print("Defeat! You got shot.")
        start = ""
    elif(start == "F"):
      print("Defeat! You have walked into a wall.")
      start = ""
    elif(start == "L"):
      start = input("Enter another key. ")
      if(start == "F"):
        start = input("Enter another key. ")
        if(start == "F"):
          print("Defeat! You have walked into a wall")
          start = ""
        elif(start == "R"):
          start = input("Enter another key. ")
          if(start == "F"):
            print("Defeat! You have walked into a wall")
            start = ""
          elif(start == "R"):
            print("You are in shooting range")
            start = input("Enter another key. ")
            if(start == "S"):
              print("Victory!")
              start = ""
            else:
              print("Defeat! You got shot.")
              start = ""
          elif(start == "L"):
            print("Defeat! You got shot in the back.")
            start = ""
        elif(start == "L"):
          start = input("Enter another key. ")
          if(start == "L"):
            print("You are in shooting range")
            start = input("Enter another key. ")
            if(start == "S"):
              print("Victory!")
              start = ""
            else:
              print("Defeat! You got shot.")
              start = ""
          elif(start == "R"):
            print("Defeat! You got shot in the back.")
            start = ""
          elif(start == "F"):
            start = input("Enter another key. ")