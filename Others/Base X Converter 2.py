print("Convert to binary (and base X)")

import sys

def toBinary():
  num = input("Enter the base 10 number: ")
  if str.isdigit(num):
    num_bin = bin(int(num))
    binary = ""
    for i in range((len(str(num_bin))-2)):
      binary += str(num_bin)[i+2]
    print(binary)
  else:
    sys.exit()

def toBaseX(base):
  num = input("Enter the base 10 number (max " + str(((base**5)-1)) + "): ")
  if str.isdigit(num):
    num = int(num)
    if num < base ** 5:

      num_list = [0, 0, 0, 0, 0]
      
      while num >= base ** 4:
        num -= base**4
        num_list[0] += 1
      
      while num >= base ** 3:
        num -= base**3
        num_list[1] += 1
      
      while num >= base ** 2:
        num -= base**2
        num_list[2] += 1
      
      while num >= base ** 1:
        num -= base**1
        num_list[3] += 1

      while num >= base ** 0:
        num -= base**0
        num_list[4] += 1

      total = ""
      for i in num_list:
        total += str(i)

      print(total)
      
    else:
      sys.exit()
  else:
    sys.exit()

base = input("Enter base: ")

if base.isdigit() == False:
  sys.exit()
elif int(base) == 2:
  toBinary()
else:
  toBaseX(int(base))