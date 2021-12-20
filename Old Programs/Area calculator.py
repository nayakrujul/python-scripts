shape = input("What shape do you want to find the area of (rectangle, triangle, circle)? ")

if(shape == "Rectangle"):
  rl = input("Please type the length in centimetres. ")
  rw = input("Please type the width in centimetres. ")
  rans = int(rl) * int(rw)
  print(str(rans) + "cm2")
elif(shape == "Triangle"):
  tb = input("Please type the base in centimetres. ")
  th = input("Please type the height in centimetres. ")
  tans = (int(tb) * int(th)) / 2
  print(str(tans) + "cm2")
elif(shape == "Circle"):
  cr = input("Please type the radius in centimetres. ")
  cans = int(cr) * 6.28
  print(str(cans) + "cm2")
else:
  shape = input("Please enter a valid shape. ")

# Go to https://repl.it/repls/PessimisticLivelyShoutcast
## Thank you