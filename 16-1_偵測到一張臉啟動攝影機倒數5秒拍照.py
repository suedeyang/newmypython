# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:51:07 2020

@author: suedeyang
"""
import cv2
import time
from datetime import datetime



def face_add(img):
    print('later')

def face_who(img):
    print('later')



def face_shot(job):
    isCnt = False #是否正在倒數
    face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    capture=cv2.VideoCapture(0)
    while capture.isOpened():
        sucess,img=capture.read()
        if not sucess:
            print('擷取失敗')
            continue
        img_copy=img.copy()
        faces=face_detector.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5,minSize=(200,200))
        if len(faces) == 1:
            if isCnt == False:  #判斷要使用 ==
                t1=time.time()
                isCnt=True
            cnter=5-int(time.time()-t1)
            for (x,y,w,h) in faces:
                cv2.rectangle(img_copy,(x,y),(x+w,y+h),(0,255,255),2)
                cv2.putText(img_copy,str(cnter),(x+int(w/2),y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
            if cnter == 0:
                inCnt=False
                filename=datetime.now().strftime('%Y-%m-%d %H.%M.%S')
                cv2.imwrite(filename+'.jpg',img)
        else: 
            isCnt = False #沒偵測到臉或多於一張臉 停止倒數
        cv2.imshow('Frame',img_copy)
        k=cv2.waitKey(1)
        if k == ord('q') or k==ord('Q'):
            cv2.destroyAllWindows()
            capture.release()
            break
    else:
        print('Camera失敗')
    
face_shot('who')