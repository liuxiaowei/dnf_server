from . import Config


class TestConfig(Config):
    INFLUXDB_DATABASE = 'itunes_test'

    REDIS_DB = 8

    CHECK_USER_TOKEN = False
    CHECK_ADMIN_TOKEN = False

    RESET_PWD_URI = 'https://dev.paean.net:9050/#/user/change-password/{code}'

    CACHE_KEY_PREFIX = 'api_cache:'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 8
    CACHE_REDIS_PASSWORD = ''

    MAIL_API = 'http://localhost:19073/demo/email'