# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 22:25:21 2020

@author: suedeyang
"""


import cv2

capture=cv2.VideoCapture(0)

while True:
    success,img=capture.read()
    cv2.imshow("Frame",img)
    k=cv2.waitKey(100)
    if k == ord('q'):
        capture.release()
        cv2.destroyAllWindows()
        break