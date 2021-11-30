vowels = ("a", "e", "i", "o", "u")

def encode(s):

  s = s.lower()

  string = ""

  for word in s.split():

    if word[0].lower() in vowels:

      string += word + "way "
    
    else:

      string += word[1:] + word[0] + "ay "

  return string