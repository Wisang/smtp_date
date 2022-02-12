import smtplib

my_email = "testwisangeom@gmail.com"
my_password = "eomm9409"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr="testwisangeom@gmail.com",
        to_addrs="wisang.eom@lge.com",
        msg="Subject:from test google\n\nHello! This is the mail body!")
