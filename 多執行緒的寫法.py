# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:45:31 2020

@author: YANGS
"""
import threading

def job(num):
    print("子執行緒",num)

threads=[]
for i in range(3):
    threads.append(threading.Thread(target=job,args=(i,)))
    threads[i].start()

for i in range(3):
    print("主程式",i)

for i in threads:
    i.join()

print("結束")
