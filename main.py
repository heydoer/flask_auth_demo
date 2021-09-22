# -*- coding: UTF-8 -*-
""" 入口文件&路由.
"""

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from facade.phone_code_auth import authImpl
import module.auth

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('home'))


# 主页 HTML page
@app.route('/home', methods=['GET'])
def home():
    token = request.headers.get('token')
    sess = authImpl.get_user_session(token=token)
    if not sess:
        return redirect(url_for('login'))
    return render_template('home.html')


# 登陆页面 HTML page
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


if '__main__' == __name__:
    app.register_blueprint(module.auth.app, url_prefix='/auth')
    app.run(debug=True)
