print("")
print("Welcome to TextSend.")
print("TextSend is an RN corporation and is registered under the name of RN TextSend Corporations Ltd.")
print("")
TSContacts = open("TextSend_Contacts.txt", "r")
for Contact in TSContacts:
  split = Contact.split(" @ ")
  counter = 0
  display = ""
  for ele in split:
    detail = ele.strip()
    if(counter == 0):
        display = display + "The contact " + detail
    elif(counter == 1):
        display = display + "'s phone number is " + detail
    counter = counter + 1
  print(display)

print("")
quit_count = 0
message_count = 0
cost = float(0)
while(quit_count == 0):
    message = raw_input("Please enter your message. Each message will cost 1 pence per character. Enter a blank message to quit. ")
    if(message != "" and (message_count + 1) < 10):
        cost = cost + (len(message) * 0.01)
        message_count = message_count + 1
        filename = "TS_Messages_" + str(message_count) + ".txt"
        with open (filename, "w") as f:
            f.write (message)

    elif((message_count + 1) == 10):
        message_count = message_count + 1
        cost = cost + 0.01
        print("Your last message wasn't delivered. ")

    else:
        quit_count = 1

if(message_count != 0):
    print("You entered " + str(message_count) + " messages and " + str((int(round(cost, 2) * 100))) + " characters. Please pay " + str(round(cost, 2)) + " GBP.")
    card = raw_input("Please enter card number. ")
    print("")
    if(len(card) == 16):
        print("Error. Stolen card. Transaction disapproved.")
    else:
        print("Error. Invalid card. Transaction disapproved.")
print("")
print("Goodbye. We hope you had a good time at TextSend.")
print("")

