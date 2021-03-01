# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:57:51 2020

@author: suedeyang
"""


import requests
base='https://yangface.cognitiveservices.azure.com/face/v1.0'
pson_url= base + '/persongroups/gp01/persons'

key=''

headers_json={'Ocp-Apim-Subscription-Key': key ,'Contect-Type':'application/json'}
body={'name':'周詠','userData':'苗栗人'}
body=str(body).encode('utf-8')

response=requests.post(pson_url, headers=headers_json, data = body)


if response.status_code == 200:
    print('新增人員完成',response.json())
else:
    print('失敗',response.json())
    
