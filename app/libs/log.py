import os
import logging
from logging.handlers import TimedRotatingFileHandler


APP_LOGGER = logging.getLogger('itunes_api')


def init_app_logger(app):
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}

    log_dir = os.path.join(app.config['LOG_PATH'])
    log_file = os.path.join(app.config['LOG_PATH'], '{}-{}'.format(os.getpid(), app.config['LOG_FILENAME']))
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)

    log_level = LEVELS.get(app.config['LOG_LEVEL'].lower(), 'info')

    rotate_handler = TimedRotatingFileHandler(log_file, when='MIDNIGHT', backupCount=30)
    rotate_handler.suffix = "%Y%m%d"

    formatter = logging.Formatter('%(asctime)-10s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s')
    rotate_handler.setFormatter(formatter)

    global APP_LOGGER
    APP_LOGGER.addHandler(rotate_handler)
    APP_LOGGER.setLevel(log_level)