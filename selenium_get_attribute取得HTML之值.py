from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
url = "https://www.lhps.kh.edu.tw/view/index.php?WebID=180&MainType=HOME"
driver.get(url)
time.sleep(3)
vvv = driver.find_element(By.XPATH, '//*[@id="menu_sub_54793"]/div[1]/a').get_attribute('textContent')
print(vvv)
time.sleep(10)

