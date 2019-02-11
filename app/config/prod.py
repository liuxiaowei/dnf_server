from . import Config


class ProdConfig(Config):
    LOG_LEVEL = 'info'
    SENTRY_ENABLE = False

    INFLUXDB_DATABASE = 'itunes_prod'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Kaigedb_prod_mysql@itunes-prod-mysql.cpwnyzpuu5np.ap-northeast-1.rds.amazonaws.com:3306/itunes_prod?charset=utf8'

    REDIS_HOST = 'itunes-redis.k1div5.0001.apne1.cache.amazonaws.com'
    REDIS_PORT = 6379
    REDIS_DB = 3

    MAIL_API = 'http://localhost:19063/demo/email'