#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "your_email"
MY_PASSWORD = "your_password"
TARGET_MAIL = "target_email"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TARGET_MAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )