# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:16:21 2020

@author: suedeyang
"""


import cv2,time
capture=cv2.VideoCapture(0)

if capture.isOpened() == True:
    while True:
        success,img=capture.read()
        if success:
            cv2.imshow('Frame',img)
            k=cv2.waitKey(10000) #超過時間回傳的keycode=-1 
            if k == ord('s') or k == ord('S'):
                file_time=time.strftime("%H%M%S")
                cv2.imwrite(f'{file_time}.jpg',img)
                print(f'{file_time}.jpg 影像儲存成功')
            if k == ord('q') or k == ord('Q'):
                print('結束')
                cv2.destroyAllWindows()
                capture.release()
                break
    
else:
    print('Camera Failure')