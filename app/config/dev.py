from . import Config


class DevConfig(Config):
    LOG_LEVEL = 'debug'

    CHECK_USER_TOKEN = False
    CHECK_ADMIN_TOKEN = False

    SQLALCHEMY_ECHO = True

    RESET_PWD_URI = 'https://dev.paean.net:9060/#/user/change-password/{code}'

    INFLUXDB_DATABASE = 'itunes_dev'


    MAIL_API = 'http://localhost:19083/demo/email'