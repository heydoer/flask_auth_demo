# -*- coding: UTF-8 -*-

import jwt


if '__main__' == __name__:
    payload = {'name': 'dou'}
    salt = '123123'
    token = jwt.encode(payload, salt, algorithm="HS256")
    print(token)
    try:
        result = jwt.decode(token, '123', algorithms=["HS256"])
        print(result)
    except jwt.exceptions.InvalidSignatureError:
        print('InvalidSignatureError')
