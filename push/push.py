"""
push the task info in social communication app
"""

import requests
import json


def sever_push(msg, token):
    data = {
        "title": "Bilibili助手提醒",
        "desp": msg
    }
    headers = {
        "Content-Type": "application/json;charset=utf-8"
    }
    res = requests.post(url=f"https://sctapi.ftqq.com/{token}.send",
                        headers=headers,
                        data=json.dumps(data)).json()
    print(res)


def wechat_push(msg, wechat_id, wechat_app_secret, wechat_app_id):
    access_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={wechat_id}&corpsecret={wechat_app_secret}"

    access_token_res = requests.get(url=access_token_url).json()
    send_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    send_data = {
        "touser": "@all",
        "msgtype": "text",
        "agentid": wechat_app_id,
        "text": {
            "content": msg
        }
    }
    if "access_token" in access_token_res:
        access_token = access_token_res["access_token"]
        send_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        if len(msg) <= 1024:
            send_res = requests.post(url=send_url,
                                     headers=send_headers,
                                     data=json.dumps(send_data))
            print(send_res.json())
        else:
            # 消息超过1024个字符，分多次发送
            split_msg = [msg[i:i + 1024] for i in range(0, len(msg), 1024)]
            for msgs in split_msg:
                send_data["text"]["content"] = msgs
                res = requests.post(url=send_url,
                                    headers=send_headers,
                                    data=json.dumps(send_data)
                                    )
                print(res)
