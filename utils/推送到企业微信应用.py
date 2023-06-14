import requests
import json



def 推送消息(消息, 企业ID, 企业应用secret, 企业应用的id):
    """
     推送消息函数用于向企业微信应用推送消息。

     参数:
     - 消息 (str): 要推送的消息内容。
     - 企业ID (str): 企业微信的唯一标识ID。
     - 企业应用secret (str): 企业微信应用的密钥。
     - 企业应用的id (str): 企业微信应用的ID。
     参数获取及细节见文档https://developer.work.weixin.qq.com/document/path/90236

     返回:
     无返回值。

     异常:
     如果推送消息过程中出现错误，将抛出异常并打印错误信息。

     示例:
     推送消息("Hello, World!", "企业ID", "应用密钥", "应用ID")
     """

    # 获取 access_token
    请求地址 = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={企业ID}&corpsecret={企业应用secret}"
    请求返回结果 = requests.get(请求地址)
    body = 请求返回结果.json()
    if "access_token" in body:
        access_token = body["access_token"]
        #print("企业微信应用推送 access token 为", access_token)

        # 判断消息长度是否超过1024个字符，因为该api超过2048个字节会截断，所以进行判断
        if len(消息) <= 1024:
            # 构造请求体
            data = {
                "touser": "@all",
                "msgtype": "text",
                "agentid": 企业应用的id,
                "text": {
                    "content": 消息
                }
            }
            json_data = json.dumps(data)

            # 发送请求
            url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            请求返回结果 = requests.post(url, data=json_data, headers=headers)
            responseCode = 请求返回结果.status_code
            if responseCode == 200:
                pass
                #rint_f("消息推送成功！")

            else:
                失败原因 = 请求返回结果.json()
                print("消息推送失败：", 失败原因)
        else:
            # 消息超过1024个字符，分多次发送
            分段消息列表 = [消息[i:i+1024] for i in range(0, len(消息), 1024)]
            for 分段消息 in 分段消息列表:
                # 构造请求体
                data = {
                    "touser": "@all",
                    "msgtype": "text",
                    "agentid": 企业应用的id,
                    "text": {
                        "content": 分段消息
                    }
                }
                json_data = json.dumps(data)

                # 发送请求
                url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }
                请求返回结果 = requests.post(url, data=json_data, headers=headers)
                responseCode = 请求返回结果.status_code
                if responseCode == 200:
                    pass
                    #print("消息推送成功！")
                else:
                    失败原因 = 请求返回结果.json()
                    print("消息推送失败：", 失败原因)
    else:
        失败原因 = body.get("errmsg", "获取access_token失败")
        print("获取access_token失败：", 失败原因)


