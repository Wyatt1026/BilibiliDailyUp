'''
Author: ForMemRS
Date: 2022-07-16 19:38:29
LastEditors: ForMemRS
LastEditTime: 2022-07-16 19:38:33
FilePath: /bilibili_daily/utools.py
Blog: https://www.52pojie.cn/?1507943
Copyright (c) 2022 by ForMemRs, All Rights Reserved. 
'''

import time

def formate_print(content):
    _time = time.strftime('%H:%M:%S', time.localtime())
    print(f'[{_time}]INFO: {content}')


def formate_time(timestamp):
    time_dict = time.localtime(timestamp / 1000)
    _time = time.strftime('%Y-%m-%d', time_dict)
    return _time