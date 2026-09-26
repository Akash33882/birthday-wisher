##################### Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt
import os

birthday_file = pandas.read_csv("birthdays.csv")
birthdays_list = birthday_file.to_dict(orient="records")
birthday_dict = {}

for data in birthdays_list:
    birthday_dict[(data["month"], data["day"])] = data
print(birthday_dict)

date = dt.datetime.today()
today_day = date.day
today_month = date.month
friend_name = birthday_dict[(today_month, today_day)]["name"]
friend_email = str(birthday_dict[(today_month, today_day)]["email"])
print(friend_email)

entries = os.listdir("letter_templates")
files = [f for f in entries]
random_letter = str(random.choice(files))

with open(f"letter_templates\\{random_letter}") as text_file:
    text = text_file.read()
message = text.replace("[NAME]",friend_name)

if (today_month, today_day) in birthday_dict:
    my_email = "akashcn259@gmail.com"
    password = "dhrzfnzttmkrerux"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=friend_email,
        msg=f"subject:Happy Birthday\n\n {message}")
    connection.close()





