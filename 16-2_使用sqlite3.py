# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:41:52 2020

@author: suedeyang
"""

import sqlite3
from datetime import datetime


def db_save(db,name):
    connect=sqlite3.connect(db)
    sql='create table if not exists mytable ("姓名" TEXT,"打卡時間" TEXT)'
    connect.execute(sql)
    
    save_time=str(datetime.now().strftime('%Y-%m-%d %H.%M.%S'))
                                          
    sql=f'insert into mytable values("{name}","{save_time}")'
    connect.execute(sql)
    connect.commit()
    connect.close()
    print('儲存成功')
    
    
db_save('mydatabase.sqlite','洋洋')

            