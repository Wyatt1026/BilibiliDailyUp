"""
The http request for bilibili
"""
from data.api import Api
from data.post_data import PostData
from utils.utils import BilibiliUtils

from random import choice, randint
import requests


class BilibiliHttp:

    @staticmethod
    def verify_ck(ck: str):
        """
        verify the cookie is valid or not
        """
        if BilibiliHttp.get_coins(ck) == -1:
            return False
        return True

    @staticmethod
    def get_coins(ck: str) -> int:
        """
        get the coin num
        """
        try:
            resp = requests.get(url=Api.COIN_URL, headers=PostData.get("video_list_headers"),
                                cookies=BilibiliUtils.parse_ck(ck)).json()
            return resp['data']['money']
        except Exception as e:
            print(str(e))
            return -1

    @staticmethod
    def inquire_tasks(ck: str) -> dict:
        """
        inquire the tasks status
        {'code': 0, 'message': '0', 'ttl': 1, 'data': {'login': True, 'watch': True, 'coins': 0, 'share': False, 'email': False, 'tel': True, 'safe_question': False, 'identify_card': False}}

        """
        try:
            inquire_res = requests.get(
                url=Api.INQUIRE_URL,
                headers=PostData.get("headers"),
                cookies=BilibiliUtils.parse_ck(ck)).json()
            return inquire_res['data']
        except Exception as e:
            print(str(e))
            return {}

    @staticmethod
    def get_user_info(ck: str) -> str:
        """
        get the user info
        """
        try:
            info_res = requests.get(
                url=Api.INFO_URL,
                headers=PostData.get("headers"),
                cookies=BilibiliUtils.parse_ck(ck)).json()
            uid = info_res['data']['mid']
            name = info_res['data']['name']
            level = info_res['data']['level']
            current_exp = info_res['data']['level_exp']['current_exp']
            next_exp = info_res['data']['level_exp']['next_exp']
            diff_exp = next_exp - current_exp
            up_days = int(diff_exp / 65) if diff_exp > 0 else 0
            coin_num = info_res['data']['coins']
            info_content = (f"用户{name}, uid为{uid},\n"
                            f"您目前的等级是{level}级,目前的经验{current_exp},\n"
                            f"离下个等级还差{diff_exp}经验,需要{up_days}天,\n"
                            f"剩余硬币还有{coin_num}个")
            return info_content
        except Exception as e:
            print(str(e))
            return str(e)

    def share_video(ck: str, bvid: str) -> bool:
        """
        share the video
        """
        try:
            share_video_data = PostData.get("share_video_data")
            share_video_data['bvid'] = bvid
            share_video_data['csrf'] = BilibiliUtils.get_csrf(ck)
            share_video_res = requests.post(url=Api.SHARE_VIDEO_URL,
                                            headers=PostData.get("headers"),
                                            data=share_video_data,
                                            cookies=BilibiliUtils.parse_ck(ck)).json()
            return share_video_res['code'] == 0
        except Exception as e:
            print(str(e))
            return False

    @staticmethod
    def insert_coin(ck: str, aid: str, like: bool) -> bool:
        insert_coin_data = PostData.get("insert_coin_data")
        insert_coin_headers = PostData.get("insert_coin_headers")
        insert_coin_data['aid'] = aid
        insert_coin_data['csrf'] = BilibiliUtils.get_csrf(ck)
        if not like:
            insert_coin_data['select_like'] = 0
        try:
            insert_coin_res = requests.post(
                url=Api.INSERT_COINS_URL,
                headers=insert_coin_headers,
                data=insert_coin_data,
                cookies=BilibiliUtils.parse_ck(ck)).json()
            res = insert_coin_res['data']['like']
            return res
        except Exception as e:
            print(str(e))
            return False

    # @staticmethod
    # def live_sign(ck: str) -> str:
    #     try:
    #         res = requests.get(url=Api.LIVE_SIGN_URL,
    #                            headers=PostData.get('live_sign_headers'),
    #                            cookies=BilibiliUtils.parse_ck(ck)).json()
    #         print(res)
    #         if res['code'] == 0:
    #             text = res['data']['text']
    #             sign_days = res['data']['hadSignDays']
    #             live_sign_res = f'签到奖励:{text},连续签到{sign_days}天'
    #         else:
    #             live_sign_res = '直播签到:当天已签到~'
    #         return live_sign_res
    #     except Exception as e:
    #         print(str(e))
    #         return str(e)

    @staticmethod
    def inquire_silver_num(ck: str) -> int:
        res = requests.get(url=Api.LIVE_SLIVER_NUM_URL,
                           headers=PostData.get('headers'),
                           cookies=BilibiliUtils.parse_ck(ck)).json()
        silver_num = res['data']['silver']
        return silver_num

    @staticmethod
    def silver_to_coins(ck: str) -> bool:
        """
            get silver coins
        """
        try:
            silver_data = PostData.get('silver_to_coin_data')
            silver_data['csrf'] = BilibiliUtils.get_csrf(ck)
            silver_data['csrf_token'] = BilibiliUtils.get_csrf(ck)
            res = requests.post(url=Api.SILVER_TO_COIN_URL,
                                headers=PostData.get('para_headers'),
                                cookies=BilibiliUtils.parse_ck(ck),
                                data=silver_data).json()
            if res['code'] == 403:
                return False
            return True
        except Exception as e:
            print(str(e))
            return False

    # @staticmethod
    # def get_comics_sign_status(ck:str) -> bool:
    #     """
    #     check the comics sign status
    #     """
    #     comics_header = PostData.get('comics_sign_header')
    #     comics_header['Cookie'] = ck
    #     res = requests.post(url=Api.COMICS_SIGN_STATUS_URL,
    #                         headers=comics_header,
    #                         cookies=BilibiliUtils.parse_ck(ck)).json()
    #     print(res)
    #     time.sleep(1000)
    #     return res['data']['status']
    #
    # @staticmethod
    # def comics_sign(ck:str) -> bool:
    #     res = requests.post(Api.COMICS_SIGN_URL,
    #                             headers=PostData.get('comics_sign_header'),
    #                             data=PostData.get('comics_sign_data'),
    #                             cookies=BilibiliUtils.parse_ck(ck)).json()
    #     print(res)
    #     time.sleep(1000)
    #     return res.get('code', 0) == 0
    #
    def get_video_list(ck: str, uid: list) -> list:
        uid_list = uid
        random_uid = choice(uid_list)
        headers = PostData.get("video_list_headers")
        query = BilibiliUtils.get_query(ck=ck, mid=random_uid, ps=30, pn=1)
        headers['path'] = f'/x/space/wbi/arc/search?{query}'
        try:
            video_res = requests.get(url=Api.GET_VIDEO_LIST_URL.value.format(query),
                                     headers=headers,
                                     cookies=BilibiliUtils.parse_ck(ck)).json()
            video_list = video_res["data"]["list"]["vlist"]
            return video_list
        except Exception as e:
            print(str(e))
            return []

    @staticmethod
    def watch_video(ck: str, bvid: str) -> bool:
        try:
            watch_time = randint(30, 60)
            watch_video_data = PostData.get("watch_video_data")
            watch_video_data['bvid'] = bvid
            watch_video_data['played_time'] = str(watch_time)
            watch_video_data['csrf'] = BilibiliUtils.get_csrf(ck)
            watch_video_res = requests.post(
                url=Api.WATCH_VIDEO_URL,
                headers=PostData.get('headers'),
                data=watch_video_data,
                cookies=BilibiliUtils.parse_ck(ck)).json()
            return watch_video_res['code'] == 0
        except Exception as e:
            print(str(e))
            return False
