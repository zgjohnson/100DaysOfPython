from pandas import *
import datetime as dt
from random import randint
import smtplib
from email.message import EmailMessage


# Extra Hard Starting Project #


def get_birthdays():
    now = dt.datetime.now()
    month = now.month
    day = now.day
    return read_csv("birthdays.csv").query(f'month == {month} and day == {day}')


def get_letter(name):
    with open(f'letter_templates/letter_{randint(1, 3)}.txt', mode='r') as letter_template:
        return letter_template.read().replace('[NAME]', name)


def generate_email(to_address, content):
    email = EmailMessage()
    email.set_content(content)
    email["Subject"] = 'Happy Birthday!!'
    email['From'] = MY_EMAIL
    email['To'] = to_address
    return email


MY_EMAIL = "100DaysOfPython32@gmail.com"
PASSWORD = "mvrl gxqb jywx ibxk"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthdays = get_birthdays()
if birthdays.empty:
    print('Sorry, no birthdays today.')

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
for x in birthdays.index:
    letter = get_letter(birthdays['name'][x])
    # 4. Send the letter generated in step 3 to that person's email address.
    message = generate_email(to_address=birthdays['email'][x], content=letter)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.send_message(message)


