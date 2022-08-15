'''
Author: ForMemRS
Date: 2022-07-16 19:28:42
LastEditors: ForMemRS
LastEditTime: 2022-07-16 19:29:14
FilePath: /bilibili_daily/index.py
Blog: https://www.52pojie.cn/?1507943
Copyright (c) 2022 by ForMemRs, All Rights Reserved. 
'''

from bilibili import Bilibili


def main_handler(*args):  # 腾讯云函数
    bilibili = Bilibili()
    bilibili.go()
