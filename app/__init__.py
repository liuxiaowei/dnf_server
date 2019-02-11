import os
import time

from flask import Flask, g, current_app
from sqlalchemy import engine, event
from raven.contrib.flask import Sentry

from app.config import config
from app.models.base import db
from app.libs.cache import init_api_cache
from app.libs.log import init_app_logger, APP_LOGGER
from app.libs.error import APIError, HTTPError, api_error_handler, http_error_handler, generic_exception_handler
from app.libs.hooks import before_request_handler, after_request_handler, before_first_request_handler
from app.libs.mail import init_mail
from app.libs.redis_client import init_redis_client


def init_config(flask_app):
    run_mode = os.environ.get('ITUNES_RUN_MODE', 'test')
    print('run mode: {}'.format(run_mode))

    flask_app.config.from_object(config[run_mode])
    flask_app.config['RUN_MODE'] = run_mode

def init_logger(flask_app):
    init_app_logger(flask_app)


def init_sentry(flask_app):
    sentry_enable = flask_app.config.get('SENTRY_ENABLE', False)
    if sentry_enable:
        Sentry(flask_app, dsn='https://2ef721a502174765ad14d561578ed4fa:2a0a702a56ab45fe97f8c3bb8e08f2f9@sentry.io/1223613')


def init_db(flask_app):
    db.init_app(flask_app)


def init_error_handlers(flask_app):
    flask_app.register_error_handler(APIError, api_error_handler)
    flask_app.register_error_handler(HTTPError, http_error_handler)
    flask_app.register_error_handler(Exception, generic_exception_handler)


def init_hooks(flask_app):
    flask_app.before_first_request(before_first_request_handler)
    flask_app.before_request(before_request_handler)
    flask_app.after_request(after_request_handler)


def init_redis(flask_app):
    init_redis_client(flask_app)

def init_sqlalchemy_event():
    @event.listens_for(engine.Engine, 'before_cursor_execute')
    def before_cursor_execute(conn, cursor, statement, parameters,
                              context, exceutemany):
        context.query_start_ts = int(time.time() * 1000)

    @event.listens_for(engine.Engine, 'after_cursor_execute')
    def after_cursor_execute(conn, cursor, statement, parameters,
                             context, exceutemany):
        cost = int(time.time() * 1000) - context.query_start_ts
        str_statement = statement.replace('\n', ' ')
        sql_log = '[cost: {}ms]sql: {}'.format(cost, str_statement)
        APP_LOGGER.debug(sql_log)


def init_cache(flask_app):
    init_api_cache(flask_app)


def register_blueprints(flask_app):
    from app.api.itunes_trade import itunes_trade_bp

    flask_app.register_blueprint(itunes_trade_bp, url_prefix='/dnf')



def create_app():
    flask_app = Flask(__name__)
    init_config(flask_app)
    init_logger(flask_app)
    init_sentry(flask_app)
    init_db(flask_app)
    init_redis(flask_app)
    init_error_handlers(flask_app)
    init_hooks(flask_app)
    init_sqlalchemy_event()
    init_mail(flask_app)
    init_cache(flask_app)
    register_blueprints(flask_app)

    APP_LOGGER.info('app初始化完成')

    return flask_app
