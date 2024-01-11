"""
core function for scripts
"""

import time

from core.bilibili_utils import random_video_para, get_insert_num
from utils.push import pushplus_push, wechat_push, sever_push
from core.bilibili_http import BilibiliHttp
from utils.log_f import print_f
from config import config


class Bilibili:
    """
    Bilibili的等级升级脚本
    你每天可以获得65个经验值
    """

    def __init__(self, ck) -> None:
        self.log = ''
        self.bilibili_http = BilibiliHttp(ck)

    def __push_f(self, content: str):
        temp = f'{content}</br>'
        self.log = f'{self.log}{temp}'

    def log_and_push(self, content):
        self.__push_f(content)
        print_f(content)

    def is_insert(self):
        coin_num = self.bilibili_http.get_coin_num()
        return config.COIN_OR_NOT and coin_num >= 5

    def insert_coins(self) -> int:
        video_list = self.bilibili_http.get_video_list()
        bvid, title, author, aid = random_video_para(video_list)
        self.log_and_push(f'开始向{author}的视频{title}投币……')
        coin_res = self.bilibili_http.insert_coin(aid)
        return coin_res

    def do_insert_coin(self, strict_mode, coin_has_inserted_num):
        if not self.is_insert():
            self.log_and_push('投币任务已跳过～')
            return
        self.log_and_push('投币任务未完成,即将开始投币任务')
        insert_num = get_insert_num(coin_has_inserted_num)
        self.log_and_push(f'本次投币任务数量:{insert_num}')
        success_count = 0
        fail_count = 0
        if strict_mode:
            while 1:
                coin_res = self.insert_coins()
                if success_count == 5 or fail_count == 5:
                    break
                if coin_res:
                    success_count += 1
                else:
                    fail_count += 1
                self.log_and_push(f'当前投币成功{success_count},失败{fail_count}次')
                time.sleep(1)
        else:
            for x in range(0, insert_num):
                self.insert_coins()
                time.sleep(1)
        self.log_and_push(f'每日投币:完成~获得{insert_num * 10}点经验值')

    def do_share_video(self):
        video_list = self.bilibili_http.get_video_list()
        bvid, title, author, aid = random_video_para(video_list)
        self.log_and_push(f'开始分享{author}的视频{title}……')
        self.bilibili_http.share_video(bvid)
        self.log_and_push('分享视频任务已完成～')

    def do_watch_video(self):
        video_list = self.bilibili_http.get_video_list()
        bvid, title, author, aid = random_video_para(video_list)
        self.log_and_push(f'开始观看{author}的视频{title}……')
        self.bilibili_http.watch_video(bvid)
        self.log_and_push('观看视频任务完成～')

    def handle_login(self, status):
        self.log_and_push('登陆任务已完成')

    def handle_watch_video(self, status):
        if status:
            self.log_and_push('观看视频任务已完成')
        else:
            self.log_and_push('观看视频任务未完成')
            self.do_watch_video()

    def handle_insert_coin(self, status):
        if status == 50:
            self.log_and_push('投币任务已完成')
        else:
            self.do_insert_coin(strict_mode=config.STRICT_MODE, coin_has_inserted_num=status)

    def handle_share_video(self, status):
        if status:
            self.log_and_push('分享任务已完成')
        else:
            self.log_and_push('分享任务未完成')
            self.do_share_video()

    def do_job(self) -> None:
        cookie_status = self.bilibili_http.get_cookie_status()
        if not cookie_status:
            self.log_and_push("cookie 无效任务终止...")
            return
        self.log_and_push('cookie有效即将开始查询任务……')
        self.log_and_push('=========以下是任务信息=========')
        inquire_job_res = self.bilibili_http.inquire_job()
        job_handlers = {
            'login': self.handle_login,
            'watch': self.handle_watch_video,
            'insert': self.handle_insert_coin,
            'share': self.handle_share_video,
        }
        for job_name, job_status in inquire_job_res.items():
            handler = job_handlers.get(job_name)
            handler(job_status)

        self.log_and_push('=========直播签到========')
        live_sign_res = self.bilibili_http.live_sign()
        self.log_and_push(live_sign_res)

        self.log_and_push('=========银瓜子转硬币========')
        if config.SILVER2COIN_OR_NOT and self.bilibili_http.inquire_live_info() > 700:
            silver_to_coin_res = self.bilibili_http.silver_to_coin()
            if silver_to_coin_res.get('status'):
                self.log_and_push(f"转换成功～剩余瓜子{silver_to_coin_res.get('msg')}")
            else:
                self.log_and_push(f"转换失败-{silver_to_coin_res.get('msg')}")
        else:
            self.log_and_push('银瓜子转换币:跳过~')

        self.log_and_push('=========漫画签到情况========')
        if self.bilibili_http.check_comics_sign():
            self.log_and_push("漫画签到:当天已签到~")
        else:
            if self.bilibili_http.comics_sign():
                self.log_and_push("漫画签到: 完成~")
            else:
                self.log_and_push("漫画签到: 失败~")

        self.log_and_push('=========以下是个人信息=========')
        user_info = self.bilibili_http.get_info()
        self.log_and_push(user_info)

    def go(self) -> None:
        """
        Entrance function
        """
        self.do_job()
        if config.PUSH_OR_NOT:
            pushplus_push(config.TOKEN, self.log)

        if config.WECHAT_PUST_OR_NOT:
            wechat_push(self.log.replace("</br>", "\n"),
                        config.WECHAT_ID,
                        config.WECHAT_SECRET,
                        config.WECHAT_APP_ID)

        if config.SERVER_PUSH_OR_NOT:
            sever_push(self.log.replace("</br>", "\n"),
                       config.SERVER_KEY)
