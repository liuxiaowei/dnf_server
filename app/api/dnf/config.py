from . import dnf_bp
import json
from app.libs.http_utils import *


# 获取定义
@dnf_bp.route('/config/defines', methods=['GET'])
def defines():
    data = {}
    with open("config.json") as load_f:
        data = json.load(load_f)
    return render_ok(data)