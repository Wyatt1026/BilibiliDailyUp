import time

import requests
import random

from core.bilibili_encrypt import get_query
from utils.cookie_f import format_ck, get_csrf
from data.post_data import PostData
from utils.data_f import time_f
from config import config
from data.api import Api


class BilibiliHttp:
    def __init__(self, ck: str):
        self.api = Api
        self.post_data = PostData
        self.session = requests.session()
        self.ck_str = ck
        self.ck = format_ck(ck)

    def get_cookie_status(self) -> bool:
        """
        check the cookie is valid or not
        """
        ck_status_res = self.session.get(url=self.api.coin_url.value,
                                        headers=self.post_data.video_list_headers.value,
                                         cookies=self.ck).json()
        code = ck_status_res.get('code', 0)
        # code equal 0 means cookie is valid
        return code == 0

    def get_coin_num(self) -> int:
        """
        get the coin num
        """
        res = self.session.get(
            url=self.api.coin_url.value, headers=self.post_data.headers.value,
            cookies=self.ck).json()
        coin_num = res.get('data', {}).get('money', 0)
        return coin_num

    def inquire_job(self) -> dict:
        """
        inquire the job status
        """
        inquire_res = self.session.get(
            url=self.api.inquire_url.value, headers=self.post_data.headers.value, cookies=self.ck).json()
        jobs = {
            'login': inquire_res['data'].get('login', False),
            'watch': inquire_res['data'].get('watch', False),
            'insert': inquire_res['data'].get('coins', False),
            'share': inquire_res['data'].get('share', False),
        }
        return jobs

    def get_info(self) -> str:
        """
        get the user info
        """
        info_res = self.session.get(
            url=self.api.info_url.value,
            headers=self.post_data.headers.value,
            cookies=self.ck).json()
        user_data = info_res.get('data', {})
        uid = user_data.get('mid', '未知')
        name = user_data.get('name', '未知')
        level = user_data.get('level', 0)
        current_exp = user_data.get('level_exp', {}).get('current_exp', 0)
        next_exp = user_data.get('level_exp', {}).get('next_exp', 0)
        sub_exp = next_exp - current_exp
        up_days = int(sub_exp / 65) if sub_exp > 0 else 0
        coin_num = user_data.get('coins', 0)
        vip_status = user_data.get('vip', {}).get('status', 0)
        vip_due_data = time_f(user_data.get('vip', {}).get('due_date', 0))

        if vip_status:
            info_content = (f"用户{name}, uid为{uid}您是大会员, "
                            f"大会员到期时间为{vip_due_data}, "
                            f"您目前的等级是{level}级, 目前的经验{current_exp}, "
                            f"离下个等级还差{sub_exp}经验, 需要{up_days}天, "
                            f"剩余硬币还有{coin_num}个")
        else:
            info_content = (f"用户{name}, uid为{uid}您的大会员已过期, "
                            f"过期时间为{vip_due_data}, "
                            f"您目前的等级是{level}级, 目前的经验{current_exp}, "
                            f"离下个等级还差{sub_exp}经验, 需要{up_days}天, "
                            f"剩余硬币还有{coin_num}个")

        return info_content

    def share_video(self, bvid: str) -> bool:
        """
        share the video
        """
        share_video_data = self.post_data.share_video_data.value
        share_video_data['bvid'] = bvid
        share_video_data['csrf'] = get_csrf(self.ck_str)
        share_video_res = self.session.post(
            url=self.api.share_video_url.value, data=share_video_data, cookies=self.ck,
            headers=self.post_data.headers.value).json()
        code = share_video_res['code']
        return code == 0

    def insert_coin(self, aid: str) -> bool:
        insert_coin_data = self.post_data.insert_coin_data.value
        insert_coin_headers = self.post_data.insert_coin_headers.value
        insert_coin_data['aid'] = aid
        insert_coin_data['csrf'] = get_csrf(self.ck_str)
        insert_coin_headers['cookie'] = self.ck_str
        if not config.LIKE_OR_NOT:
            insert_coin_data['select_like'] = 0
        insert_coin_res = self.session.post(
            url=self.api.insert_coins_url.value, headers=insert_coin_headers,
            data=insert_coin_data, cookies=self.ck).json()
        # print(insert_coin_res)
        like = insert_coin_res.get('data', {}).get('like', False)
        return like

    def live_sign(self) -> str:
        headers = self.post_data.live_sign_headers.value
        headers['cookie'] = self.ck_str
        res = self.session.get(url=self.api.live_sign_url.value,
                               headers=headers,
                               cookies=self.ck).json()
        if res.get('code') == 0:
            text = res.get('data', {}).get('text', '获得奖励信息出错啦~')
            sign_days = res.get('data', {}).get('hadSignDays', 0)

            live_sign_res = f'签到奖励:{text},连续签到{sign_days}天'
        else:
            live_sign_res = '直播签到:当天已签到~'
        return live_sign_res

    def inquire_live_info(self) -> int:
        res = self.session.get(url=self.api.live_info_url.value, headers=self.post_data.headers.value,
                               cookies=self.ck).json()
        silver_num = res.get('data', {}).get('silver', 0)
        return silver_num

    def silver_to_coin(self) -> dict:
        silver_data = self.post_data.silver_to_coin_data.value
        silver_data['csrf'] = get_csrf(self.ck_str)
        silver_data['csrf_token'] = get_csrf(self.ck_str)
        res = self.session.post(url=self.api.silver_to_coin_url.value,
                                cookies=self.ck, data=silver_data).json()
        if not res.get('code', 0):
            silver = res.get('data', {}).get('silver', 0)
            silver_to_coin_res = {"status": True, "msg": silver}
        else:
            silver_to_coin_res = {"status": False, "msg": "出错啦～"}
        return silver_to_coin_res

    def check_comics_sign(self) -> bool:
        """
        check the comics sign status
        """
        comics_header = self.post_data.comics_sign_header.value
        comics_header['Cookie'] = self.ck_str
        res = self.session.post(url=self.api.comics_check_url.value,
                                headers=comics_header,
                                cookies=self.ck).json()
        return res.get('data', {}).get('status', -1) == 0

    def comics_sign(self) -> bool:
        comics_header = self.post_data.comics_sign_header.value
        comics_header['Cookie'] = self.ck_str
        res = self.session.post(self.api.comics_sign_url.comics_sign_url.value,
                                headers=comics_header,
                                data=self.post_data.comics_sign_data.value,
                                cookies=self.ck).json()
        return res.get('code', 0) == 0

    def get_video_list(self) -> list:
        uid_list = config.UID_LIST
        random_uid = random.choice(uid_list)
        headers = self.post_data.video_list_headers.value
        query = get_query(ck=self.ck_str, mid=random_uid, ps=30, pn=1)
        headers['path'] = f'/x/space/wbi/arc/search?{query}'
        headers['cookie'] = self.ck_str
        get_video_list_url = self.api.get_video_list_url.value.format(query)
        video_res = self.session.get(url=get_video_list_url, headers=headers).json()
        video_list = video_res.get('data', {}).get('list', {}).get('vlist', [])
        return video_list

    def watch_video(self, bvid: str) -> bool:
        watch_time = random.randint(30, 60)
        watch_video_data = self.post_data.watch_video_data.value
        watch_video_data['bvid'] = bvid
        watch_video_data['played_time'] = str(watch_time)
        watch_video_data['csrf'] = get_csrf(self.ck_str)
        watch_video_res = self.session.post(
            url=self.api.watch_video_url.value, data=watch_video_data, cookies=self.ck).json()
        code = watch_video_res.get('code', 1)
        return code == 0
