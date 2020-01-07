# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:44:15 2019

@author: YANGS
"""

import requests
from bs4 import BeautifulSoup
page=requests.get("http://www.flag.com.tw")
soup=BeautifulSoup(page.text,"html.parser")
print(soup.link)


url="http://httpbin.org/post"
r=requests.post(url,data="hello")
print(r.text)