# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:57:55 2020

@author: suedeyang
"""


import cv2,time,re,requests

base="https://computer-vision-python.cognitiveservices.azure.com/"
recog_url=f'{base}vision/v2.0/recognizeText?mode=Printed'
key=""
headers={'Ocp-Apim-Subscription-Key':key}
headers_stream={'Ocp-Apim-Subscription-Key':key,'Content-Type':'application/octet-stream'}


def get_license(img):
    img_encode=cv2.imencode('.jpg',img)[1] #編碼存在記憶體中 [0]表示成功與否的布林值 [1]是暫存區的影像資料
    img_bytes=img_encode.tobytes() #轉換為byte物件 透過POST傳送
    r1=requests.post(recog_url,headers=headers_stream,data=img_bytes)
    if r1.status_code != 202:  #202代表接受請求
        print(r1.json())
        return '請求失敗'
    result_url=r1.headers['Operation-Location'] 
    r2=requests.get(result_url,headers=headers) #索取辨識的結果
    while r2.status_code == 200 and r2.json()['status'] != 'Succeeded':
        r2=requests.get(result_url,headers=headers)
        time.sleep(0.5)
        print('status:',r2.json()['status'])
    carcard=''
    lines=r2.json()['recognitionResult']['lines']
    for i in range(len(lines)):
        text=lines[i]['text']
        m=re.match(r'^[\w]{2,4}[-. ][\w]{2,4}$', text)
        if m != None:
            carcard=m.group()
            return carcard
    if carcard == '':
        return '找不到車牌'
    
try:
    img=cv2.imread('15402836187765.jpeg')
    print('status:start')
    text=get_license(img)
    print('車牌',text)
    cv2.imshow('Frame',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except :
    print('圖片讀取失敗')
    
        
    