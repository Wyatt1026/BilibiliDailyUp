from random import choice
from config import config


def random_video_para(video_list: list) -> tuple:
    """
    Randomly selected videos
   """
    selected_video = choice(video_list)
    bvid = selected_video.get('bvid', '未知')
    title = selected_video.get('title', '无标题')
    author = selected_video.get('author', '未知作者')
    aid = selected_video.get('aid', '未知')
    return bvid, title, author, aid


def get_insert_num(coin_has_inserted_num):
    if config.COIN_NUM == -1:
        insert_num = int((50 - coin_has_inserted_num) / 10)
    else:
        insert_num = config.COIN_NUM
    return insert_num



