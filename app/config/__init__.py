
class Config:
    LOG_PATH = 'logs/'
    LOG_FILENAME = 'itunes.log'
    LOG_LEVEL = 'debug'

    CHECK_USER_TOKEN = True
    CHECK_ADMIN_TOKEN = True

    SENTRY_ENABLE = True
    SENTRY_DSN = 'https://2ef721a502174765ad14d561578ed4fa:2a0a702a56ab45fe97f8c3bb8e08f2f9@sentry.io/1223613'

    SQLALCHEMY_POOL_RECYCLE = 50 * 60
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Kaigedb_dev_mysql@rm-wz9bp66pjz4w72ss1ko.mysql.rds.aliyuncs.com:3306/dnf?charset=utf8'

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 6
    REDIS_PASSWORD = ''

    MAIL_SERVER = 'smtp.mxhichina.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'no-reply@utomarket.com'
    MAIL_PASSWORD = 'Kaigemail123!@#'

    CACHE_KEY_PREFIX = 'api_cache:'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 6
    CACHE_REDIS_PASSWORD = ''

    QINIU_AK = 'dQQDVyqrHXk6GcPQlktgbLbggO0U9noCJPXIaSsb'
    QINIU_SK = 'Po2FIbJiK_XDTehxTuTzV3a_0wIvUzVIRyMJ9bRJ'

    QCLOUD_SMS_APPID = 1400100785
    QCLOUD_SMS_APPKEY = '9454c7c3170a83a11d4b2a209167caac'

    MAIL_API = 'http://47.52.250.12:19083/demo/email'

    ORDER_CHECK_TIMEOUT = 10

    ENABLE_INFLUXDB = False
    INFLUXDB_HOST = '47.106.111.213'
    INFLUXDB_PORT = 8086
    INFLUXDB_USER = 'root'
    INFLUXDB_PASSWORD = 'root'
    INFLUXDB_DATABASE = 'itunes_dev'

    RESET_PWD_URI = 'https://www.paean.net/#/user/change-password/{code}'

    REGISTER_ADMIN_ROUTES = True



from .dev import DevConfig
from .test import TestConfig
from .prod import ProdConfig
from .localdev import LocalDevConfig
from .localprod import LocalProdConfig


config = {
    'dev': DevConfig,
    'localdev': LocalDevConfig,

    'test': TestConfig,

    'prod': ProdConfig,
    'localprod': LocalProdConfig,
}