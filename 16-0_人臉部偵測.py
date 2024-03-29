# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:57:17 2020

@author: suedeyang
"""

import cv2

face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture=cv2.VideoCapture(0)
while capture.isOpened():
    success,img=capture.read()
    if success:
        faces=face_detector.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5,minSize=(200,200))
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.imshow('Frame',img)
    k =cv2.waitKey(1)
    if k == ord('q') or k == ord('Q'):
        print('exit')
        cv2.destroyAllWindows()
        capture.release()
        break
else:
    print('camera fail')