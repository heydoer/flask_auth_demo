# -*- coding: UTF-8 -*-

import time
import util
from const import STATUS


class PhoneCode:
    """ 手机验证码 """

    created_at = 0
    phone = ''
    code = ''

    __VERIFY_TTL = 60 * 5  # 手机验证码有效期
    __RETRY_TTL = 60  # 手机验证码可以重复推送的等待时间

    def __init__(self, phone):
        self.phone = phone
        self.created_at = int(time.time())

    def post(self):
        """ 推送验证码 """
        if time.time() < self.created_at + self.__RETRY_TTL:
            return STATUS.PHONE_CODE_POST_TOO_FREQUENTLY

        # TODO 生成验证码，调用第三方服务推送

        util.post_phone_code("", "")
        return STATUS.SUC

    def verify(self, code):
        """ 验证码校验 """
        if not code or self.code != code:
            return False
        if time.time() >= self.created_at + self.__VERIFY_TTL:
            return False
        return True

    def __gen_code(self):
        """ 生成手机验证码 """
        return ''
