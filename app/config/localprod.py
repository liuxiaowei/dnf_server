from . import Config


class LocalProdConfig(Config):
    INFLUXDB_DATABASE = 'itunes_prod'

    CHECK_USER_TOKEN = False
    CHECK_ADMIN_TOKEN = False

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Kaigedb_prod_mysql@localhost:13306/itunes_prod?charset=utf8mb4'

    REDIS_HOST = 'localhost'
    REDIS_PORT = 16379
    REDIS_DB = 3