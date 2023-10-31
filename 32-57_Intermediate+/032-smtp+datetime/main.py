##################### Extra Hard Starting Project ######################
import os
import csv
import smtplib
import datetime as dt
import random

GMAIL = "emptypork@gmail.com"
PASSWORD = "okamuchajpxxfcxv"
NOW = dt.datetime.now()


def pick_letter(name):
    ltr_choice = random.choice(os.listdir("letter_templates"))
    with open(f"letter_templates\\{ltr_choice}", 'r') as ltr:
        letter = ltr.read()
    letter = letter.replace(f"[NAME]", f"{name}")
    return letter


def send_email(email, name, body):
    pass
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday {name}!\n\n"
                f"{body}"
        )


with open('birthdays.csv', 'r') as birthday_file:
    birthdays = csv.DictReader(birthday_file)
    for row in birthdays:
        if int(NOW.month) == int(row['month']) and int(NOW.day) == int(row['day']):
            email_body = pick_letter(row['name'])
            send_email(row['email'], row['name'], email_body)
