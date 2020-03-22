# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:50:40 2020

@author: suedeyang
"""


import cv2
cap=cv2.VideoCapture(0)
img_pre=None
while cap.isOpened():
    success,img=cap.read()
    if success:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰階處理
        img_now=cv2.GaussianBlur(gray,(13,13),15) #高斯模糊
        if img_pre is not None:  #避免沒有pre_img卡住
            diff=cv2.absdiff(img_now,img_pre)
            cv2.imshow("frame",diff)
        img_pre=img_now.copy()
    k=cv2.waitKey(30)
    if k==ord('q'):
        cv2.destroyAllWindows()
        cap.release
        break