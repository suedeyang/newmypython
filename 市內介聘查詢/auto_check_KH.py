#-*-coding:utf-8-*-
from selenium import webdriver
import time
import requests
url = "https://portal.kh.edu.tw/"
url2 = "https://portal.kh.edu.tw/redirect.php?func=kh:exc"
url3 = "https://exc.kh.edu.tw/p/tea/school_apply_no_i.jsp?school="


school_no = []
#讀取高雄市國小學校代碼
response = requests.get("https://www2.lhps.kh.edu.tw/school_no.txt").text.split('\n')
for i in response:
    school_no.append(i)

print(f'共有 {len(school_no)} 間高市國小要讀取資料\n接下來會跳轉到資訊服務入口網，請"立刻"輸入帳號、密碼、驗證碼後按"登入"等待程式啟動\n \n提醒您!本程式僅能查詢「高市某校有多少人想調入貴校」\n執行過程中請勿關閉跳動的瀏覽器視窗 \n執行完畢會出現一個「檢查結果」的文字檔')
time.sleep(20)

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
        with open('檢查結果.txt', 'a') as f:
            f.write(f'{result}\n')
