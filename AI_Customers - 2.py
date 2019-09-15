BA_Customers = open("BA_Customers.txt", "r")
for Customer_Detail in BA_Customers:
  split = Customer_Detail.split("|| ")
  counter = 0
  for ele in split:
    detail = ele.strip()
    print("The first passenger is called " + detail)
    counter = counter + 1