TABLE = {
  "cm": 1,
  "mt": 0.01,
  "km": 0.00001,
  "mm": 10,
  "in": 0.393701,
  "ft": 0.0328084,
  "yd": 0.0109361,
  "mi": 0.000006213693181818
}

def isdigit(s,allowFloat=False,allowNegative=False):
  digit = True
  digits = ["0","1","2","3","4","5","6","7","8","9"]
  if allowFloat:
    digits.append(".")
  if allowNegative:
    digits.append("-")
  for c in s:
    if c not in digits:
      digit = False
  return digit

def convert(s):

  s = s.replace(" ", "")

  if s.count("->") != 1:

    print("ERROR")
    return -1
  
  prev = s.split("->")[0]
  to = s.split("->")[1]

  if len(prev) < 3:

    print("ERROR")
    return -1
  
  num = prev[:-2]
  unit = prev[-2:]

  if not isdigit(num, True):

    print("ERROR")
    return -1
  
  num = float(num)

  if unit.lower() not in TABLE.keys():

    print("ERROR")
    return -1
  
  cm = num / TABLE[unit.lower()]

  if to.lower() not in TABLE.keys():
    print("ERROR")
    return -1
  
  print(str(round(float(cm) * TABLE[to.lower()], 4)), to)

print("Format your conversion like this:\n5cm -> in\nusing the abbreviations:\n")
for a in TABLE.keys():
  print(a)
conversion = input("(mt = metres)\n\nConvert ")

convert(conversion)