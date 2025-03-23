"""
The config for this script, you can read the description in README.md
"""
import os

LIKE_OR_NOT = True
# 投币时是否点赞

USE_ENVIRONMENT_VARIABLE = True
# 从环境变量中读取CK 确保已经设置环境变量BILIBILI 只支持单个账号

COIN_OR_NOT = True
# 是否投币

COIN_NUM = -1
# 投币数量 -1为完成所有也就是如果你已经投过1次那就只会投4次
# 如果不是 -1 则指定投币数量范围1-5

SILVER2COIN_OR_NOT = True
# 是否将银瓜子兑换为硬币


STRICT_MODE = True
# 是否开启严格模式，严格模式会保证至少5次成功投币，因为官方投币API存在缺陷，会有投币成功但是返回失败的情况
# 默认开启严格模式，如果关闭则只会投币5次，无论成功失败，会出现少投币的情况，因为可能失败，但是不会造成浪费硬币的情况，自行选择
NUM_MODE = False
# 该模式与严格模式互斥,开启此模式,投币只会投COIN_NUM次,无论成功失败

UID_LIST = ['473837611', '1131457022', '433587902', '2026561407', '50329118']
# 投币UP主的ID号,如果不修改，默认将用上面这个列表里的,可以选择自己喜欢的UP主
# 获取UID的方法见README.md

COOKIE_LIST = [
    r"buvid3=9861459B-C6AE-30F1-1C0A-E44A874F3CCA38140infoc; b_nut=1709894038; _uuid=103753A810-FD79-FDBC-1010BD-5107E5BBD29B339279infoc; buvid4=AD422B7D-5D49-7758-7152-2C14F28DAC4138921-024030810-3%2Fdq6MhSXavtbsTZPUsYofldkmDVrKET%2Ffgp91VD6KkSjOhPw9ziZNVwGaySO80G; rpdid=0zbfVGeOUx|X0AFTDpw|2AS|3w1RIxy7; enable_web_push=DISABLE; header_theme_version=CLOSE; hit-dyn-v2=1; LIVE_BUVID=AUTO9517099011483532; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; CURRENT_QUALITY=80; buvid_fp_plain=undefined; go-back-dyn=0; fingerprint=177532d1718af28f2ff1468460bdda48; buvid_fp=177532d1718af28f2ff1468460bdda48; PVID=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzUzMDQwNzEsImlhdCI6MTczNTA0NDgxMSwicGx0IjotMX0.T5mTLKJNtkz_5wo2PoChoTA3q1QUvJVNAe_gCo7aRt8; bili_ticket_expires=1735304011; SESSDATA=aa96ed54%2C1750606574%2Cd5f1e%2Ac1CjAeODR7OTd3smz2pDTYHpV3DKPbJHH3DQ8qksuxG9G3m7rl0lOLYW5pVKAqCkLwBtcSVnJ5aUJwTlV4Tnp6YzBTZWJ6ay1aVzB3cnRDRS13YTRkanNVWUM0dms2YTgyVW4zLTYtU0hPWjdzWjZLdUhPd0t3eklDN0I1UU96OUItbnAtTjBNQ1lBIIEC; bili_jct=266ca16113aa2cb417ddcff21279c512; DedeUserID=312026488; DedeUserID__ckMd5=27339ecc5e827bcd; bp_t_offset_312026488=1014901081282445312; home_feed_column=4; browser_resolution=1192-902; b_lsid=8546EE110_194021E3429; CURRENT_FNVAL=2000; sid=g7ijxs54",
]
# Bilibili的COOKIE获取的方法见README.md 支持多账号

PUSH_OR_NOT = False
TOKEN = ''
# PUSH PLUS的TOKEN 官网为https://www.pushplus.plus

WECHAT_PUST_OR_NOT = True
# 默认关闭企业微信推送

WECHAT_ID = os.environ.get('WECHAT_ID')
# 企业ID
WECHAT_SECRET = os.environ.get('WECHAT_SECRET')
# 企业应用secret
WECHAT_APP_ID = os.environ.get('WECHAT_APP_ID')
# 企业应用的id
# 企业应用推送 文档https://developer.work.weixin.qq.com/document/path/90236

SERVER_PUSH_OR_NOT = False
SERVER_KEY = ""
# 是否开启sever酱,有填写则推送,空字符串则不推送 https://sct.ftqq.com/sendkey获取key
