"""
Contains data for sending post requests
"""
from enum import Enum


class PostData(Enum):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "keep-alive",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4728.0 Safari/537.36 Edg/98.0.1093.6"}

    insert_coin_headers = {
        'authority': 'api.bilibili.com',
        'method': 'POST',
        'path': '/x/web-interface/coin/add',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '94',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '',
        'priority': 'u=1, i',
        'origin': 'https://www.bilibili.com',
        'referer': 'https://www.bilibili.com/video/BV19iSoYEEmp/?spm_id_from=333.999.0.0&vd_source=5c112284a27b3ea53056fcb5622c2c75',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',

    }
    comics_sign_header = {
        "Cookie": '',
        "Content-Type": "application/x-www-form-urlencoded"
    }

    video_list_headers = {
        'authority': 'api.bilibili.com',
        'method': 'GET',
        'path': '',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '',
        'origin': 'https://space.bilibili.com',
        'priority': 'u=1, i',
        'referer': 'https://space.bilibili.com/431316421/video',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "macOS",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    para_headers = {
        'authority': 'api.bilibili.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    live_sign_headers = {
        'authority': 'api.bilibili.com',
        'method': 'GET',
        'path': '/xlive/web-ucenter/v1/sign/DoSign',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '',
        'origin': 'https://space.bilibili.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "macOS",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
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
        'cross_domain': True,
        'eab_x': 2,
        'ramval': 0,
        'source': 'web_normal',
        'ga': 1,
        'csrf': '',
    }
    silver_to_coin_data = {
        'csrf_token': '',
        'csrf': ''
    }
    comics_sign_data = {
        "platform": "android"
    }
