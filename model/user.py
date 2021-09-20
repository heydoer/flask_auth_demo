# -*- coding: UTF-8 -*-

import jwt


class User:
    """ 用户模型 """
    uid = 0
    phone = ''
    created_at = ''


class UserSession:
    """ 用户会话 """
    user = None

    __TOKEN_KEY = 'Dxm/1993-12-20'

    def __init__(self, token=None, phone=None):
        """ 验证token """
        if token:  # 根据token初始化session
            try:
                user = jwt.decode(token, self.__TOKEN_KEY)
            except jwt.exceptions.InvalidSignatureError:
                return
            # TODO 初始化UserSession
            self.user = user

        if phone:  # 根据phone初始化session
            # TODO
            pass

    def is_login(self):
        """ 是否登陆 """
        return not not self.user

    def get_token(self):
        """ 返回token """
        # TODO 返回token
        return ''
