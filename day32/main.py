import pandas as pd
import datetime as dt
import random 
import smtplib

data=pd.read_csv("birthdays.csv")
date=dt.datetime.now()
today_bd_list=[]

for row in data.iterrows():
  birth_day=f"""{row[1]["month"]}-{row[1]["day"]}"""
  today_date=f"""{date.month}-{date.day}"""
  if birth_day == today_date:
    today_bd_list.append(row[1])

def send_mail(resever,msg):
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login("deviddevid287@gmail.com","xxxxxx")
    connection.sendmail(from_addr="deviddevid287@gmail.com",to_addrs=resever,msg=msg)

for person in today_bd_list:
  file_name=f"letter_templates/letter_{random.randint(1,3)}.txt"
  with open(file_name,"r") as file:
    letter = file.read()
  letter = letter.replace("[NAME]",person["name"])
  letter = letter.replace("[YEAR]",f"""{int(date.year) - int(person["year"])}""")
  massage=f"Subject:Happy birthday\n\n{letter}"
  send_mail(person["year"],massage)




