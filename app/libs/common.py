import string
import random
import hashlib

import time
from datetime import datetime, timedelta


def gen_verify_code(len=6):
    return ''.join(random.choice(string.digits) for _ in range(len))


def gen_token():
    str_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    m = hashlib.md5()
    raw = '%s%s' % (str_now, ''.join(random.choice(string.ascii_letters) for _ in range(12)))
    m.update(raw.encode('utf-8'))
    return m.hexdigest()


def multiple_num(num, multiple):
    if num % multiple == 0:
        return num

    r = int(num / multiple)
    return multiple * (r + 1)


def format_time(v):
    if isinstance(v, datetime):
        v = v.strftime('%Y-%m-%d %H:%M:%S')
    return v


def fmt_utc2cn(v):
    if isinstance(v, datetime):
        v += timedelta(hours=8)
        v = v.strftime('%Y-%m-%d %H:%M:%S')
    return v


def bj_time2utc(dt):
    dt = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
    dt = dt - timedelta(hours=8)
    return dt


def bj_date2utc(dt):
    #截取年月日的字符串
    dt = datetime.strptime(dt[0:10], '%Y-%m-%d')
    dt = dt - timedelta(hours=8)
    return dt
