"""
The API for Bilibili
"""

from enum import StrEnum


class Api(StrEnum):
    NAV_URL = 'https://api.bilibili.com/x/web-interface/nav'
    INFO_URL = 'http://api.bilibili.com/x/space/myinfo'
    COIN_URL = 'http://account.bilibili.com/site/getCoin'
    INQUIRE_URL = 'https://api.bilibili.com/x/member/web/exp/reward'
    GET_VIDEO_LIST_URL = 'https://api.bilibili.com/x/space/wbi/arc/search?{}'
    WATCH_VIDEO_URL = 'https://api.bilibili.com/x/click-interface/web/heartbeat'
    SHARE_VIDEO_URL = 'https://api.bilibili.com/x/web-interface/share/add'
    INSERT_COINS_URL = 'https://api.bilibili.com/x/web-interface/coin/add'
    LIVE_SIGN_URL = 'https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign'
    LIVE_SLIVER_NUM_URL = 'https://api.live.bilibili.com/xlive/web-ucenter/user/get_user_info'
    SILVER_TO_COIN_URL = 'https://api.live.bilibili.com/xlive/revenue/v1/wallet/silver2coin'
    COMICS_SIGN_URL = 'https://manga.bilibili.com/twirp/activity.v1.Activity/ClockIn'
    COMICS_SIGN_STATUS_URL = 'https://manga.bilibili.com/twirp/activity.v1.Activity/GetClockInInfo'
