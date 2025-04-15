##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "your_email"
MY_PASSWORD = "your_password"
TARGET_EMAIL = "their_email"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birtdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows}

if today in birtdays_dict:
    celebrated_person = birtdays_dict[today]
    file_path = f"letter_template/letter_{random.ranint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", celebrated_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TARGET_EMAIL,
            msg = f"Subject:Happy Birthday!\n\n{content}"
        )
        