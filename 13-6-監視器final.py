# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:21:28 2020

@author: suedeyang
"""
import cv2
import smtplib
# from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from twilio.rest import Client

def send_sms(text,sid,token,us_phone,tw_phone):
    client=Client(sid,token)
    sms=client.messages.create(from_=us_phone,
                               to = tw_phone,
                               body=text)
    print("發送時間", sms.date_created) 
    
def send_gmail(gmail_addr,gmail_pwd,to_address,msg):
    smtp_gmail=smtplib.SMTP("smtp.gmail.com",587)
    print(smtp_gmail.ehlo())
    print(smtp_gmail.starttls())
    print(smtp_gmail.login(gmail_addr,gmail_pwd))
    status=smtp_gmail.sendmail(gmail_addr,to_address,msg)
    if not status:
        print("寄信成功")
    else:
        print("寄信失敗")
    smtp_gmail.quit()
        
def get_mime_img(subject,fr,to,img):
    img_encode=cv2.imencode('.jpg',img)[1]
    img_bytes=img_encode.tobytes()
    mime_img=MIMEImage(img_bytes)
    mime_img['Content-type']='application/octet-stream'
    mime_img['Content-Disposition']='attachment;filename="pic.jpg"'
    mime_img['Subject']=subject
    mime_img['From']=fr
    mime_img['To']=to
    return mime_img.as_string()

gmail_addr="suedeyang@gmail.com"
gmail_pwd="zkj7939A"
to_address="54suede@gmail.com"

sid=""
token=""
us_phone=""
tw_phone=""


cap=cv2.VideoCapture(0)
img_pre=None
while cap.isOpened():
    success,img=cap.read()
    if success:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_now=cv2.GaussianBlur(gray,(13,13),5)
        if img_pre is not None:
            diff = cv2.absdiff(img_now,img_pre)
            ret,thresh=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)
            contours,_=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                cv2.drawContours(img,contours,-1,(255,255,255),2)
                print('偵測到移動')
                msg=get_mime_img('小偷入侵','鷹眼防盜器','警察局',img)
                send_gmail(gmail_addr, gmail_pwd, to_address, msg)
                send_sms('小偷來了',sid,token,us_phone,tw_phone)
            else:
                print('靜止畫面')
        cv2.imshow("frame",img)
        img_pre=img_now.copy()
    k=cv2.waitKey(50)
    if k == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break