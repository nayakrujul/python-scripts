import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("rujulnayak@gmail.com", "Rujul@2009")

#Send the mail
msg = "Hello!"
# The /n separates the message from the headers
server.sendmail("rujulnayak@gmail.com", "nayakmanju@hotmail.com.com", msg)