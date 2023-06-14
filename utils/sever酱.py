import requests
import json


def sever酱推送(消息, 发送密钥):
    """
     sever酱推送函数用于通过Server酱向指定的微信账号推送消息。

     参数:
     - 消息 (str): 要推送的消息内容。
     - 发送密钥 (str): Server酱的发送密钥。
     发送密钥获取https://sct.ftqq.com/sendkey

     返回:
     无返回值。

     异常:
     如果推送消息过程中出现错误，将抛出异常并打印错误信息。

     示例:
     sever酱推送("签到成功！", "发送密钥")
     """
    推送地址 = f"https://sctapi.ftqq.com/{发送密钥}.send"
    标题 = "签到情况"
    消息内容 = 消息
    try:
        数据 = {
            "title": 标题,
            "desp": 消息内容
        }
        请求头 = {
            "Content-Type": "application/json;charset=utf-8"
        }
        响应 = requests.post(推送地址, data=json.dumps(数据), headers=请求头)
        响应码 = 响应.status_code
        print("响应码 :", 响应码)
        #print(响应.text.encode().decode('unicode_escape'))
        if 响应码 == 400:
            错误信息 = 响应.text.encode().decode('unicode_escape')
            print("错误信息：", 错误信息)
    except Exception as e:
        print(e)

