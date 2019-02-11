import time
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor

from influxdb import InfluxDBClient
from flask import g, request, current_app

from app.libs.log import APP_LOGGER


pool_exector = ThreadPoolExecutor(max_workers=4)


def before_request_handler():
    g.begin = time.time()


def after_request_handler(response):
    api_path = request.path
    cost = (time.time() - g.begin) * 1000

    path_array = api_path.split('/')
    if len(path_array)>3:
        api_module = path_array[2]
    else:
        APP_LOGGER.debug('[%s]cost: %.2fms' % (api_path, cost))
        return response
    if response.is_sequence:
        if current_app.config['ENABLE_INFLUXDB']:
            pool_exector.submit(record_api_cost,
                                current_app._get_current_object(),
                                api_module,
                                api_path,
                                cost,
                                response.status_code,
                                len(response.get_data())
                                )

    APP_LOGGER.debug('[%s]cost: %.2fms' % (api_path, cost))
    return response



def before_first_request_handler():
    return



def record_api_cost(current_app, api_module, api_path, cost, status_code, response_body_size):
    json_body = [
        {
            "measurement": "api_module_{}".format(api_module),
            "tags": {
                "path": api_path,
                "status_code": status_code,
            },
            "fields": {
                "value": cost,
                "url": api_path,
                "response_body_size": response_body_size,
            }
        },
        {
            "measurement": "api_cost",
            "tags": {
                "path": api_path,
                "status_code": status_code,
            },
            "fields": {
                "value": cost,
                "url": api_path,
                "response_body_size": response_body_size,
            }
        }
    ]

    client = InfluxDBClient(current_app.config['INFLUXDB_HOST'], current_app.config['INFLUXDB_PORT'],
                            current_app.config['INFLUXDB_USER'], current_app.config['INFLUXDB_PASSWORD'],
                            current_app.config['INFLUXDB_DATABASE'],
                            timeout=3)
    client.write_points(json_body)