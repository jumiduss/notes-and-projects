import smtplib

my_email = "ploperdop1@gmail.com"
my_password = "SHUTUPGOOGLE"
connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()

connection.login(user=my_email,password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="dontneedmynam@yahoo.com", msg="SHUTUP")
connection.close()