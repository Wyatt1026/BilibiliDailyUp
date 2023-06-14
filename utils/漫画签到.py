import re
import requests
"""
为了不修改原代码,改出bug,在这里增加功能.api参考https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga/ClockIn.md
"""

def 提取SESSDATA(cookie):
    """
    从Cookie中提取SESSDATA值。

    参数:
    - cookie (str): 包含SESSDATA的Cookie字符串。

    返回:
    - str: 提取到的SESSDATA值，如果未找到则返回None。

    示例:
    cookie = "your_cookie_string"
    extract_sessdata(cookie)
    """
    模式 = r"SESSDATA=([^;]+)"
    匹配结果 = re.search(模式, cookie)
    if 匹配结果 :
        return 匹配结果 .group(1)
    else:
        return None

def 漫画签到(cookie):

    """
    漫画签到函数用于通过Bilibili漫画进行签到。

    参数:
    - cookie (str): 包含用户登录信息的Cookie字符串。

    返回:
    - True: 签到成功。
    - False: 签到失败。

    异常:
    如果无法提取到SESSDATA或签到过程中出现错误，将打印错误信息。

    示例:
    cookie = "your_cookie_string"
    漫画签到(cookie)
    """
    sessdata = 提取SESSDATA(cookie)
    if sessdata:
        url = "https://manga.bilibili.com/twirp/activity.v1.Activity/ClockIn"
        headers = {
            "Cookie": f"SESSDATA={sessdata}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "platform": "android"
        }

        response = requests.post(url, headers=headers, data=data)
        result = response.json()
        if result.get("code") == 0:
            #print("签到完成")
            return True
        else:
            #print(f"签到失败：{result.get('msg')}")
            return False
    else:
        print("无法提取到 SESSDATA")



def 检查是否已签到(cookie: str) -> bool:
    """
    检查是否已签到函数用于检查Bilibili漫画是否已经进行签到。

    参数:
    - cookie (str): 包含SESSDATA的Cookie字符串。

    返回:
    - bool: 如果已签到返回True，否则返回False。

    异常:
    如果查询签到状态失败，将打印错误信息并返回False。

    示例:
    cookie = "your_cookie_string"
    检查是否已签到(cookie)
    """
    sessdata = 提取SESSDATA(cookie)
    url = "https://manga.bilibili.com/twirp/activity.v1.Activity/GetClockInInfo"
    headers = {
        "Cookie": f"SESSDATA={sessdata}",
    }
    响应 = requests.post(url, headers=headers)
    数据 = 响应.json()

    if 数据["code"] == 0:
        签到状态 = 数据["data"]["status"]
        if 签到状态 == 1:
            return True  # 已签到
        else:
            return False  # 未签到
    else:
        print("查询签到状态失败:", 数据["msg"])
        return False  # 查询失败

