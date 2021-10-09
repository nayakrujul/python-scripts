import cmath, math

def SINE(x):
  return cmath.sin(math.radians(x)).real
def COSINE(x):
  return cmath.cos(math.radians(x)).real
def TANGENT(x):
  return cmath.tan(math.radians(x)).real

def ARCSINE(o,h):
  return math.degrees(cmath.asin(o/h).real)
def ARCCOSINE(a,h):
  return math.degrees(cmath.acos(a/h).real)
def ARCTANGENT(o,a):
  return math.degrees(cmath.atan(o/a).real)

def isdigit(s,allowFloat=False,allowNegative=False):
  if type(s) != type("abc"):
    return False
  digit = True
  digits = ["0","1","2","3","4","5","6","7","8","9"]
  if allowFloat:
    digits.append(".")
  if allowNegative:
    digits.append("-")
  if len(s) == 0:
    return False
  for c in s:
    if c not in digits:
      digit = False
  return digit

def check(x,y=-1):
  if isdigit(x, True):
    x = float(x)
    if y > 0:
      if x <= y and x > 0:
        return x
    else:
      if x > 0:
        return x
  return False
  
def GET_SINE_1_INPUTS():
  o = input("O. = ")
  x = input("x  = ")
  o = check(o,-1)
  x = check(x,-1)
  if o != False and x != False:
    # o/h = sin(x)
    sin = SINE(x)
    # h * sin(x) = o
    # h = o / sin(x)
    return o / sin
def GET_SINE_2_INPUTS():
  h = input("H. = ")
  x = input("x  = ")
  h = check(h,-1)
  x = check(x,-1)
  if h != False and x != False:
    # o/h = sin(x)
    sin = SINE(x)
    # o = h * sin(x)
    return h * sin

def GET_COSINE_1_INPUTS():
  a = input("A. = ")
  x = input("x  = ")
  a = check(a,-1)
  x = check(x,-1)
  if a != False and x != False:
    # a/h = cos(x)
    cos = COSINE(x)
    # h * cos(x) = a
    # h = a / sin(x)
    return a / cos
def GET_COSINE_2_INPUTS():
  h = input("H. = ")
  x = input("x  = ")
  h = check(h,-1)
  x = check(x,-1)
  if h != False and x != False:
    # a/h = cos(x)
    cos = COSINE(x)
    # a = h * cos(x)
    return h * cos

def GET_TANGENT_1_INPUTS():
  o = input("O. = ")
  x = input("x  = ")
  o = check(o,-1)
  x = check(x,-1)
  if o != False and x != False:
    # o/a = tan(x)
    tan = TANGENT(x)
    # a * tan(x) = o
    # a = o / tan(x)
    return o / tan
def GET_TANGENT_2_INPUTS():
  a = input("A. = ")
  x = input("x  = ")
  a = check(a,-1)
  x = check(x,-1)
  if a != False and x != False:
    # o/a = tan(x)
    tan = TANGENT(x)
    # o = a * tan(x)
    return a * tan

def GET_ARCSINE_INPUTS():
  o = input("O. = ")
  h = input("H. = ")
  o = check(o,-1)
  h = check(h,-1)
  if o != False and h != False:
    return ARCSINE(o,h)
def GET_ARCCOSINE_INPUTS():
  a = input("A. = ")
  h = input("H. = ")
  a = check(a,-1)
  h = check(h,-1)
  if a != False and h != False:
    return ARCCOSINE(a,h)
def GET_ARCTANGENT_INPUTS():
  o = input("O. = ")
  a = input("A. = ")
  o = check(o,-1)
  a = check(a,-1)
  if o != False and a != False:
    return ARCTANGENT(o,a)

def PYTHAGORAS_1():
  x = input("O. = ")
  y = input("A. = ")
  x = check(x,-1)
  y = check(y,-1)
  if x != False and y != False:
    return math.sqrt(x**2 + y**2)
def PYTHAGORAS_2():
  x = input("O. = ")
  y = input("H. = ")
  x = check(x,-1)
  y = check(y,-1)
  if x != False and y != False:
    return math.sqrt(y**2 - x**2)
def PYTHAGORAS_3():
  x = input("A. = ")
  y = input("H. = ")
  x = check(x,-1)
  y = check(y,-1)
  if x != False and y != False:
    return math.sqrt(y**2 - x**2)

def GET_INPUT():
  print("This is your triangle:\n\n\n      |\ \n      | \ \n      |  \ \n   O. |   \ H.\n      |_   \ \n      |_| _ \ <-- x\n         A.\n")
  print("""
Key:

x  = angle of interest
A. = Adjacent Side
O. = Opposite Side
H. = Hypotenuse

  """)
  sides = input("Enter two side lengths (for angle) OR one side length and one angle OR two side lengths (for side length):\n\n[1] O. and H. (Solve for x)\n[2] A. and H. (Solve for x)\n[3] O. and A. (Solve for x)\n[4] O. and x (Solve for A.)\n[5] O. and x (Solve for H.)\n[6] A. and x (Solve for O.)\n[7] A. and x (Solve for H.)\n[8] H. and x (Solve for O.)\n[9] H. and x (Solve for A.)\n[10] O. and A. (Solve for H.)\n[11] O. and H. (Solve for A.)\n[12] A. and H. (Solve for O.)\n\n > ")
  num = check(sides)
  print()
  if num == False:
    return False
  if num == 1:
    return GET_ARCSINE_INPUTS()
  if num == 2:
    return GET_ARCCOSINE_INPUTS()
  if num == 3:
    return GET_ARCTANGENT_INPUTS()
  if num == 4:
    return GET_TANGENT_1_INPUTS()
  if num == 5:
    return GET_SINE_1_INPUTS()
  if num == 6:
    return GET_TANGENT_2_INPUTS()
  if num == 7:
    return GET_COSINE_1_INPUTS()
  if num == 8:
    return GET_SINE_2_INPUTS()
  if num == 9:
    return GET_COSINE_2_INPUTS()
  if num == 10:
    return PYTHAGORAS_1()
  if num == 11:
    return PYTHAGORAS_2()
  if num == 12:
    return PYTHAGORAS_3()

print("\nAnswer:", GET_INPUT())