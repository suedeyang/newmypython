# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:58:24 2020

@author: YANGS
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials


auth_json_path = '1.json' ##頻政黨按
gss_scopes = ['https://spreadsheets.google.com/feeds']

#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)

#開啟 Google Sheet 資料表
spreadsheet_key = '12312312312'  google表單的key

#建立工作表1
sheet = gss_client.open_by_key(spreadsheet_key).sheet1
#自定義工作表名稱
#sheet = gss_client.open_by_key(spreadsheet_key).worksheet('測試1')

sheet.update_acell('D2', 'ABC')  #D2加入ABC
sheet.update_cell(2, 4, 'ABC')   #D2加入ABC(第2列第4行即D2)
values = ['A','B','C','D']
sheet.insert_row(values, 1) #插入values到第1列