# -*- coding: UTF-8 -*-
""" 手机验证码相关API.
"""

from const import STATUS
from util import misc
from model.phone_code import PhoneCode
from facade.user_session import UserSession


class AuthFacade:
    """ 鉴权操作对象 """

    def __init__(self):
        pass

    @staticmethod
    def post_phone_code(phone):
        """ 发送手机验证码 """
        if not misc.verify_phone_num(phone):
            return STATUS.PHONE_NUM_ILLEGAL

        return PhoneCode(phone).post()

    @staticmethod
    def login(phone, code_num):
        """ 验证手机验证码 """
        code = PhoneCode(phone)
        if not code.verify(code_num):
            return None

        user_session = UserSession(phone=phone)
        if not user_session.is_login():
            return None
        return user_session.get_token()

    @staticmethod
    def get_user_session(token):
        """ 根据token获取用户会话 """
        if not token:
            return None

        sess = UserSession(token=token)
        return sess if sess.is_login() else None


authImpl = AuthFacade()
