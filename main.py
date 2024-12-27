"""
Author: Wyatt1026
Project Address: https://github.com/Wyatt1026/BilibiliDailyUp
"""


from core.bilibili import Bilibili
from config import config
import os

if __name__ == '__main__':
    if config.USE_ENVIRONMENT_VARIABLE:
        cookies = os.environ.get('COOKIES')
        ck_list = cookies.split(",")
    else:
        ck_list = config.COOKIE_LIST
    
    for ck in ck_list:
        bilibili = Bilibili(ck)
        bilibili.go() 
        
    
