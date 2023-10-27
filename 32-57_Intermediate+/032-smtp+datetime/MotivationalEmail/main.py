import smtplib
import datetime as dt
import random

GMAIL = "emptypork@gmail.com"
YAHOO = "redshift@myyahoo.com"
PASSWORD = "okamuchajpxxfcxv"

now = dt.datetime.now()
# Used for testing on any day.
today = now.weekday()

if now.weekday() == today:
    with open("quotes.txt", "r") as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs=YAHOO,
            msg=f"Subject:{now.strftime('%A')} motivation!\n\n"
                f"{quote}"
        )
