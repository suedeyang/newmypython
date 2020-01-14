#-*-coding:utf-8-*-

import re,requests
url="http://www2.lhps.kh.edu.tw/lhps/introduction/introduction-lhps/members.html"
html=requests.get(url).text
#print(html)
regex=r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)" #正規式表達法還是需要修改
emails=re.findall(regex,html) #重點在findall
for email in emails:
    print(email)