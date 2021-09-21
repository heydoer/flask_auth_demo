# -*- coding: UTF-8 -*-
""" 路由.
"""

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from const import STATUS
from facade.phone_code_auth import authImpl

app = Flask(__name__)


# 登陆页面 HTML page
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


# 主页 HTML page
@app.route('/home', methods=['GET'])
def home():
    token = request.headers.get('token')
    sess = authImpl.get_user_session(token=token)
    if not sess:
        return redirect(url_for('login'))
    return render_template('home.html')


# 请求手机验证码 JSON API
# req: {'phone': str}
@app.route('/phone_code', methods=['GET'])
def get_phone_code():
    req = request.get_json()

    if 'phone' not in req or not req['phone']:
        return STATUS.ERR.to_json()

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


if '__main__' == __name__:
    app.run(debug=True)
