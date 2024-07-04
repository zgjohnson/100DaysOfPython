# import smtplib
# from email.message import EmailMessage
#
# my_email = "100DaysOfPython32@gmail.com"
# password = "mvrl gxqb jywx ibxk"
#
# message = EmailMessage()
# message.set_content('This is the body of my email.')
# message["Subject"] = 'Hello'
# message['From'] = my_email
# message['To'] = 'zgjohnson94@gmail.com'
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.send_message(message)

import datetime as dt

now = dt.datetime.now()
year = now.year
print()
