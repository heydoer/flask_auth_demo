# -*- coding: UTF-8 -*-
""" 用户会话相关API.
"""

import time
import jwt
from model.user import User
from util import misc
from const import JWT


class UserSession:
    """ 用户会话 """
    user = None
    expired_at = 0

    # 新建一个用户会话
    def __init__(self, token=None, phone=None):
        if token:
            self.__init_by_token(token)
        elif phone:
            self.__init_by_phone(phone)

        if not self.user or not self.user.exist():
            self.user = None

    # 当前会话是否可用
    def is_login(self):
        return bool(self.user) \
               and not self.__is_expired()

    # 获取会话token
    def get_token(self):
        """ 返回token """
        if not self.is_login():
            return None
        return jwt.encode({
            'uid': self.user.uid,
            'expired_at': self.expired_at,
        }, key=JWT.key, algorithm=JWT.algorithm)

    # 会话是否过期
    def __is_expired(self):
        return time.time() >= self.expired_at

    def __init_by_phone(self, phone):
        self.expired_at = int(time.time()) + JWT.TTL
        phone = misc.encrypt_phone(phone)
        self.user = User(phone=phone)
        if not self.user.exist():  # 如果手机号不存在，则注册一个
            self.user.create()

    def __init_by_token(self, token):
        try:
            jwt_data = jwt.decode(token, JWT.key, algorithms=[JWT.algorithm])
        except jwt.exceptions.InvalidSignatureError:
            return

        if 'uid' not in jwt_data or 'expired_at' not in jwt_data:
            return

        self.user = User(uid=jwt_data['uid'])
        self.expired_at = int(jwt_data['expired_at'])
