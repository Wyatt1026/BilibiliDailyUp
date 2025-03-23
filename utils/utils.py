"""
The utils for Bilibili
"""
from data.post_data import PostData
from data.api import Api

from functools import reduce
from random import choice
from hashlib import md5
import urllib.parse
import time
import requests

class BilibiliUtils:

    mixinKeyEncTab = [
        46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49,
        33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40,
        61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11,
        36, 20, 34, 44, 52
    ]

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static utility class and cannot be instantiated.")


    @staticmethod
    def parse_ck(ck_str: str) -> dict:
        cookie_dict = {}
        for item in ck_str.split(';'):
            if '=' in item:
                key, value = item.strip().split('=', 1)
                cookie_dict[key] = value
        return cookie_dict

    @staticmethod
    def get_csrf(ck: str) -> str:
        """
        get the csrf value from cookie
        """
        cookie_dict = BilibiliUtils.parse_ck(ck)
        return cookie_dict['bili_jct']


    @staticmethod
    def time_f(timestamp):
        time_dict = time.localtime(timestamp / 1000)
        _time = time.strftime('%Y-%m-%d', time_dict)
        return _time


    @staticmethod
    def random_video_para(video_list: list) -> tuple:
        """
        Randomly selected videos
       """
        selected_video = choice(video_list)
        bvid = selected_video['bvid']
        title = selected_video['title']
        author = selected_video['author']
        aid = selected_video['aid']
        return bvid, title, author, aid


    def get_mixed_key(orig: str):
        return reduce(lambda s, i: s + orig[i], BilibiliUtils.mixinKeyEncTab, '')[:32]

    @staticmethod
    def enc_wbi(params: dict, img_key: str, sub_key: str):
        mixin_key = BilibiliUtils.get_mixed_key(img_key + sub_key)
        curr_time = round(time.time())
        params['wts'] = curr_time
        params = dict(sorted(params.items()))
        params = {
            k: ''.join(filter(lambda chr: chr not in "!'()*", str(v)))
            for k, v
            in params.items()
        }
        query = urllib.parse.urlencode(params)
        wbi_sign = md5((query + mixin_key).encode()).hexdigest()
        params['w_rid'] = str(wbi_sign)
        return params

    @staticmethod
    def get_wbi_keys(ck:str)->tuple:
        resp = requests.get(url=Api.NAV_URL,
                            headers=PostData.get("para_headers"),
                            cookies=BilibiliUtils.parse_ck(ck))
        resp.raise_for_status()
        json_content = resp.json()
        img_url: str = json_content['data']['wbi_img']['img_url']
        sub_url: str = json_content['data']['wbi_img']['sub_url']
        img_key = img_url.rsplit('/', 1)[1].split('.')[0]
        sub_key = sub_url.rsplit('/', 1)[1].split('.')[0]
        return img_key, sub_key

    @staticmethod
    def get_query(ck: str, **parameters: dict):
        img_key, sub_key = BilibiliUtils.get_wbi_keys(ck)
        signed_params = BilibiliUtils.enc_wbi(
            params=parameters,
            img_key=img_key,
            sub_key=sub_key
        )
        query = urllib.parse.urlencode(signed_params)
        return query

