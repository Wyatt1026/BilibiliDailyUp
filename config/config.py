"""
The config for this script, you can read the description in README.md
"""

LIKE_OR_NOT = True
# 投币时是否点赞

USE_ENVIRONMENT_VARIABLE = False
# 从环境变量中读取CK 确保已经设置环境变量BILIBILI 只支持单个账号

COIN_OR_NOT = True
# 是否投币

COIN_NUM = 1
# 投币数量 -1为完成所有也就是如果你已经投过1次那就只会投4次
# 如果不是 -1 则指定投币数量范围1-5

SILVER2COIN_OR_NOT = True
# 是否将银瓜子兑换为硬币


STRICT_MODE = True
# 是否开启严格模式，严格模式会保证至少5次成功投币，因为官方投币API存在缺陷，会有投币成功但是返回失败的情况
# 默认开启严格模式，如果关闭则只会投币5次，无论成功失败，会出现少投币的情况，因为可能失败，但是不会造成浪费硬币的情况，自行选择
NUM_MODE = False
# 该模式与严格模式互斥,开启此模式,投币只会投COIN_NUM次,无论成功失败

UID_LIST = ['431316421', '3546766586678158', '1794984662']
# 投币UP主的ID号,如果不修改，默认将用上面这个列表里的,可以选择自己喜欢的UP主
# 获取UID的方法见README.md
# 新华网 人民日报 央视频  王冰冰 英雄联盟赛事

COOKIE_LIST = [
    r"SESSDATA=bef42707%2C1742714866%2Cbd55c%2A92CjAuqVjFlpRLFekmlRJPAKTqzJLqw00iKQm3h1pLk_J6q0ucplZ4AYkl6h9bwgrkQ28SVmlmaE5GMVA1V1lqU0VDVTRPSmxMYXI0Q2V0cGxjX3RIeTViY0lNamVwaUNRMHNTWHRnbUh3cVhpTHU5UHFTR01lMlN1a0t6OF9oemZpTXNEcERWemJRIIEC; bili_jct=629114af80382005a8eab0677b7a98bb; DedeUserID=1794984662; DedeUserID__ckMd5=ff00be248f5441ef; sid=ptw9ioew; buvid3=8DA78115-5A0E-00CE-DE2C-E9C0335B7D8883844infoc; b_nut=1727162883",
    r"SESSDATA=c4a81736%2C1743602215%2Cb4f3e%2Aa2CjAQ5QGn16PxfkyQS1b5iiKH6F1KGVNm_94l5qdM2PNb8WPJsl0Otm35aZYXzIY8DoMSVjVfTWJiaVhMYnFKeUpDMnowLThrX0txWlp2RVE5MXJpTlhzQmg4SlpQbE95MFRaUk44c1N1eHhaaFd1SDg5WHk1M1hrMW16MU1IY0NKMjlGV2YtclRRIIEC; bili_jct=e4b5fc3519d8c1f3b4ccfcbec24319ef; DedeUserID=3546766586678158; DedeUserID__ckMd5=311e687f25e3b9b5; sid=pyrqde1b; buvid3=5A07915F-E561-586D-2CF5-1488A348142937260infoc; b_nut=1728050237",
    r"buvid3=35264C13-CFB2-DE38-C44A-F54D3C5C916610134infoc; b_nut=1728960610; _uuid=9C45FEAE-E5A3-8E12-F62A-E3833E519E10410765infoc; enable_web_push=DISABLE; buvid4=963F0DC0-0AB6-6A0F-26B0-B3BAEB3EB9C911538-024101502-pTl/QoSssHMwHTofBBTPX9jnzcD5LppC+eKteDDBvQMpv2UQ417hO0dZBXyQn9vz; buvid_fp=8741fd7b610676e58a7b650b22553b7a; DedeUserID=3546777600919923; DedeUserID__ckMd5=52f8c8280d7b52ac; header_theme_version=CLOSE; CURRENT_FNVAL=4048; home_feed_column=5; rpdid=0zbfvSbQGu|qxpYJV8m|2kf|3w1T0yl1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjk0Nzc1MzksImlhdCI6MTcyOTIxODI3OSwicGx0IjotMX0.zlyV3RZw3Mdo4FBeDjNANC_67wRqfThL0qXCopeEM0o; bili_ticket_expires=1729477479; SESSDATA=0eec1500%2C1744772199%2C4e320%2Aa1CjAcaWryw0yCzGU4OpY_X7vRWXwKzB-n9f9b5ZWiubnHq1Dpz_9q5vhkwVfxSGrEVrUSVnV1YlE4bGFTWTlYdzdkaUtZSUE5ZmlERHJzdlduYjJtQjB1MlZPQU5Rb2tONGlaaXlHdF9VOXRub2pWalRmOWFLRldPdGNsbjViZnpNNHBLUDRneW9nIIEC; bili_jct=d7417ad7f00061cf4b77ee277319ed57; sid=8vbo0khc; b_lsid=1010BB394D_192ACD2896C; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bp_t_offset_3546777600919923=990582521185959936; browser_resolution=1777-1435",
    r"buvid3=10879112-092E-AC02-E3E1-727C505B208D98619infoc; b_nut=1727862298; _uuid=12F63F68-D1078-71075-36FD-8685D7DE753699400infoc; enable_web_push=DISABLE; buvid4=96E59510-68D8-BE3F-23D6-F93CBA76DD9602285-024100209-xBCrltfYy0zks+MDWCytQutrofaTRg3Pzh/ITb6sR37FxMTLR+u91LRwLoonC68v; buvid_fp=dfe12467d3b82339c01923765a568f89; header_theme_version=CLOSE; DedeUserID=3546776470555432; DedeUserID__ckMd5=93636570af93a5ee; CURRENT_FNVAL=4048; rpdid=0zbfvSbQGu|qxp9hzR0|vO8|3w1T0i3g; CURRENT_QUALITY=80; bp_t_offset_3546776470555432=988118541397917696; b_lsid=5CEEC5610_192E5BC7E36; SESSDATA=bc2662c4%2C1745983194%2Ca6835%2Ab1CjDLOT-7p77q-YLu1omD2YkqFHbuBYgxPhhyHgxaZgyMlzKI7v6Dyga_np1RCIz9wHUSVjN4Wno0cm9FZEpaMlExQ1l3eXFXZ2dwcDRNM0N0QzZRM2hUMVo0dm9YemdrSWxsZGR4Uk1HTml1M2NWUmp1dGFwajl2aUlUV0lwazc2SGRsWVpiRWR3IIEC; bili_jct=7344dc4e19b6fd2ee623033635237300; sid=pt5ytlgk; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA2OTAzOTgsImlhdCI6MTczMDQzMTEzOCwicGx0IjotMX0.oPGWyNx7rgTaR6ul4Dj9tpaTGOBbKlHff_-IhhyU34Y; bili_ticket_expires=1730690338; home_feed_column=4; browser_resolution=400-888",
    r"SESSDATA=2ca65c1f%2C1742714747%2Cb5f86%2A92CjAa_GcFIvyt5wNTum0OtBKF9G2bIG87J4Sf4H5qxhvdvtXCM8UfaKhM60f9q579et0SVkI2cE81Ujc2aHQwcGt0SmY4TGRCRHhzRE1DY1FiZG1mRENaWFFVdndNdmV6R0xuakh1Mk5ONkk1c0wtLXdvcHYyYUdlRGVjZ3NuUnFzV3RfNDYzcTRBIIEC; bili_jct=4778f1a6218bc94a2e9fed7ad0ec98e9; DedeUserID=431316421; DedeUserID__ckMd5=8a4b6a7508bfcfca; sid=fswv209s; buvid3=703EBE82-6F9D-BCED-926B-16768B58E30266225infoc; b_nut=1727162766"
]
# Bilibili的COOKIE获取的方法见README.md 支持多账号

PUSH_OR_NOT = False
TOKEN = ''
# PUSH PLUS的TOKEN 官网为https://www.pushplus.plus

WECHAT_PUST_OR_NOT = True
# 默认关闭企业微信推送

WECHAT_ID = "wwf8996175e40b25ac"
# 企业ID
WECHAT_SECRET = "cUzqXTv-ycuxUkGoqUFoi3HLLo9Xd50GNPmKtC1lxLM"
# 企业应用secret
WECHAT_APP_ID = "1000002"
# 企业应用的id
# 企业应用推送 文档https://developer.work.weixin.qq.com/document/path/90236

SERVER_PUSH_OR_NOT = False
SERVER_KEY = ""
# 是否开启sever酱,有填写则推送,空字符串则不推送 https://sct.ftqq.com/sendkey获取key
