print("")
def is_Power_of_x(x, y):
   while (x % y == 0):
       x = x / y
   return x == 1
ext = 0
while(ext == 0):
    num = input("Number: ")
    power = input("Power: ")
    if(str.isdigit(str(num)) and str.isdigit(str(power))):
        print(str(is_Power_of_x(int(num), int(power))))
    elif(str(num) == "" and str(power) == ""):
        ext = 1
    else:
        print("Must be a number")
    print("")
