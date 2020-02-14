# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:59:02 2020

@author: suedeyang
"""


import requests
import pandas as pd
url='https://www.coingecko.com/price_charts/1/twd/90_days.json'

data=requests.get(url)
price=data.json()['stats'] #要寫成data.json()['stats']解析才會正確
#print(price)

df=pd.DataFrame(price)
df.columns=['datetime','twd']
#print(df.head(1))

df['datetime']=pd.to_datetime(df['datetime'], unit='ms')
print(df.head())


df.index=df['datetime']
df['twd'].plot(kind='line',figsize=[20,5])