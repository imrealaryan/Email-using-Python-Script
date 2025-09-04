import smtplib

email = "sender's mail ID"
receiver_email = "receiver's mail ID"
app_password = "app password generated from your sender's gmail account"

subject = "Testing"
message = "We are testing emails for devops job prep"

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
print(email,app_password)
server.login(email,app_password)
server.sendmail(email,receiver_email,text)

print("Email has been sent to :" + receiver_email)