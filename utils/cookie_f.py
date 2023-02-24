"""
formate the cookies from the user input in config/config.py
"""


def formate_cookie(cookie: str):
    """
    formate the cookie from string to dict
    """
    cookie_dict = dict([l.split("=", 1) for l in cookie.split("; ")])
    return cookie_dict


def get_csrf(ck: str) -> str:
    """
    get the csrf value from cookie
    """
    cookie_dict = formate_cookie(ck)
    csrf = cookie_dict['bili_jct']
    return csrf
