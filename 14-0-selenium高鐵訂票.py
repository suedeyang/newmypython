# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:55:49 2020

@author: suedeyang


"""

from selenium import webdriver
from time import sleep

def input_ticket_info(driver):
    driver.find_element_by_id("btn-confirm").click()
    driver.find_element_by_xpath('//*[@id="content"]/tbody/tr[1]/td[2]/span/select/option[3]').click()
    driver.find_element_by_xpath('//*[@id="content"]/tbody/tr[1]/td[2]/select/option[12]').click()
    driver.find_element_by_id('trainCon:trainRadioGroup_1').click()
    driver.find_element_by_id('toTimeInputField').clear()
    driver.find_element_by_id('toTimeInputField').send_keys("2020/04/09")
    driver.find_element_by_xpath('//*[@id="toTimeTable"]/select/option[21]').click()
    driver.find_element_by_xpath('//*[@id="content"]/tbody/tr[6]/td[2]/span/span[1]/span/select/option[3]').click()

def input_train_and_person(driver):
    driver.find_element_by_name("TrainQueryDataViewPanel:TrainGroup").click()
    driver.find_element_by_name('SubmitButton').click()
    driver.find_element_by_id('idNumber').send_keys('A123456789')
    driver.find_element_by_id('mobilePhone').send_keys('0931425878')
    driver.find_element_by_name('agree').click()
    driver.find_element_by_id('isSubmit').click()
    


    
url='https://irs.thsrc.com.tw/IMINT'
#driver=webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options = option) #加入選項來指定不要有自動控制的訊息

driver.get(url)
driver.maximize_window()

input_ticket_info(driver)
driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode').screenshot('capcha.png')
code=input("暫時輸入驗證碼:")
driver.find_element_by_name('homeCaptcha:securityCode').send_keys(code)
driver.find_element_by_id('SubmitButton').click()
sleep(5)
input_train_and_person(driver)