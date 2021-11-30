from FormatNum import format_num, estimate

print("Model Pascal's Triangle\n")

rows = input("Rows: ")

def PascalTriangle(n):
   ret = []
   trow = [1]
   y = [0]
   for x in range(n):
      ret.append(trow)
      trow=[left+right for left,right in zip(trow+y, y+trow)]
   return ret

print("\n")

try:
  rows = int(rows)
except:
  print("Default: 5\n")
  rows = 5

if rows > 12:
  print("Limited to 12\n")
  rows = 12

row = 1

nums = PascalTriangle(rows)

spaces = {
  1: [1,1],
  2: [0,1],
  3: [0,0]
}

print((rows - 1) * "  " + "-----")
while row <= rows:
  print((rows - row) * "  ", end="")
  for i in range(len(nums[row-1])):
    num = str(nums[row-1][i])
    print("|" + spaces[len(num)][0] * " " + num + spaces[len(num)][1] * " ", end="")
  print("|" + (rows - row) * "  " + " (11^" + str(row - 1) + ") =", format_num(11 ** (row - 1)), estimate(11 ** (row - 1)))
  if row < rows:
    print((rows - row - 1) * "  " + (row + 1) * "----" + "-")
  else:
    print((rows - row - 1) * "  " + row * "----" + "-")
  row += 1