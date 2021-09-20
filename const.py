# -*- coding: UTF-8 -*-

class STATUS:
    """ 状态码，返回值用 """

    class __status:
        def __init__(self, code, msg):
            self.code = code
            self.msg = msg

    SUC = __status(0, 'success')
    ERR = __status(1, 'fail')

    PHONE_NUM_ILLEGAL = __status(1000, 'phone num illegal')
    PHONE_CODE_ALREADY_POSTED = __status(1001, 'phone code already posted')
    PHONE_CODE_POST_TOO_FREQUENTLY = __status(1002, 'phone code posted too frequently')
