import json

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from markupsafe import escape
from facade.auth import authImpl

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('login'))


# 登陆页面
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


# 请求手机验证码
@app.route('/phone_codes', methods=['POST'])
def get_phone_code():
    req = request.get_json()
    status = authImpl.post_phone_code(req['phone'])
    return json.dumps(status)


# 提交手机验证码
@app.route('/login', methods=['POST'])
def post_phone_code(phone):
    return 'phone %s' % escape(phone)


if '__main__' == __name__:
    app.run(debug=True)
