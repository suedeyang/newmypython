import streamlit as st
import streamlit.components.v1 as components
import requests
#import pyautogui
import time
import smtplib
from email.mime.text import MIMEText
import pandas as pd
import datetime

#改勾選的電子郵件寄送的參數要改
# emoji位置 https://www.emojiall.com/zh-hant/copy#categories-B  https://www.emojiall.com/zh-hant

st.set_page_config(
	    layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
	    page_title="龍華國小傷病登記系統",  # String or None. Strings get appended with "• Streamlit". 
	    page_icon=None,  # String, anything supported by st.image, or None.
        )

reload_html_string = '''
<head>
        <meta http-equiv="refresh" content="0" />
</head>
'''

button_color_code='''
<style>
div.stButton > button:first-child {
    background-color: #0048ff;
    color:#ffffff;
    font-weight:bold;
}
div.stButton > button:hover {
    background-color: #ffffff;
    color:#0048ff;
    font-weight:bold;
    }
</style>
'''
st.markdown(button_color_code, unsafe_allow_html=True)

fp=open("db.txt",'r')
stu_list=fp.readlines()

#The ID of this base is appdbFYpupPu5iPPc.
KEY=""
endpoint='https://api.airtable.com/v0/appdbFYpupPu5iPPc/harm-data'
endpoint2='https://api.airtable.com/v0/appdbFYpupPu5iPPc/harm-data-history'

#找出老師的電子郵件信箱
def find_class_teachers(classes_of_student):
    url="http://school.kh.edu.tw/view/index.php?WebID=180&MainType=103&SubType=0&MainMenuId=69026&SubMenuId=0&NowMainId=69026&NowSubId=0"
    html=pd.read_html(url,header=0)
    df=html[0]
    df.drop(['NO.'],axis=1)
    df=df.fillna("")
    final_class_result_list=[]
    
    classes=list(df.職稱)
    for i in classes:
        i=i.replace("-","0")
        if len(i) == 4:
            i=i.replace("0","",1)
            final_class_result_list.append(str(i))
        else:
            final_class_result_list.append(str(i))
    
    index_number=final_class_result_list.index(classes_of_student)
    return df.Email[index_number],df.姓名[index_number]

#寄送班級導師電子郵件
def send_gmail(basic_data,teachers_email,teachers_name,injured_area,trauma,pre_get_hurt_places,Internal_Medicine,treat_method_choice,body_temperature,pre_obseravtion_time,txtMemo):
    dt=datetime.datetime.now()
    gmail_addr='@mail.lhps.kh.edu.tw'
    gmail_pwd=''
    email_msg=f'{teachers_name}老師您好：\n貴班{basic_data}小朋友於健康中心登記傷病，特此通知，登載資料如下：\n時間：{dt.strftime("%Y/%m/%d %H:%M:%S")}\n受傷部位：{injured_area}\n外傷種類：{trauma}\n受傷地點：{pre_get_hurt_places}\n症狀：{Internal_Medicine}\n處置作為：{treat_method_choice}\n記錄體溫：{body_temperature}\n紀錄休息觀察時間：{pre_obseravtion_time}\n備註：{txtMemo}\n\n若有任何問題勿回信，請直接與健康中心聯絡'
    
    mime_text=MIMEText(email_msg,'plain','utf-8')
    mime_text['Subject']=f'{basic_data}傷病資料'
    mime_text['From']='龍華國小健康中心'
    mime_text['to']=f'{basic_data}班級老師{teachers_name}'
    #mime_text['Cc']='副本收件者'
    mime_text=mime_text.as_string() #送出之前要先轉換為字串
    #send_gmail(gmail_addr,gmail_pwd,to_addrs,mime_text) #注意msg的格式
    
    smtp_gmail=smtplib.SMTP('smtp.gmail.com',587) #587為ttl的port
    smtp_gmail.ehlo() #打招呼說hello
    smtp_gmail.starttls()
    smtp_gmail.login(gmail_addr,gmail_pwd) #https://myaccount.google.com/lesssecureapps 低安全性登入要打開
    status=smtp_gmail.sendmail(gmail_addr,teachers_email,mime_text)
    if not status:  #因為成功的話 回傳的dic會是空的
        st.success("導師通知信 寄送成功")
    else:
        st.error('導師通知信 寄信失敗 不過沒關係，不需要重新登記')
    smtp_gmail.quit()

#資料寫入airtable
def add_to_airtable(basic_data,injured_part_result,trauma_result,Internal_Medicine_result,treat_method_result,body_temperature,obseravtion_time,get_hurt_places,txtMemo):
    #Python requests headers
    headers={
        "Authorization": f'Bearer {KEY}', #注意前面的,
        "Content-Type" : "application/json"
    }

    data= {
    "records": [
            {
            "fields": {
                "ID": basic_data ,
                "injured_area":injured_part_result,
                "trauma": trauma_result,
                "Internal_Medicine":Internal_Medicine_result,
                "treat_method":treat_method_result,
                "get_hurt_places":get_hurt_places,
                "obseravtion_time":obseravtion_time,
                "body_temperature":body_temperature,
                "txt":txtMemo,
                }
            }
        ]
    }
    r=requests.post(endpoint,json=data,headers=headers)
    r2=requests.post(endpoint2,json=data,headers=headers)
    print(r.status_code) #HTTP status code
    print(r2.status_code) #HTTP status code
    return r.status_code,r2.status_code


injured_part=['頭','脖子','肩','胸','肚子','背','眼','臉','嘴(含牙齒)','耳鼻喉','手','腰','腳','屁股','會陰部']
trauma_type=['擦傷','割裂刺傷','壓夾傷','挫撞傷','扭傷','灼燙傷','叮咬傷','骨折','舊傷']
Internal_Medicine_type=['發燒','暈眩','噁心嘔吐','頭痛','牙痛','胃痛','腹痛','腹瀉','經痛','氣喘','流鼻血','疹癢','眼疾']
treat_method=['傷口處理','冰敷','熱敷','休息觀察','通知家長','家長帶回','校方送醫','衛生教育','其他']
injured_places=['不登記','操場','遊戲運動器材','班級教室','科任教室','走廊、露台','樓梯','地下室','活動中心','廁所','校外','蝴蝶園、飛龍廣場、龍之華廣場、林間教室及其他']
rest_time=[5,10,15,20,25,30,45,60,75,90,120,150,180,240,300,360,420,480,540,600]

#st.sidebar.title("龍華國小傷病管理系統")
st.sidebar.title("1.填寫基本資料")
grade=st.sidebar.selectbox('年級',range(0,7))
if grade == 4:
    classes=st.sidebar.selectbox('班級',range(0,18))
else:
    classes=st.sidebar.selectbox('班級',range(0,16))
numbers=st.sidebar.selectbox('座號',range(0,36))
#body_temperature = None
#obseravtion_time=None
#get_hurt_places=None
basic_data=str(grade)+str(classes).zfill(2)+str(numbers).zfill(2)
classes_of_student=str(grade)+str(classes).zfill(2)

txtMemo=[]
pre_obseravtion_time=[]
pre_get_hurt_places=[]
body_temperature=[]
obseravtion_time=0
get_hurt_places=0

with st.sidebar.expander("補充資料(體溫、時間)"):
    #colx,coly,colz=st.columns(3)
    if st.checkbox("記錄體溫"):
       body_temperature.append(st.slider("體溫",34.0,40.0,36.0,0.1))
       
    if st.checkbox("紀錄休息觀察時間"):
       #obseravtion_time.append(st.selectbox("休息觀察時間",rest_time))
       pre_obseravtion_time=st.selectbox("休息觀察時間",rest_time)
       obseravtion_time=rest_time.index(pre_obseravtion_time)+1


#id="ctl00_ContentPlaceHolder1_txtMemo"

with st.sidebar.expander("文字備註"):
    input_txt=st.text_input("輸入文字、更新文字一定要按ENTER",placeholder="請在此輸入")
    if input_txt:
        st.write("檢查：備註欄的文字為「",input_txt,"」")
        txtMemo.append(input_txt)


if grade == 0 or classes == 0 or numbers == 0:
    st.error("先在左邊 輸入班級、姓名、座號")
    #st.image("https://pic.pimg.tw/c41666/1560907397-2167670633_n.png",caption='身體部位圖')
if not grade == 0 and not classes == 0 and not numbers == 0:
    if basic_data+"\n" in stu_list:
        messages=f"{grade}年{classes}班{numbers}號 資料驗證正確，登記完傷病資料(至少勾選一個)請按最下方藍色按鈕送出"
        st.success(messages)
        fp.close()

        st.header("部位")
        injured_area=[]#寄送電子郵件用的串列
        injured_part_result=[] #受傷部位結果之串列
        col1, col2, col3,col4,col5 = st.columns(5)
        if col1.checkbox('頭'):
            injured_part_result.append(injured_part.index("頭"))
            injured_area.append('頭')
        if col2.checkbox('臉'):
            injured_part_result.append(injured_part.index('臉'))
            injured_area.append('臉')
        if col3.checkbox('眼'):
            injured_part_result.append(injured_part.index('眼'))
            injured_area.append('眼')
        if col4.checkbox('耳鼻喉'):
            injured_part_result.append(injured_part.index('耳鼻喉'))
            injured_area.append('耳鼻喉')
        if col5.checkbox('嘴(含牙齒)'):
            injured_part_result.append(injured_part.index('嘴(含牙齒)'))
            injured_area.append('嘴(含牙齒)')
         
        col6, col7, col8,col9,col10 = st.columns(5)
        if col6.checkbox('手'):
            injured_part_result.append(injured_part.index('手'))
            injured_area.append('手')
        if col7.checkbox('脖子'):
            injured_part_result.append(injured_part.index('脖子'))
            injured_area.append('脖子')
        if col8.checkbox('肩'):
            injured_part_result.append(injured_part.index('肩'))
            injured_area.append('肩')
        if col9.checkbox('胸'):
            injured_part_result.append(injured_part.index('胸'))
            injured_area.append('胸')
        if col10.checkbox('肚子'):
            injured_part_result.append(injured_part.index('肚子'))
            injured_area.append('肚子')
        
        col11, col12, col13,col14,col15 = st.columns(5)
        if col11.checkbox('腳'):
            injured_part_result.append(injured_part.index('腳'))
            injured_area.append('腳')
        if col12.checkbox('背'):
            injured_part_result.append(injured_part.index('背'))
            injured_area.append('背')
        if col13.checkbox('腰'):
            injured_part_result.append(injured_part.index('腰'))
            injured_area.append('腰')
        if col14.checkbox('屁股'):
            injured_part_result.append(injured_part.index('屁股'))
            injured_area.append('屁股')
        if col15.checkbox('會陰部'):
            injured_part_result.append(injured_part.index('會陰部'))
            injured_area.append('會陰部')
        #st.write(injured_area)
        #st.write(injured_part_result)
        #舊選擇法
        #injured_area = st.multiselect('',['頭','手','腳','臉','眼','嘴(含牙齒)','脖子','肩','胸','肚子','背','耳鼻喉','腰','屁股','會陰部'])
        #for i in injured_area:
        #    selected_number=injured_part.index(i)
        #    injured_part_result.append(selected_number)
        #st.write(injured_part_result)       
        st.write('------------')
        
        st.header("外傷種類")
        trauma=[]
        trauma_result=[]
        cola1, cola2, cola3,cola4,cola5 = st.columns(5)
        if cola1.checkbox('擦傷'):
            trauma_result.append(trauma_type.index('擦傷'))
            trauma.append('擦傷')
        if cola2.checkbox('割裂刺傷'):
            trauma_result.append(trauma_type.index('割裂刺傷'))
            trauma.append('割裂刺傷')
        if cola3.checkbox('壓夾傷'):
            trauma_result.append(trauma_type.index('壓夾傷'))
            trauma.append('壓夾傷')
        if cola4.checkbox('挫撞傷'):
            trauma_result.append(trauma_type.index('挫撞傷'))
            trauma.append('挫撞傷')
        if cola5.checkbox('扭傷'):
            trauma_result.append(trauma_type.index('扭傷'))
            trauma.append('扭傷')
         
        cola6, cola7, cola8,cola9,cola10= st.columns(5)
        if cola6.checkbox('灼燙傷'):
            trauma_result.append(trauma_type.index('灼燙傷'))
            trauma.append('灼燙傷')
        if cola7.checkbox('叮咬傷'):
            trauma_result.append(trauma_type.index('叮咬傷'))
            trauma.append('叮咬傷')
        if cola8.checkbox('骨折'):
            trauma_result.append(trauma_type.index('骨折'))
            trauma.append('骨折')
        if cola9.checkbox('舊傷'):
            trauma_result.append(trauma_type.index('舊傷'))
            trauma.append('舊傷')
        cola10.empty()
        #st.write(trauma_result)
        #st.write(trauma)
        #舊外傷種類選擇法
        #trauma = st.multiselect('',trauma_type)
        #for i in trauma:
        #    selected_number=trauma_type.index(i)
        #    trauma_result.append(selected_number)

        if trauma_result:
            st.header("🗺受傷地點(外傷需點選)")
            pre_get_hurt_places=st.radio("",injured_places)
            get_hurt_places=injured_places.index(pre_get_hurt_places)
        #st.write(get_hurt_places)
        st.write('------------')

        st.header("症狀")
        Internal_Medicine_result=[]
        Internal_Medicine=[]
        colb1, colb2, colb3,colb4,colb5 = st.columns(5)
        if colb1.checkbox('發燒'):
            Internal_Medicine_result.append(Internal_Medicine_type.index("發燒"))
            Internal_Medicine.append('發燒')
        if colb2.checkbox('暈眩'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('暈眩'))
            Internal_Medicine.append('暈眩')
        if colb3.checkbox('噁心嘔吐'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('噁心嘔吐'))
            Internal_Medicine.append('噁心嘔吐')
        if colb4.checkbox('頭痛'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('頭痛'))
            Internal_Medicine.append('頭痛')
        if colb5.checkbox('牙痛'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('牙痛'))
            Internal_Medicine.append('牙痛')
         
        colb6, colb7, colb8,colb9,colb10 = st.columns(5)
        if colb6.checkbox('胃痛'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('胃痛'))
            Internal_Medicine.append('胃痛')
        if colb7.checkbox('腹痛'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('腹痛'))
            Internal_Medicine.append('腹痛')
        if colb8.checkbox('腹瀉'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('腹瀉'))
            Internal_Medicine.append('腹瀉')
        if colb9.checkbox('經痛(女生才能選)'):
            components.iframe("https://linux.lhps.kh.edu.tw/h5p/?p=692", width=0,height=0)
            Internal_Medicine_result.append(Internal_Medicine_type.index('經痛'))
            Internal_Medicine.append('經痛')
        if colb10.checkbox('氣喘'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('氣喘'))
            Internal_Medicine.append('氣喘')
        
        colb11, colb12, colb13,colb14,colb15 = st.columns(5)
        if colb11.checkbox('流鼻血'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('流鼻血'))
            Internal_Medicine.append('流鼻血')
        if colb12.checkbox('疹癢'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('疹癢'))
            Internal_Medicine.append('疹癢')
        if colb13.checkbox('眼疾'):
            Internal_Medicine_result.append(Internal_Medicine_type.index('眼疾'))
            Internal_Medicine.append('眼疾')
        colb14.empty()
        colb15.empty()
        #st.write(Internal_Medicine_result)
        #st.write(Internal_Medicine)
        st.write('------------')
        #舊症狀選擇法
        #Internal_Medicine = st.multiselect('',Internal_Medicine_type)
        #for i in Internal_Medicine:
        #    selected_number=Internal_Medicine_type.index(i)
        #    Internal_Medicine_result.append(selected_number)

        st.header("處置作為")
        #treat_method=['','','','','通知家長','家長帶回','校方送醫','衛生教育','其他']
        treat_method_choice=[]
        treat_method_result=[]
        colc1, colc2, colc3,colc4,colc5 = st.columns(5)
        if colc1.checkbox('傷口處理'):
            treat_method_result.append(treat_method.index("傷口處理"))
            treat_method_choice.append('傷口處理')
        if colc2.checkbox('冰敷'):
            treat_method_result.append(treat_method.index('冰敷'))
            treat_method_choice.append('冰敷')
        if colc3.checkbox('熱敷'):
            treat_method_result.append(treat_method.index('熱敷'))
            treat_method_choice.append('熱敷')
        if colc4.checkbox('休息觀察'):
            treat_method_result.append(treat_method.index('休息觀察'))
            treat_method_choice.append('休息觀察')
        if colc5.checkbox('通知家長'):
            treat_method_result.append(treat_method.index('通知家長'))
            treat_method_choice.append('通知家長')
         
        colc6, colc7, colc8,colc9,colc10 = st.columns(5)
        if colc6.checkbox('家長帶回'):
            treat_method_result.append(treat_method.index('家長帶回'))
            treat_method_choice.append('家長帶回')
        if colc7.checkbox('校方送醫'):
            treat_method_result.append(treat_method.index('校方送醫'))
            treat_method_choice.append('校方送醫')
        if colc8.checkbox('衛生教育'):
            treat_method_result.append(treat_method.index('衛生教育'))
            treat_method_choice.append('衛生教育')
        if colc9.checkbox('其他'):
            treat_method_result.append(treat_method.index('其他'))
            treat_method_choice.append('其他')
        colc10.empty()    
        #st.write(treat_method_result)
        #st.write(treat_method_choice)
        #treat_method_choice = st.multiselect('',treat_method)
        #
        #for i in treat_method_choice:
        #    selected_number=treat_method.index(i)
        #    treat_method_result.append(selected_number)
        
        st.write("-------")
        if not injured_part_result  and not trauma_result and not Internal_Medicine_result and not treat_method_result and not txtMemo:
            #st.error("請輸入傷病資料")    
            st.empty()
        else:
            if st.button(basic_data+" 輸入完畢送出(按1下就好)"):
                st.write("資料處理中 請不要再按滑鼠")
                x1,x2=add_to_airtable(basic_data,str(injured_part_result),str(trauma_result),str(Internal_Medicine_result),str(treat_method_result),str(body_temperature),obseravtion_time,get_hurt_places,str(txtMemo))
                #st.write("資料寫入中")
                if x1 > 300 or x2 > 300:
                    st.error("資料寫入失敗，網路部份出了問題，清除資料重新登記")
                    #time.sleep(3)
                    #pyautogui.hotkey("ctrl","F5")
                    st.markdown(reload_html_string, unsafe_allow_html=True)
                else:
                    st.success("資料寫入成功!!")
                    teachers_email,teachers_name=find_class_teachers(classes_of_student)
                    send_gmail(basic_data,teachers_email,teachers_name,injured_area,trauma,pre_get_hurt_places,Internal_Medicine,treat_method_choice,body_temperature,pre_obseravtion_time,txtMemo)
                    #st.balloons()
                    #time.sleep(2)
                    #pyautogui.hotkey("ctrl","F5")
                    st.markdown(reload_html_string, unsafe_allow_html=True)
                                        
    else:
        messages=f"龍華國小沒有{grade}年{classes}班{numbers}號 這位小朋友喔!!"
        st.error(messages)
        


