from flask import request, jsonify, g, current_app
from flask_sqlalchemy import Pagination

from app.libs.error import APIError
from app.libs.error_code import *


def get_error_msg(code, msg, *params):
    if msg:
        return msg


    return msg


def render_ok(data=None):
    if data is None:
        data = {}
    return jsonify({'code': 0, 'msg': '', 'data': data})


def render_error(code, msg=None, **args):
    ret_msg = get_error_msg(code, msg,  *tuple(args.values()))
    return jsonify({'code': code, 'msg': ret_msg, 'data': {}})


def get_qs_arg(name, parser=None, validator=None):
    val = request.args.get(name, None)
    if val is None:
        raise APIError(code=CommonErrorCode.MISSING_HTTP_PARAMS.value, name=name)

    if parser and callable(parser):
        try:
            val = parser(val)
        except Exception as e:
            raise APIError(code=CommonErrorCode.CONVERSION_PARAMS_FAILED.value, name=name)

    if validator and callable(validator):
        if not validator(val):
            raise APIError(code=CommonErrorCode.PARAM_ILLEGAL.value, name=name)

    return val


def get_qs_arg_default(name, default=None, parser=None, validator=None):
    val = request.args.get(name, None)
    if val is None:
        if default is not None:
            return default
        raise APIError(code=CommonErrorCode.MISSING_HTTP_PARAMS.value, name=name)

    if parser and callable(parser):
        try:
            val = parser(val)
        except Exception as e:
            raise APIError(code=CommonErrorCode.CONVERSION_PARAMS_FAILED.value, name=name)

    if validator and callable(validator):
        if not validator(val):
            raise APIError(code=CommonErrorCode.PARAM_ILLEGAL.value, name=name)

    return val


def get_json_arg(name, parser=None, validator=None):
    jdata = request.get_json(force=True, silent=True)

    if not request.is_json:
        raise APIError(code=CommonErrorCode.WRONG_DATA_FORMAT.value)

    if jdata is None:
        raise APIError(code=CommonErrorCode.WRONG_DATA_FORMAT.value)

    val = jdata.get(name, None)
    if val is None:
        raise APIError(code=CommonErrorCode.MISSING_HTTP_PARAMS.value, name=name)

    if parser and callable(parser):
        try:
            val = parser(val)
        except Exception as e:
            raise APIError(code=CommonErrorCode.CONVERSION_PARAMS_FAILED.value, name=name)

    if validator and callable(validator):
        if not validator(val):
            raise APIError(code=CommonErrorCode.PARAM_ILLEGAL.value, name=name)
    return val


def get_json_arg_default(name, default=None, parser=None, validator=None):
    jdata = request.get_json(force=True, silent=True)

    if not request.is_json:
        raise APIError(code=CommonErrorCode.WRONG_DATA_FORMAT.value)

    if jdata is None:
        raise APIError(code=CommonErrorCode.WRONG_DATA_FORMAT.value)

    val = jdata.get(name, None)
    if val is None:
        if default is not None:
            return default
        raise APIError(code=CommonErrorCode.MISSING_HTTP_PARAMS.value, name=name)

    if parser and callable(parser):
        try:
            val = parser(val)
        except Exception as e:
            raise APIError(code=CommonErrorCode.CONVERSION_PARAMS_FAILED.value, name=name)

    if validator and callable(validator):
        if not validator(val):
            raise APIError(code=CommonErrorCode.PARAM_ILLEGAL.value, name=name)
    return val


def get_paginate_params(paginator):
    if not (isinstance(paginator, Pagination)):
        return None

    return dict(
        page=paginator.page,
        pages=paginator.pages,
        has_prev=paginator.has_prev,
        prev_num=paginator.prev_num,
        has_next=paginator.has_next,
        next_num=paginator.next_num,
        page_num=paginator.per_page,
        total=paginator.total
    )