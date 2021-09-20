# -*- coding: UTF-8 -*-

import threading
import util
from const import STATUS
from model.phone_code import PhoneCode
from model.user import UserSession


class AuthFacade:
    """ 鉴权操作对象 """

    __phone_codes = {}
    __login_users = {}

    def __init__(self):
        self.__phone_codes_lock = threading.Lock()
        self.__login_users_lock = threading.Lock()

    def post_phone_code(self, phone):
        """ 发送手机验证码 """
        if not util.verify_phone_num(phone):
            return STATUS.PHONE_NUM_ILLEGAL

        code = self.__get_code_cache(phone)
        if not code:
            code = PhoneCode(phone)
            self.__set_code_cache(code)

        return code.post()

    def login(self, phone, code_num):
        """ 验证手机验证码 """
        code = self.__get_code_cache(phone)
        if not code.verify(code_num):
            return None
        # TODO 生成user session，返回token
        user_session = UserSession(phone=phone)
        if not user_session.is_login():
            return None
        return user_session.get_token()

    def __get_code_cache(self, phone):
        """ 获取短信验证码缓存对象 """
        with self.__phone_codes_lock:
            if phone not in self.__phone_codes:
                return None
            return self.__phone_codes[phone]

    def __set_code_cache(self, code):
        """ 设置验证码 """
        with self.__phone_codes_lock:
            self.__phone_codes[code.phone] = code

    def __get_user_cache(self, uid):
        """ 获取短信验证码缓存对象 """
        with self.__login_users_lock:
            if uid not in self.__login_users:
                return None
            return self.__login_users[uid]

    def __set_user_cache(self, user):
        """ 设置验证码 """
        with self.__login_users_lock:
            self.__login_users[user.uid] = user


authImpl = AuthFacade()
