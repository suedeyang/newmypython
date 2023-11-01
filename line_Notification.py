import requests
# https://steam.oxxostudio.tw/category/python/spider/line-notify.html
# https://notify-bot.line.me/doc/en/


line_notify_token={
    "使用者": ""
}
'''
token = ''
headers={
    "Authorization": "Bearer " + token   #Bearer後要有一個空白
    }

# https://developers.line.biz/en/docs/messaging-api/sticker-list/
'''

data={
    'message':'測試一下',
    'stickerPackageId':'446',
    'stickerId': '1990',
    #'notificationDisabled':'True'
}

teacher_name = '使用者'
#response_result=requests.post("https://notify-api.line.me/api/notify",headers=headers,data=data)
#print(response_result)
if teacher_name in line_notify_token:
    token = line_notify_token[teacher_name]
    headers = {
        "Authorization": "Bearer " + token  # Bearer後要有一個空白
    }
    response_result = requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)

