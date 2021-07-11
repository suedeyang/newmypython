import pandas as pd
import smtplib

SendAddress=""
password=""

e=pd.read_excel("email.xlsx") #放在同個目錄下
emails=e.values

server=smtplib.SMTP("smtp.gmail.com",587) #gmail安全性需要去調整
server.starttls()
server.login(SendAddress,password)
msg="Hello"
subject="This is a email"

for email in emails:
    body=f'Subject:{subject} {msg} {email[0]}\n{email[1]}' #\n後面是信件內容
    server.sendmail(SendAddress,email[0],body)
server.quit()
