# -*- coding: UTF-8 -*-
""" 用户对象.
"""


class User:
    """ 用户模型 """
    uid = 0
    phone = ''

    def __init__(self, uid=0, phone=''):
        # TODO 从数据库/缓存中读取用户数据
        if uid:
            pass
        elif phone:
            pass

    def exist(self):
        return bool(self.uid)

    # 创建一个用户
    def create(self):
        # TODO
        pass



