import smtplib
import datetime as dt
from random import choice

my_email = "testwisangeom@gmail.com"
my_password = "eomm9409"
quotes = []


def send_mail(mail_body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr="testwisangeom@gmail.com",
            to_addrs="testwisangeom@yahoo.com",
            msg=f"Subject:Python Exercise\n\n{mail_body}")


with open("quotes.txt", 'r') as quotes_file:
    quotes = quotes_file.readlines()


def get_quotes():
    return choice(quotes)


now = dt.datetime.now()
today = now.weekday()

if now.weekday() == today:
    send_mail(get_quotes())
