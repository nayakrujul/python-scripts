def rot13(s):

  string = ""

  for c in s:

    if ord(c) >= ord("a") and ord(c) <= ord("z"):

      if ord(c) <= ord("m"):

        string += chr(ord(c) + 13)
      
      else:

        string += chr(ord(c) - 13)
    
    elif ord(c) >= ord("A") and ord(c) <= ord("Z"):

      if ord(c) <= ord("M"):

        string += chr(ord(c) + 13)
      
      else:

        string += chr(ord(c) - 13)

    else:

      string += c
  
  return string