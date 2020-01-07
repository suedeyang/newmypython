# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 07:22:27 2020

@author: YANGS
"""

import twstock
#stock=twstock.Stock('2330')
#print("日期",stock.date[-1])
#print("開盤價",stock.open[-1])
#print("最高價",stock.high[-1])
#print("最低價",stock.low[-1])
#print('收盤價',stock.price[-1])

rt=twstock.realtime.get('2330')
if rt['success']==True:
    print(rt)
