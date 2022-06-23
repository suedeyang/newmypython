#影片連結 https://www.youtube.com/watch?v=mYX9AaJF2lw

from openpyxl import Workbook,load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font


wb=load_workbook("123.xlsx")
ws=wb.active


wb.save("123.xlsx")

'''
wb=load_workbook("123.xlsx")

ws=wb.active
ws['A5'].value="小小灰"

wb.sheetnames #會將sheet輸出成list
print(wb.sheetnames) 
ws=wb["工作表1"]
print(ws)

wb.create_sheet("999")

wb=Workbook() #建立檔案
ws=wb.active #當前的sheet
ws.title='qq' #重新命名worksheet
wb.save("999.xlsx")

ws.append([123,456,789,0]) #新增一列資料(橫排)

#讀取or修改範圍資料 需要用get_column_letter套件將A轉成1 B轉成2
for row in range(1,7): #共6個橫排
    for col in range(1,5): #直行
         char = get_column_letter(col) #依序回傳直行的字母A就是1 B就是2 以此類推
         #print(char+str(row)) #A1,B1,C1,D1,A2,B2,C2,D2
         #print(ws[char+str(row)].value) 
         ws[char+str(row)].value=char+str(row)
wb.save("1234.xlsx")


#ws.merge_cells("A1:E1") #合併儲存格
#ws.unmerge_cells("A1:E1") #分割儲存格

#插入刪除直橫排
ws.insert_rows(3) #row 橫排
#ws.insert_cols(3)
ws.delete_cols(3) #刪除直排

ws.move_range('A1:D6',rows=2,cols=3) #可以輸入負值往左往上

#用for迴圈找出BCD 使用excel公式 需要用到  get_column_letter
for col in range(2,5): #2,3,4轉B C D
    char=get_column_letter(col)
    ws[char+"7"].value=f'=AVERAGE({ char + "2" } : { char +"6"} )'  #B2:B6 C2:C6 D2:D6  #公式當字串寫進去就可以調用excel函數

#調整字型(粗體)與顏色
for col in range(1,5):
    char = get_column_letter(col)
    ws[char+"1"].font=Font(bold=True,color="000000FF" )  #https://openpyxl.readthedocs.io/en/stable/styles.html


'''