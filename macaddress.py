# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:46:19 2020

@author: YANGS
"""

import socket,getmac,requests,time
class_name=''
reasonable_year=[1,2,3,4,5,6]
while True:
    class_name=input("請用3位數字輸入您的班級 例：五年一班請輸入501(輸入完畢請按ENTER):")
    if class_name == "":
        print("你忘記輸入資料")
        continue
    if class_name.isdigit() == False:
        print("請以阿拉伯數字輸入")
        continue
    if len(class_name) != 3:
        print("3位數字喔!!")
        continue
    if int(class_name[0]) ==2:
        if int(class_name[1:]) > 16:
            print("這個年段有這麼多班嗎?")
            continue
    if int(class_name[0]) <=6 and int(class_name[0]) != 2 and int(class_name[0]) != 0 :
        if int(class_name[1:]) > 14:
                print("這個年段有這麼多班嗎?")
                continue
    if int(class_name[0]) > 6 or int(class_name[0]) == 0:
        print("年級有誤")
        continue
    else:
        print("工作結束")
        time.sleep(1)
        break

macadd=getmac.get_mac_address()
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)

def send_ifttt(v1,v2,v3):
    url='https://maker.ifttt.com/trigger/toline/with/key/1WjdQ89uBOKzhnQYsDtLg'+'?value1='+str(v1)+'&value2='+str(v2)+'&value3='+str(v3)
    r=requests.get(url)
    if r.text[:4]=="Cong":
        print(f'{class_name[0]}年{class_name[1:]}班的mac資料{macadd}已傳送完畢 感謝您的協助 視窗將會自動關閉')

send_ifttt(class_name,macadd,hostname)
time.sleep(5)