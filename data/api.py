"""
the api for bilibili
"""

from enum import Enum


class Api(Enum):
    info_url = 'http://api.bilibili.com/x/space/myinfo'
    coin_url = 'http://account.bilibili.com/site/getCoin'
    inquire_url = 'https://api.bilibili.com/x/member/web/exp/reward'
    get_video_list_url = 'https://api.bilibili.com/x/space/wbi/arc/search?{}'
    watch_video_url = 'https://api.bilibili.com/x/click-interface/web/heartbeat'
    share_video_url = 'https://api.bilibili.com/x/web-interface/share/add'
    insert_coins_url = 'https://api.bilibili.com/x/web-interface/coin/add'
    live_sign_url = 'https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign'
    live_info_url = 'https://api.live.bilibili.com/xlive/web-ucenter/user/get_user_info'
    silver2coin_url = 'https://api.live.bilibili.com/xlive/revenue/v1/wallet/silver2coin'
    comics_sign_url = 'https://manga.bilibili.com/twirp/activity.v1.Activity/ClockIn'
    comics_check_url = "https://manga.bilibili.com/twirp/activity.v1.Activity/GetClockInInfo"

