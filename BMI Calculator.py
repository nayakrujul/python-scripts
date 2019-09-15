print("")

testlist = [1, 2, 3]

def test():
  testlist.append(4)
  print(testlist)

test()

print("")

print("-------------------------------------")

print("")

name = input('What is your name? ')
print("Welcome " + name + ". This is your Python world.")
age = int(input('How old are you? ')) 

if age < 12:
  print("You are still at primary school.")
elif age < 18:
  print("You are still in secondary school.")
elif age < 23:
  print("You are in college / university.")
elif age < 50:
  print("You've still got over half your life remaining.")
else:
  print("You are an old man / woman.")

height = float(input('What is your height in metres? '))

weight = float(input('What is your weight in kilograms? '))

bmi = 0

bmi = float(weight) / (float(height) * float(height))

print("Your BMI is " + str(bmi))

if bmi < 18:
  print("You are underweight.")
elif bmi < 25:
  print("You are healthy.")
elif bmi < 30:
  print("You are overweight.")
else:
  print("You are obese")

# Go to https://repl.it/repls/VividLittleOutlier (Command + Click)
## Thank you