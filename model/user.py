# -*- coding: UTF-8 -*-
""" 用户对象.
"""


class User:
    """ 用户模型 """
    uid = 0
    phone = ''

    def __init__(self, uid=0, phone=''):
        self.__mock_fill_from_db(uid, phone)

    def exist(self):
        return bool(self.uid)

    # 创建一个用户
    def create(self):
        self.__mock_insert_into_db()

    def __mock_fill_from_db(self, uid=0, phone=''):
        # TODO 从数据库/缓存中读取用户数据
        self.uid = 1
        self.phone = '15600000000'

    def __mock_insert_into_db(self):
        # TODO 插入一条数据到db/缓存
        self.uid = 1
        self.phone = '15600000000'
