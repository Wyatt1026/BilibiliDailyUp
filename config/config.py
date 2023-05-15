"""
The config for this script, you can read the description in README.md
"""


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

COOKIE_LIST = [r"buvid3=B212DE5F-21D8-165E-F277-16EFE7411D3C34728infoc; b_nut=1665194134; i-wanna-go-back=-1; _uuid=3E58257C-910A3-BA28-CEDE-26F4E3210AC4835640infoc; buvid4=F6D07EC4-B9BF-BB71-A43B-98DAAE8CD7EF36028-022100809-TSSuvLJGlEsEFDYnGZat0w%3D%3D; buvid_fp_plain=undefined; DedeUserID=400419811; DedeUserID__ckMd5=4c4a5815f6fbb057; nostalgia_conf=-1; b_ut=5; hit-dyn-v2=1; CURRENT_QUALITY=80; rpdid=0zbfvUmyH6|2qZ0vHQw|aGG|3w1OZbM8; is-2022-channel=1; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; fingerprint=b6825de596a7a65c188c3c89f6f4bda4; buvid_fp=4fd63da359c8405de43d2c8911a711a8; LIVE_BUVID=AUTO5016791992765837; header_theme_version=CLOSE; SESSDATA=35b66429%2C1695123133%2C08123%2A31; bili_jct=b4242db54c8ee4d92f402dcc4e6ea02c; CURRENT_PID=2cb8ff00-d371-11ed-a3c6-bd05e2d7d425; FEED_LIVE_VERSION=V8; PVID=1; sid=6vv1akgi; home_feed_column=4; bp_video_offset_400419811=795172397215907800; innersign=0; b_lsid=21FB1235_1881F3291EB; browser_resolution=465-764"]
# Bilibili的COOKIE获取的方法见README.md 支持多账号

PUSH_OR_NOT = False
TOKEN = ''
# PUSH PLUS的TOKEN 官网为https://www.pushplus.plus
