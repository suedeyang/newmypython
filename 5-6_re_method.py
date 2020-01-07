# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:19:50 2020

@author: YANGS
"""

import re
m=re.search(r'p[a-z]+e','apples')
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())