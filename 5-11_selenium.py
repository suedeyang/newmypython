# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:48:49 2020

@author: YANGS
"""

from selenium import webdriver
opt=webdriver.ChromeOptions()
opt.add_experimental_option('prefs',
        {'profile.default_content_setting_values':{'notifications':2}})
driver=webdriver.Chrome(options=opt)
driver.get('https://www.google.com')
driver.find_element_by_id('gb_70').click()
driver.find_element_by_id('identifierId').send_keys("suedeyang@gmail.com")
driver.find_element_by_id('identifierNext').click()
driver.find_element_by_class_name("whsOnd zHQkBf").send.keys('123232')
driver.find_element_by_id('passwordNext').click()
