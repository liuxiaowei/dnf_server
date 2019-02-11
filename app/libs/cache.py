import functools

from flask import g
from flask_cache import Cache


cache = None

def init_api_cache(flask_app):
    global cache
    cache = Cache(flask_app, config={'CACHE_TYPE': 'redis'})



def userinfo_cache_key():
    key = 'view_userinfo_{}'.format(g.user.id)
    return key



def clear_userinfo_cache(func):
    @functools.wraps(func)
    def wrapper():
        rv = func()
        cache.delete(userinfo_cache_key())
        return rv
    return wrapper

