# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:36:46 2020

@author: suedeyang
"""


import requests
import time
urls=['http://linux.lhps.kh.edu.tw/lib/','http://163.32.203.208/webpac700/']

while True:
    for url in urls:
        print(requests.get(url,verify=False).status_code)
        time.sleep(20)
        