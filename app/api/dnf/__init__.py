from flask import Blueprint, request, current_app, g
from app.libs.error import HTTPError
from app.libs.redis_client import get_redis
from app.libs.error_code import *


dnf_bp = Blueprint("dnf", __name__)
from app.api.dnf import user
from app.api.dnf import config

NO_CHECK_URLS = ['/user/query', '/user/register', '/config/defines', '/config/user', '/user/reset_password',
                 '/user/send_code', '/defines', '/config/footer', ]


def need_check():
    api_path = request.path[1:]
    for item in NO_CHECK_URLS:
        if item in api_path:
            return False
    return True


def set_language():
    language = request.headers.get('ITUNES-LANGUAGE', 'zh-CN')
    language = language.lower()
    language = language.split('-')
    g.language = '_'.join(language)


@dnf_bp.before_request
def before_request_hook():
    set_language()

    if not need_check():
        return

    uid = request.headers.get('ITUNES-UID')
    if not uid:
        raise HTTPError(ret=CommonErrorCode.NO_HEADERS.value, status_code=401, field='ITUNES-UID')

    try:
        uid = int(uid)
    except Exception:
        raise HTTPError(ret=CommonErrorCode.INVALID_HEADERS.value, status_code=401, field='ITUNES-UID')

    try:
        user = TUser.get_by_id(uid)
    except:
        raise HTTPError(ret=CommonErrorCode.NO_USER.value, status_code=401)

    token = request.headers.get('ITUNES-TOKEN')
    if not token:
        raise HTTPError(ret=CommonErrorCode.NO_HEADERS.value, status_code=401, field='ITUNES-TOKEN')

    redis_key = 'user:token:{}'.format(uid)
    check_user_token = current_app.config['CHECK_USER_TOKEN']
    if check_user_token:
        db_token = get_redis().get(redis_key)
        if not db_token:
            raise HTTPError(ret=CommonErrorCode.NO_TOKEN.value, status_code=401)

        db_token = db_token.decode('utf-8') if isinstance(db_token, bytes) else db_token
        if db_token != token:
            raise HTTPError(ret=CommonErrorCode.VERIFY_USER_FAILED.value, status_code=401)

    get_redis().expire(redis_key, 60 * 60)
    g.token = token
    g.user = user
    return
