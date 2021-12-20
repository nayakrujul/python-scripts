from random import choice
from os import system

print("Welcome to the Leadership Calculator. How good are your leadership skills?\nSource: www.mindtools.com\n")

a = (0,1,2,3,4,5,6,7,8,9,10) # Questions where '10' is the best
b = (10,9,8,7,6,5,4,3,2,1,0) # Questions where '0' is the best

q_dict = {
  "When assigning tasks, I consider people's skills and interests. ": a,
  "I doubt myself and my ability to succeed. ": b,
  "I expect nothing less than top-notch results from people. ": a,
  "I expect my people to work harder than I do.	": b,
  "When someone is upset, I try to understand how he or she is feeling.	": a,
  "When circumstances change, I can struggle to know what to do.	": b,
  "I think that personal feelings shouldn't be allowed to get in the way of performance and productivity.	": b,
  "I am highly motivated because I know I have what it takes to be successful.	": a,
  "Time spent worrying about team morale is time that's wasted.	": b,
  "I get upset and worried quite often in the workplace.	": b,
  "My actions show people what I want from them.	": a,
  "When working with a team, I encourage everyone to work toward the same overall objectives.	": a,
  "I make exceptions to my rules and expectations. It's easier than being the enforcer all the time!	": b,
  "I enjoy planning for the future.	": a,
  "I feel threatened when someone criticizes me.	": b,
  "I make time to learn what people need from me, so that they can be successful.	": a,
  "I'm optimistic about life, and I can see beyond temporary setbacks and problems.	": a,
  "I think that teams perform best when individuals keep doing the same tasks and perfecting them, instead of learning new skills and challenging themselves.	": b
}

q_list = list(q_dict.keys())

input("Press ENTER to start. ")

score = 0

for x in range(len(q_list)):

  system('clear')

  question = choice(q_list)
  q_list.remove(question)
  scores = q_dict[question]

  loop = True
  while loop:

    answer = input(f"Question {x+1} of 18:\n\nTo what extent (0 to 10, with 0 being 'Not at all' and 10 being 'Completely') do you agree with the following statement?\n{question}\n")

    if answer.isdigit():

      answer = int(answer)
      if answer <= 10:

        loop = False

        score += scores[answer]

system('clear')
print(f"Your final score: {score} / 180 ({round(score/1.8,1)}%)")