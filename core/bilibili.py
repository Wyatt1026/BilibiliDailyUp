"""
core function for scripts
"""

from request.bilibili_http import BilibiliHttp
from utils.utils import BilibiliUtils
from logger.logger import BilibiliLogger
from config import config

from time import sleep


class Bilibili:
    """
    Bilibili的等级升级脚本
    你每天可以获得65个经验值
    """

    def __init__(self, ck) -> None:
        self.logger = BilibiliLogger(name='Bilibili每日一键脚本')
        self.ck = ck

    def is_insert(self):
        coin_num = BilibiliHttp.get_coins(self.ck)
        return config.COIN_OR_NOT and coin_num >= 5

    def insert_coins(self) -> int:
        video_list = BilibiliHttp.get_video_list(self.ck,config.UID_LIST)
        bvid, title, author, aid = BilibiliUtils.random_video_para(video_list)
        self.logger.info(f'开始向{author}的视频{title}投币……')
        coin_res = BilibiliHttp.insert_coin(self.ck,aid,config.LIKE_OR_NOT)
        return coin_res

    @staticmethod
    def get_insert_num(has_inserted_num):
        if config.COIN_NUM == -1:
            insert_num = int((50 - has_inserted_num) / 10)
        else:
            insert_num = config.COIN_NUM
        return insert_num

    def do_insert_coin(self, strict_mode, has_inserted_num):
        if not self.is_insert():
            self.logger.info('投币任务已跳过～')
            return
        self.logger.info('投币任务未完成,即将开始投币任务')
        insert_num = Bilibili.get_insert_num(has_inserted_num)
        self.logger.info(f'本次投币任务数量:{insert_num}')
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
                self.logger.info(f'当前投币成功{success_count},失败{fail_count}次')
                sleep(1)
        else:
            for x in range(0, insert_num):
                self.insert_coins()
                sleep(1)
        self.logger.info(f'每日投币:完成~获得{insert_num * 10}点经验值')

    def do_share_video(self):
        video_list = BilibiliHttp.get_video_list(self.ck,config.UID_LIST)
        bvid, title, author, aid = BilibiliUtils.random_video_para(video_list)
        self.logger.info(f'开始分享{author}的视频{title}……')
        BilibiliHttp.share_video(self.ck,bvid)
        self.logger.info('分享视频任务完成～')

    def do_watch_video(self):
        video_list = BilibiliHttp.get_video_list(self.ck,config.UID_LIST)
        bvid, title, author, aid = BilibiliUtils.random_video_para(video_list)
        self.logger.info(f'开始观看{author}的视频{title}……')
        BilibiliHttp.watch_video(self.ck,bvid)
        self.logger.info('观看视频任务完成～')


    def do_job(self) -> None:
        self.logger.start()
        if not BilibiliHttp.verify_ck(self.ck):
            self.logger.warning("cookie 无效任务终止...")
            return
        self.logger.info('cookie有效即将开始查询任务……')
        self.logger.info('=========开始任务=========')
        tasks = BilibiliHttp.inquire_tasks(self.ck)

        self.do_watch_video() if tasks["watch"] else self.logger.info("观看视频任务已完成～")
        self.do_share_video() if tasks["share"] else self.logger.info("分享视频任务已完成～")
        self.do_insert_coin(config.STRICT_MODE,tasks["coins"]) if tasks["coins"]!=50 else self.logger.info("投币任务已完成～")

        #活动已经失效
        # self.logger.info('=========直播签到========')
        # live_sign_res = BilibiliHttp.live_sign(self.ck)
        # self.logger.info(live_sign_res)

        self.logger.info('=========银瓜子转硬币========')
        if config.SILVER2COIN_OR_NOT and BilibiliHttp.inquire_silver_num(self.ck) > 700:
            silver_to_coin_res = BilibiliHttp.silver_to_coins(self.ck)
            if silver_to_coin_res:
                self.logger.info(f"转换成功～")
            else:
                self.logger.info(f"转换失败!")
        else:
            self.logger.info('银瓜子转换币:跳过~')



        self.logger.info('=========以下是个人信息=========')
        user_info = BilibiliHttp.get_user_info(self.ck)
        self.logger.info(user_info)
        self.logger.end()

