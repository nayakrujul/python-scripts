import random, string

class CandyCrush:

  def __init__(self, size=10):

    self.board = []
    for x in range(size):

      self.board.append([])
      for y in range(size):

        self.board[x].append(random.choice(["\033[1;31mR\033[1;0m","\033[1;32mG\033[1;0m","\033[1;34mB\033[1;0m","\033[1;33mY\033[1;0m","W"]))
  
  def display(self):
    
    letters = string.ascii_uppercase
    print("   ", end="|")
    for a in range(len(self.board)):
      print("", letters[a], end=" |")
    print("")

    print("   " + len(self.board)*"| - " + "|")
    for x in range(len(self.board)):
      print(str(x+1).zfill(2), end=" ")

      for y in self.board[x]:
        print("|", y, end=" ")

      print("|")
      print("   " + len(self.board)*"| - " + "|")
  
  def check_lines(self):

    lst = []

    for x in range(len(self.board)):
      
      last = ""
      count = 1

      for y in range(len(self.board[x])):

        if self.board[x][y] == last:
          count += 1

          if count == 3:
            lst.append("")
            lst.append((x,y-2))
            lst.append((x,y-1))
            lst.append((x,y))

          elif count > 3:
            lst.append((x,y))
        else:
          last = self.board[x][y]
          count = 1
    
    lst.append(" ")

    for a in range(len(self.board)):
      
      last = ""
      count = 1

      for b in range(len(self.board[a])):

        if self.board[b][a] == last:
          count += 1

          if count == 3:
            lst.append("")
            lst.append((b-2,a))
            lst.append((b-1,a))
            lst.append((b,a))
            
          elif count > 3:
            lst.append((b,a))
        else:
          last = self.board[b][a]
          count = 1

    return lst
  
  def humanise(self):

    lines = self.check_lines()
    letters = string.ascii_uppercase

    lst = [[[]],[[]]]

    for x in lines[1:lines.index(' ')]:

      if type(x) == type(tuple()):

        lst[0][-1].append(letters[x[1]] + str(x[0]+1))
      
      else:

        lst[0].append([])
    
    for y in lines[lines.index(' ')+1:]:

      if type(y) == type(tuple()):

        lst[1][-1].append(letters[y[1]] + str(y[0]+1))
      
      else:

        lst[1].append([])
    
    return lst
  
  def display_lines(self):

    lines = self.humanise()

    print("Horizontal:\n")
    for i in lines[0]:
      for j in i:
        print(j, end=" ")
      print("")
    
    print("\n\nVertical:")
    for k in lines[1]:
      for l in k:
        print(l, end=" ")
      print("")

board = CandyCrush(26)
board.display()
print("\n")
board.display_lines()