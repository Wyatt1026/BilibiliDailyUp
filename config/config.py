"""
The config for this script, you can read the description in README.md
"""

LIKE_OR_NOT = True
# 投币时是否点赞

USE_ENVIRONMENT_VARIABLE = True
# 从环境变量中读取CK 确保已经设置环境变量BILIBILI 只支持单个账号

COIN_OR_NOT = True
# 是否投币

COIN_NUM = 5
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
# 新华网 人民日报 央视频  王冰冰 英雄联盟赛事

COOKIE_LIST = [
    r"buvid3=FD30E0D6-F5FD-6ABD-1188-5EE86578FE9751466infoc; b_nut=1717163951; _uuid=10884FDBB-57D3-73EB-16F4-77753CE34610852125infoc; enable_web_push=DISABLE; header_theme_version=CLOSE; DedeUserID=312026488; DedeUserID__ckMd5=27339ecc5e827bcd; rpdid=|(Y|l)k)JR)0J'u~u~uYR|mu; hit-dyn-v2=1; buvid4=91DFF52E-C49D-EE32-CD95-366C8CD3DC3455694-023122509-Qe3B8WAIjlAEG%2FR1%2FY3v3Q%3D%3D; fingerprint=73d197823a405b732d45dae4dc3891d7; buvid_fp_plain=undefined; buvid_fp=73d197823a405b732d45dae4dc3891d7; home_feed_column=4; CURRENT_QUALITY=80; enable_feed_channel=ENABLE; browser_resolution=1380-754; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDI3Mjc3MTYsImlhdCI6MTc0MjQ2ODQ1NiwicGx0IjotMX0.rwXxG-glHHJr0rv0Le6nZmGHmRyb3xq8M3dn4SBWsVU; bili_ticket_expires=1742727656; SESSDATA=b18814ea%2C1758020517%2C3a31f%2A32CjDGdfDf-Fd6jGjxthFw9Gjp56NmKydXaNFeaGMAxtq4PtFz7SRdgTSOVfhzdZ8ZUP4SVlpkSnRjc3JtX1FsVnNwTVFIYVRuS1d4OGVBQVdmZTUxS3pMcUUwVzRkNlpFWElnbHMwZXJGN2dmcGNkTVJPVlZEWUlHRDFoRTNtRnkwVC1IenA3Szh3IIEC; bili_jct=8f41c69aa17c2c5a3a5f0ecb78bfae8a; sid=58irmn1r; CURRENT_FNVAL=2000; LIVE_BUVID=AUTO6417426359549477; PVID=2; bp_t_offset_312026488=1047422672432005120; b_lsid=3210D101089_195C1F6EA08"
]
# Bilibili的COOKIE获取的方法见README.md 支持多账号

PUSH_OR_NOT = False
TOKEN = ''
# PUSH PLUS的TOKEN 官网为https://www.pushplus.plus

WECHAT_PUST_OR_NOT = False
# 默认关闭企业微信推送

WECHAT_ID = ""
# 企业ID
WECHAT_SECRET = ""
# 企业应用secret
WECHAT_APP_ID = ""
# 企业应用的id
# 企业应用推送 文档https://developer.work.weixin.qq.com/document/path/90236

SERVER_PUSH_OR_NOT = False
SERVER_KEY = ""
# 是否开启sever酱,有填写则推送,空字符串则不推送 https://sct.ftqq.com/sendkey获取key
