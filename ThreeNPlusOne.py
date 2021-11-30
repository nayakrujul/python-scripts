def three_n_plus_one(num):

  if num < 5:

    return [[],0]

  lst = [num]

  counter = 10000

  one_counter = 0

  while counter > 0:

    if num % 2 == 1:
      num = (3 * num) + 1
    else:
      num = num // 2

    lst.append(num)

    if num == 1:
      one_counter += 1

      if one_counter >= 2:
        break

    counter -= 1

  return [lst, len(lst)-3]

print("42:", three_n_plus_one(42)[0], "\ntakes", three_n_plus_one(42)[1], "numbers to get back to 1.\n")

print("1403:", three_n_plus_one(1403)[0], "\ntakes", three_n_plus_one(1403)[1], "numbers to get back to 1.\n")

highest = [[],1,0]

for i in range(5,100):

  if three_n_plus_one(i)[1] > highest[2]:

    highest = [three_n_plus_one(i)[0], i, three_n_plus_one(i)[1]]
  
print(f"The longest sequence for a starting number below 100 is {highest[1]}:\n{highest[0]}\n{highest[2]} numbers to get back to 1")