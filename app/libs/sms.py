import requests
from flask import current_app

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError


g_template_map = {
    182599: 182516,
    181820: 182518,
    145067: 182210,
    145019: 182209,
    145000: 182208,
    144597: 182206,
    144595: 182204,
    144592: 182203,
    144590: 182200,
    144589: 182199,
    144588: 182198,
    144586: 182197,
    182654: 182196,
    134384: 182195,
}


def tranlate_sms_template(nation_code, template_id):
    if int(nation_code) not in (86, ):
        return g_template_map.get(template_id, template_id)

    return template_id



def send_sms(nation_code, phone_number, template_id, params):
    ssender = SmsSingleSender(current_app.config['QCLOUD_SMS_APPID'],
                              current_app.config['QCLOUD_SMS_APPKEY'])

    template_id = tranlate_sms_template(nation_code, template_id)
    try:
        r = ssender.send_with_param(nation_code, phone_number, template_id, params)
    except HTTPError as e:
        return False
    except Exception as e:
        return False

    if r['result'] != 0:
        return False

    return True


def send_mail(mail_to, subject, body):
    params = {
        'receiver': mail_to,
        'subject': subject,
        'body': body,
    }
    r = requests.post(current_app.config['MAIL_API'], json=params, timeout=3)
    if r.status_code != 200:
        return False

    ret = r.json()
    if ret['code'] != 0:
        return False

    return True