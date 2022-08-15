'''
Author: ForMemRs
Date: 2022-06-19 17:42:27
LastEditors: ForMemRS
LastEditTime: 2022-07-17 00:30:53
FilePath: /bilibili_daily/push.py
Blog: https://www.52pojie.cn/?1507943
Copyright (c) 2022 by ForMemRs, All Rights Reserved.
'''

import requests
import json


def pushplus(token, content, title='Bilibili助手提醒', template='markdown'):
    url = 'http://www.pushplus.plus/send'
    data = {
        "token": token,
        "title": title,
        "content": content,
        "template": template
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=body, headers=headers)
    print(response.text)
    if response.status_code == 200:
        return 1
    return 0


