# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:08:15 2019

@author: YANGS
"""

a=[[1,4,3,2],[5,3,6],[4,7,3,8,3],[8,3]]
cnt=0
for s in a:
    for n in s:
        if n == 3:
            cnt+=1
print(f'一共有{cnt}個3')