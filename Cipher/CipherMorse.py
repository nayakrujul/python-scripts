codes = open("CipherMorse.csv")
morse_split = codes.read().split("\n")
morse = []
for i in morse_split:
  morse.append(i.split(","))
codes.close()

def encode(s):

  s = s.upper()

  string = ""

  for c in s:

    for x in morse:

      if c in x:

        string += x[1] + " "

        break
    
    else:

      return False
  
  return string

def decode(s):

  string = ""

  for c in s.split():

    for x in morse:

      if c in x:

        string += x[0] + ""

        break
    
    else:

      return False
  
  return string