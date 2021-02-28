# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:21:54 2020

@author: suedeyang
"""


import requests
base='https://yangface.cognitiveservices.azure.com/face/v1.0'
gp_url= base + '/persongroups/gp01'
key=''



headers={'Ocp-Apim-Subscription-Key': key}
response=requests.get(gp_url,headers=headers)


if response.status_code == 200:
    print(response.json())
    
else:
    print('查詢失敗',response.json())