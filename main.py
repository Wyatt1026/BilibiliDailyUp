"""
Author: Wyatt1026
Project Address: https://github.com/Wyatt1026/BilibiliDailyUp
"""


from core.bilibili import Bilibili
from config import config
from os import environ

if __name__ == '__main__':
    if not config.USE_ENVIRONMENT_VARIABLE:
        ck_list = config.COOKIE_LIST
        for ck in ck_list:
            bilibili = Bilibili(ck)
            bilibili.go()
    else:
        ck = environ.get('BILIBILI')
        if not ck:
            print("未设置BILIBILI这个环境变量 任务终止")
        else:
            bilibili = Bilibili(ck)
            bilibili.go()
