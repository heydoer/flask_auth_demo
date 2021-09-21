# -*- coding: UTF-8 -*-
""" 常量.
"""


class STATUS:
    """ 状态码常量 """

    class __status:
        """ 状态码类型 """

        def __init__(self, code, msg):
            self.code = code
            self.msg = msg

        # 状态码JSON返回格式
        def to_json(self, with_json=None):
            if dict != type(with_json):
                with_json = {}
            with_json['code'] = self.code
            with_json['msg'] = self.msg
            return with_json

    """ 状态码定义
    """
    SUC = __status(0, 'success')
    ERR = __status(1, 'fail')

    PHONE_NUM_ILLEGAL = __status(1000, 'phone num illegal')
    PHONE_CODE_ALREADY_POSTED = __status(1001, 'phone code already posted')
    PHONE_CODE_POST_TOO_FREQUENTLY = __status(1002, 'phone code posted too frequently')
    AUTH_FAIL = __status(1003, 'auth fail')
