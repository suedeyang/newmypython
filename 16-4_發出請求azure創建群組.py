# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:14:14 2020

@author: suedeyang
"""


import requests
base='https://yangface.cognitiveservices.azure.com/face/v1.0'
gp_url= base + '/persongroups/gp01'
key=''



headers_json={'Ocp-Apim-Subscription-Key': key ,'Contect-Type':'application/json'}
body={'name':'旗標公司','userData':'台北市'}
body=str(body).encode('utf-8')
response=requests.put(gp_url,headers=headers_json,data=body)
if response.status_code == '200':
    print('創建群組成功')
else:
    print('創建失敗',response.json())
    

