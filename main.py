# Check SMTP server for email provider and replace as necessary (Gmail currently)
# Check account settings with for email account to allow unsecure apps

import datetime as dt
from random import randint
import smtplib
import pandas

current_time = dt.datetime.now()
current_year = current_time.year
current_month = current_time.month
current_day = current_time.day

birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_records = birthdays_df.to_records()
birthday_days = birthdays_records["day"].tolist()

my_email = "REPLACE WITH EMAIL"
password = "REPLACE WITH PASSWORD TO EMAIL"

for person in birthdays_records:
    if person.day == current_day and person.month == current_month:

        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as birthday_letter:
            letter = birthday_letter.read()
            named_letter = letter.replace('[NAME]', person.name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=person.email, msg=named_letter)
