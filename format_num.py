def format_num(num, sepChar=",", chars=3):

  # Raise error if the argument is not in the desired format
  if not str(num).isdigit():
    raise ValueError

  try:

    if chars == 0:

      raise ValueError
  
  except Exception:

    raise ValueError

  s = str(num)

  new = ""

  # Reverse the string

  for c in range(1, len(s)+1):

    new += s[-c]

  sep = ""

  # Reverse the separator

  for m in range(1, len(sepChar)+1):

      sep += sepChar[-m]

  final = ""

  # Loop through the reversed string and add separators to every third character

  for i in range(len(new)):

    if i % chars == 0 and i != 0:

      final += sep + new[i]

    else:

      final += new[i]

  returnstr = ""

  # Reverse the full string and return

  for x in range(1, len(final) + 1):

    returnstr += final[-x]

  return returnstr

def estimate(num):

  # Raise error if the argument is not in the desired format
  if not str(num).isdigit():
    raise ValueError

  s = str(num)
  num = int(num)

  digits = {
    13: [1, " trillion"],
    12: [100, " billion"],
    11: [10, " billion"],
    10: [1, " billion"],
    9: [100, " million"],
    8: [10, " million"],
    7: [1, " million"],
    6: [100, " thousand"],
    5: [10, " thousand"],
    4: [1, " thousand"],
  }

  for i in digits.keys():
    if len(s) >= i:
      ext = digits[i]
      break
  else:
    return ""
  
  return "(~" + str(round(((num/(10**(len(s)-1))) * ext[0]), 1)) + ext[1] + ")"