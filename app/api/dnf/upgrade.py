import os
from app.libs.http_utils import *
from . import dnf_bp
from flask import  send_from_directory, make_response


# 获取服务器最新程序的版本
@dnf_bp.route('/upgrade/version', methods=['GET'])
def upgrade_version():
    version = '1.0.0.2'
    data = {
        'version': version
    }
    return render_ok(data)


# 获取服务器最新程序的版本
@dnf_bp.route('/upgrade/files', methods=['GET'])
def upgrade_files():
    data = {
        'files': []
    }
    for dirpath, dirnames, filenames in os.walk('static/version/'):
        for filepath in filenames:
           data['files'].append(os.path.join(dirpath, filepath))
    return render_ok(data)


@dnf_bp.route('/upgrade/download', methods=['GET'])
def download():
    filename = request.headers.get('filename')
    if filename:
        directory = os.getcwd()  # 假设在当前目录
        response = make_response(send_from_directory(directory, filename, as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
        return response
    return render_ok()


