# -*- coding: UTF-8 -*-

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

        code = PhoneCode(phone)

        return code.post()

    @staticmethod
    def login(phone, code_num):
        """ 验证手机验证码 """
        code = PhoneCode(phone)
        if not code.verify(code_num):
            return None
        # TODO 生成user session，返回token
        user_session = UserSession(phone=phone)
        if not user_session.is_login():
            return None
        return user_session.get_token()


authImpl = AuthFacade()
