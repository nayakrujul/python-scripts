BA_Customers = open("BA_Customers.txt", "r")
for Customer_Detail in BA_Customers:
  print(Customer_Detail)
  split = Customer_Detail.split("|| ")
  counter = 0
  for ele in split:
    print(ele.strip())
    if(counter == 0):
        print("^ Name")
    elif(counter == 1):
        print("^ Age")
    elif(counter == 2):
        print("^ Gender")
    else:
        print("System Malfunction. Try again later.")
    counter = counter + 1