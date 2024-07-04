import datetime as dt
import smtplib, random
from email.message import EmailMessage

my_email = "100DaysOfPython32@gmail.com"
password = "mvrl gxqb jywx ibxk"

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

