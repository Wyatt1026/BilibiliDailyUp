"""
Contains data for sending post requests
"""
from enum import Enum


class PostData(Enum):
    HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "keep-alive",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4728.0 Safari/537.36 Edg/98.0.1093.6"
    }

    INSERT_COIN_HEADERS = {
        'authority': 'api.bilibili.com',
        'method': 'POST',
        'path': '/x/web-interface/coin/add',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '94',
        'content-type': 'application/x-www-form-urlencoded',
        'priority': 'u=1, i',
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

    COMICS_SIGN_HEADER = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    VIDEO_LIST_HEADERS = {
        'authority': 'api.bilibili.com',
        'method': 'GET',
        'path': '',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://space.bilibili.com',
        'priority': 'u=1, i',
        'referer': 'https://space.bilibili.com/268941858/video',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "macOS",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    PARA_HEADERS = {
        'authority': 'api.bilibili.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
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

    LIVE_SIGN_HEADERS = {
        'authority': 'api.bilibili.com',
        'method': 'GET',
        'path': '/xlive/web-ucenter/v1/sign/DoSign',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
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

    WATCH_VIDEO_DATA = {
        'bvid': '',
        'played_time': '',
        'csrf': ''
    }

    SHARE_VIDEO_DATA = {
        'bvid': '',
        'csrf': ''
    }

    INSERT_COIN_DATA = {
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

    SILVER_TO_COIN_DATA = {
        'csrf_token': '',
        'csrf': ''
    }

    COMICS_SIGN_DATA = {
        "platform": "android"
    }

    @classmethod
    def get(cls, name: str):
        """Safe getter to access PostData values by name."""
        try:
            return cls[name.upper()].value
        except KeyError:
            raise ValueError(f"PostData has no entry named '{name}'")
