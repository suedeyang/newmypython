# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 21:55:51 2020

@author: suedeyang
"""


import license_module as m
import cv2

capture=cv2.VideoCapture(0)
if capture.isOpened():
    while True:
        success,img=capture.read()
        if success:
            cv2.imshow("Frame",img)
        k=cv2.waitKey(50)
        if k == ord('s') or k == ord('S'):
            cv2.imwrite('shot.jpg',img)
            text=m.get_license(img)
            print("車牌:",text)
        if k == ord('q') or k == ord('Q'):
             print('離開')
             capture.release()
             cv2.destroyAllWindows()
             break
else:
    print('攝影機沒開啟')