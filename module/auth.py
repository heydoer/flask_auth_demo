# -*- coding: UTF-8 -*-
""" 鉴权相关
"""

from flask import Blueprint
from flask import request
from const import STATUS
from facade.phone_code_auth import authImpl


app = Blueprint('auth', __name__)


# 请求手机验证码 JSON API
# req: {'phone': str}
@app.route('/phone_code', methods=['GET'])
def get_phone_code():
    req = request.get_json()

    if not req or 'phone' not in req or not req['phone']:
        return STATUS.PARAM_ERR.to_json()

    status = authImpl.post_phone_code(req['phone'])
    return status.to_json()


# 登陆/提交手机验证码 JSON API
# req: {'phone': str, 'code', str}
# resp: {'token': str}
@app.route('/phone_code', methods=['POST'])
def post_phone_code():
    req = request.get_json()

    if 'phone' not in req or not req['phone'] \
            or 'code' not in req or not req['code']:
        return STATUS.ERR.to_json()

    token = authImpl.login(req['phone'], req['code'])

    if not token:
        return STATUS.AUTH_FAIL.to_json()

    return STATUS.SUC.to_json(with_json={'token': token})
