from guizero import App, Text, TextBox, PushButton
import os, random, sys, threading, time

def question(level):
  os.system('clear')

  global num1
  global num2
  global op

  if level == 1:
    num1 = random.randint(1,20)
    op = random.choice([" + ", " - "])
    if op == " - ":
      num2 = random.randint(1,num1)
    else:
      num2 = random.randint(1,20)
  elif level == 2:
    num1 = random.randint(10,25)
    op = random.choice([" + ", " - ", " x "])
    if op == " - ":
      num2 = random.randint(10,num1)
    else:
      num2 = random.randint(10,25)
  elif level == 3:
    num1 = random.randint(20,50)
    op = random.choice([" + ", " - ", " x "])
    if op == " - ":
      num2 = random.randint(20,num1)
    else:
      num2 = random.randint(20,50)

  questionText.value = str(num1) + op + str(num2)

def submit():
  os.system('clear')
  
  if op == " + ":
    answer = num1 + num2
  elif op == " - ":
    answer = num1 - num2
  elif op == " x ":
    answer = num1 * num2

  if str(answerText.value) == str(answer):
    correctWrong.value = "Correct."
    answerText.value = ""
    question(level)
  else:
    correctWrong.value = "Wrong."
    #print(counter, "seconds")
    sys.exit()

def Insane():

  os.system('clear')

  global score

  if correctWrong.value == "Correct.":
    score += 1

  global num1
  global num2

  num1 = random.randint(10,99)
  op = " x "
  num2 = random.randint(10,99)

  questionText.value = str(num1) + op + str(num2)


def InsaneSubmit():
  os.system('clear')

  answer = num1 * num2

  if answerText.value == str(answer):

    correctWrong.value = "Correct."

  else:

    correctWrong.value = "Wrong."

  answerText.value = ""

  Insane()

def submit_choice():
  if str(level) in "123":
    submit()
  else:
    InsaneSubmit()

def timer():
  global counter
  counter = 30
  while counter > 0:
    time.sleep(0.1)
    counter -= 0.1
  questionText.value = "Time up! You got " + str(score) + "!"
  answerText.hide()
  correctWrong.hide()
  submitButton.hide()


app = App("Test your Maths skills!")

questionText = Text(app, text="Choose a level", size="30")
Text(app, text="")
Text(app, text="")
correctWrong = Text(app, text="")

level = str(input("[1] Easy\n[2] Medium\n[3] Hard\n[4] Insane\n > "))
if "1" in level:
  level = 1
elif "2" in level:
  level = 2
elif "3" in level:
  level = 3
elif "4" in level:
  level = 4
  myThread = threading.Thread(target=timer)
  myThread.start()
  score = 0
  Insane()
else:
  level = random.randint(1,3)

print("You chose level", level)

answerText = TextBox(app, "")
submitButton = PushButton(app, submit_choice, text="Submit")
Text(app, text="")
correctWrong = Text(app, text="")

if str(level) in "123":
  question(level)

app.display()