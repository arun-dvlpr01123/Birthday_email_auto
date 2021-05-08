import datetime as dt
import random, calendar
import smtplib

f = open("quotes.txt", "r")
quotes_list = f.readlines()
f.close()
today_quote = random.choice(quotes_list)
print(today_quote)

now = dt.datetime.now()
day_of_the_week = calendar.day_name[now.weekday()]

if day_of_the_week == "Saturday":
    my_email = "arun.dvlpr01123@gmail.com"
    password = "Muruga123#"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="textile.arun@gmail.com",
                        msg=f"Subject:{day_of_the_week}'s Quote\n\n{today_quote}")
    connection.close()
