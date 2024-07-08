import datetime as dt
import random
import smtplib
from email.message import EmailMessage
from Config import email_config

my_email = email_config.MY_EMAIL
password = email_config.PASSWORD

if dt.datetime.now().weekday() == 0:
    with open('quotes.txt') as quote_file:
        quotes = quote_file.readlines()

    message = EmailMessage()
    message.set_content(random.choice(quotes))
    message["Subject"] = 'Monday Motivation'
    message['From'] = my_email
    message['To'] = 'zgjohnson94@gmail.com'

    with smtplib.SMTP("smtp.gmail.com", 587) as email:
        email.starttls()
        email.login(user=my_email, password=password)
        email.send_message(message)

