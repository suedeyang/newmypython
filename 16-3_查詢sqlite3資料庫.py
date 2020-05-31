# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:52:18 2020

@author: suedeyang
"""


import sqlite3
def db_check(db):
    try:
        connect=sqlite3.connect(db)
        sql='select * from mytable'
        cursor=connect.execute(sql)
        dataset=cursor.fetchall()
        for data in dataset:
            print("姓名 \t 打卡時間")
            print("---- \t --------")
            print(f"{data[0]} \t {data[1]}")
    except:
        print('讀取資料錯誤')
    connect.close()

db_check('mydatabase.sqlite')