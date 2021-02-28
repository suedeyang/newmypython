# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:12:23 2020

@author: suedeyang
"""

import requests
base='https://yangface.cognitiveservices.azure.com/face/v1.0'
key='51cc59e80c7345459a362a5328255b34'
headers_json={'Ocp-Apim-Subscription-Key': key ,'Contect-Type':'application/json'}


def person_list(gid):
    pson_url= base + f'/persongroups/{gid}/persons'
    response=requests.get(pson_url,headers=headers_json)
    if response.status_code == 200:
        print('查詢完成')
        return response.json()
    else:
        print('no man',response.json())

persons=person_list('gp01')
print(persons)