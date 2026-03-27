import smtplib
import datetime
import random
import pandas
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

def send_birthday_email(name, email_address):
    letter_to_use = f"letter_{random.randint(1,3)}.txt"

    with open("./letter_templates/" + letter_to_use, "r") as f:
        wish_text = f.read().replace("[NAME]", name)

    with smtplib.SMTP("smtp.163.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email_address,
            msg=f"Subject:Happy Birthday!\n\n{wish_text}"
        )

df = pandas.read_csv('birthdays.csv')
persons = df.to_dict(orient='records')
now = datetime.datetime.now()

for person in persons:
    if person['month'] == now.month and person['day'] == now.day:
        send_birthday_email(person['name'], person['email'])
