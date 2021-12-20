print("Welcome to the Magic 8 ball")

messages = [
  "It is certain."
, "It is decidedly so."
, "Without a doubt."
, "Yes - definitely."
, "You may rely on it."
, "As I see it, yes."
, "Most likely."
, "Outlook good."
, "Yes."
, "Signs point to yes."
, "Reply hazy, try again."
, "Ask again later."
, "Better not tell you now."
, "Cannot predict now."
, "Concentrate and ask again."
, "Don't count on it."
, "My reply is no."
, "My sources say no."
, "Outlook not so good."
, "Very doubtful."]


question = input("Please enter your question. Please remember that it has to be a yes/no question.")

while (len(question) != 0):

    import random
    for x in range(1):
        val = random.randint(0,19)

    print(messages[val])

    question = input("Please enter your next question. Press key enter to exit. ")

print("End of the game")