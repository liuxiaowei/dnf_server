from functools import wraps

from flask import g

from app.libs.error import APIError
from app.libs.http_utils import get_json_arg, get_qs_arg
from app.models import TOrderCard
from app.libs.error_code import *


def order_permission_r(f):
    @wraps(f)
    def _wrapper():
        order_id = get_qs_arg('id', parser=int)

        order = TOrderCard.get_by_id(order_id)
        if g.user.id not in (order.userid, order.ad_owner_userid):
            raise APIError(code=OrderErrorCode.PERMISSION_DENY.value)

        rv = f()
        return rv
    return _wrapper



def order_permission_w(f):
    @wraps(f)
    def _wrapper():
        order_id = get_json_arg('order_id', parser=int)

        order = TOrderCard.get_by_id(order_id)
        if g.user.id not in (order.userid, order.ad_owner_userid):
            raise APIError(code=OrderErrorCode.PERMISSION_DENY_TO_OPERATE.value)

        rv = f()
        return rv
    return _wrapper