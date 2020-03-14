# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:44:46 2020

@author: suedeyang
"""


import smtplib
import cv2
from email.mime.image import MIMEImage

def send_gmail(gmail_addr,gmail_pwd,to_addr,msg):
    gmail_smtp=smtplib.SMTP('smtp.gmail.com',587)
    print(gmail_smtp.ehlo())
    print(gmail_smtp.starttls())
    print(gmail_smtp.login(gmail_addr,gmail_pwd))
    status=gmail_smtp.sendmail(gmail_addr,to_addr,msg)
    if not status:
        print('寄信成功')
    else:
        print('寄信有問題')
    gmail_smtp.quit()

def get_mime_img(subject,fr,to,img):
    img_encode=cv2.imencode('.jpg',img)[1] 
    img_bytes=img_encode.tobytes()
    mime_img=MIMEImage(img_bytes)
    mime_img['Content-type']='application/octect-stream'
    mime_img['Content-Dispostion']='attachment;filename="pic.jpg"'
    mime_img['Subject']=subject
    mime_img['From']=fr
    mime_img['to']=to
    return mime_img.as_string()

gmail_addr=''
gmail_pwd=''
to_addr=''

cap=cv2.VideoCapture(0)
while cap.isOpened():
    success,img=cap.read()
    if success:
        cv2.imshow('frame',img)
        k=cv2.waitKey(1)
        if k == ord('s') or k == ord('S'):
            msg=get_mime_img("小偷入侵","鷹眼防盜器",'經查局',img)
            send_gmail(gmail_addr,gmail_pwd,to_addr,msg)
            cap.release
            cv2.destroyAllWindows()
            break

    