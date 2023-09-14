"""
formate the cookies from the user input in config/config.py
"""


def format_cookie(cookie: str) -> dict:
    """
    Format the cookie from string to dict.
    """
    return {k: v for k, v in (item.split("=", 1) for item in cookie.split("; "))}



def get_csrf(ck: str) -> str:
    """
    get the csrf value from cookie
    """
    cookie_dict = format_cookie(ck)
    csrf = cookie_dict['bili_jct']
    return csrf
