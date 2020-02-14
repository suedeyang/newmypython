# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:42:28 2020

@author: suedeyang
"""


import requests
import pandas as pd
def get_price(url):
    res=requests.get(url)
    data_prices=res.json()['stats']
    
    df=pd.DataFrame(data_prices)
    df.columns=['datetime','twd']
    df['datetime']=pd.to_datetime(df['datetime'],unit='ms')
    df.index=df['datetime']
    
    return df #整理完畢的Datafram丟出來


url='https://www.coingecko.com/price_charts/1/twd/90_days.json'
bitcoin=get_price(url)
print(bitcoin.shape)
print(bitcoin.head())
print('-----------------------')
bitcoin['ma']=bitcoin['twd'].rolling(window=100).mean()#以twd欄位的值計算窗口為100 計算出的均線 加入bitcoin的datafram中  (新增的方式)

print(bitcoin.shape)
print(bitcoin.head()) #多了一個ma的欄位
bitcoin[['twd','ma']].plot(kind='line',figsize=[15,5],xlim=('2019-12-01','2019-12-31'))
