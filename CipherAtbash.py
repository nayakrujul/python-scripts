cipher = {
  "A": "Z",
  "B": "Y",
  "C": "X",
  "D": "W",
  "E": "V",
  "F": "U",
  "G": "T",
  "H": "S",
  "I": "R",
  "J": "Q",
  "K": "P",
  "L": "O",
  "M": "N"
}

def atbash(s):

  s = s.upper()

  string = ""

  for c in s:

    if c in cipher.keys():

      string += cipher[c]
    
    elif c in cipher.values():

      string += list(cipher.keys())[list(cipher.values()).index(c)]
    
    else:

      string += c
  
  return string