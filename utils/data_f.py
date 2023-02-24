"""
formate the data  output in terminal
"""

import time
from random import randint


def print_f(content):
    _time = time.strftime('%H:%M:%S', time.localtime())
    print(f'[{_time}]INFO: {content}')


def time_f(timestamp):
    time_dict = time.localtime(timestamp / 1000)
    _time = time.strftime('%Y-%m-%d', time_dict)
    return _time


def random_video_para(video_list: list) -> tuple:
    """
    Randomly selected videos
   """
    random_int = randint(0, len(video_list) - 1)
    bvid = video_list[random_int]['bvid']
    title = video_list[random_int]['title']
    author = video_list[random_int]['author']
    aid = video_list[random_int]['aid']
    return bvid, title, author, aid