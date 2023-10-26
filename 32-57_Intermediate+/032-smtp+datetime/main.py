import smtplib

GMAIL = "emptypork@gmail.com"
YAHOO = "redshift@myyahoo.com"
PASSWORD = "okamuchajpxxfcxv"


connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=GMAIL, password=PASSWORD)
connection.sendmail(from_addr=GMAIL, to_addrs=YAHOO, msg="Hello Yahoo!")
connection.close()
