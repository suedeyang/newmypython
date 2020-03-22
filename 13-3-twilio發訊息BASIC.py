# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:29:32 2020

@author: suedeyang
"""


from twilio.rest import Client

sid=""
token=''
us_phone=''
tw_phone=''

def send_sms(text,sid,token,us_phone,tw_phone):
    client=Client(sid,token)
    sms=client.messages.create(from_=us_phone,
                           to=tw_phone,
                           body=text)
    print(sms.date_created)

send_sms("注意，家中有人入侵",sid,token,us_phone,tw_phone)

