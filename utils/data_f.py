"""
formate the data  output in terminal
"""

import time
from random import randint
import logging

logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为INFO
    format='%(asctime)s [%(levelname)s] %(message)s',  # 定义日志输出格式
    handlers=[
        logging.FileHandler('app.log'),  # 将日志写入文件
        logging.StreamHandler()  # 将日志打印到控制台
    ]
)

def print_f(content):
    """
    将内容打印到日志以及控制台，执行完毕后会将日志文件写到运行目录，如果不需要写入将 logging.FileHandler('app.log'),这一行注释即可

    参数:
        content (str): 要打印到日志的内容
    """

    #原来的写法在阿里云函数中无法打印日志，故而重写
    #_time = time.strftime('%H:%M:%S', time.localtime())
    #print(f'[{_time}]INFO: {content}')

    # 获取根日志记录器
    logger = logging.getLogger()
    logger.info(content)


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