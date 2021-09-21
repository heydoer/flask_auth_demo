# -*- coding: UTF-8 -*-
import re
from const import STATUS


def verify_phone_num(phone):
    """ 验证手机号合法性 """
    return not not re.match(r'1[3,4,5,7,8][0-9]{9}', phone)


def post_phone_code(phone, code):
    """ 调用第三方服务推送手机验证码 """
    if not verify_phone_num(phone):
        return STATUS.PHONE_NUM_ILLEGAL
    # TODO
    return STATUS.SUC


def encrypt_phone(phone):
    """ 加密手机号 """
    # TODO
    return phone


def decrypt_phone(secret):
    """ 解密手机号 """
    # TODO
    return secret
