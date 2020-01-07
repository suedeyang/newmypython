# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:29:40 2020

@author: YANGS
"""
import twstock
import requests
import time

def get_setting():
    try:
        res=[]
        with open("stock.txt") as f:
            lists=f.readlines()
            print("讀入資料:",lists)
            for lst in lists:
                s=lst.split(',')
                res.append([s[0],float(s[1]),float(s[2])])
    except:
        print("讀取資料有誤")
    return(res)


def get_price(stockid):
    rt=twstock.realtime.get(stockid)
    if rt['success']:
        return (rt['info']['name'],float(rt['realtime']['latest_trade_price']))
    else:
        return(False,False)
    
def get_best(stockid):
    stock=twstock.Stock(stockid)
    bp=twstock.BestFourPoint(stock).best_four_point()
    if(bp):
        return ('買進' if bp[0] else '賣出',bp[1])
    else:
        return(False,False)
        
        
def send_ifttt(v1,v2,v3):
    url='https://maker.ifttt.com/trigger/toline/with/key/1WjdQ89uBOKzhnQYsDtLg'+'?value1='+str(v1)+'&value2='+str(v2)+'&value3='+str(v3)
    r=requests.get(url)
    if r.text[:4]=="Cong":
        print("Success")
    return r.text
    
stocklist=get_setting()
cnt=len(stocklist)
log1=[]
log2=[]

for i in range(cnt):
    log1.append('')
    log2.append('')
    
check_cnt=20
while True:
    for i in range(cnt): #0,1,2 共3支股票
        id,low,high=stocklist[i] #id會度給下一個函數找出價格
        name,price=get_price(id)
        print("檢查:",name,"股價:",price,"區間:",low,"~",high)
        if price <= low:
            if log1[i] != '買進':
                send_ifttt(name,price,'買進(股價低於'+str(low))
                log1[i]='買進'
        elif price >= high:
            if log1[i] != '賣出':
                send_ifttt(name,price,'賣出(股價高於'+str(high))
                log1[i] ='賣出'
        act,why=get_best(id)
        if why:
            if log2[i] != why:
                send_ifttt(name,price,act+why)
                log2[i] = why
    print("-----------------------")
    check_cnt -=1
    if check_cnt == 0:
        break
    time.sleep(180)
    