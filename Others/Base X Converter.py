import sys

print("\033[4mBinary (and base x) converter.\033[0m")
print("")

def baseXToBase10(base):
  baseX = input("Enter the base " + str(base) + " number: ")
  if str.isdigit(baseX) == False:
    sys.exit()
  length = len(str(baseX))
  total = 0
  for i in range(length):
    if int(str(baseX)[i]) < base:
      total += int(str(baseX)[i]) * (base ** (length - i - 1))
    else:
      sys.exit()
    # print(i, total)
  print(total)

base = input("Enter your base: ")
if str(base).isdigit():
  baseXToBase10(int(base))
else:
  sys.exit()