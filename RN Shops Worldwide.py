print("Hello and welcome to RN Shops worldwide!")
itemrange = input("Please type your selection range. Clothes or Groceries? ")
if (itemrange == "Clothes"):
  cItem = input("Please enter a range. Womens, Mens or Kids. ")
  if (cItem == "Womens"):
    cwItem = input("Please enter your size. ")
    cwCost = int(cwItem) / 4 - 0.01
    print("Total cost is £" + str(cwCost))
  elif (cItem == "Mens"):
    cmItem = input("Please enter your size. S, M or L. ")
    if (cmItem == "S"):
      print("Total cost is £5.99")
    elif (cmItem == "M"):
      print("Total cost is £7.99")
    elif (cmItem == "L"):
      print("Total cost is £9.99")
    else:
      cmItem = input("Please enter a valid size. ")
  elif (cItem == "Kids"):
    ckItem = input("Enter the age in years. ")
    ckCost = int(ckItem) - 0.01
    print("Total cost is £" + str(ckCost))
  else:
    cItem = input("Please enter a valid range. ")
elif (itemrange == "Groceries"):
  gItem = input("Please enter an item. Fruit, Milk or Bread. ")
  if (gItem == "Fruit"):
    gfItem = input("What type of fruit would you like? Strawberries, Apples or Bananas. ")
    if (gfItem == "Strawberries"):
      gfsNo = input("Please enter number of packs. ")
      gfsCost = int(gfsNo) * 1.99
      print("Total cost is £" + str(gfsCost))
    elif (gfItem == "Apples"):
      gfaG = input("Please enter weight in grams. ")
      gfaCost = int(gfaG) * 0.008
      print("Total cost is £" + str(gfaCost))
    elif (gfItem == "Bananas"):
      gfbG = input("Please enter weight in grams. ")
      gfbCost = int(gfbG) * 0.005
      print("Total cost is £" + str(gfbCost))
    else:
      gfItem = input("Please enter a valid fruit. ")
  elif (gItem == "Milk"):
    gmItem = input("Please enter type of milk. Skimmed or Whole? ")
    if (gmItem == "Skimmed"):
      gmsPts = input("How many pints do you need? ")
      gmsCost = int(gmsPts) * 0.34
      print("Total cost is £" + str(gmsCost))
    elif (gmItem == "Whole"):
      gmwPts = input("How many pints do you need? ")
      gmwCost = int(gmwPts) * 0.24
      print("Total cost is £" + str(gmwCost))
    else:
      gmItem = input("Please enter a valid type. ")
  elif (gItem == "Bread"):
    print("Total cost is £1.10")
else:
  itemrange = input("Please enter a valid category. ")

# Go to https://repl.it/repls/SilkyOptimisticCustomer (Command + Click)
## Thank you