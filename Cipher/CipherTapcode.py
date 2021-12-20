grid = [
  ["A", "B", "C", "D", "E"],
  ["F", "G", "H", "I", "J"],
  ["L", "M", "N", "O", "P"],
  ["Q", "R", "S", "T", "U"],
  ["V", "W", "X", "Y", "Z"]
]

def encode(s):

  s = s.upper().replace("K", "C")

  lst = []

  string = ""

  for c in s:

    for row in range(len(grid)):

      if c in grid[row]:

        index = grid[row].index(c)
        break

    else:

      row = -1
      index = -1
  
    lst.append((row+1, index+1))
  
  for x, y in lst:

    string += x*"." + " " + y*"." + " / "
  
  return string

def decode(s):

  split = s.split(" / ")

  letters = []

  lst = []

  for letter in split:

    letters.append(letter.split(" "))
  
  for x in letters:

    if x[0] != "":

      lst.append(grid[x[0].count(".")-1][x[1].count(".")-1])
    
    else:

      lst.append(" ")
  
  return "".join(lst)