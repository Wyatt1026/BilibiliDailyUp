"""
Author: Wyatt1026
Project Address: https://github.com/Wyatt1026/BilibiliDailyUp
"""


from core.bilibili import Bilibili


if __name__ == '__main__':
    bilibili = Bilibili()
    bilibili.go()
    
def main_handler(*args):  # 腾讯云函数
    bilibili = Bilibili()
    bilibili.go()
