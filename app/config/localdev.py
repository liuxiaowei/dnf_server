from . import DevConfig


class LocalDevConfig(DevConfig):
    REDIS_PORT = 16379
    CHECK_USER_TOKEN = False

    INFLUXDB_DATABASE = 'itunes_dev'
    SQLALCHEMY_ECHO = True