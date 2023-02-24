"""
the example for entrance file in tencentCloud
"""

from core.bilibili import Bilibili


def main_handler(*args):  # 腾讯云函数
    bilibili = Bilibili()
    bilibili.go()
