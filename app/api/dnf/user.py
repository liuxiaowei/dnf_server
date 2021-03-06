import json
import base64
import random
from io import BytesIO
from datetime import datetime
from app.libs.defines import *
from app.models import TUser
import pyotp
from sqlalchemy import or_

from app.libs.http_utils import *
from . import dnf_bp


@dnf_bp.route('/user/register', methods=['POST'])
def register():
    mac = get_json_arg('mac')
    note = get_json_arg('note')
    user = TUser.query.filter(TUser.mac == mac).first()
    data = {
        'status': 0
    }
    if user:
        data['status'] = user.status
    else:
        user = TUser()
        user.mac = mac
        user.note = note
        user.save()
    return render_ok(data)


@dnf_bp.route('/user/query', methods=['GET'])
def login():
    mac = request.headers.get('mac')
    user = TUser.query.filter(TUser.mac == mac).first()
    data = {
        'status': 0,
        'note': ''
    }
    if user:
        data['status'] = user.status
        data['note'] = user.note
    return render_ok(data)

