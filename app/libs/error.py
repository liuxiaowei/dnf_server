from flask import jsonify, g
from app.libs.log import APP_LOGGER


class APIError(Exception):
    def __init__(self, code, msg=None, status_code=200, **args):
        from .http_utils import get_error_msg
        Exception.__init__(self)
        self.code = code
        self.msg = get_error_msg(code, msg, *tuple(args.values()))
        self.status_code = status_code

    def to_dict(self):
        return {'code': self.code, 'msg': self.msg, 'data': {}}


class HTTPError(Exception):
    def __init__(self, ret, msg=None,  status_code=200, **args):
        from .http_utils import get_error_msg
        super().__init__(self)
        self.ret = ret
        self.msg = get_error_msg(ret, msg, *tuple(args.values()))
        self.status_code = status_code

    def to_dict(self):
        return {'code': self.ret, 'msg': self.msg, 'data': {}}



def api_error_handler(error):
    response = jsonify(error.to_dict())
    return response, error.status_code


def generic_exception_handler(e):
    resp = jsonify({'code': -1, 'msg': '服务器内部错误{}'.format(str(e)), 'data': {}})
    resp.status_code = 500
    APP_LOGGER.error('generic exception: {}'.format(str(e)))
    return resp


def http_error_handler(error):
    response = jsonify(error.to_dict())
    return response, error.status_code