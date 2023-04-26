#-*-coding:utf-8-*-
from selenium import webdriver
import time
url = "https://portal.kh.edu.tw/"
url2 = "https://portal.kh.edu.tw/redirect.php?func=kh:exc"
url3 = "https://exc.kh.edu.tw/p/tea/school_apply_no_i.jsp?school="

#讀取高雄市國小學校代碼
f = open('school_no.txt', 'r')
school_no = []
for line in f:
    school_no.append(line)
f.close()


driver=webdriver.Chrome()
driver.get(url)
#driver.implicitly_wait(10)
time.sleep(15)
#等待輸入帳密完畢

#代入使用者的身分
driver.get(url2)
time.sleep(3)

for i in school_no:
    driver.get(f'https://exc.kh.edu.tw/p/tea/school_apply_no_i.jsp?school={i}')
    time.sleep(0.5)
    result=driver.find_element("xpath",'/html/body/div[3]/p/font').text
    if result[-3] != "0":
        with open('appendSomething.txt', 'a') as f:
            f.write(f'{result}\n')
