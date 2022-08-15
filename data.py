'''
Author: ForMemRS
Date: 2022-07-16 19:38:08
LastEditors: ForMemRS
LastEditTime: 2022-07-16 19:38:14
FilePath: /bilibili_daily/data.py
Blog: https://www.52pojie.cn/?1507943
Copyright (c) 2022 by ForMemRs, All Rights Reserved. 
'''


headers = {"Content-Type": "application/x-www-form-urlencoded",
                "Connection": "keep-alive",
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4728.0 Safari/537.36 Edg/98.0.1093.6'}
insert_coin_headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '94',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '',
    'origin': 'https://www.bilibili.com',
    'referer': 'https://www.bilibili.com/video/BV1MT411G7fG?vd_source=1970993e2eff4af7be029aefcfa468b8',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',

}
watch_video_data = {
    'bvid': '',
    'played_time': '',
    'csrf': ''
}
share_video_data = {
    'bvid': '',
    'csrf': ''
}
insert_coin_data = {
    'aid': '',
    'multiply': 1,
    'select_like': 1,
    'cross_domain': 'true',
    'csrf': ''
}
silver2coin_data = {
    'csrf_token': '',
    'csrf': ''
}