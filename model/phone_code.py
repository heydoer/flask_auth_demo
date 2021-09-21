# -*- coding: UTF-8 -*-
""" 手机验证码对象.
"""
import random
import time
from util import misc
import const
from collections import defaultdict

codes_pool = defaultdict(lambda: PhoneCode.InnerData())


class PhoneCode:
    """ 手机验证码 """

    class InnerData:
        created_at = 0
        phone = ''
        code = ''

        def available(self):
            # 验证码是否在有效期内
            return bool(self.phone) \
                   and time.time() < self.created_at + const.PhoneCode.verify_ttl

        def can_post(self):
            # 是否可以重新推送该手机验证码
            return not self.code or \
                   time.time() > self.created_at + const.PhoneCode.retry_ttl

    __data = None

    def __init__(self, phone):
        if not misc.verify_phone_num(phone):
            return

        self.__data = codes_pool[phone]

        if not self.__data.created_at or not self.__data.available():
            # 刷新对象
            self.__data.phone = phone
            self.__data.created_at = int(time.time())
            codes_pool[phone] = self.__data

    def post(self):
        """ 推送验证码 """
        if not self.__data.available():
            return const.STATUS.PHONE_NUM_ILLEGAL
        if not self.__data.can_post():
            return const.STATUS.PHONE_CODE_POST_TOO_FREQUENTLY

        # 生成验证码，并刷新缓存
        self.__data.code = self.__gen_code()
        codes_pool[self.__data.phone] = self.__data

        return misc.post_phone_code(self.__data.phone, self.__data.code)

    def verify(self, code):
        """ 验证码校验 """
        if not (self.__data.available()
                and self.__data.code
                and self.__data.code == code):
            return False
        del codes_pool[self.__data.phone]
        return True

    @staticmethod
    def __gen_code():
        """ 生成6位手机验证码 """
        # return str(random.Random().randint(100000, 999999))
        return '000000'
