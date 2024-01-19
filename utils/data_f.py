"""
formate the data  output in terminal
"""

import time


def time_f(timestamp):
    time_dict = time.localtime(timestamp / 1000)
    _time = time.strftime('%Y-%m-%d', time_dict)
    return _time


